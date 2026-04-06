Title: The Typical Set
Date: 2019-05-05 16:57
Status: published
Category: mathematics
Tags: information theory
Slug: the-typical-set

(Part of [Math and Wellness Month](http://zackmdavis.net/blog/2019/05/may-is-math-and-wellness-month/).)

Say you have a biased coin that comes up Heads 80% of the time. (I like to imagine that the Heads side has a portrait of [Bernoulli](https://en.wikipedia.org/wiki/Bernoulli_process).) Flip it 100 times. The naïve way to report the outcome—just report the sequences of Headses and Tailses—costs 100 bits. But maybe you don't have 100 [bits](https://mlp.fandom.com/wiki/Bits). What to do?

One thing to notice is that because it was a biased coin, some bit sequences are _vastly_ more probable than others: "all Tails" has probability 0.2100 ≈ 1.268 · 10−70, whereas "all Heads" has probability 0.8100 ≈ 2.037 · 10−10, differing by a factor of _sixty orders of magnitude_!!

Even though "all Heads" is the uniquely most probable sequence, you'd still be pretty surprised to see it—there's only _one_ such possible outcome, and it only happens a 2.037 · 10−10th of the time. You _probably_ expect to get a sequence with _about_ twenty Tails in it, and there are _lots_ of those, even though each individual one is less probable than "all Heads."

Call the number of times we flip our Bernoulli coin _N_, and call the [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of the coinflip _H_. (For the 80/20 biased coin, _H_ is ⅕ lg 5 + 4/5 lg 5/4 ≈ 0.7219.)

It turns out for sufficiently large _N_ (I know, one of _those_ theorems, right?), _almost all_ of the probability mass is going to live in a subset of 2NH outcomes, each of which have a probability close to 2−NH (and you'll notice that 2NH · 2−NH = 1).
