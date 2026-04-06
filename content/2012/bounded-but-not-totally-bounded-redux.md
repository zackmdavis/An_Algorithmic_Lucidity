Title: Bounded but Not Totally Bounded, Redux
Date: 2012-10-16 05:00
Status: published
Category: mathematics
Tags: analysis
Slug: bounded-but-not-totally-bounded-redux

_Theorem_. An open set in real sequence space under the ℓ∞ norm is not totally bounded.

_Proof_. Consider an open set _U_ containing a point _p_. Suppose by way of contradiction that _U_ is totally bounded. Then for every ε > 0, there exists a finite ε-net for _U_. Fix ε, and let _m_ be the number of points in our ε-net, which net we'll denote {_S__i_}_i_∈{1, ..., _m_}. We're going to construct a very special point _y_, which does not live in _U_. For all _i_ ∈ {1, ..., _m_}, we can choose the _i_th component _y__i_ such that the absolute value of its difference from the _i_th component of the _i_th point in the net is strictly greater than ε (that is, |_yi_ – _Si,i_| > ε) but also so that the absolute value of its difference from the _i_th component of _p_ is less than or equal to ε (that is, |_yi_ – _pi_| ≤ ε). Then for _j_ > _m_, set _yj_ = _pj_. Then |_y_ – _p_| ≤ ε, but that means there are points arbitrarily close to _p_ which are not in _U_, which is an absurd thing to happen to a point in an open set! But that's what I've been trying to tell you this entire time.
