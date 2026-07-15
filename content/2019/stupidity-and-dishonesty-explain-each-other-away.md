Title: Stupidity and Dishonesty Explain Each Other Away
Date: 2019-12-28 11:21
Status: published
Category: philosophy
Tags: rationality, honesty
Slug: stupidity-and-dishonesty-explain-each-other-away

[(originally published at _Less Wrong_)](https://www.lesswrong.com/posts/y4bkJTtG3s5d6v36k/stupidity-and-dishonesty-explain-each-other-away)

The _explaining-away effect_ (or, collider bias; or, Berkson's paradox) is a statistical phenomenon in which statistically independent causes with a common effect become anticorrelated when conditioning on the effect.

In the language of [_d_-separation](https://en.wikipedia.org/wiki/Bayesian_network#d-separation), if you have a [causal graph](https://www.lesswrong.com/posts/hzuSDMx7pd2uxFc5w/causal-diagrams-and-causal-models) X → Z ← Y, then conditioning on Z unblocks the path between X and Y.

Daphne Koller and Nir Friedman give an example of reasoning about disease etiology: if you have a sore throat and cough, and aren't sure whether you have the flu or [mono](https://en.wikipedia.org/wiki/Infectious_mononucleosis), you should be relieved to find out it's "just" a flu, because that decreases the probability that you have mono. You _could_ be inflected with both the influenza and mononucleosis viruses, but if the flu is completely sufficient to explain your symptoms, there's no _additional_ reason to expect mono.[^koller-and-friedman]

[^koller-and-friedman]: Daphne Koller and Nier Friedman, _Probabilistic Graphical Models: Principles and Techniques_, §3.2.1.2 "Reasoning Patterns"

Judea Pearl gives an example of reasoning about a burglar alarm: if your neighbor calls you at your dayjob to tell you that your burglar alarm went off, it could be because of a burglary, or it could have been a false-positive due to a small earthquake. There _could_ have been both an earthquake _and_ a burglary, but if you get news of an earthquake, you'll stop worrying so much that your stuff got stolen, because the earthquake alone was sufficient to explain the alarm.[^pearl]

[^pearl]: Judea Pearl, _Probabilistic Reasoning in Intelligent Systems_, §2.2.4 "Multiple Causes and 'Explaining Away'"

Here's another example: if someone you're arguing with is wrong, it could be either because they're just too stupid to get the right answer, or it could be because they're being dishonest—or some combintation of the two, but more of one means that less of the other is required to explain the observation of the person being wrong. As a causal graph—[^code]

[^code]: Thanks to Daniel Kumor for [example $\LaTeX$ code for causal graphs](https://dkumor.com/posts/technical/2018/08/15/causal-tikz/).

![stupidity → wrongness ← dishonesty](https://i.imgur.com/aAblF44.png)

Notably, the decomposition still works whether you count subconscious motivated reasoning as "stupidity" or "dishonesty". (Needless to say, it's also symmetrical across persons—if _you're_ wrong, it could be because _you're_ stupid or are being dishonest.)
