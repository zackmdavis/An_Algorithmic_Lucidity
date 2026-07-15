Title: Bounded but Not Totally Bounded, Redux
Date: 2012-10-16 05:00
Status: published
Category: mathematics
Tags: analysis
Slug: bounded-but-not-totally-bounded-redux

_Theorem_. An open set in real sequence space under the ℓ∞ norm is not totally bounded.

_Proof_. Consider an open set $U$ containing a point $p$. Suppose by way of contradiction that $U$ is totally bounded. Then for every ε > 0, there exists a finite ε-net for $U$. Fix ε, and let $m$ be the number of points in our ε-net, which net we'll denote $\{S_i\}_{i \in \{1, ..., m\}}$. We're going to construct a very special point $y$, which does not live in $U$. For all $i \in \{1, ..., m\}$, we can choose the $i$th component $y_i$ such that the absolute value of its difference from the $i$th component of the $i$th point in the net is strictly greater than ε (that is, $|y_i - S_{i,i}| > \varepsilon$) but also so that the absolute value of its difference from the $i$th component of $p$ is less than or equal to ε (that is, $|y_i - p_i| \le \varepsilon$). Then for $j > m$, set $y_j = p_j$. Then $|y - p| \le \varepsilon$, but that means there are points arbitrarily close to $p$ which are not in $U$, which is an absurd thing to happen to a point in an open set! But that's what I've been trying to tell you this entire time.
