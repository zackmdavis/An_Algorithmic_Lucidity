Title: Algorithms of Deception!
Date: 2019-10-19 11:06
Status: published
Category: philosophy
Tags: honesty, Python

[(originally published at _Less Wrong_)](https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception)

I want you to imagine a world consisting of a sequence of independent and identically distributed random variables $X_i$, and two computer programs.

The first program is called Reporter. As input, it accepts a bunch of the random variables $X_i$. As output, it returns a list of sets whose elements belong to the domain of the $X_i$.

The second program is called Audience. As input, it accepts the output of Reporter. As output, it returns a probability distribution.

Suppose the $X_i$ are drawn from the following distribution:

$$P(X = x) = \begin{cases} 1/2 & x = 1 \\ 1/4 & x = 2 \\ 3/16 & x = 3 \\ 1/16 & x = 4 \\ \end{cases}$$

We can model drawing a sample from this distribution using this function in the [Python programming language](https://www.python.org/):

```python
import random

def x():
    r = random.random()
    if 0 <= r < 1/2:
        return 1
    elif 1/2 <= r < 3/4:
        return 2
    elif 3/4 <= r < 15/16:
        return 3
    else:
        return 4
```

For compatibility, we can imagine that Reporter and Audience are also written in Python. This is just for demonstration in the blog post that I'm writing—the _real_ Reporter and Audience (out there in the world I'm asking you to imagine) might be much more complicated programs written for some kind of _alien_ computer the likes of which we have not yet dreamt! But I like Python, and for the moment, we can pretend.

So pretend that Audience looks like this (where the dictionary, or hashmap, that gets returned represents a probability distribution, with the keys being random-variable outcomes and the values being probabilities):

```python
from collections import Counter

def audience(report):
    a = Counter()
    for sight in report:
        for possibility in sight:
            a[possibility] += 1/len(sight)            
    d = sum(a_j - len(a) for a_j in a.values())
    return {x: (a_i - 1)/d for x, a_i in a.items()}
```

Let's consider multiple possibilities for the form that Reporter could take. A particularly simple implementation of Reporter (call it `reporter_0`) might look like this:

```python
def reporter_0(xs):
    output = []
    for x in xs:
        output.append({x})
    return output
```

The pairing of `audience` and `reporter_0` has a _Very Interesting Property!_ When we call our Audience on the output of this Reporter, the probability distribution that Audience returns is _very similar_ to the distribution that our random variables are from![^wrong]

[^wrong]: But _only_ "very" similar: the code for `audience` is _not_ the mathematically correct thing to do in this situation; it's just an approximation that ought to be good enough for the point I'm trying to make in this blog post, for which I'm trying to keep the code simple. (Specifically, the last two lines of `audience` are based on [the mode of the Dirichlet distribution](https://en.wikipedia.org/wiki/Dirichlet_distribution#Mode), but, firstly, that part about increasing the hyperparameters fractionally when you're uncertain about what was observed (`a[possibility] += 1/len(sight)`) is pretty dodgy, and secondly, if you were _actually_ going to try to predict an outcome drawn from a [categorical distribution](https://en.wikipedia.org/wiki/Categorical_distribution) like $P(X)$ using the Dirichlet distribution as a [conjugate prior](https://en.wikipedia.org/wiki/Conjugate_prior), you'd need to integrate over the Dirichlet hyperparameters; you shouldn't just pretend that the mode/peak represents the true parameters of the categorical distribution—but as I said, we _are_ just pretending.)

```
>>> audience(reporter_0([x() for _ in range(100000)]))
{1: 0.5003300528084493, 2: 0.2502900464074252, 3: 0.1873799807969275, 4: 0.062119939190270444}

# Compare to P(X) expressed as a Python dictionary—
>>> {1: 1/2, 2: 1/4, 3: 3/16, 4: 1/16}
{1: 0.5, 2: 0.25, 3: 0.1875, 4: 0.0625}
```

Weird, right?!

Of course, there are _other_ possible implementations of Reporter. For example, this choice of Reporter (`reporter_1`) does _not_ result in the Very Interesting Property—

```python
def reporter_1(xs):
    output = []
    for _ in range(len(xs)):
        output.append({4})
    return output
```

It instead induces Audience to output a very different (and rather boring) distribution. It doesn't even matter how the $X_i$ turned up; the result will always be the same:

```
>>> audience(reporter_1([x() for _ in range(100000)]))
{4: 1.0}
```

We could go on imagining other versions of Reporter, like this one (`reporter_2`)—

```
def reporter_2(xs):
    output = []
    for x in xs:
        if x == 4 or random.random() < 0.2:
            output.append({x})
        else:
            continue
    return output
```

While the distribution that `reporter_2` makes Audience output isn't as boring as the one we saw for `reporter_1`, it still doesn't result in the Very Interesting Property of matching the distribution of the $X_i$. It comes _closer_ than `reporter_1` did—notice how the _ratios_ of probabilities assigned to the first three outcomes is similar to that of the original distribution—but it's assigning way too much probability-mass to the outcome "4":

```
>>> audience(reporter_2([x() for _ in range(100000)]))
{1: 0.3971289947471831, 2: 0.20309555314968522, 3: 0.14860259032038173, 4: 0.2516540358474678}
```

So far, all of the Reporters we've imagined are still only putting one element in the inner sets of the list-of-sets that they return. But we could imagine `reporter_3`—

```python
def reporter_3(xs):
    output = []
    for x in xs:
        if x == 1 or x == 4:
            output.append({1, 4})
        else:
            output.append({x})
    return output
```

Unlike `reporter_2` (which typically returned a list with _fewer_ elements than it received as input), the list returned by `reporter_3` has exactly as many elements as the list it took in. Yet this Reporter still prompts Audience to return a distribution with too many "4"s—and _unlike_ `reporter_2`, it doesn't even get the ratio of the other outcomes right, yielding disproportionately fewer "1"s compared to "2"s and "3"s than the original distribution—

```
>>> audience(reporter_3([x() for _ in range(100000)]))
{1: 0.2808949431909106, 2: 0.24795967354776766, 3: 0.19037045927348376, 4: 0.2808949431909106}
```

Again, I've presented Audience and various possible Reporters as simple Python programs for illustration and simplicity, but the same _input-output relationships_ could be embodied as part of a more complicated system—perhaps an entire conscious mind which could talk.

So now imagine our Audience as a _person_ with her own hopes and fears and ambitions ... ambitions whose ultimate fulfillment will require dedication, bravery—and meticulously careful planning based on an accurate estimate of $P(X)$, with almost no room for error.

So, too, imagine each of our possible Reporters as a person: loyal, responsible—and, entirely coincidentally, the supplier of a good that Audience's careful plans call for in proportion to the value of $P(X = 4)$.

When the expected frequency of "4"s fails to appear, Audience's lifework is in ruins. All of her training, all of her carefully calibrated plans, all the interminable hours of hard labor, were for nothing. She confronts Reporter in a furor of rage and grief.

"You _lied_," she says through tears of betrayal, "I _trusted you_ and _you lied to me!_"

The Reporter whose behavior corresponds to `reporter_2` replies, "How _dare_ you accuse me of lying?! Sure, I'm not a perfect program free from all bias, but everything I said was true—every outcome I reported corresponded to one of the $X_i$. [You can't call that misleading!](https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting)"

He is perfectly sincere. Nothing in his _consciousness_ reflects _intent_ to deceive Audience, any more than an eight-line Python program could be said to have such "intent." (Does a `for` loop "intend" anything? Does a conditional "care"? Of course not!)

The Reporter whose behavior corresponds to `reporter_3` replies, "_Lying?!_ I told you the truth, the whole truth, and nothing but the truth: everything I saw, I reported. When I said an outcome was a oneorfour, it actually was a oneorfour. Perhaps you have a different category system, such that what _I_ think of as a 'oneorfour', appears to you to be any of several completely different outcomes, which you think my 'oneorfour' concept is conflating. If those outcomes had wildly different probabilities, if one was much more common than fou—I mean, than the other—then you'd have no way of knowing that from my report. But using language in a way _you_ dislike, is not lying. [I can define a word any way I want!](https://www.lesswrong.com/posts/FaJaCgqBKphrDzDSj/37-ways-that-words-can-be-wrong)"

He, too, is perfectly sincere.

### Commentary

Much has been written on this website about reducing mental notions of "truth", "evidence", _&c._ [to the nonmental](https://www.lesswrong.com/posts/p7ftQ6acRkgo6hqHb/dreams-of-ai-design). One need not grapple with tendentious [mysteries](https://www.lesswrong.com/posts/6i3zToomS86oj9bS6/mysterious-answers-to-mysterious-questions) of "mind" or "consciousness", when so much more can be accomplished by considering systematic cause-and-effect processes [that result in](https://www.lesswrong.com/posts/6s3xABaXKPdFwA3FS/what-is-evidence) the states of one physical system becoming correlated with the states of another—a "map" that reflects a "territory."

The same methodology that was essential for studying truthseeking, is equally essential for studying the propagation of falsehood. If true "beliefs" are models that [make accurate predictions](https://www.lesswrong.com/posts/a7n8GdKiAZRX86T5A/making-beliefs-pay-rent-in-anticipated-experiences), then _deception_ would presumably be communication that systematically results in _less_ accurate predictions (by a listener applying the same inference algorithms that would result in more accurate predictions when applied to direct observations or "honest" reports).

In a peaceful world where most falsehood was due to random mistakes, there would be little to be gained by studying processes that systematically create erroneous maps. In a world of [conflict](https://slatestarcodex.com/2018/01/24/conflict-vs-mistake/), where there are [forces trying to slash your tires](https://www.lesswrong.com/posts/XTWkjCJScy2GFAgDt/dark-side-epistemology), one would do well do study these—_algorithms of deception!_
