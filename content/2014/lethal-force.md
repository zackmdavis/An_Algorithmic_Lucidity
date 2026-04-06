Title: Lethal --force
Date: 2014-03-17 05:00
Status: published
Category: Uncategorized
Tags: Git
Slug: lethal-force

Dear reader, if you're like me—and if you're not, why are you reading this stupid blog about random shit that no one who's anyone could possibly care about?—close the tab and go do something worthwhile instead. No, I mean it. I'll wait ...

Right. Dear remaining readers, since you're like me, you've probably considered force-pushing to a remote Git repository. ___Do not force-push to a remote Git repository___.

I can hear you protest, "But, but—what about when I want branch B to have content from branch A but I don't want to do a merge like any sane person would, because rebasing would make the history more elegant in my completely arbitrary aesthetic opinion and because I'm a reckless degenerate who is too dumb to live?" _Do the merge._

Because, commit my words, if you rebase and force-push—well, it's a story nearly as old as history itself ([which began on 3 April 2005](http://en.wikipedia.org/wiki/Git_%28software%29#History); so, like, a really long time ago). You might get away with it this time. And the next, and the next. But one day, your project will start failing with mysterious errors, errors ominously reminiscent of those caused by a nasty bug your gracious and talented colleague had fixed the other week. Your feeble attempts at investigation will fail, and you'll entreat your gracious and talented colleague to take a look.

You will never forget the expression of bafflement and horror that you'll infer must have crossed his face when he discovered that his fix for the nasty bug of last week had vanished, as if it had never been written. (_Infer_ because all you'll actually observe is the message "FUCK" over the company IRC channel.)

After the hypothesis occurs to you, you'll have to explain to your gracious and talented coworker what you think could have happened—that you thought you had communicated with him about rebasing branch B eight days ago, but maybe you hadn't been clear, and that it was just barely possible, in theory, that maybe, possibly he had pushed his fix just before you force-pushed your newly-rebased branch ... overwriting your gracious and talented colleague's work on the remote. Not to be noticed for more than a week, long after your colleague had pulled the new version of branch B, overwriting his local copy.

Heed my words, dear reader! Unless you mend your ways, _this is your future!_ I hear you sneer, "But pulling doesn't actually destroy data. It only retrieves the new commit and blob objects and updates the branch pointer; I know because I read it on Hacker News when I should have been working but wasn't because I'm a scoundrel and a thief. The missing commits should still be in the reflog, both in my hypothetical colleague's repository and on the remote."

But suppose the remote is an off-site hosting service that doesn't offer an API to the reflog. What will you do when your gracious, talented, long-suffering (from having to work with the likes of you) colleague fails to find the missing work in his local reflog? "But how could that be?" you ask. Well, I don't know. Maybe the Git garbage-collector ran at an inopportune time? Maybe your understanding of Git's internals gleaned from the _tl;dr_ section of a blog post eight months ago wasn't entirely accurate? Whatever happened, and however it happened, eventually your gracious and talented colleague will give up and spend an hour rewriting his earlier work.

"Oh. Well," you say, "that's a bit unfortunate, but it's far from a disaster. Between the time we spent being confused about the cause of the errors, and looking for the lost commits, and my colleague rewriting his work, that costs the company, what, maybe five developer-hours? That's pocket change," you continue, a slight quaver in your voice betraying your knowledge that you wouldn't speak that way about $250 of your own money being set on fire.

But you're right. It won't be a disaster. You won't get fired or disciplined. Your gracious and talented colleague won't even be angry at you (as far as you can tell), over this one little mistake. You won't do it again.

Except it's _never_ "just one mistake," and you _will_ do it again. "It" maybe not being this _specific_ sin of force-pushing to a shared remote branch (or maybe even that is too optimistic), but _something_ in the equivalence class of "mistakes you could and should have avoided for some reasonable if currently-unknown operationalizations of _could_ and _should_" ...

"So what?" you ask. "If one stupid mistake is non-disastrous, why not say the same of a lifetime's worth of stupid mistakes?" Because, because—

Because I like living in a technological civilization. I like being cool in the summer and warm in the winter, and having plenty of tasty food to eat, and [internet](http://zackmdavis.net/blog/2014/01/house-style/) to play in. These things aren't guaranteed to us by nature; they exist _only_ by of the grace of people being sufficiently non-incompetent at their jobs. And we may not know what we're missing by not being even more non-incompetent. Even if any one mistake or triumph doesn't make a perceptible difference on its own—it adds up. So I don't think you should blame me for caring.
