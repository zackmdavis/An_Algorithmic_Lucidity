Title: Colon-Equals
Date: 2012-10-05 05:00
Status: published
Category: computing
Tags: notation
Slug: colon-equals

Sometimes I think it's sad that the most popular programming languages use "=" for assignment rather than ":=" (like Pascal). Equality is a symmetrical relationship: "_a_ equals _b_" means that _a_ and _b_ are the same thing or have the same value, and this is clearly the same as saying that "_b_ equals _a_". Assignment isn't like that: putting the value _b_ in a box named _a_ isn't the same as putting the value _a_ in a box named _b_!—surely an asymmetrical operation deserves an asymmetrical notation? Okay, so it is an extra character, but any decent editor can be configured to save you the keystroke.

I'd like to see the colon-equals assignment symbol more often in math, too. For example, shouldn't we be writing lower indices of summation like this?—

$$!\sum\_{j:=0}^n f(j)$$

—the rationale being that the text under the sigma _isn't_ asserting that _j_ _equals_ zero, but rather that _j_ is _assigned_ zero as the initial index value of what is, in fact, a for loop:

```
sum = 0;
for (int j=0; j<=n; j++)
{
    sum += f(j);
}
return sum;
```
