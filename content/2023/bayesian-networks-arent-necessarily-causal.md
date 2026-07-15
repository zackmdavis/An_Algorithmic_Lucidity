Title: Bayesian Networks Aren’t Necessarily Causal
Date: 2023-05-13 18:42
Status: published
Category: mathematics
Tags: statistics, Bayes-structure of the universe

[(originally published at _Less Wrong_)](https://www.lesswrong.com/posts/qPrPNakJBq23muf4n/bayesian-networks-aren-t-necessarily-causal)

As a casual formal epistemology fan, you've probably [heard that the philosophical notion of causality can be formalized in terms of Bayesian networks](https://www.lesswrong.com/posts/hzuSDMx7pd2uxFc5w/causal-diagrams-and-causal-models)—but also as a casual formal epistemology fan, [you also probably don't](https://www.lesswrong.com/posts/tp4rEtQqRshPavZsr/learn-bayes-nets) know the details all that well.

One day, while going through the family archives, you come across a meticulously maintained dataset describing a joint probability distribution over four variables: whether it rained that day, whether the sprinkler was on, whether the sidewalk was wet, and whether the sidewalk was slippery. The distribution is specified in this table (using the abbreviated labels "rain", "slippery", "sprinkler", and "wet"):

$$\begin{matrix} \mathrm{rain}=\mathrm{True},\, \mathrm{slippery}=\mathrm{True},\, \mathrm{sprinkler}=\mathrm{True},\, \mathrm{wet}=\mathrm{False} & \frac{1}{140000} \approx 0.0000 \cr \mathrm{rain}=\mathrm{False},\, \mathrm{slippery}=\mathrm{True},\, \mathrm{sprinkler}=\mathrm{True},\, \mathrm{wet}=\mathrm{False} & \frac{3}{14000} \approx 0.0002 \cr \mathrm{rain}=\mathrm{True},\, \mathrm{slippery}=\mathrm{True},\, \mathrm{sprinkler}=\mathrm{False},\, \mathrm{wet}=\mathrm{False} & \frac{3}{14000} \approx 0.0002 \cr \mathrm{rain}=\mathrm{True},\, \mathrm{slippery}=\mathrm{False},\, \mathrm{sprinkler}=\mathrm{True},\, \mathrm{wet}=\mathrm{False} & \frac{99}{140000} \approx 0.0007 \cr \mathrm{rain}=\mathrm{False},\, \mathrm{slippery}=\mathrm{False},\, \mathrm{sprinkler}=\mathrm{False},\, \mathrm{wet}=\mathrm{True} & \frac{9}{5600} \approx 0.0016 \cr \mathrm{rain}=\mathrm{False},\, \mathrm{slippery}=\mathrm{True},\, \mathrm{sprinkler}=\mathrm{False},\, \mathrm{wet}=\mathrm{True} & \frac{27}{5600} \approx 0.0048 \cr \mathrm{rain}=\mathrm{False},\, \mathrm{slippery}=\mathrm{True},\, \mathrm{sprinkler}=\mathrm{False},\, \mathrm{wet}=\mathrm{False} & \frac{891}{140000} \approx 0.0064 \cr \mathrm{rain}=\mathrm{True},\, \mathrm{slippery}=\mathrm{False},\, \mathrm{sprinkler}=\mathrm{True},\, \mathrm{wet}=\mathrm{True} & \frac{7}{800} \approx 0.0088 \cr \mathrm{rain}=\mathrm{False},\, \mathrm{slippery}=\mathrm{False},\, \mathrm{sprinkler}=\mathrm{True},\, \mathrm{wet}=\mathrm{False} & \frac{297}{14000} \approx 0.0212 \cr \mathrm{rain}=\mathrm{True},\, \mathrm{slippery}=\mathrm{False},\, \mathrm{sprinkler}=\mathrm{False},\, \mathrm{wet}=\mathrm{False} & \frac{297}{14000} \approx 0.0212 \cr \mathrm{rain}=\mathrm{False},\, \mathrm{slippery}=\mathrm{False},\, \mathrm{sprinkler}=\mathrm{True},\, \mathrm{wet}=\mathrm{True} & \frac{3}{140} \approx 0.0214 \cr \mathrm{rain}=\mathrm{True},\, \mathrm{slippery}=\mathrm{True},\, \mathrm{sprinkler}=\mathrm{True},\, \mathrm{wet}=\mathrm{True} & \frac{21}{800} \approx 0.0262 \cr \mathrm{rain}=\mathrm{True},\, \mathrm{slippery}=\mathrm{False},\, \mathrm{sprinkler}=\mathrm{False},\, \mathrm{wet}=\mathrm{True} & \frac{27}{560} \approx 0.0482 \cr \mathrm{rain}=\mathrm{False},\, \mathrm{slippery}=\mathrm{True},\, \mathrm{sprinkler}=\mathrm{True},\, \mathrm{wet}=\mathrm{True} & \frac{9}{140} \approx 0.0643 \cr \mathrm{rain}=\mathrm{True},\, \mathrm{slippery}=\mathrm{True},\, \mathrm{sprinkler}=\mathrm{False},\, \mathrm{wet}=\mathrm{True} & \frac{81}{560} \approx 0.1446 \cr \mathrm{rain}=\mathrm{False},\, \mathrm{slippery}=\mathrm{False},\, \mathrm{sprinkler}=\mathrm{False},\, \mathrm{wet}=\mathrm{False} & \frac{88209}{140000} \approx 0.6301 \cr \end{matrix}$$

(You wonder what happened that one day out of 140,000 when it rained, and the sprinkler was on, and the sidewalk was slippery but not wet. Did—did someone put a tarp up to keep the sidewalk dry, but also spill slippery oil, which didn't count as being relevantly "wet"? Also, 140,000 days is more than 383 years—were "sprinklers" even a thing in the year 1640 C.E.? You quickly put these questions out of your mind: it is not your place to question the correctness of the family archives.)

You're slightly uncomfortable with this unwieldy sixteen-row table. You think that there must be some other way to represent the same information, while making it clearer that it's not a coincidence that rain and wet sidewalks tend to co-occur.

You've read that Bayesian networks "factorize" an unwieldly joint probability distribution into a number of more compact _conditional_ probability distributions, related by a directed acyclic graph, where the arrows point from "cause" to "effect". (Even a casual formal epistemology fan knows _that_ much.) The graph represents knowledge that each variable is [conditionally independent](https://en.wikipedia.org/wiki/Conditional_independence) of its non-descendants given its parents, which enables "local" computations: given the values of just a variable's parents in the graph, we can compute a conditional distribution for that variable, without needing to consider what is known about other variables elsewhere in the graph ...

You've _read_ that, but you've never actually done it before! You decide that constructing a Bayesian network to represent this distribution will be a useful exercise.

To start, you re-label the variables for brevity. (On a whim, you assign indices in reverse-alphabetical order: $X_1$ = wet, $X_2$ = sprinkler, $X_3$ = slippery, $X_4$ = rain.)

$$\begin{matrix} X_1=\mathrm{False},\: X_2=\mathrm{True},\: X_3=\mathrm{True},\: X_4=\mathrm{True} & \frac{1}{140000} \cr X_1=\mathrm{False},\: X_2=\mathrm{True},\: X_3=\mathrm{True},\: X_4=\mathrm{False} & \frac{3}{14000} \cr X_1=\mathrm{False},\: X_2=\mathrm{False},\: X_3=\mathrm{True},\: X_4=\mathrm{True} & \frac{3}{14000} \cr X_1=\mathrm{False},\: X_2=\mathrm{True},\: X_3=\mathrm{False},\: X_4=\mathrm{True} & \frac{99}{140000} \cr X_1=\mathrm{True},\: X_2=\mathrm{False},\: X_3=\mathrm{False},\: X_4=\mathrm{False} & \frac{9}{5600} \cr X_1=\mathrm{True},\: X_2=\mathrm{False},\: X_3=\mathrm{True},\: X_4=\mathrm{False} & \frac{27}{5600} \cr X_1=\mathrm{False},\: X_2=\mathrm{False},\: X_3=\mathrm{True},\: X_4=\mathrm{False} & \frac{891}{140000} \cr X_1=\mathrm{True},\: X_2=\mathrm{True},\: X_3=\mathrm{False},\: X_4=\mathrm{True} & \frac{7}{800} \cr X_1=\mathrm{False},\: X_2=\mathrm{True},\: X_3=\mathrm{False},\: X_4=\mathrm{False} & \frac{297}{14000} \cr X_1=\mathrm{False},\: X_2=\mathrm{False},\: X_3=\mathrm{False},\: X_4=\mathrm{True} & \frac{297}{14000} \cr X_1=\mathrm{True},\: X_2=\mathrm{True},\: X_3=\mathrm{False},\: X_4=\mathrm{False} & \frac{3}{140} \cr X_1=\mathrm{True},\: X_2=\mathrm{True},\: X_3=\mathrm{True},\: X_4=\mathrm{True} & \frac{21}{800} \cr X_1=\mathrm{True},\: X_2=\mathrm{False},\: X_3=\mathrm{False},\: X_4=\mathrm{True} & \frac{27}{560} \cr X_1=\mathrm{True},\: X_2=\mathrm{True},\: X_3=\mathrm{True},\: X_4=\mathrm{False} & \frac{9}{140} \cr X_1=\mathrm{True},\: X_2=\mathrm{False},\: X_3=\mathrm{True},\: X_4=\mathrm{True} & \frac{81}{560} \cr X_1=\mathrm{False},\: X_2=\mathrm{False},\: X_3=\mathrm{False},\: X_4=\mathrm{False} & \frac{88209}{140000} \cr \end{matrix}$$

Now, how do you go about building a Bayesian network? As a casual formal epistemology fan, you are proud to own a copy of [the book by Daphne Koller and the other guy](https://mitpress.mit.edu/9780262013192/probabilistic-graphical-models/), which explains how to do this in—you leaf through the pages—probably §3.4, "From Distributions to Graphs"?—looks like ... _here_, in Algorithm 3.2. It says to start with an empty graph, and it talks about random variables, and setting directed edges in the graph, and you know from chapter 2 that the ⟂ and | characters are used to indicate conditional independence. That has to be it.

![](https://i.imgur.com/iSmD6of.jpg)

(As a casual formal epistemology fan, you haven't actually _read_ chapter 3 up through §3.4, but you don't see why that would be necessary, since this Algorithm 3.2 pseudocode is telling you what you need to do.)

It looks like the algorithm says to pick a variable, allocate a graph node to represent it, find the smallest subset of the previously-allocated variables such that the variable represented by the new node is conditionally independent of the other previously-allocated variables given that subset, and then draw directed edges from each of the nodes in the subset to the new node?—and keep doing that for each variable—and then compute conditional probability tables for each variable given its parents in the resulting graph?

That seems complicated when you say it abstractly, but you have faith that it will make more sense as you carry out the computations.

First, you allocate a graph node for $X_1$. It doesn't have any parents, so the associated conditional ("conditional") probability distribution, is really just the marginal distribution for $X_1$.

![](https://i.imgur.com/J2pKDNh.png)

Then you allocate a node for $X_2$. $X_2$ is not independent of $X_1$. (Because $P(X_1 \land X_2)$ = 169/1400, which isn't the same as $P(X_1) \cdot P(X_2)$ = 8/25 · 1/7 = 8/175.) So you make $X_1$ a parent of $X_2$, and your conditional probability table for $X_2$ separately specifies the probabilities of $X_2$ being true or false, depending on whether $X_1$ is true or false.

![](https://i.imgur.com/7KdHvGn.png)

Next is $X_3$. Now that you have two possible parents, you need to check whether conditioning on either of $X_1$ and $X_2$ would render $X_3$ conditionally independent of the other. If not, then both $X_1$ and $X_2$ will be parents of $X_3$; if so, then the variable you conditioned on will be the sole parent. (You assume that the case where $X_3$ is just independent from both $X_1$ and $X_2$ does not pertain; if that were true, $X_3$ wouldn't be connected to the rest of the graph at all.)

It turns out that $X_3$ and $X_2$ are conditionally independent given $X_1$. That is, $P(X_3 \land X_2 \mid X_1) = P(X_3 \mid X_1) \cdot P(X_2 \mid X_1)$. (Because the left-hand side is $\frac{P(X_3 \land X_2 \land X_1)}{P(X_1)} = \frac{507}{1792}$, and the right-hand side is $\frac{3}{4} \cdot \frac{169}{448} = \frac{507}{1792}$.) So $X_1$ is a parent of $X_3$, and $X_2$ isn't; you draw an arrow from $X_1$ (and only $X_1$) to $X_3$, and compile the corresponding conditional probability table.

![](https://i.imgur.com/MaiOwOx.png)

Finally, you have $X_4$. The chore of finding the parents is starting to feel more intuitive now. Out of the $2^3 = 8$ possible subsets of the preceding variables, you need to find the smallest subset, such that conditioning on that subset renders $X_4$ (conditionally) independent of the variables not in that subset. After some calculations that the authors of expository blog posts have sometimes been known to callously leave as an exercise to the reader, you determine that $X_1$ and $X_2$ are the parents of $X_4$.

And with one more conditional probability table, your Bayesian network is complete!

![](https://i.imgur.com/eXv5jsn.png)

Eager to interpret the meaning of this structure regarding the philosophy of causality, you translate the $X_i$ variable labels back to English:

![](https://i.imgur.com/k8kpMLo.png)

...

This can't be right. The arrow from "wet" to "slippery" seems fine. But all the others are clearly absurd. Wet sidewalks cause rain? Sprinklers cause rain? Wet sidewalks cause the sprinkler to be on?

You despair. You thought you had understood the algorithm. You can't find any errors in your calculations—but surely there must be some? What did you do wrong?

After some thought, it becomes clear that it wasn't just a calculation error: the procedure you were trying to carry out _couldn't_ have given you the result you expected, because it never draws arrows from later-considered to earlier-considered variables. You considered "wet" _first_. You considered "rain" _last_, and then did independence tests to decide whether or not to draw arrows from "wet" (or "sprinkler" or "slippery") to "rain". An arrow from "rain" to "wet" was never a possibility. The output of the algorithm is sensitive to the ordering of the variables.

(In retrospect, _that_ probably explains the "given an ordering" part of Algorithm 3.2's title, "Procedure to build a minimal I-map given an ordering." You hadn't read up through the part of chapter 3 that presumably explains what an "I-map" is, and had disregarded the title as probably unimportant.)

You try carrying out the algorithm with the ordering "rain", "sprinkler", "wet", "slippery" (or $X_4$, $X_2$, $X_1$, $X_3$ using your $X_i$ labels from before), and get this network:

![](https://i.imgur.com/ccpePrQ.png)

—for which giving the arrows a causal interpretation seems much more reasonable.

You notice that you are very confused. The "crazy" network you originally derived, and this "true" network derived from a more intuitively causal variable ordering, are different: they don't have the same structure, and (except for the wet → slippery link) they don't have the same conditional probability tables. You would assume that they can't "both be right". If the network output by the algorithm depends on what variable ordering you use, how are you supposed to know which ordering is correct? In this example, you know from reasons _outside_ the math, that "wet" shouldn't cause "rain", but you couldn't count on that were you to apply these methods to problems further removed from intuition.

Playing with both networks, you discover that despite their different appearances, they both seem to give the same results when you use them to calculate marginal or conditional probabilities. For example, in the "true" network, $P(\mathrm{rain})$ is 1/4 (read directly from the "conditional" probability table, as "rain" has no parents in the graph). In the "crazy" network, the probability of rain can be computed as

$$P(\mathrm{rain} \mid \mathrm{sprinkler}, \mathrm{wet}) \cdot P(\mathrm{sprinkler} \mid \mathrm{wet}) \cdot P(\mathrm{wet}) +$$

$$P(\mathrm{rain} \mid \neg \mathrm{sprinkler}, \mathrm{wet}) \cdot P(\neg \mathrm{sprinkler} \mid \mathrm{wet}) \cdot P(\mathrm{wet}) +$$

$$P(\mathrm{rain} \mid \mathrm{sprinkler}, \neg \mathrm{wet}) \cdot P(\mathrm{sprinkler} \mid \neg \mathrm{wet}) \cdot P(\neg \mathrm{wet}) +$$

$$P(\mathrm{rain} \mid \neg \mathrm{sprinkler}, \neg \mathrm{wet}) \cdot P(\neg \mathrm{sprinkler} \mid \neg \mathrm{wet}) \cdot P(\neg \mathrm{wet})$$

$$= \frac{49}{169} \cdot \frac{169}{448} \cdot \frac{8}{25} + \frac{30}{31} \cdot \frac{279}{448} \cdot \frac{8}{25} + \frac{1}{31} \cdot \frac{31}{952} \cdot \frac{17}{25} + \frac{10}{307} \cdot \frac{921}{952} \cdot \frac{17}{25}$$

... which also equals 1/4.

That actually makes sense. You were wrong to suppose that the two networks couldn't "both be right". They _are_ both right; they both represent the same joint distribution. The result of the algorithm for constructing a Bayesian network—or a "minimal I-map", whatever that is—depends on the given variable ordering, but since the algorithm is valid, each of the different possible results is also valid.

But if the "crazy" network and the "true" network are both right, what happened to the promise of understanding causality using Bayesian networks?! (You may only be a casual formal epistemology fan, but you remember reading a variety of secondary sources unanimously agreeing that this was a thing; you're definitely not misremembering or making it up.) If both networks give the same answers to marginal and conditional probability queries, that amounts to them making the _same predictions_ about the world. So if beliefs are supposed to correspond to predictions, in what sense could the "true" network be _better_? What does your conviction that rain causes wetness even _mean_, if someone who believed the opposite could make all the same predictions?

You remember the secondary sources talking about _interventions_ on causal graphs: severing a node from its parents and forcing it to take a particular value. And the "crazy" network and the "true" network _do_ differ with respect to _that_ operation: in the "true" network, setting "wet" to be false—you again imagine putting a tarp up over the sidewalk—wouldn't change the probability of "rain". But in the "crazy" network, forcing "wet" to be false _would_ change the probability of rain—to $P(\mathrm{rain} \mid \mathrm{sprinkler}, \neg \mathrm{wet}) \cdot P(\mathrm{sprinkler} \mid \neg \mathrm{wet}) + P(\mathrm{rain} \mid \neg \mathrm{sprinkler}, \neg \mathrm{wet}) \cdot P(\neg \mathrm{sprinkler} \mid \neg \mathrm{wet})$, which is $\frac{1}{31} \cdot \frac{31}{952} + \frac{10}{307} \cdot \frac{921}{952} \approx 0.032$ (greatly reduced from the 1/4 you calculated a moment ago). Notably, this intervention—$P(\mathrm{rain} \mid \mathrm{do}(\neg \mathrm{wet}))$, if you're remembering correctly what some of the secondary sources said about a _do_ operator—isn't the same thing as the conditional probability $P(\mathrm{rain}| \neg \mathrm{wet})$.

This would seem to satisfy your need for a sense in which the "true" network is "better" than the "crazy" network, even if Algorithm 3.2 indifferently produces either depending on the ordering it was given. (You're sure that Daphne Koller and the other guy have more to say about other algorithms that can make finer distinctions, but this feels like enough studying for one day—and enough for one expository blog post, if someone was writing one about your inquiries. You're a _casual_ formal epistemology fan.) The two networks represent the same predictions about the world recorded in your family archives, but starkly different predictions about nearby _possible_ worlds—about what _would_ happen if some of the factors underlying the world were to change.

You feel a slight philosophical discomfort about this. You don't like the idea of forced change, of intervention, being so integral to such a seemingly basic notion as causality. It feels almost anthropomorphic: you want the notion of cause and effect within a system to make sense without reference to the intervention of some outside agent—for there's nothing outside of the universe. But whether this intuition is a clue towards deeper insights, or just a place where your brain has tripped on itself and gotten confused, it's more than you understand now.
