Title: Epiphenomenal Coordinates
Date: 2013-01-15 05:00
Status: published
Category: mathematics
Tags: linear algebra
Slug: epiphenomenal-coordinates

In the study of elementary linear algebra, unwary novices are often inclined to think of a vector as an ordered list of real numbers; to them, linear algebra is then conceived of as the study of multiplying matrices with column vectors. But this is a horribly impoverished perspective; we can do so much better for ourselves with a bit of abstraction and generality.

You _can_ think of arrows or lists of numbers if you want or if you must, but the true, ultimate meaning of a _vector space_ is ... well, anything that satisfies the vector space axioms. If you have things that you can "add" (meaning that we have an associative, commutative binary operation and we have inverse elements and an identity element with respect to this operation), and you can "multiply" these things by other things that come from a field (the "vectors" in the space and the "scalars" from the field play nicely together in a way that is distributive _&c._), then these things you that you have are a vector space over that field, and any of the theorems that we prove about vector spaces in general apply in full force to the things you have, which don't have to be lists of real numbers; they could be matrices or polynomials or functions or whatever.

Okay, so it _turns out_ that _n_-dimensional vector spaces are isomorphic to lists of _n_ numbers (elements of the appropriate field), but that's not part of our _fundamental_ notion of vectorness; it's something we can _prove_—

Let's say a set of _n_ elements {_v__j_}_j_ from a vector space _V_ _span_ the space iff every element _v_ in the space can be written as a linear combination of elements in the set: _v_ = Σ_j_ _c__j__v__j_ for some coefficients _c__j_. Let's also say that a set of vector space elements is _linearly independent_ iff the only way a linear combination of them can be the zero vector is if all the coefficients are zero: Σ_j_ _c__j__v__j_ = __0__ implies ∀_j_ _c__j_ = 0. We say a set is a _basis_ if and only if it spans the space and is linearly independent. Bases are important because of the following

_Theorem_. Every element of a vector space can be written uniquely as a linear combination of basis elements.

_Proof._ Consider an arbitrary _v_ in a vector space _V_ with basis {_v__j_}_j_. Because a basis is a spanning set, it follows trivially that we can write _v_ as a linear combination of basis elements, but we want to show that such a representation is unique. But uniqueness follows from the linear independence of the basis: suppose _v_ = Σ_j_ _c__j__v__j_ and that _v_ = Σ_j_ _d__j__v__j_. It turns out that the corresponding _c_ and _d_ coefficients have to be the same: Σ_j_ _c__j__v__j_ = Σ_j_ _d__j__v__j_ implies that Σ_j_ _c__j__v__j_ – _d__j__v__j_ equals the zero vector, which implies that Σ_j_ (_c__j_ – _d__j_)_v__j_ equals the zero vector, which (from linear independence) implies that ∀_j_ _c__j_ – _d__j_ = 0 and thus that ∀_j_ _c__j_ = _d__j_, yielding uniqueness, which is what I've been trying to tell you this entire time.

_Because_ (given a particular basis) we have a unique representation of every _v_ as a linear combination of basis elements, we can use the coefficients of that linear combination as coodinates and treat the vector as a list of numbers ... but that's just our convenience; the coordinates with respect to a different basis would be different, and the vector itself simply _is_.
