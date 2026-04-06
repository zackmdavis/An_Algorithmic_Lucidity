Title: Computing the Arithmetic Derivative
Date: 2012-10-24 05:00
Status: published
Category: computing
Tags: Python
Slug: computing-the-arithmetic-derivative

Jurij Kovič's paper "[The Arithmetic Derivative and Antiderivative](https://cs.uwaterloo.ca/journals/JIS/VOL15/Kovic/kovic4.html)" contains a curious remark in Section 1.2. Having just stated the definition of the _logarithmic arithmetic derivative_ (_L_(_n_) = _n_′/_n_ = Σj _a__j_/_p__j_ where the prime mark indicates the arithmetic derivative, and Πi_p__i__a__i_ is the prime factorization of _n_), Kovič writes:

> The logarithmic derivative is an additive function _L_(_xy_) = _L_(_x_) + _L_(_y_) for any _x_, _y_ ∈ ℚ. Consequently, using a table of values _L_(_p_) = 1/_p_ (computed to sufficient decimal places!) and the formula _D_(_x_) = _L_(_x_)·_x_, it is easy to find _D_(_n_) for _n_ ∈ ℕ having all its prime factors in the table.

... a _table of values_? Did I read that correctly? Surely there must be some mistake; surely a paper published in 2012 can't expect us to rely on a printed table, for all the world as if we were John Napier in the seventeenth century! But never fear, dear reader, for the situation is easily rectified—with just a few lines of Python, you can take all the arithmetic derivatives you like on your own personal computing device.

Although first, we will need a function to find the prime factorization of a natural number. You can write your own, copy-paste [someone else's](http://glowingpython.blogspot.com/2011/07/prime-factor-decomposition-of-number.html), or (my personal favorite) use the subprocess module to call the system's _/usr/bin/factor_:

```
from subprocess import check_output

def factorize(n):
    if n == 0 or n == 1:
        return {}
    output = check_output(["factor", str(n)]).decode('utf-8')
    factors = list(map(int, output.split(": ")[1].split(' ')))
    factorization = {(f, factors.count(f)) for f in set(factors)}
    return factorization
```

But then coding the definition of the arithmetic derivative itself is easy:

```
def D(n):
    result = 0
    factorization = factorize(n)
    for p in factorization:
        term = 1
        term *= p[1]*p[0]**(p[1]-1)
        for q in factorization:
            if q is not p:
                term *= q[0]**q[1]
        result += term
    return result
```
