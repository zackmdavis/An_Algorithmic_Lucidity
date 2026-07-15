Title: Critic Contributions Are Logically Irrelevant
Date: 2025-07-14 18:03
Status: published
Category: philosophy
Tags: epistemology

[(originally published at _Less Wrong_)](https://www.lesswrong.com/posts/bsKHthyhB7DNBxERQ/critic-contributions-are-logically-irrelevant)

## The Value of a Comment Is Determined by Its Text, Not Its Authorship

I sometimes see people express disapproval of critical blog comments by commenters who don't write many blog posts of their own. Such meta-criticism is not infrequently couched in terms of metaphors to some non-blogging domain. For example, describing his negative view of one user's commenting history, Oliver Habyrka [writes](https://www.lesswrong.com/posts/adk5xv5Q4hjvpEhhh/meta-new-moderation-tools-and-moderation-guidelines?commentId=G2PppMHPsHvhF7hfu) (emphasis mine):

> The situation seems more similar to having a competitive team where anyone gets screamed at for basically any motion, _with a coach who doesn't themselves perform the sport_, but just complaints [_sic_] in long tirades any time anyone does anything, making references to methods of practice and training long-outdated, with a constant air of superiority.

In a similar vein, [Duncan Sabien writes](https://www.lesswrong.com/posts/JcgtKunqmELefxksx/killing-socrates) (emphasis mine):

> There's only so much withering critique a given builder is interested in receiving _(frequently from those who do not themselves even build!)_ before eventually they will either stop building entirely, or leave to go somewhere where buildery is appreciated, rewarded, and (importantly) defended.

I find this stance deeply puzzling. In general, the value of a critical blog comment is in potentially alerting readers to an error, omission, or other shortcoming of the post. (If the alleged shortcoming does not in fact exist, the value of the comment is negative.) This value clearly does not depend on the identity of the author!

I recently committed the sin of publishing [a post which suffered from multiple shortcomings](https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions). For one, I implied that the set of continuous functions from ℝ to ℝ equipped with [the uniform norm](https://en.wikipedia.org/wiki/Uniform_norm) is a [normed space](https://en.wikipedia.org/wiki/Norm_(mathematics)).

That was wrong of me. The thing I wrote was wrong. The reason that the thing I wrote was wrong is because norms are defined as functions that output a real number, but there exist continuous functions that are unbounded, and if we attempt to take the uniform norm of such a function—the [least upper bound](https://en.wikipedia.org/wiki/Infimum_and_supremum) of its absolute value—we get +∞, which isn't a real number. (In contrast, the space of continuous functions _from a [compact](https://en.wikipedia.org/wiki/Compact_space) domain_ to ℝ under the uniform norm is a normed space, because by [the extreme value theorem](https://en.wikipedia.org/wiki/Extreme_value_theorem), those functions are bounded.)

[A comment pointed out that I was wrong.](https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=guPEbeKtPnqsBhrjg) That comment was valuable because it alerted readers of the comment section to an error in the post. (It also happened to alert me, the author, because I happened to be one of the readers of the comment section.)

The reason it makes sense for me to write "_A comment_ pointed out that I was wrong" even though comments aren't people is because the identity of the commenter doesn't matter. It doesn't matter what their name is. It doesn't matter whether they have a math degree. It doesn't matter whether they went to school at all.

It doesn't matter whether they're _human_. If a large language model had written the same comment, it would be the same comment. The same sequence of bytes would be stored [in the `content` field of the `Comments` table of the website's database](https://github.com/ForumMagnum/ForumMagnum/blob/bd038d3f84a2915a8e07f2b74a053c2a8d3f4376/schema/accepted_schema.sql#L264). Because it would be the same sequence of bytes, the effect of rendering those bytes as text on a monitor and showing them to a human would be the same. The human reading the comment has no way of knowing who or what wrote those bytes to the database. In [the language of causal graphical models](https://plato.stanford.edu/entries/causal-models/#MarkCond), we can say that the text of the comment ["screens off"](https://www.lesswrong.com/posts/5yFRd3cjLpm3Nd6Di/argument-screens-off-authority) the process that produced it.

In principle, it doesn't matter whether the process that generated the comment is "intelligent" in any sense. A so-called "large language model" is just a conditional probability distribution expressed as a computer program: generating text is sampling from the distribution. But you could do that with any distribution. If by some exponentially improbable cosmic coincidence, uniformly sampling from printable ASCII characters (in Python, `''.join(chr(random.randint(32, 126)) for _ in range(n))` for a sample `n` characters long) somehow produced the same comment, it would still be the same comment.

Given that a commenter's name, educational attainment, humanity, or existence as an independent entity does not affect the value of a given comment, it should be clear that another thing that doesn't matter is whether the commenter writes blog posts in addition to blog comments. That doesn't matter. Why would someone think that matters?

## However, Critic Contributions Can Inform Uncertain Estimates of Comment Value

Except we should not be premature. The people who write metaphors about coaches who don't themselves perform the sport they coach or builders who do not themselves build, seem to think it matters. We should search harder for reasons why someone would think that.

It turns out that there are some important nuances here that must be addressed. The value of a comment doesn't depend on whether the commenter also writes posts—_if_ the value of the comment is known with certainty (such that its authorship is screened off). If we're uncertain about the comment's value, our uncertain estimate of its value can depend on what other things the author has done. In Bayesian terms, the likelihood provided by our imperfect estimation of the comment's value isn't strong enough to fully overcome our author-based prior.

Author-based priors can be decision-relevant, as can be seen from the limiting case of the uniform printable ASCII distribution: you wouldn't want to give a random-character-generating program commenting privileges on your blog, because an exponentially vast hypermajority of its output is worthless gibberish (and of the tiny fraction that looks sensible by sheer cosmic coincidence, the vast hypermajority won't furthermore happen to be right by another cosmic coincidence). Even July 2025–era language models don't make the cut in most blog administrators' eyes.

The decision-relevance of author-based priors neatly explains the appeal of the coach and builder metaphors. If aspiring athletes and builders don't know how to distinguish between good and bad advice (and ignore the bad advice at zero cost), it makes sense for them to only listen to people likely on priors to give good advice, which would mostly be people who have excelled at the activity before. Taken on their own terms, the examples make sense: you probably wouldn't want a coach who had never been a player, a building advisor who had never built.

There's still a problem, however: just because the examples make sense on their own terms, doesn't mean they make sense _as blogging analogies_. It makes sense that a coach who had never played would thereby be a bad coach, because the way you gain intimate knowledge of the best way to play the game is by playing it for years.

But would a commenter who had never written "top-level" posts thereby be a worse commenter? It's hard to see why that would be the case. In the analogy, coaching is an activity that depends on playing, but comment-writing doesn't seem to depend on post-writing to nearly the same extent or even in the same way, in large part because it's not even clear to what extent comment-writing and post-writing are even different activities, rather than just being the same activity, writing. (It's not uncommon that text that was originally drafted with the intent of being a "comment", ends up being revised into a "post.")

Maybe if a post is on some specialized topic, like DNA polymerase mutations in _C. elegans_ or maritime salvage law in international waters, it might make sense to disapprove of ignorant commenters mouthing off without themselves being nematode microbiologists or navy [JAGs](https://en.wikipedia.org/wiki/Judge_advocate_general). It's not crazy to think that people who aren't nematode microbiologists won't have any good opinions about DNA polymerase mutations in _C. elegans_, such that we're not missing anything important by refusing to let them comment.

But it doesn't make sense to gatekeep blog commenting privileges on writing posts for the same blog, because there's no particular reason why someone shouldn't happen to do more of their writing in the form of comments rather than posts. That doesn't matter. Why would someone think that matters?

## A Caveat: Critic Contributions Can Be Relevant If You Don't Care About Maximizing Correctness

That wasn't a rhetorical question. Why _would_ someone think that matters? The explanations given above for why the value of a critical comment doesn't depend on its author, and why whether a commenter also writes posts does not have much evidential bearing on the uncertain value of a comment, seem pretty straightforward, even obvious. Where is the error in the reasoning?

If there's no error in the reasoning, perhaps the disagreement comes down to different starting premises. It doesn't matter whether a commenter also writes posts—_if_ one accepts as a premise that the value of a critical blog comment is in potentially alerting readers to an error, omission, or other shortcoming of the post. If one denies that premise and embraces some other theory of comment value, other conclusions are possible.

For a simple example of what such an alternative theory could look like, one could hold that the function of a critical blog comment is to attempt to raise the commenter's social status and lower the status of the post author. Then, given some separate criterion of who deserves what status, a good comment would be by someone who deserves to be high status, criticizing a post written by someone who deserves to be low status. Conversely, a bad comment would be by someone who deserves to have low status, criticizing a post written by someone who deserves to have high status—and the more persuasive the comment is, the worse it is, because more successful persuasion increases the misallocation of status (in the minds of persuaded readers) to the commenter who, _ex hypothesi_, doesn't deserve it.

Of course, that's not the only possible alternative theory of comment value. One could imagine an intricate "hybrid" theory that strikes a carefully computed compromise between alerting readers to errors and omissions in a post, and optimizing status allocation with respect to some criterion of deservingness.

Suppose the administrators of some website are trying to optimize some quantity, like "total number of interesting ideas posted to the website", or maybe "advertising revenue." Let's go with ad revenue because it's easier to measure and should be a good proxy for interesting ideas. (If the website is the place to go for interesting ideas, then lots of people will want to visit it, and advertisers will pay for all those people's clicks.) Suppose furthermore that contributors are motivated by status: if people lose too much status from their posts or comments, they'll stop writing, which has a negative effect on ad revenue.

Under this hybrid theory of comment value, it can make sense to disapprove of people who write critical comments and not posts, if the error-correction value of the comments is outweighed by lost ad revenue due to demotivated authors.

Thus, our earlier conclusion must be revised to be conditional. It doesn't make sense to disapprove of commenters who don't write posts, _if you only care about correctness_. If you care about something other than correctness, such as ad revenue, then it can make sense to disapprove of commenters who don't write posts. The inference also works in the other direction: if you disapprove of commenters who don't write posts, that implies that _you care about something other than correctness_.
