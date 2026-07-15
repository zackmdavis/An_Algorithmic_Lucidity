Title: "Being Wrong Doesn't Mean You're Stupid and Bad (Probably)"
Date: 2019-06-29 16:58
Status: published
Category: philosophy
Tags: Bayes-structure of the universe

[(originally published at _Less Wrong_)](https://www.lesswrong.com/posts/6dmKBjc7XarcQMRYW/being-wrong-doesn-t-mean-you-re-stupid-and-bad-probably)

Sometimes, people are reluctant to admit that they were wrong about something, because they're afraid that "You are wrong about this" carries inextricable connotations of "You are stupid and bad." But this behavior is, itself, wrong, for _at least_ two reasons.

First, because it's evidential decision theory. The so-called "rationalist" "community" has a lot of [cached](https://www.lesswrong.com/posts/2MD3NMLBPCqPfnfre/cached-thoughts) clichés about this! A blank map does not correspond to a blank territory. [What's true is already so](https://www.lesswrong.com/posts/HYWhKXRsMAyvRKRYz/you-can-face-reality); owning up to it doesn't make it worse. Refusing to go to the doctor (thereby _avoiding encountering evidence_ that you're sick) doesn't keep you healthy.

_If_ being wrong means that you're stupid and bad, then preventing yourself from _knowing_ that you were wrong doesn't stop you from being stupid and bad _in reality_. It just prevents you from _knowing_ that you're stupid and bad—which is an important fact to know (if it's true), because if you don't _know_ that you're stupid and bad, then it probably won't occur to you to even _look_ for possible interventions to make yourself _less_ stupid and _less_ bad.

Second, while "You are wrong about this" _is_ evidence for the "You are stupid and bad" hypothesis if stupid and bad people are more likely to be wrong, I claim that it's _very weak_ evidence. (Although it's possible that I'm wrong about this—and if I'm wrong, it's furthermore possible that the _reason_ I'm wrong is because I'm stupid and bad.)

Exactly _how weak_ evidence is it? It's hard to guess directly, but fortunately, we can use probability theory to reduce the claim into more "atomic" conditional and prior probabilities that might be easier to estimate!

Let $W$ represent the proposition "You are wrong about something", $S$ represent the proposition "You are stupid", and $B$ represent the proposition "You are bad."

By Bayes's theorem, the probability that you are stupid and bad given that you're wrong about something is given by—

$$P(S,B|W)=\frac{P(W|S,B)P(S,B)}{P(W|S,B)P(S,B)+P(W|S, \neg B)P(S, \neg B)+P(W| \neg S,B)P( \neg S,B)+P(W| \neg S, \neg B)P( \neg S, \neg B)}$$

For the purposes of this calculation, let's assume that badness and stupidity are statistically independent. I doubt this is true in the real world, but because I'm stupid and bad (at math), I want that simplifying assumption to make the algebra easier for me. That lets us unpack the conjunctions, giving us—

$$P(S,B|W)=\frac{P(W|S,B)P(S)P(B)}{P(W|S,B)P(S)P(B)+P(W|S, \neg B)P(S)P(\neg B)+P(W| \neg S,B)P( \neg S)P(B)+P(W| \neg S, \neg B)P( \neg S)P(\neg B)}$$

This expression has six degrees of freedom: $P(S)$, $P(B)$, $P(W|S,B)$, $P(W|S, \neg B)$, $P(W|\neg S,B)$, $P(W|\neg S, \neg B)$. Arguing about the values of these six individual parameters is probably more productive than arguing about the value of $P(S,B|W)$ directly!

Suppose half the people are stupid ($P(S) = 0.5$), one-tenth of people are bad ($P(B) = 0.1$), and that most people are wrong, but that being stupid or bad each make you somewhat more likely to be wrong, to the tune of $P(W|\neg S, \neg B) = 0.8$, $P(W|S, \neg B) = P(W|\neg S,B) = 0.85$, and $P(W|S,B) = 0.9$. So our posterior probabilty that someone is stupid and bad given that they were wrong once is

$$P(S,B|W) = \frac{(0.9)(0.5)(0.1)}{(0.9)(0.5)(0.1)+(0.85)(0.5)(0.9)+(0.85)(0.5)(0.1)+(0.8)(0.5)(0.9)}$$

$$\approx 0.0542$$

But the base rate of being stupid and bad is (0.1)(0.5) = 0.05. Learning that someone was wrong only raised our probability that they are stupid and bad by 0.0042. That's a small number that you shouldn't worry about!
