Title: <em><strong>[RETRACTED]</strong></em> Introducing the Fractional Arithmetic Derivative
Date: 2012-10-03 12:30
Status: published
Category: mathematics
Slug: introducing-the-fractional-arithmetic-derivative

[__NOTICE__: _The conclusion of this post is hereby __retracted___ because it turns out that the proposed definition of a "fractional arithmetic derivative" doesn't actually make sense. It fails to meet the basic decideratum of corresponding with an iterated [arithmetic derivative](http://en.wikipedia.org/wiki/Arithmetic_derivative). _E.g._, consider that 225″ = (225′)′ = ((32·52)′)′ = (2·3·52 + 32·2·5)′ = (150 + 90)′ = 240′ = (24·3·5)′ = 4·23·3·5 + 24·5 + 24·3 = 480 + 80 + 48 = 608. Whereas, under the proposed definition we would _allegedly_ equivalently have 225(2) = (2!·30·52 + 32·2!·50) = 50 + 18 = 68. I apologize to anyone who read the original post (??) who was thereby misled. The original post follows (with the erroneous section struck through).]

_Wikipedia_ [informs us of](http://en.wikipedia.org/wiki/Arithmetic_derivative) the idea of an _arithmetic derivative_—personally, I think this is a terrible name because it doesn't seem to be a rate of change of anything, but the motivation is clear enough, so let's go with it. It's a function on the natural numbers which we'll denote with the prime mark (" ′ "—the name of this symbol is not to be confused with the name for positive integers with exactly two divisors, which are also of—forgive me—"prime" importance in this discussion). It works like this: 0′ is 0, 1′ is 0, _p_′ is 1 for any prime number _p_, and the composite numbers get filled in with the _product rule_ (_ab_)′ = _a_′_b_ + _ab_′ (hence the "derivative" moniker).

For prime powers, the product rule degenerates into a _power rule_:

$$!(p^a)' = \sum\_{j:=1}^{a} 1 \cdot p^{a-1} = ap^{a-1}$$

And this in turn makes it easy to compute the arithmetic derivative in general. Say that _n_∈ℕ has the prime factorization Πi _p__i__a__i_. Then—

$$!n' = \sum\_{i} a\_{i}p\_{i}^{a\_{i}-1} \prod\_{j:\neq i} p\_{j}^{a\_{j}} = \sum\_{i} a\_{i}\frac{n}{p\_{i}} = n \sum\_{i} \frac{a\_{i}}{p\_{i}}$$

Arithmetic derivatives for small natural numbers are given as [sequence A003415](http://oeis.org/A003415) in the _Online Encyclopedia of Integer Sequences_.

Some generalizations of this arithmetic derivative idea are discussed online (_e.g._, they say you can extend it to rational numbers using the familiar _quotient rule_), but (to my surprise) I didn't see any mentions of the obviously compelling idea of a _fractional arithmetic derivative_ (in analogy to the [fractional calculus](http://en.wikipedia.org/wiki/Fractional_calculus)). ~~Repeated applications of the power rule for a prime power give us~~

$$!(p^{a})^{(k)} = \frac{a!}{(a-k)!}p^{a-k}$$

~~where the superscript parenthetical _k_ indicates the _k_th arithmetic derivative for natural number _k_. But then if we just swap out those factorials for their gamma-function equivalents, we should have a _q_th power rule for real _q_—~~

$$!(p^{a})^{(q)} = \frac{\Gamma(a+1)}{\Gamma(a-q+1)}p^{a-q}$$

~~which in turn should give us a "fractional" _q_th arithmetic derivative for natural numbers:~~

$$!n^{(q)} = \sum\_{i} \frac{\Gamma(a\_{i}+1)}{\Gamma(a\_i-q+1)} \frac{n}{p\_{i}^{q}}$$

~~So this is a cute definition that seems to work, but what can we _do_ with it? At time of writing I can only demur that further research is needed.~~
