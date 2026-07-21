Title: Blogging Technology Interlude
Date: 2026-07-17 15:00
Status: published
Category: meta

When I started _An Algorithmic Lucidity_ back in 2011 when I didn't know anything about computers, I used WordPress—briefly on _wordpress.com_, but then on my own site on Namecheap's true-to-its-brandname shared hosting service.

[![WordPress Media Library edit screen for a file named reciprocalx2.png, with arrows pointing to the File type and File URL fields to show the appended "2"]({static}/images/wordpress_filename_suffix.png){: width="360" .alignright }]({static}/images/wordpress_filename_suffix.png)

Even early on, the technical limitations of WordPress were chafing. In my first post, ["The Derivative of the Natural Logarithm"](https://zackmdavis.net/blog/2011/Dec/the-derivative-of-the-natural-logarithm/), I included images of graphs of $y = \log x$ (`lnx.png`) and $y = \frac{1}{x}$ (`reciprocalx.png`), but I must have tried to re-upload edited versions that (I can only infer) WordPress automatically renamed to avoid filename collisions, because I somehow ended up with images called `lnx3.png` and `reciprocalx2.png` in my "Media Library" _whose filenames I couldn't edit_ (the "File URL" field being "grayed out" in the GUI). Maybe it was a well-intentioned technical limitation—you don't want your GUI to let people edit filenames that might break references elsewhere—but it still felt like something precious had been stolen from me.

I want to control my work! The human mind is too small to micromanage every byte, and we wouldn't want to, but we can at least stive to have clean interfaces to what is there whenever possible. The same impulse condemns [WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG) editors, which is why I soon took to writing my posts in Markdown and then pasting the converted HTML into WordPress's "Code Editor". How can people stand [not knowing what lies beneath](https://xkcd.com/2109/) the friendly illusion of paper?

By the time I started [my gender-politics blog](http://unremediatedgender.space/) in 2016, I knew a little more about computers and used the [Pelican](https://getpelican.com/) static-site generator, which suited my taste much better: my posts are canonically in Markdown and the entire site is versioned in Git. If I want to change how something works, it's all Python. I can control my work with tools that I know how to use.

<figure class="alignleft">
<a href="{static}/images/vintage_blog.png"><img src="{static}/images/vintage_blog.png" width="360"></a>
<figcaption>The previous WordPress site, September 2012</figcaption>
</figure>

Meanwhile, while this site stayed functional, it felt shabby to work with. As I grew as a writer and started writing longer and more serious (and non-gender-political) essays from 2019, most of them went up as "exclusives" on [_Less Wrong_](https://www.lesswrong.com/) (and merely linkposted from my own site, if that), unless something seemed more personal or less rationality-flavored, in which case the canonical copy lived here and _Less Wrong_ got a crosspost/linkpost if I thought it would be of interest there.

My tolerance for the old WordPress stack ran out in March of this year when my ["Terrified Comments on Corrigibility in Claude's Constitution"](https://zackmdavis.net/blog/2026/Mar/terrified-comments-on-corrigibility-in-claudes-constitution/) failed to post here: the request just hung when I tried to save the post. I don't know what went wrong, but it wasn't even worth debugging: I put up "Terrified Comments on Corrigibility" as a _Less Wrong_ exclusive and vowed to throw out WordPress and switch to Pelican soon.

Pelican already shipped with [a tool for](https://docs.getpelican.com/en/latest/importer.html) importing from other blogging systems (including, obviously, WordPress), but I didn't like that the Markdown it generated from WordPress's HTML used asterisks (`*`) rather than underscores (`_`) for emphasis, and it turned out that the emphasis character isn't configurable in Pandoc (which `pelican-importer` was using). If I had been doing the conversion even just a couple years ago, the lack of configurability would have presented me with an uncomfortable trade-off (either eat the asterisks, or accept a significantly more labor-intensive conversion process), but in our terrifying new era of agentic coding, I just had Claude Code do the conversion with `markdownify` (which does have a `strong_em_symbol` parameter) and trusted that sanding down the edge-cases I hit by forgoing the standard battle-hardened importer could also be substantially delegated to Claude Code.

The full conversion (including styling the new site to mostly look like the old one, deployment to a DigitalOcean VPS, _&c_.) still took a fair amount of work (the bulk of it during two full days), but much of it was supervisory in nature: the same work would have taken a lot longer (or would have been somewhat lower quality) if I'd had to personally master the intricacies of CSS and Nginx site configuration and unfortunate Markdown/MathJax interactions rather than telling Sonnet 5 what I wanted to happen, asking questions, and clarifying when I didn't like the result. There were several straightforward tasks that I wouldn't have needed to learn anything to do myself, like porting over most of my _Less Wrong_ exclusives (which I mostly had Markdown source for, scattered [across](https://github.com/zackmdavis/Category_War) [two](https://github.com/zackmdavis/Less_Wrong_Drafts/) Git repos) to live here, but delegating to Claude was easier.

I'm pleased with the result. I'll be happier writing this way, and it was an opportunity to add cool enhancements. (The site responds to HTTPS now. We're serving [Markdown alternatives](/blog/2026/Jul/blogging-technology-interlude.md) in case any agents or crawlers prefer that. I'm using `/20XX/Jul/` rather than `/20XX/07/` paths now, but that doesn't break any URLs because Nginx is issuing redirects.)

I didn't even bother with setting up comments for now (I'm using [Isso](https://isso-comments.de/) on the other blog), but comments will probably be back soon. It's not like it's hard anymore.
