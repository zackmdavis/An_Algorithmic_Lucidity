Title: Interpolating Between Vectorized Green's Theorems
Date: 2012-06-21 20:09
Status: published
Category: mathematics
Tags: calculus
Slug: interpolating-between-vectorized-greens-theorems

Green's theorem says that (subject to some very reasonable conditions that we need not concern ourselves with here) the counterclockwise line integral of the vector field __F__ = [P Q] around the boundary of a region is equal to the double intregral of $$\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}$$ over the region itself. It's natural to think of it as a special case of Stokes's theorem in the case of a plane. We can also think of the line integral as the integral of the inner product of the vector field with the unit tangent, leading us to write Green's theorem like this:

$$! \oint\_{\partial D}\vec{\mathbf{F}}\cdot\vec{\mathbf{T}}\, ds=\iint\_{D}(\mathrm{curl\,}\vec{\mathbf{F}})\cdot\vec{\mathbf{k}}\, ds$$

But some texts (I have Mardsen and Tromba's _Vector Calculus_ and Stewart's _Calculus: Early Transcendentals_ in my possession; undoubtedly there are others) point out that we can also think of Green's theorem as a special case of the divergence theorem! Suppose we take the integral of the inner product of the vector field with the outward-facing unit normal (instead of the unit tangent)—it turns out that

$$!\oint\_{\partial D}\vec{\mathbf{F}}\cdot\vec{\mathbf{n}}\, ds=\iint\_{D}\mathrm{div\,}\vec{\mathbf{F}} ds$$

—which suggests that there's some deep fundamental sense in which Stokes's theorem and the divergence theorem are really just _mere surface manifestations of one and the same underlying idea_! (I'm told that it's called the generalized Stokes's theorem, but regrettably I don't know the details yet.)

But here's something I thought was pretty. We have these two equations, one of which involves the unit tangent vector, and one of which involves the unit normal vector. (It's actually pointing in the opposite direction of the unit normal that we use to define the Frenet frame, which one might argue is an unfortunate clash of conventions, but whatever.) So my linear-algebraic intuitions say: hey, why not smoosh them together in a linear combination? (Making linear combinations is just what you _do_ when you see orthogonal unit vectors, right?) Then it's like we're interpolating between the two forms of Green's theorem. Specifically, let θ be a constant. Then we have

$$!\oint\_{\partial D}\vec{\mathbf{F}}\cdot((\sin\theta)\vec{\mathbf{T}}+(\cos\theta)\vec{\mathbf{n}})\, ds$$ (component decomposition of some unit vector)

$$!=\oint\_{\partial D}\vec{\mathbf{F}}\cdot(\sin\theta)\vec{\mathbf{T}}+\vec{\mathbf{F}}\cdot(\cos\theta)\vec{\mathbf{n}}\, ds$$

(inner product distributes over vector addition)

$$!=(\sin\theta)\oint\_{\partial D}\vec{\mathbf{F}}\cdot\vec{\mathbf{T}}\, ds+(\cos\theta)\oint\_{\partial D}\vec{\mathbf{F}}\cdot\vec{\mathbf{n}}\, ds$$

(linearity of integrals, bilinearity of inner product)

$$!=(\sin\theta)\iint\_{D}(\mathrm{curl\,}\vec{\mathbf{F}})\cdot\vec{\mathbf{k}}\, dA+(\cos\theta)\iint\_{D}\mathrm{div\,}\vec{\mathbf{F}} dA$$

(vectorized Green's theorem)

$$!=(\sin\theta)\iint\_{D}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\, dA+(\cos\theta)\iint\_{D}\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}\right)dA$$

(planar curl and divergence)

$$!=\iint\_{D}(\cos\theta)\frac{\partial P}{\partial x}+(\sin\theta)\frac{\partial Q}{\partial x}-(\sin\theta)\frac{\partial P}{\partial y}+(\cos\theta)\frac{\partial Q}{\partial y}\, dA$$

(linearity of integrals)

Isn't that great!? Nor is it a mere coincidence that the coefficients in the final line resemble the entries of the two-by-two matrix representing a counterclockwise rotation by θ. Ideally, we would then generalize this to an arbitrary number of dimensions and gain true insight into the generalized Stokes's theorem, and thus, a facet of _the nature of reality itself._

But I'm not there yet.
