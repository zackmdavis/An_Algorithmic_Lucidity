Title: Blades
Date: 2012-09-29 18:17
Status: published
Category: mathematics
Tags: geometric algebra
Slug: blades

What is a _vector_ in Euclidean space? Some might say it's an entity characterized by possessing a _magnitude_ and a _direction_. But scholars of the geometric algebra (such as [Eric Chisolm](http://arxiv.org/abs/1205.5935) and [Dorst _et al._](http://www.geometricalgebra.net/)) tell us that it's better to decompose the idea of _direction_ into the two ideas of subspace _attitude_ (our vector's quality of living in a particular line) and _orientation_ (its quality of pointing in a particular direction in that line, and not the other). On this view, a vector is an _attitudinal oriented length element_. But having done this, it becomes inevitable that we should want to talk about attitudinal oriented _area_ (volume, 4-hypervolume, _&c._) elements. To this end we introduce the _outer_ or wedge product ∧ on vectors. It is _bilinear_, it is _anticommutative_ (swapping the order of arguments swaps the sign, so __a__∧__b__ = –__b__∧__a__), and that's all you need to know.

Suppose we have two vectors __a__ and __b__ in Euclidean space and also a basis for the subspace that the vectors live in, __e__1 and __e__2, so that we can write __a__ := a1__e__1 + a2__e__2 and __b__ := b1__e__1 + b2__e__2. Then the claim is that the outer product __a__∧__b__ can be said to represent a generalized vector (call it a _2-blade_—and in general, when we wedge _k_ vectors together, it's a _k_-blade) with a subspace attitude of the plane that our vectors live in and a magnitude equal to the area of the parallelogram spanned by them. Following Dorst _et al_., let's see what happens when we expand __a__∧__b__ in terms of our basis—

__a__∧__b__ = (a1__e__1 + a2__e__2)∧(b1__e__1 + b2__e__2)

= a1__e__1∧(b1__e__1 + b2__e__2) + a2__e__2∧(b1__e__1 + b2__e__2)

= a1__e__1∧b1__e__1 + a1__e__1∧b2__e__2 + a2__e__2∧b1__e__1 + a2__e__2∧b2__e__2

But the anticommutativity property implies that the outer product of a vector with itself is _zero_, because __e__∧__e__ = –__e__∧__e__. So we have

(a1b2 – a2b1)__e__1∧__e__2

It's a determinant! And since determinants tell us about the oriented volumes of parallelepipeds, we can see why these blades defined by this outer product are a sensible generalization of the _vector_ idea. And none can doubt that they shall play but ever such an essential role in our vaunted geometric algebra!
