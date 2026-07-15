Title: Eigencritters
Date: 2012-12-03 05:00
Status: published
Category: mathematics
Tags: linear algebra

Say we have a linear transformation $A$ and some nonzero vector $\vec{v}$, and suppose that $A\vec{v} = \lambda\vec{v}$ for some scalar λ. This is a very special situation; we say that λ is an _eigenvalue_ of A corresponding to the _eigenvector_ $\vec{v}$.

How can we find eigenvalues? Here's one criterion. If $A\vec{v} = \lambda\vec{v}$ for some unknown λ, we at least know that $A\vec{v} - \lambda\vec{v}$ equals the zero vector, which implies that the linear transformation $(A - \lambda I)$ maps $\vec{v}$ to zero. If $(A - \lambda I)$ maps $\vec{v}$ to zero, then it must have a nontrivial kernel, which is to say that it can't be invertible, and this happens exactly when its determinant is zero, because the determinant measures how the linear transformation distorts (signed) areas (volumes, 4-hypervolumes, _&c._), so if the determinant is zero, it means you've lost a dimension; the space has been smashed infinitely thin. But $\det(A - \lambda I)$ is a polynomial in λ, and so the roots of that polynomial are exactly the eigenvalues of $A$.
