Title: The True Secret About Conjugate Roots and Field Automorphisms
Date: 2012-09-18 14:25
Status: published
Category: mathematics
Tags: algebra
Slug: the-true-secret-about-conjugate-roots-and-field-automorphisms

In the study of the elementary algebra, one occasionally hears of the conjugate roots theorem, which says that if _z0_ is a root of a polynomial with real coefficients, then its complex conjugate is also a root. Or if you prefer, nonreal roots come in conjugate pairs. It also works in the other direction: if nonreal roots of a polynomial come in conjugate pairs, then the polynomial has real coefficients, because the purely imaginary parts cancel when you do the algebra: (_x_ – (_a_ + _bi_))(_x_ – (_a_ – _bi_)) = _x_2 – _x_(_a_ + _bi_) – _x_(_a_ – _bi_) + (_a_2 – (_bi_)2) = _x_2 – 2_ax_ + _a_2 + _b_2.

There's also this idea that conjugation is the unique nontrivial "well-behaved" _automorphism_ on ℂ, a map from ℂ to itself that respects addition and multiplication: the sum (respectively product) of the conjugates is the conjugate of the sum (respectively product). The complex numbers are _symmetrical_ around the real axis in a way that they're not around the imaginary axis: while _i_ and –_i_ are different from _each other_, you can't "tell which is which" because they _behave_ the same way. Contrast to 1 and –1, which _do_ behave differently: if someone put either 1 or –1 in a box, but they wouldn't tell you which, but they _were_ willing to tell you that "The number in the box squares to itself," then you could figure out that the number in the box was 1, because –1 doesn't do that.

The existence of these two ideas (the conjugate roots theorem and conjugation-as-automorphism) can't possibly be a coincidence; there must be some sense in which nonreal roots of real-coefficient polynomials come in conjugate pairs _because_ the polynomial "can't tell" "which is which". But it would be unsatisfying to just say this much and nothing more ("_Theorem_: That can't possibly be a coincidence. _Proof_ ...??"); we want to say something much more general and precise. And in fact, we can—

Say that _L_ is a field, and that _K_ is a field that lives inside _L_, and that σ is a member of the group of field automorphisms of _L_ that leave _K_ alone (that is, map all members of _K_ to themselves). Then we can show that

_Theorem (generalized conjugate roots theorem)._ If _z0_ is a root of a polynomial with coefficients in _K_, then σ(_z0_) is too.

_Proof._ Let $$P(z) := \sum\_j a\_jz^{j}$$ and suppose _P_(_z0_) = 0. Then consider the value of _P_(σ(_z_0)). Precisely because σ respects multiplication, we have $$\sum\_j a\_j\sigma(z\_{0})^{j} = \sum\_j a\_j\sigma(z\_{0}^{j})$$ and because σ doesn't disturb anything in _K_, that's the same as $$\sum\_j \sigma(a\_j z\_{0}^{j})$$ (because _a_σ(_z_) = σ(_a_)σ(_z_) = σ(_az_)), and because σ respects addition, that's also the same as $$\sigma(\sum\_j a\_j z\_{0}^{j})$$. But $$\sigma(\sum\_j a\_j z\_{0}^{j}) = \sigma(0)$$, and σ(0) has to be zero for the automorphism to work. So _P_(σ(_z0_)) is zero, but that's what I've been trying to tell you this entire time.
