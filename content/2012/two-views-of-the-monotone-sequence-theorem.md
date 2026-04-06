Title: Two Views of the Monotone Sequence Theorem
Date: 2012-11-05 21:51
Status: published
Category: mathematics
Tags: analysis
Slug: two-views-of-the-monotone-sequence-theorem

If a sequence of real numbers (_an_) is _bounded_ and _monotone_ (and I'm actually going to say _nondecreasing_, without loss of generality), then it _converges_. I'm going to tell you _why_ and I'm going to tell you _twice_.

If our sequence is bounded, the completeness of the reals ensures that it has a _least_ upper bound, which we'll call, I don't know, _B_, but there have to be sequence elements arbitrarily close to (but not greater than) _B_, because if there weren't, then _B_ couldn't be a _least_ upper bound. So for whatever arbitrarily small ε, there's an _N_ such that _aN_ > _B_ – ε, which implies that |_aN_ – _B_| < ε, but if the sequence is nondecreasing, we also have |_an_ – _B_| < ε for _n_ ≥ _N_, which is what I've been trying to tell you—

—_twice_; suppose by way of contraposition that our sequence is _not_ convergent. Then there _exists_ an ε such that for all _N_, there exist _m_ and _n_ greater or equal to _N_, such that |_am_ – _an_| is greater or equal to ε. Suppose it's monotone, without loss of generality _nondecreasing_; that implies that for all _N_, we can find _n_ > _m_ ≥ _N_ such that _an_ – _am_ ≥ ε. Now suppose our sequence is bounded above by some bound _B_. However, we can actually describe an algorithm to find sequence points greater than _B_, thus showing that this alleged bound is really not a bound at all. Start at _a1_. We can find points later in the sequence that are separated from each other by at least ε, but if we do this ⌈(_B_ – _a1_)/ε⌉ times, then we'll have found a sequence point greater than the alleged bound.
