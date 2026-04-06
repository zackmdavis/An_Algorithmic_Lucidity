Title: The Parity Decomposition Trick
Date: 2012-09-30 05:00
Status: published
Category: mathematics
Slug: the-parity-decomposition-trick

Earlier this year, Robert Hasner showed me something that I assume everyone else ("everyone else") already knows, but which _I_ didn't know: every function on ℝ can be decomposed into the sum of an even function and an odd function—

$$!f(x) = \frac{f(x)+f(-x)}{2} + \frac{f(x)-f(-x)}{2}$$

(In fact, as I later read elsewhere, there's nothing essentially _twoful_ about this idea (at least, if you don't care about restricting yourself to ℝ): you can split a function into a sum of _n_ functions _fj_ for _j_ ∈ {0, ..., _n_–1} such that _fj_(ω_z_) = ω_j__fj_(_z_) where ω is an _n_th root of unity.)

I started seeing the same pattern in my reading, too. Like, every matrix can be decomposed into the sum of a symmetric and a skew-symmetric matrix:

_A_ = ½(_A_ + _A_T) + ½(_A_ – _A_T)

(In fact, I have been given to understand that this observation is actually expressing a deep truth about the nature of linear transformations: every linear transformation is in some sense—which I hope to make more explicit later—the sum of a scaling in orthogonal directions (from the symmetric matrix; consider the spectral theorem) and a rotation (from the skew-symmetric matrix, which is said to represent an infinitesimal rotation).)

Also (and _probably_ related to the matrix thing), in the geometric algebra, the geometric product of vectors can be expressed as the sum of an inner product and an [anticommutative outer product](http://zackmdavis.net/blog/2012/09/blades/).

Are there more examples of this theme of splitting something into symmetric and antisymmetric parts? Is there a general theorem explaining exactly which mathematical objects do this kind of thing?
