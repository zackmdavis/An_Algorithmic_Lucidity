Title: Inclusion, Exclusion
Date: 2012-09-09 05:00
Status: published
Category: mathematics
Tags: combinatorics
Slug: inclusion-exclusion

In this modern day and age, it simply cannot be doubted that it is of the very utmost importance that we find the size of the union of some sets. One might try just adding the sizes of all the sets, but that's not correct, because then one would be double-counting the elements that appear in more than one set. But it's a good start. One might then think that one could _begin_ by adding the sizes of the sets, but then _subtract_ the sizes of the intersections of each pair of sets, in order to correct for the double-counting. But this is also incorrect, because then what about the elements that appear in _three_ sets and had thus initially been triple-counted?—after subtracting the pairwise intersections, these elements haven't been included in the count at all! So one realizes that one must then _add_ the sizes of the triplewise intersections ...

And in one of the dark recesses of the human mind, untouched by outside light or sound, silent and unyielding to the invidious scrutiny of introspection and cognitive science—a conjecture is formed—

_The size of the union of_ n _sets is given by the alternating (starting from positive) sum of the sums of the sizes of all_ j_-way intersections amongst the sets from_ j_:=1 to_ n_!_
(_N.b._, the exclamation mark indicates an excited tone, not "factorial".)

This conjecture turns out to be entirely correct, as demonstrated in the following

_Theorem ([Inclusion–Exclusion Principle](http://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle))_. $$\left|\bigcup\_{i=1}^{n}A\_{i}\right|=\sum\_{j=1}^{n}(-1)^{j+1}\left(\sum\_{S\subset\mathcal{P}(\{A\_{i}\});|S|=j}\left|\bigcap\_{A\_{s}\in S}A\_{s}\right|\right)$$

_Proof._ By induction.

_(Basis.)_ |A1 ∪ A2| = |A1| + |A2| – |A1 ∩ A2|

_(Induction.)_ We want to show that _given_ that we can express a union of _n_ sets using the proposed method, _then_ we can do the same for a union of _n_+1 sets. From the basis, we can write:

$$\left|\left(\bigcup\_{i=1}^{n}A\_{i}\right)\cup A\_{n+1}\right|=\left|\bigcup\_{i=1}^{n}A\_{i}\right| + |A\_{n+1}|-\left| \left(\bigcup\_{i=1}^{n}A\_{i}\right) \cap A\_{n+1} \right|.$$

Our inductive hypothesis says that the first term on the right side can be written as our proposed sum of appropriately signed sizes of intersections. Also, we can distribute the intersection-with-An+1 over the union in the last term on the right side and then use the inductive hypothesis again to likewise rewrite _that_ term as a sum of appropriately signed sizes of intersections. But then notice that we have all the terms we need, and that the signs are correct as well. So this is what I've been trying to tell you this whole time.
