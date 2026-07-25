#!/usr/bin/env python3

"""Daily digest of AI-crawler activity in the nginx access log.

Scans nginx's access log(s) for the User-Agent strings of known
AI-training/AI-search crawlers (GPTBot, ClaudeBot, CCBot, &c.), tallies what
each one fetched in a trailing window (default 24h), and files a dated summary.
Written for the An_Algorithmic_Lucidity VPS, where nginx logs to
/var/log/nginx/access.log* in the `combined_extended` format -- nginx's stock
`combined`, unchanged, plus two appended fields: "$host"
"$sent_http_content_type" (see conf.d/common_log_formats.conf).

The Content-Type field is what makes a Markdown *content negotiation* visible:
it's served by try_files without rewriting the request, so `GET
/blog/2016/Jun/foo/` with `Accept: text/markdown` is otherwise
indistinguishable in the log from the same URL fetched as HTML. Both extra
fields are parsed as optional, so rotated archives written under plain
`combined` still work -- negotiated fetches in those simply can't be seen and
count as HTML.

SECOND SITE ON THIS BOX
-----------------------
Nothing here assumes one site, but the defaults describe this one. When another
blog moves onto the VPS:

  * If it writes its own access log (the tidy option -- give its server block
    its own `access_log /var/log/nginx/<site>.access.log combined_extended;`),
    just run a second copy of this job with --log-glob and --site.
  * If it shares this access log, pass --host to attribute lines: that's what
    the logged $host is for. Lines predating `combined_extended` have no host
    field and are always kept, since they can only be this site's.
  * If its URLs are shaped differently, adjust BLOG_PREFIX and ARTICLE_PATTERN
    (below) -- every path-structural rule derives from those two, so no other
    code needs touching. A blog served at the domain root rather than under
    /blog/ wants BLOG_PREFIX = "".

Per-site systemd units are the natural way to run several: copy the .service
with an --site/--log-glob-bearing ExecStart, one timer each.

WHAT THIS CAN AND CAN'T TELL YOU
--------------------------------
This only sees crawlers that *honestly self-identify* by User-Agent -- which is
exactly the set of well-behaved training/search bots you'd want to watch. A
scraper that spoofs an ordinary browser UA (or lies and claims to be Googlebot)
will not show up here. And a log line means a *fetch happened*, not that the
bytes were necessarily used to train anything. Treat this as "who's politely
crawling me," not "have I been scraped," which is unknowable from logs alone.

The list of crawlers lives in BOTS below; add or prune to taste. Note the class
of AI training this approach structurally cannot see: Google-Extended and
Applebot-Extended are robots.txt *tokens*, not User-Agents. No request ever
carries them -- they govern what a vendor may do with bytes its ordinary
crawler (Googlebot, Applebot) already fetched. So a Googlebot hit destined for
Gemini training and one destined for the search index are identical in the log,
and no amount of UA matching will separate them. See the note above BOTS.

Stdlib only (no venv needed); safe to run as root or any user that can read the
logs. Robust to logrotate: it reads access.log, access.log.1, and rotated .gz
archives, and filters by each line's own timestamp rather than trusting which
file a line landed in.

OUTPUT
------
Each run writes its digest to ARCHIVE_DIR as <site>-<YYYY-MM-DD>.txt and prints
a one-line summary (so a healthy timer is visible in the journal without the
whole report going there). --stdout prints the report too; --archive-dir ""
turns the file off and prints instead.

The point of running it on a timer even though nothing emails you: nginx's
access logs rotate away (Debian's default is daily, 14 kept), so without a
standing job there is no way to ask in October what the crawlers were doing in
July -- the data is simply gone. These digests outlive the logs they came from.
Read them whenever you're curious:

      ls /var/log/ai-bot-digest/
      less /var/log/ai-bot-digest/zackmdavis.net-2026-07-25.txt
      grep -l ClaudeBot /var/log/ai-bot-digest/*   # which days had ClaudeBot

Nothing prunes them: ~13KB/day is a few MB/year, not worth managing. They do
outlast the access logs they came from, which is mildly nice if you ever want
to compare months. If a cap is ever wanted, a tmpfiles.d age sweep fits better
than logrotate, whose rename-the-active-file model doesn't suit dated files:

      # /etc/tmpfiles.d/ai-bot-digest.conf
      d /var/log/ai-bot-digest 0755 root root 365d

DEPLOY
------
  1. Copy to the VPS (it does not need the blog's venv):
         scp provisioning/ai_bot_digest.py blogmistress@zackmdavis.net:~/
         # then, on the box, somewhere on root's path:
         sudo install -m 0755 ai_bot_digest.py /usr/local/bin/ai_bot_digest
  2. Install the units in provisioning/systemd/ (see SYSTEMD below).

  Test it by hand first -- print a week's worth without writing a file:
         ai_bot_digest --stdout --archive-dir "" --window-hours 168

SYSTEMD  (preferred over cron on a systemd box: `journalctl -u ai-bot-digest`
          shows every run, and a failure is visible in `systemctl list-timers`)
------------------------------------------------------------------------------
  The unit files live in provisioning/systemd/ next to this script, so they're
  version-controlled rather than pasted from a comment:

        sudo install -m 0644 provisioning/systemd/ai-bot-digest.service \\
                             provisioning/systemd/ai-bot-digest.timer \\
                             /etc/systemd/system/
        sudo systemctl daemon-reload
        sudo systemctl enable --now ai-bot-digest.timer
        sudo systemctl start ai-bot-digest.service   # fire once now to test
        journalctl -u ai-bot-digest -n 20            # confirm it ran clean

CRON alternative
----------------
  # crontab of a user that can read the logs
  0 8 * * *  /usr/local/bin/ai_bot_digest
"""

import argparse
import glob
import gzip
import os
import re
import sys
import textwrap
from collections import Counter
from datetime import datetime, timedelta, timezone

# --- configuration (command-line flags override these) -----------------------

LOG_GLOB = "/var/log/nginx/access.log*"
WINDOW_HOURS = 24

# The site this run reports on. HOST filters by the logged $host, which only
# matters once a second site shares this box (and only for lines written under
# `combined_extended`, which logs it); until then every line is this site's and
# the filter is a no-op. SITE is just the label in the subject and header.
SITE = "zackmdavis.net"
HOST = None                     # e.g. "zackmdavis.net"; None = don't filter

# Where the Pelican blog is mounted, and how its article permalinks are shaped.
# Everything path-structural is derived from these two, so pointing this script
# at a differently-organized site is configuration rather than surgery -- see
# the SECOND SITE note in the module docstring.
BLOG_PREFIX = "/blog"
# Article permalinks are /blog/YYYY/Mon/slug/ (ARTICLE_URL in pelicanconf.py),
# optionally with the .md source alternative or an explicit index.html.
ARTICLE_PATTERN = (r"/(?P<year>\d{4})/(?P<month>[A-Za-z]{3}|\d{2})/"
                   r"(?P<slug>[^/]+?)(?P<md>\.md)?/?(?:index\.html)?$")

# Per-crawler cap on listed pages (0 = list everything). Keeps a bot that swept
# the entire archive from turning the digest into thousands of lines.
MAX_PAGES = 30

# Where each run's digest is filed, as <site>-<YYYY-MM-DD>.txt. Set to "" (or
# pass --archive-dir "") to just print instead.
ARCHIVE_DIR = "/var/log/ai-bot-digest"

# Known AI-training / AI-search crawlers, matched (case-insensitively) as
# substrings of the User-Agent. First match wins, so keep specific labels above
# generic patterns.
#
# Deliberately absent: Google-Extended and Applebot-Extended. Those are
# robots.txt *tokens*, not User-Agents -- they're how a site opts out of having
# its content used for Gemini / Apple Intelligence training, but no request ever
# carries them, because the fetching is done by the vendor's ordinary crawler
# (Googlebot, Applebot). Listing them here would be a pattern that can never
# match, and worse, would imply this digest can see AI-training use by Google or
# Apple. It can't: for those two, whether crawled bytes reach a training run is
# decided after the fetch, by a control surface that leaves no trace in an
# access log. Nothing here can distinguish a Googlebot search crawl from a
# Googlebot fetch destined for Gemini.
BOTS = [
    ("GPTBot (OpenAI, training)",        r"GPTBot"),
    ("ChatGPT-User (OpenAI, on-demand)", r"ChatGPT-User"),
    ("OAI-SearchBot (OpenAI, search)",   r"OAI-SearchBot"),
    # Anthropic runs three distinct crawlers, per its crawler docs: ClaudeBot
    # collects training data, Claude-User fetches a page because a human asked
    # Claude about it, Claude-SearchBot builds a search index. Only the first is
    # pretraining. (Claude-Web and anthropic-ai are older UAs, kept because
    # impostors still wear them -- see the scanner section.)
    ("ClaudeBot (Anthropic, training)",  r"ClaudeBot"),
    ("Claude-User (Anthropic, on-demand)", r"Claude-User"),
    ("Claude-SearchBot (Anthropic, search)", r"Claude-SearchBot"),
    ("Claude-Web (Anthropic)",           r"Claude-Web"),
    ("anthropic-ai (Anthropic)",         r"anthropic-ai"),
    # Google's non-search crawler: fetches for product/R&D purposes rather than
    # the web index ("one-off crawls for internal research and development,"
    # per Google's crawler docs). A real User-Agent, unlike Google-Extended --
    # see the note above BOTS about why that one isn't listed here.
    ("GoogleOther (Google, non-search)", r"GoogleOther"),
    ("CCBot (Common Crawl)",             r"CCBot"),
    ("PerplexityBot",                    r"PerplexityBot"),
    ("Perplexity-User",                  r"Perplexity-User"),
    ("Bytespider (ByteDance)",           r"Bytespider"),
    ("Amazonbot",                        r"Amazonbot"),
    ("Applebot",                         r"Applebot"),
    ("Meta / Facebook AI",               r"Meta-ExternalAgent|meta-externalfetcher|FacebookBot"),
    ("cohere-ai (Cohere)",               r"cohere-ai"),
    ("Diffbot",                          r"Diffbot"),
    ("YouBot (You.com)",                 r"YouBot"),
    ("Timpibot",                         r"Timpibot"),
    ("ImagesiftBot",                     r"ImagesiftBot"),
    ("Omgili / Webz.io",                 r"[Oo]mgili"),
    ("PetalBot (Huawei)",                r"PetalBot"),
    ("DataForSeoBot",                    r"DataForSeoBot"),
]
BOTS = [(label, re.compile(pattern, re.IGNORECASE)) for label, pattern in BOTS]

# nginx "combined" log format:
#   $remote_addr - $remote_user [$time_local] "$request" $status
#   $body_bytes_sent "$http_referer" "$http_user_agent"
# ...plus, since conf.d/common_log_formats.conf (the `combined_extended`
# format), a trailing "$host" "$sent_http_content_type". A combined line is a
# strict prefix of an extended one, so the extras are optional groups here --
# that's what lets this single pattern read both the current logs and the
# plain-combined rotated archives beside them.
LINE_RE = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] '
    r'"(?P<request>[^"]*)" (?P<status>\d{3}) \S+ '
    r'"[^"]*" "(?P<ua>[^"]*)"'
    r'(?: "(?P<host>[^"]*)")?(?: "(?P<ctype>[^"]*)")?'
)
# Parse the timestamp without depending on the process locale (strptime's %b is
# locale-sensitive; server logs are always English month abbreviations).
TIME_RE = re.compile(
    r'(?P<d>\d{2})/(?P<b>\w{3})/(?P<Y>\d{4}):'
    r'(?P<H>\d{2}):(?P<M>\d{2}):(?P<S>\d{2}) (?P<sign>[+-])(?P<oh>\d{2})(?P<om>\d{2})'
)
MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], start=1)}


def parse_time(raw):
    """'25/Jul/2026:08:00:00 +0000' -> aware datetime, or None if unparseable."""
    m = TIME_RE.match(raw)
    if not m:
        return None
    month = MONTHS.get(m.group("b").title())
    if month is None:
        return None
    offset = timedelta(hours=int(m.group("oh")), minutes=int(m.group("om")))
    if m.group("sign") == "-":
        offset = -offset
    return datetime(int(m.group("Y")), month, int(m.group("d")),
                    int(m.group("H")), int(m.group("M")), int(m.group("S")),
                    tzinfo=timezone(offset))


def match_bot(user_agent):
    for label, pattern in BOTS:
        if pattern.search(user_agent):
            return label
    return None


def open_log(path):
    if path.endswith(".gz"):
        return gzip.open(path, "rt", errors="replace")
    return open(path, "rt", errors="replace")


class BotStats:
    def __init__(self):
        self.requests = 0
        self.hits = Counter()    # (status, method, path, got_md) -> count
        self.ips = set()

    def record(self, method, path, ip, status, got_md):
        self.requests += 1
        self.hits[(status, method, path, got_md)] += 1
        self.ips.add(ip)

    def distinct_urls(self):
        return len({(method, path) for _s, method, path, _md in self.hits})


def scan(log_glob, cutoff, host=None):
    """Return {bot_label: BotStats} for lines at/after cutoff (aware datetime).

    `host`, if given, keeps only lines whose logged $host matches -- for when
    more than one site shares an access log. Lines with no host field (written
    before `combined_extended`) are kept either way: they predate the second
    site, so they can only be this one's.
    """
    stats = {}
    cutoff_ts = cutoff.timestamp()
    for path in sorted(glob.glob(log_glob)):
        try:
            # Cheap skip: if nothing was written to this file since the cutoff,
            # none of its lines can be in-window -- don't bother decompressing.
            if os.path.getmtime(path) < cutoff_ts:
                continue
        except OSError:
            continue
        try:
            with open_log(path) as log:
                for line in log:
                    m = LINE_RE.match(line)
                    if not m:
                        continue
                    bot = match_bot(m.group("ua"))
                    if bot is None:
                        continue
                    if host and (m.group("host") or host) != host:
                        continue
                    when = parse_time(m.group("time"))
                    if when is None or when < cutoff:
                        continue
                    request = m.group("request").split()
                    method = request[0] if request else "?"
                    raw_path = request[1] if len(request) > 1 else "?"
                    clean_path = raw_path.split("?", 1)[0]  # drop query string
                    # Markdown reached by content negotiation rather than by a
                    # ".md" URL: the request line looks like an ordinary page
                    # fetch (try_files doesn't rewrite it), so the response's
                    # Content-Type is the only tell. Absent on pre-format-change
                    # archives, in which case negotiated hits stay invisible.
                    ctype = m.group("ctype") or ""
                    got_md = ("markdown" in ctype
                              or ctype.startswith("application/octet-stream")
                              and clean_path.endswith(".md"))
                    stats.setdefault(bot, BotStats()).record(
                        method, clean_path, m.group("ip"), m.group("status"),
                        got_md)
        except OSError as e:
            print("warning: could not read {}: {}".format(path, e),
                  file=sys.stderr)
    return stats


def plural(n, noun):
    return "{} {}{}".format(n, noun, "" if n == 1 else "s")


# --- classifying what a request was actually for ----------------------------
# The digest exists to answer "who is ingesting my *writing*." Several kinds of
# request bury that signal, so we bucket them away from the per-post listing:
#   source -- /blog/source is the gitweb repo browser: an effectively infinite
#             spider trap (every commit x file x diff is its own URL), and on a
#             real run it is ~99% of the raw hit count.
#   asset  -- css/js/images/fonts, incidental to rendering.
#   meta   -- robots.txt, sitemap.xml, feeds: machine plumbing.
#   nav    -- tag/category/author/dated archive index pages: navigation, not posts.
#   content-- everything left: post permalinks, .md alternates, /docs, /software.
_ASSET_EXT = (".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg",
              ".webp", ".woff", ".woff2", ".ttf", ".map")
_PREFIX = re.escape(BLOG_PREFIX)
_NAV_RE = re.compile(_PREFIX + r"/(tag|category|author|page)/", re.IGNORECASE)
# /blog/2016/ , /blog/2016/Jun/ , /blog/2016/06/ -- archive indexes (no slug):
_ARCHIVE_RE = re.compile(_PREFIX + r"/\d{4}(/([A-Za-z]{3}|\d{2}))?/?$")
_SOURCE_PREFIX = BLOG_PREFIX + "/source"
_ASSET_PREFIXES = tuple(BLOG_PREFIX + p
                        for p in ("/theme/", "/images/", "/gitweb-static/"))


def classify_path(path):
    if path.startswith(_SOURCE_PREFIX):
        return "source"
    if path.startswith(_ASSET_PREFIXES) or path.endswith(_ASSET_EXT):
        return "asset"
    # Feeds live at a path segment named exactly "feed" (/blog/feed/,
    # /blog/feed/rss/, /blog/category/<slug>/feed/). Test segments, not a
    # substring: `"/feed" in path` would swallow a post slugged "feedback" or
    # "feed-forward-networks" and silently drop it from the content listing.
    if (path in ("/robots.txt", "/sitemap.xml") or path.endswith(".xml")
            or "feed" in path.strip("/").split("/")):
        return "meta"
    if (_NAV_RE.match(path) or _ARCHIVE_RE.match(path)
            or path in (BLOG_PREFIX, BLOG_PREFIX + "/")):
        return "nav"
    return "content"


# Parsing permalinks lets the digest report *posts* rather than URLs: the .md
# and the HTML of one post are the same piece of writing, and belong on one
# line. Shape comes from ARTICLE_PATTERN/BLOG_PREFIX up top.
POST_RE = re.compile("^" + _PREFIX + ARTICLE_PATTERN)


def parse_post(path):
    """-> (year, slug, is_md) for an article permalink, else None."""
    m = POST_RE.match(path)
    if not m:
        return None
    slug = m.group("slug")
    if slug.endswith(".html"):
        return None
    return m.group("year"), slug, bool(m.group("md"))


class Analysis:
    """Per-bot rollup derived from a BotStats, in digest-ready form."""

    def __init__(self, label, stats):
        self.label = label
        self.total = stats.requests
        self.ips = stats.ips
        self.buckets = Counter()      # bucket -> request count
        self.content = Counter()      # content display-path -> request count
        self.posts = {}               # (year, slug) -> {"n", "md", "html"}
        self.other = Counter()        # non-post content (/, /docs/*, ...)
        self.paths = Counter()        # every path -> request count (for scanners)
        self.four_xx = 0
        for (status, method, path, got_md), n in stats.hits.items():
            self.paths[path] += n
            # Only a 2xx means the crawler actually got your words. A 3xx is a
            # hop (it then fetches the canonical URL, counted on its own line --
            # listing both would double-count and litter the list with the old
            # WordPress-era /06/ paths that exist only to redirect to /Jun/), and
            # a 4xx means it got nothing at all. Neither is an ingestion, so both
            # are collapsed rather than listed as pages read.
            if status.startswith("4"):
                self.four_xx += n
                self.buckets["notfound"] += n
                continue
            if status == "304":
                # Not Modified is a cache revalidation, not a redirect: the
                # crawler already has this page and is checking freshness. No
                # bytes moved, so it isn't a read either -- its own bucket.
                self.buckets["notmodified"] += n
                continue
            if status.startswith("3"):
                self.buckets["redirect"] += n
                continue
            bucket = classify_path(path)
            self.buckets[bucket] += n
            if bucket == "content":
                key = path if method == "GET" else "{} {}".format(method, path)
                self.content[key] += n
                post = parse_post(path)
                if post:
                    year, slug, is_md_url = post
                    entry = self.posts.setdefault(
                        (year, slug), {"n": 0, "md_url": False,
                                       "md_neg": False, "html": False})
                    entry["n"] += n
                    # Three routes to one post, tracked separately because
                    # which one a crawler takes says something different about
                    # it: following a <link rel="alternate"> to a .md URL is
                    # ordinary link-walking, whereas sending Accept:
                    # text/markdown for the page URL is a deliberate choice to
                    # prefer source. (An explicit .md URL also comes back as
                    # text/markdown, so test the URL shape first.)
                    if is_md_url:
                        entry["md_url"] = True
                    elif got_md:
                        entry["md_neg"] = True
                    else:
                        entry["html"] = True
                else:
                    self.other[key] += n

    def is_scanner(self):
        # A host forging bot UAs to probe for holes fetches nothing real: its
        # traffic is almost all 404s. Genuine crawlers sit far below this line
        # (real ClaudeBot here is ~18% 404; the impostors are 90-100%).
        return self.total >= 3 and self.four_xx / self.total >= 0.6

    def content_pages(self):
        return len(self.posts) + len(self.other)


# The three ways a crawler can reach one post, in the order they're listed in a
# tag. Short tags because they're stamped inline next to slugs; the legend line
# spells them out via describe_routes().
ROUTE_TAGS = [("md_url", ".md"), ("md_neg", "neg"), ("html", "html")]
_ROUTE_PHRASES = {
    ".md": "the .md URL",
    "neg": "Accept: text/markdown negotiation",
    "html": "the rendered page",
}


def describe_routes(tag):
    """'.md+neg' -> 'the .md URL and Accept: text/markdown negotiation'."""
    parts = [_ROUTE_PHRASES[t] for t in tag.split("+")]
    if len(parts) == 1:
        return parts[0]
    return "{} and {}".format(", ".join(parts[:-1]), parts[-1])


def _join_items(items):
    """Join slugs for wrapping.

    A comma, not the ' · ' used elsewhere: textwrap can only break at spaces, so
    a free-standing separator between two slugs longer than the line width gets
    stranded alone on a line. A comma binds to the slug before it and wraps the
    way ordinary prose does.
    """
    return ", ".join(items)


def render_posts(a, max_pages):
    """Which posts this crawler read, grouped by year, slugs packed per line.

    One post = one entry, however many URLs it was reached by: the .md source
    alternative is folded into its post and flagged rather than given a line of
    its own. Slugs are what identify a post to a human, so the /blog/YYYY/Mon/
    prefix becomes the year label and drops out of every entry.
    """
    lines = []
    by_year = {}
    for (year, slug), info in a.posts.items():
        by_year.setdefault(year, []).append((slug, info))

    # How a crawler reached each post is interesting -- several take the .md
    # source and never the rendered page -- but stamping the *majority* case on
    # every slug is noise. Build a tag per post naming the routes actually used,
    # state the dominant one once, and mark only departures from it.
    def mark_for(info):
        return "+".join(tag for key, tag in ROUTE_TAGS if info[key])

    habits = Counter(mark_for(i) for i in a.posts.values())
    dominant = None
    if len(a.posts) >= 4:
        top, count = habits.most_common(1)[0]
        if count / len(a.posts) >= 0.6:
            dominant = top
    if dominant and dominant != "html":
        lines.append("  [fetched via {}, except as marked]".format(
            describe_routes(dominant)))
    # With no clear house style, treat the rendered page as the unmarked norm --
    # it's what a human reader would get.
    dominant = dominant or "html"

    # Newest first, and truncate whole years rather than an arbitrary slice of
    # a count-sorted list: "412 more from 2011-2015" says something; thirty
    # 1-fetch slugs picked by tie-break order does not.
    years = sorted(by_year, reverse=True)
    budget = max_pages or len(a.posts)
    spent, cut_from = 0, []
    for year in years:
        entries = sorted(by_year[year])
        if spent >= budget:
            cut_from.append(year)
            continue
        spent += len(entries)
        rendered = []
        for slug, info in entries:
            tag = mark_for(info)
            mark = slug + ("" if tag == dominant else "({})".format(tag))
            if info["n"] > 1:
                mark += "×{}".format(info["n"])
            rendered.append(mark)
        lines += textwrap.wrap(
            _join_items(rendered), width=76,
            initial_indent="  {}  ".format(year),
            subsequent_indent="        ",
            # Slugs are hyphen-heavy; breaking inside one makes it unscannable.
            break_on_hyphens=False, break_long_words=False)
    if cut_from:
        dropped = sum(len(by_year[y]) for y in cut_from)
        lines.append("  ... and {} more from {}{} (--max-pages 0 for all)".format(
            dropped, min(cut_from),
            "" if len(cut_from) == 1 else "-" + max(cut_from)))

    # Content that isn't an article permalink (the landing page, /docs/*.pdf,
    # /software/*) has no year or slug to group by, so it keeps its full path
    # under its own label rather than dangling under the last year listed.
    if a.other:
        others = ["{}{}".format(page, "" if n == 1 else "×{}".format(n))
                  for page, n in sorted(a.other.items(),
                                        key=lambda kv: (-kv[1], kv[0]))]
        lines += textwrap.wrap(_join_items(others), width=76,
                               initial_indent="  else  ",
                               subsequent_indent="        ",
                               break_on_hyphens=False, break_long_words=False)
    return lines


def _footer(saw_scanners=False):
    # The forgery caveat points at the scanner/forged-identity sections when
    # they're present, but those only render when something tripped them --
    # don't cite sections that aren't in this particular digest.
    forgery = ("hence the scanner and forged-identity sections above."
               if saw_scanners else
               "when a forger shows up, it gets its own section here.")
    return [
        "-" * 60,
        "Caveats: matching is by User-Agent, which is (a) absent for covert",
        "scrapers wearing an ordinary browser UA, and (b) trivially forged --",
        forgery + " A line here is a",
        "fetch, not proof of training use.",
        "Google and Apple are blind spots: whether their crawls feed Gemini or",
        "Apple Intelligence is set by a robots.txt token (Google-Extended,",
        "Applebot-Extended) that no request carries, so their training use is",
        "not visible in an access log at all.",
    ]


def build_report(stats, window_hours, log_glob, max_pages=MAX_PAGES,
                 site=SITE):
    now = datetime.now(timezone.utc)
    analyses = [Analysis(label, s) for label, s in stats.items()]
    crawlers = sorted((a for a in analyses if not a.is_scanner()),
                      key=lambda a: a.total, reverse=True)
    scanners = sorted((a for a in analyses if a.is_scanner()),
                      key=lambda a: a.total, reverse=True)
    total = sum(a.total for a in analyses)

    # A single host presenting several bot identities is forging UAs -- and a
    # promiscuous one contaminates even the genuine crawlers' tallies.
    ip_labels = {}
    for a in analyses:
        for ip in a.ips:
            ip_labels.setdefault(ip, set()).add(a.label)
    forgers = sorted(((ip, labs) for ip, labs in ip_labels.items()
                      if len(labs) >= 3),
                     key=lambda kv: len(kv[1]), reverse=True)

    lines = [
        "AI-crawler activity on {}".format(site),
        "Window: last {}h, ending {:%Y-%m-%d %H:%M} UTC".format(window_hours, now),
        "Logs:   {}".format(log_glob),
        "",
    ]

    if total == 0:
        subject = "[AI crawlers] no hits in the last {}h -- {}".format(
            window_hours, site)
        lines.append("No self-identifying AI crawlers hit the site in this window.")
        return subject, "\n".join(lines + _footer())

    # Lead with the number the fame-tracking is actually about: distinct pages
    # of yours that got read. Only mention spoofed-UA scanners when there are
    # any -- a silent "0 scanning" just raises questions it doesn't answer.
    distinct_pages = len(set().union(*(a.content for a in crawlers))
                         if crawlers else set())
    subject = "[AI crawlers] {} read {} -- {} ({}h)".format(
        plural(len(crawlers), "bot"), plural(distinct_pages, "page"),
        site, window_hours)
    if scanners:
        subject += " [+{} spoofing]".format(len(scanners))

    # --- summary of the real content crawlers ---
    lines += ["CONTENT CRAWLERS  (bots that actually fetched your writing --",
              "                   as opposed to the spoofed-UA scanners below)",
              "  {:<32}{:>12}{:>9}{:>7}".format("", "requests", "pages", "IPs")]
    for a in crawlers:
        lines.append("  {:<32}{:>12}{:>9}{:>7}".format(
            a.label[:32], a.total, a.content_pages(), len(a.ips)))
    lines += [
        "  (\"requests\" counts every fetch, incl. the /blog/source git-history",
        "   trap; \"pages\" is distinct posts/pages -- the real ingestion signal.)",
        "",
    ]

    # --- per-crawler detail: collapse the noise, list the actual pages ---
    lines += ["Pages fetched, per crawler", "=" * 26, ""]
    for a in crawlers:
        lines.append("{}  --  {} · {} · {}".format(
            a.label, plural(a.total, "request"),
            plural(a.content_pages(), "content page"), plural(len(a.ips), "IP")))
        noise = []
        if a.buckets["source"]:
            noise.append("{}× /blog/source (git browser)".format(a.buckets["source"]))
        if a.buckets["asset"]:
            noise.append("{}× assets".format(a.buckets["asset"]))
        if a.buckets["nav"]:
            noise.append("{}× archive/tag".format(a.buckets["nav"]))
        if a.buckets["meta"]:
            noise.append("{}× robots/sitemap/feeds".format(a.buckets["meta"]))
        if a.buckets["redirect"]:
            noise.append("{}× redirects".format(a.buckets["redirect"]))
        if a.buckets["notmodified"]:
            noise.append("{}× 304 revalidations".format(
                a.buckets["notmodified"]))
        if a.four_xx:
            noise.append("{}× 404".format(a.four_xx))
        if noise:
            lines += textwrap.wrap(
                "(collapsed: {})".format(" · ".join(noise)), width=76,
                initial_indent="  ", subsequent_indent="   ",
                break_on_hyphens=False, break_long_words=False)
        lines += render_posts(a, max_pages)
        lines.append("")

    # --- spoofed UAs / scanners, quarantined from the real crawlers ---
    if scanners:
        lines += [
            "LIKELY SPOOFED UAs / VULN SCANNERS",
            "(>=60% of responses are 404s -- not real crawls; a host is forging",
            " reputable bot identities to probe for secrets and misconfigurations)",
            "",
        ]
        for a in scanners:
            where = (next(iter(a.ips)) if len(a.ips) == 1
                     else "{} IPs".format(len(a.ips)))
            lines.append('  "{}"  --  {} · {}% 404 · from {}'.format(
                a.label, plural(a.total, "request"),
                round(100 * a.four_xx / a.total), where))
            probes = sorted(a.paths.items(), key=lambda kv: (-kv[1], kv[0]))
            shown = probes[:max_pages] if max_pages else probes
            for path, n in shown:
                lines.append("        {}{}".format(
                    path, "" if n == 1 else "  (x{})".format(n)))
            if len(probes) > len(shown):
                lines.append("        ... and {} more probe(s)".format(
                    len(probes) - len(shown)))
            lines.append("")

    # --- forged-identity hosts ---
    if forgers:
        lines += ["FORGED-IDENTITY HOSTS  (one IP wearing many bot UAs)"]
        for ip, labs in forgers[:10]:
            lines.append("  {}  presented {} different bot User-Agents".format(
                ip, len(labs)))
        lines.append("")

    return subject, "\n".join(lines + _footer(bool(scanners)))


def archive(report, archive_dir, site):
    """Write the digest to <archive_dir>/<site>-<date>.txt; return the path.

    Dated files rather than one appended log: nginx's own access logs rotate
    away (Debian's default is daily, 14 kept), so these summaries outlive the
    data they were derived from, and one file per run stays greppable and
    trivially prunable.
    """
    os.makedirs(archive_dir, exist_ok=True)
    name = "{}-{}.txt".format(site, datetime.now(timezone.utc)
                              .strftime("%Y-%m-%d"))
    path = os.path.join(archive_dir, name)
    # Same site, same day, run twice: overwrite rather than append, so the file
    # is always exactly one digest and a re-run after a fix is a correction
    # instead of a duplicate.
    with open(path, "w") as out:
        out.write(report + "\n")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--window-hours", type=int, default=WINDOW_HOURS)
    parser.add_argument("--log-glob", default=LOG_GLOB)
    parser.add_argument("--max-pages", type=int, default=MAX_PAGES,
                        help="per-crawler cap on listed pages (0 = no cap)")
    parser.add_argument("--site", default=SITE,
                        help="label for this site in the subject/header")
    parser.add_argument("--host", default=HOST,
                        help="only count lines whose logged $host matches"
                             " (for an access log shared by several sites)")
    parser.add_argument("--archive-dir", default=ARCHIVE_DIR,
                        help="write a dated digest here (default: {}); "
                             "empty string disables".format(ARCHIVE_DIR))
    parser.add_argument("--stdout", action="store_true",
                        help="also print the digest (implied when no archive"
                             " dir is set)")
    args = parser.parse_args()

    cutoff = datetime.now(timezone.utc) - timedelta(hours=args.window_hours)
    stats = scan(args.log_glob, cutoff, args.host)
    total = sum(s.requests for s in stats.values())
    subject, body = build_report(stats, args.window_hours, args.log_glob,
                                 args.max_pages, args.site)
    report = "{}\n\n{}".format(subject, body)

    written = None
    if args.archive_dir:
        written = archive(report, args.archive_dir, args.site)

    if args.stdout or not written:
        print(report)
    else:
        # One line per run, so a healthy job is still visible in the journal
        # even though the digest itself went to a file.
        print("{}: {} hit(s) from {} bot(s) -> {}".format(
            datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
            total, len(stats), written))


if __name__ == "__main__":
    main()
