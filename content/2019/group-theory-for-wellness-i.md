Title: Group Theory for Wellness I
Date: 2019-05-18 15:07
Status: published
Category: mathematics
Tags: algebra, theme week

(Part of [Math and Wellness Month](http://zackmdavis.net/blog/2019/05/may-is-math-and-wellness-month/).)

Groups! A group is a set with an associative binary operation such that there exists an identity element and inverse elements! And my _favorite_ thing about groups is that all the time that you spend thinking about groups, is time that you're _not_ thinking about pain, betrayal, politics, or moral uncertainty!

Groups have subgroups, which you can totally guess just from the name are subsets of the group that themselves satisfy the group axioms!

The _order_ of a finite group is its number of elements, but this is not to be confused with the order of an _element_ of a group, which is the smallest integer such that the element raised to that power equals the identity! Both senses of "order" are indicated with vertical bars like an absolute value (|_G_|, |_a_|).

Lagrange proved that the order of a subgroup divides the order of the group of which it is a subgroup! History remains ignorant of how often Lagrange cried.

To show that a nonempty subset _H_ of a group is in fact a subgroup, it suffices to show that if _x_, _y_ ∈ _H_, then _xy_⁻¹ ∈ _H_.

Exercise #6 in §2.1 of Dummit and Foote _Abstract Algebra_ (3rd ed'n) asks us to prove that if _G_ is a commutative ("abelian") group, then the _torsion subgroup_ {_g_ ∈ _G_ | |g| < ∞} is in fact a subgroup. I argue as follows: we need to show that if _x_ and _y_ have finite order, then so does _xy_⁻¹, that is, that (_xy_⁻¹)^_n_ equals the identity. But (_xy_⁻¹)^_n_ equals (_xy_⁻¹)(_xy_⁻¹)...(_xy_⁻¹), "_n_ times"—that is, pretend _n_ ≥ 3, and pretend that instead of "..." I wrote zero or more extra copies of "(_xy_⁻¹)" so that the expression has _n_ factors. (I usually dislike it when authors use ellipsis notation, which feels so icky and informal compared to a nice Π or Σ, but let me have this one.) Because group operations are associative, we can drop the parens to get _xy_⁻¹ _xy_⁻¹ ... _xy_⁻¹. And because we said the group was commutative, we can reörder the factors to get _xxx_..._y⁻¹y⁻¹y_⁻¹, and _then_ we can consolidate into powers to get _x_^_n_ y^(−_n_)—but that's the identity if _n_ is the least common multiple of |_x_| and |_y_|, which means that _xy_⁻¹ has finite order, which is what I've been trying to tell you this entire time.
