#!/usr/bin/env python3

"""Git post-receive hook: sync the working checkout and rebuild the site.
(It can also schedule future-dated posts to go live via `at`, but that's
switched off; see SCHEDULE_FUTURE_POSTS.) Adapted from
Ultimately_Untrue_Thought/provisioning/pelican_scheduler.py for the
An_Algorithmic_Lucidity blogmistress deployment.

The bare repo's hooks/post-receive is a symlink to this file's copy in the
working checkout (matching the UUT setup), not a standalone copy: the working
checkout already exists (cloned once, ahead of time) before the hook is ever
wired up, so there's no bootstrap-ordering problem, and a symlink means a
future edit to this file, once pushed, takes effect on the very next deploy
instead of silently going stale."""

import datetime
import os
import re
import subprocess

WORKING_REPO = "/home/blogmistress/An_Algorithmic_Lucidity/working"
INPUT_DIR = os.path.join(WORKING_REPO, "content")
OUTPUT_DIR = "/home/blogmistress/An_Algorithmic_Lucidity/output"
PUBLISH_CONF = os.path.join(WORKING_REPO, "publishconf.py")
SITEGEN_COMMAND = "bash -c 'cd {} && source .venv/bin/activate && pelican {} -o {} -s {}'".format(
    WORKING_REPO, INPUT_DIR, OUTPUT_DIR, PUBLISH_CONF)

# Off since 2026-10-15. Unused in practice (not since the old server), and the
# scheduling is wrong on this server anyway: post Date: lines are Pacific
# (TIMEZONE in pelicanconf.py), but get_future_publication_times compares them
# against the box's clock and `at` runs them on it, and the droplet is UTC, so a
# scheduled post would go live 7-8 hours early. (It was written for an old
# Pacific-time server, where the two agreed.) Fix that before turning this back
# on. With it off, a future-dated post isn't lost: WITH_FUTURE_DATES = False
# keeps it unpublished until the first build after its date, i.e. the next push.
SCHEDULE_FUTURE_POSTS = False

DATELINE_REGEX = re.compile(r"^Date: *(\d{4}-\d{2}-\d{2} \d{2}:\d{2}) *$",
                            re.MULTILINE)
JOBLINE_REGEX = re.compile(r"\d+\s\w{3} (\w{3} +\d{1,2} \d{2}:\d{2}:\d{2} \d{4})")

def get_future_publication_times():
    now = datetime.datetime.now()
    times = set()
    for path, _dirnames, filenames in os.walk(INPUT_DIR):
        if path.endswith("drafts"):
            continue
        for filename in filenames:
            if not filename.endswith(".md"):
                continue
            with open(os.path.join(path, filename)) as post_file:
                match = DATELINE_REGEX.search(post_file.read())
                if match:
                    time = datetime.datetime.strptime(match.group(1),
                                                      "%Y-%m-%d %H:%M")
                    if time > now:
                        times.add(time)
    return times


def get_extant_at_job_times():
    times = set()
    result = subprocess.run(["atq"], stdout=subprocess.PIPE)
    job_lines = result.stdout.decode('utf8').split('\n')
    for job_line in job_lines:
        match = JOBLINE_REGEX.match(job_line)
        if match:
            times.add(datetime.datetime.strptime(match.group(1),
                                                 "%b %d %H:%M:%S %Y"))
    return times


def schedule(command, when):
    timestamp = when.strftime("%H:%M %Y-%m-%d")
    at_command = ['at', timestamp]
    at = subprocess.Popen(
        at_command,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    at.communicate(command.encode())


def main():
    # sync our "working" repo with the bare one

    # but first, don't let the fact that this is running as a hook on the bare
    # repo confuse us. Git exports GIT_DIR=. to hooks, and every git command
    # anything here starts would then take the current directory for the
    # repository. Drop it from our own environment, not just from the git
    # calls below: the Pelican build runs `git log` too (sitemap <lastmod>, see
    # _git_last_modified in pelicanconf.py), and so would any `at` job, which
    # snapshots the environment it was scheduled from. Cleaning only the git
    # calls, as this used to, made that `git log` fail silently on every deploy
    # from 2026-09-09 to 10-15, and the sitemap went out with no dates at all.
    os.environ.pop('GIT_DIR', None)

    for git_cmd in [["git", "fetch", "origin"],
                    ["git", "reset", "--hard", "origin/master"]]:
        subprocess.run(git_cmd, cwd=WORKING_REPO)

    # sitegen now! (even if there are no posts to queue, we can at least update
    # /drafts/) and make any back-edits to published posts live
    subprocess.run(SITEGEN_COMMAND,
                   # XXX: `shell=True` is contrary to the moral law
                   shell=True)

    if not SCHEDULE_FUTURE_POSTS:
        return

    # look for scheduled future posts
    future_publication_times = get_future_publication_times()

    # look at atq
    extant_at_job_times = get_extant_at_job_times()

    # if there are future posts that don't have an atq entry, schedule a
    # site-regen at that time
    to_schedule = future_publication_times - extant_at_job_times
    for time in to_schedule:
        schedule(SITEGEN_COMMAND, time)


if __name__ == "__main__":
    main()
