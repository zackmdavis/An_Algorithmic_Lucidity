Title: Epiphenomenal Coordinates
Date: 2013-01-15 05:00
Status: published
Category: mathematics
Tags: linear algebra
Slug: epiphenomenal-coordinates

In the study of elementary linear algebra, unwary novices are often inclined to think of a vector as an ordered list of real numbers; to them, linear algebra is then conceived of as the study of multiplying matrices with column vectors. But this is a horribly impoverished perspective; we can do so much better for ourselves with a bit of abstraction and generality.

You _can_ think of arrows or lists of numbers if you want or if you must, but the true, ultimate meaning of a _vector space_ is ... well, anything that satisfies the vector space axioms. If you have things that you can "add" (meaning that we have an associative, commutative binary operation and we have inverse elements and an identity element with respect to this operation), and you can "multiply" these things by other things that come from a field (the "vectors" in the space and the "scalars" from the field play nicely together in a way that is distributive _&c._), then these things you that you have are a vector space over that field, and any of the theorems that we prove about vector spaces in general apply in full force to the things you have, which don't have to be lists of real numbers; they could be matrices or polynomials or functions or whatever.

Okay, so it _turns out_ that $n$-dimensional vector spaces are isomorphic to lists of $n$ numbers (elements of the appropriate field), but that's not part of our _fundamental_ notion of vectorness; it's something we can _prove_—

Let's say a set of $n$ elements $\{v_j\}_j$ from a vector space $V$ _span_ the space iff every element $v$ in the space can be written as a linear combination of elements in the set: $v = \sum_j c_j v_j$ for some coefficients $c_j$. Let's also say that a set of vector space elements is _linearly independent_ iff the only way a linear combination of them can be the zero vector is if all the coefficients are zero: $\sum_j c_j v_j = \vec{0}$ implies $\forall j\, c_j = 0$. We say a set is a _basis_ if and only if it spans the space and is linearly independent. Bases are important because of the following

_Theorem_. Every element of a vector space can be written uniquely as a linear combination of basis elements.

_Proof._ Consider an arbitrary $v$ in a vector space $V$ with basis $\{v_j\}_j$. Because a basis is a spanning set, it follows trivially that we can write $v$ as a linear combination of basis elements, but we want to show that such a representation is unique. But uniqueness follows from the linear independence of the basis: suppose $v = \sum_j c_j v_j$ and that $v = \sum_j d_j v_j$. It turns out that the corresponding $c$ and $d$ coefficients have to be the same: $\sum_j c_j v_j = \sum_j d_j v_j$ implies that $\sum_j c_j v_j - d_j v_j$ equals the zero vector, which implies that $\sum_j (c_j - d_j) v_j$ equals the zero vector, which (from linear independence) implies that $\forall j\, c_j - d_j = 0$ and thus that $\forall j\, c_j = d_j$, yielding uniqueness, which is what I've been trying to tell you this entire time.

_Because_ (given a particular basis) we have a unique representation of every $v$ as a linear combination of basis elements, we can use the coefficients of that linear combination as coodinates and treat the vector as a list of numbers ... but that's just our convenience; the coordinates with respect to a different basis would be different, and the vector itself simply _is_.
