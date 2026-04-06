Title: Bounded but Not Totally Bounded
Date: 2012-10-14 05:00
Status: published
Category: mathematics
Tags: analysis
Slug: bounded-but-not-totally-bounded

The idea of _total boundedness_ in metric space (for every ε, you can cover the set with a finite number of ε-balls; [discussed previously](http://zackmdavis.net/blog/2012/08/straight-talk-about-precompactness/) on _An Algorithmic Lucidity_) is distinct from (and in fact, stronger than) the idea of mere boundedness (there's an upper bound for the distance between any two points in the set), but to an uneducated mind, it's not immediately clear _why_. What would be an example of a set that's bounded but not totally bounded? _Wikipedia_ claims that the unit ball in infinite-dimensional Banach space will do. Eric Hayashi made this more explicit for me: consider sequence space under the ℓ∞ norm, and the "standard basis" set (1, 0, 0 ...), (0, 1, 0, 0, ...), (0, 0, 1, 0, 0, ...). The distance between any two points in this set is one, so it's bounded, but an open 1-ball around any point doesn't contain any of the other points, so no finite number of open 1-balls will do, so it's not totally bounded, which is what I've been trying to tell you this entire time.
