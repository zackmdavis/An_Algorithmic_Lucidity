Title: Summing the Multinomial Coefficients
Date: 2012-09-08 09:46
Status: published
Category: mathematics
Tags: combinatorics

The sum of binomial coefficients $$\sum_{j=0}^n {n \choose j}$$ equals $2^n$, because $${n \choose j}$$ is the number of ways to pick _j_ elements from a set of size _n_, and $2^n$ is the size of the powerset, the set of all subsets, of a set of size _n_: the sum, over all subset sizes, of the number of ways to choose subsets of a given size, is equal to the number of subsets. You can also see this using the binomial theorem itself:

$$2^{n} = (1 + 1)^{n} = \sum_{j=0}^{n} {n \choose j} 1^{j}1^{n-j} = \sum_{j=0}^{n} {n \choose j}$$

But of course there's nothing special about _two_; it works for multinomial coefficients just the same. The sum, over all _m_-tuples of subset sizes, of the number of ways to split a set of size _n_ into subsets of sizes given by the _m_-tuple, is equal to the number of ways to split a set of size _n_ into _m_ subsets (_viz._, _mn_).
