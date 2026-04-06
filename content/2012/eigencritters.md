Title: Eigencritters
Date: 2012-12-03 05:00
Status: published
Category: mathematics
Tags: linear algebra
Slug: eigencritters

Say we have a linear transformation _A_ and some nonzero vector __v__, and suppose that _A___v__ = λ__v__ for some scalar λ. This is a very special situation; we say that λ is an _eigenvalue_ of A corresponding to the _eigenvector_ __v__.

How can we find eigenvalues? Here's one criterion. If _A___v__ = λ__v__ for some unknown λ, we at least know that _A___v__ – λ__v__ equals the zero vector, which implies that the linear transformation (_A_ – λ_I_) maps __v__ to zero. If (_A_ – λ_I_) maps __v__ to zero, then it must have a nontrivial kernel, which is to say that it can't be invertible, and this happens exactly when its determinant is zero, because the determinant measures how the linear transformation distorts (signed) areas (volumes, 4-hypervolumes, _&c._), so if the determinant is zero, it means you've lost a dimension; the space has been smashed infinitely thin. But det(_A_ – λ_I_) is a polynomial in λ, and so the roots of that polynomial are exactly the eigenvalues of _A_.
