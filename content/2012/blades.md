Title: Blades
Date: 2012-09-29 18:17
Status: published
Category: mathematics
Tags: geometric algebra

What is a _vector_ in Euclidean space? Some might say it's an entity characterized by possessing a _magnitude_ and a _direction_. But scholars of the geometric algebra (such as [Eric Chisolm](http://arxiv.org/abs/1205.5935) and [Dorst _et al._](http://www.geometricalgebra.net/)) tell us that it's better to decompose the idea of _direction_ into the two ideas of subspace _attitude_ (our vector's quality of living in a particular line) and _orientation_ (its quality of pointing in a particular direction in that line, and not the other). On this view, a vector is an _attitudinal oriented length element_. But having done this, it becomes inevitable that we should want to talk about attitudinal oriented _area_ (volume, 4-hypervolume, _&c._) elements. To this end we introduce the _outer_ or wedge product ∧ on vectors. It is _bilinear_, it is _anticommutative_ (swapping the order of arguments swaps the sign, so $\vec{a}\wedge\vec{b} = -\vec{b}\wedge\vec{a}$), and that's all you need to know.

Suppose we have two vectors $\vec{a}$ and $\vec{b}$ in Euclidean space and also a basis for the subspace that the vectors live in, $\vec{e}_1$ and $\vec{e}_2$, so that we can write $\vec{a} := a_1\vec{e}_1 + a_2\vec{e}_2$ and $\vec{b} := b_1\vec{e}_1 + b_2\vec{e}_2$. Then the claim is that the outer product $\vec{a}\wedge\vec{b}$ can be said to represent a generalized vector (call it a _2-blade_—and in general, when we wedge _k_ vectors together, it's a _k_-blade) with a subspace attitude of the plane that our vectors live in and a magnitude equal to the area of the parallelogram spanned by them. Following Dorst _et al_., let's see what happens when we expand $\vec{a}\wedge\vec{b}$ in terms of our basis—

$$\vec{a}\wedge\vec{b} = (a_1\vec{e}_1 + a_2\vec{e}_2)\wedge(b_1\vec{e}_1 + b_2\vec{e}_2)$$

$$= a_1\vec{e}_1\wedge(b_1\vec{e}_1 + b_2\vec{e}_2) + a_2\vec{e}_2\wedge(b_1\vec{e}_1 + b_2\vec{e}_2)$$

$$= a_1\vec{e}_1\wedge b_1\vec{e}_1 + a_1\vec{e}_1\wedge b_2\vec{e}_2 + a_2\vec{e}_2\wedge b_1\vec{e}_1 + a_2\vec{e}_2\wedge b_2\vec{e}_2$$

But the anticommutativity property implies that the outer product of a vector with itself is _zero_, because $\vec{e}\wedge\vec{e} = -\vec{e}\wedge\vec{e}$. So we have

$$(a_1b_2 - a_2b_1)\vec{e}_1\wedge\vec{e}_2$$

It's a determinant! And since determinants tell us about the oriented volumes of parallelepipeds, we can see why these blades defined by this outer product are a sensible generalization of the _vector_ idea. And none can doubt that they shall play but ever such an essential role in our vaunted geometric algebra!
