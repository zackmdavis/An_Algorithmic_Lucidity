Title: Comment on “Endogenous Epistemic Factionalization”
Date: 2020-05-20 11:04
Status: published
Category: social science
Tags: politics, game theory, Python

[(originally published at _Less Wrong_)](https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization)

In ["Endogenous Epistemic Factionalization"](https://arxiv.org/abs/1812.08131) (due in a forthcoming issue of the philosophy-of-science journal [_Synthese_](https://www.springer.com/journal/11229/)), James Owen Weatherall and Cailin O'Connor propose a possible answer to the question of why people form factions that disagree on multiple subjects.

The existence of persistent disagreements is [_already_](https://www.lesswrong.com/posts/NKECtGX4RZPd7SqYp/the-modesty-argument) [kind](https://www.lesswrong.com/posts/tKa9Lebyebf6a7P2o/the-rhythm-of-disagreement) [of](https://www.lesswrong.com/posts/gTTWRkSz474o7s4Dg/principles-of-disagreement) [a puzzle](https://ppe.mercatus.org/system/files/Are_Disagreements_Honest_-_WP.pdf) from a Bayesian perspective. [There's only one](https://genius.com/They-might-be-giants-one-everything-lyrics) reality. If everyone is honestly trying to get the right answer and we can all _talk_ to each other, then we should converge on the right answer (or an answer that is [less wrong](https://tvtropes.org/pmwiki/pmwiki.php/Main/TitleDrop) given the evidence we have). The fact that we _can't do it_ is, or should be, an embarrassment to our species. And the existence of _correlated_ persistent disagreements—when not only do I say "top" when you say "bottom" even after we've gone over all the arguments for whether it is in fact the case that top or bottom, but _furthermore_, the fact that I said "top" lets you _predict_ that I'll probably say "cold" rather than "hot" even _before_ we go over the arguments for that, is an _atrocity_. (Not hyperbole. Thousands of people are dying horrible suffocation deaths because we can't figure out the optimal response to a new kind of coronavirus.)

Correlations between beliefs are often attributed to ideology or [tribalism](https://slatestarcodex.com/2014/11/04/ethnic-tension-and-meaningless-arguments/): if I believe that Markets Are the Answer, I'm likely to propose Market-based solutions to all sorts of seemingly-unrelated social problems, and if I'm [loyal to the Green tribe](https://www.lesswrong.com/posts/6hfGNLf4Hg5DXqJCF/a-fable-of-science-and-politics), I'm likely to [selectively censor my thoughts in order to fit the Green party line](https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting). But ideology can't explain correlated disagreements on unrelated topics that the content of the ideology is silent on, and tribalism can't explain correlated disagreements on narrow, technical topics that aren't [tribal shibboleths](https://slatestarcodex.com/2016/04/04/the-ideology-is-not-the-movement/).

In this paper, Weatherall and O'Connor exhibit a toy model that proposes a simple mechanism that can explain correlated disagreement: if agents disbelieve in evidence presented by those with sufficiently dissimilar beliefs, factions emerge, even though everyone is honestly reporting their observations and updating on what they are told (to the extent that they believe it). The paper didn't seem to provide source code for the simulations it describes, so I followed along in Python. (Replication!)

In each round of the model, our little Bayesian agents [choose between repeatedly performing](https://en.wikipedia.org/wiki/Multi-armed_bandit) one of two actions, A or B, that can "succeed" or "fail." A is a fair coin: it succeeds exactly half the time. _As far as our agents know_, B is _either_ slightly better or slightly worse: the per-action probability of success is either 0.5 + ɛ or 0.5 − ɛ, for some ɛ (a parameter to the simulation). But secretly, we the simulation authors know that B is better.

```python
import random

ε = 0.01

def b():
    return random.random() < 0.5 + ε
```

The agents start out with a uniformly random probability that B is better. The ones who currently believe that A is better, repeatedly do A (and don't learn anything, because they already know that A is exactly a coinflip). The ones who currently believe that B is better, repeatedly do B, but keep track of and publish their results in order to help everyone figure out whether B is slightly better or slightly worse than a coinflip.

```python
class Agent:
    ...

    def experiment(self):
        results = [b() for _ in range(self.trial_count)]
        return results
```

If $H_{+}$ represents the hypothesis that B is better than A, and $H_{-}$ represents the hypothesis that B is worse, then Bayes's theorem says

$$P(H_{+}|E) = \frac{P(E|H_{+})P(H_{+})}{P(E|H_{+})P(H_{+}) + P(E|H_{-})P(H_{-})}$$

where E is the record of how many successes we got in how many times we tried action B. The likelihoods $P(E|H_{+})$ and $P(E|H_{-})$ can be calculated from the probability mass function of the [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution), so the agents have all the information they need to update their beliefs based on experiments with B.

```python
from math import factorial

def binomial(p, n, k):
    return (
        factorial(n) / (factorial(k) * factorial(n - k)) *
        p**k * (1 - p)**(n - k)
    )

class Agent:
    ...

    def pure_update(self, credence, hits, trials):
        raw_posterior_good = binomial(0.5 + ε, trials, hits) * credence
        raw_posterior_bad = binomial(0.5 - ε, trials, hits) * (1 - credence)
        normalizing_factor = raw_posterior_good + raw_posterior_bad
        return raw_posterior_good / normalizing_factor
```

Except in order to study the emergence of clustering among multiple beliefs, we should actually have our agents face _multiple_ "A or B" dilemmas, representing beliefs about unrelated questions. (In each case, B will again be better, but the agents don't start out knowing that.) I chose three questions/beliefs, because that's all I can fit in a pretty 3D scatterplot.

If all the agents update on the experimental results published by the agents who do B, they quickly learn that B is better for all three questions. If we make a pretty 3D scatterplot where [each dimension represents](https://www.lesswrong.com/posts/WBw8dDkAWohFjWQSk/the-cluster-structure-of-thingspace) the probability that B is better for one of the dilemmas, then the points converge over time to the [1.0, 1.0, 1.0] "corner of Truth", even though they started out uniformly distributed all over the space.

![](https://i.imgur.com/E61Hp4W.png)

But suppose the agents don't trust each other's reports. ("Sure, she _says_ she performed $B_2$ 50 times and observed 26 successes, but she _also_ believes that $B_1$ is better than $A_1$, which is _crazy_. Are we sure she didn't just make up those 50 trials of $B_2$?") Specifically, our agents assign a probability that a report is made-up (and therefore should not be updated on) in proportion to their distance from the reporter in our three-dimensional beliefspace, and a "mistrust factor" (a parameter to the simulation).

```python
from math import sqrt

def euclidean_distance(v, w):
    return sqrt(sum((v[i] - w[i]) ** 2 for i in range(len(v))))

class Agent:
    ...

    def discount_factor(self, reporter_credences):
        return min(
            1, self.mistrust * euclidean_distance(self.credences, reporter_credences)
        )

    def update(self, question, hits, trials, reporter_credences):
        discount = self.discount_factor(reporter_credences)
        posterior = self.pure_update(self.credences[question], hits, trials)
        self.credences[question] = (
            discount * self.credences[question] + (1 - discount) * posterior
        )
```

(Um, the paper itself actually uses a slightly more complicated mistrust calculation that also takes into account the agent's prior probability of the evidence, but I didn't quite understand the motivation for that, so I'm going with my version. I don't think the grand moral is affected.)

Then we can simulate what happens if the distrustful agents do many rounds of experiments and talk to each other—

```python
def summarize_experiment(results):
    return (len([r for r in results if r]), len(results))

def simulation(
    agent_count,  # number of agents
    question_count,  # number of questions
    round_count,  # number of rounds
    trial_count,  # number of trials per round
    mistrust,  # mistrust factor
):
    agents = [
        Agent(
            [random.random() for _ in range(question_count)],
            trial_count=trial_count,
            mistrust=mistrust,
        )
        for i in range(agent_count)
    ]

    for _ in range(round_count):
        for question in range(question_count):
            experiments = []
            for agent in agents:
                if agent.credences[question] >= 0.5:
                    experiments.append(
                        (summarize_experiment(agent.experiment()), agent.credences)
                    )
            for agent in agents:
                for experiment, reporter_credences in experiments:
                    hits, trials = experiment
                    agent.update(
                        question,
                        hits,
                        trials,
                        reporter_credences,
                    )

    return agents
```

Depending on the exact parameters, we're likely to get a result that "looks like" this `agent_count=200, round_count=20, question_count=3, trial_count=50, mistrust=2` run—

![](https://i.imgur.com/hSD2pa1.png)

_Some_ of the agents (depicted in red) have successfully converged on the corner of Truth, but the others have polarized into factions that are all wrong about _something_. (The colors in the pretty 3D scatterplot are a [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) for k := 8.) On _average_, evidence pushes our agents towards Truth—note the linearity of the blue and purple points, illustrating convergence on two out of the three problems—but agents who erroneously believe that A is better (due to some combination of a bad initial credence and unlucky experimental results that failed to reveal B's ε "edge" in the sample size allotted) can end up too far away to trust those who are gathering evidence for, and correctly converging on, the superiority of B.

Our authors wrap up: 

> [T]his result is especially notable because there is something reasonable about ignoring evidence generated by those you do not trust—particularly if you do not trust them on account of their past epistemic failures. It would be irresponsible for scientists to update on evidence produced by known quacks. And furthermore, there is something reasonable about deciding who is trustworthy by looking at their beliefs. From my point of view, someone who has regularly come to hold beliefs that diverge from mine looks like an unreliable source of information. In other words, the updating strategy used by our agents is defensible. But, when used on the community level, it seriously undermines the accuracy of beliefs.

I think the moral here is slightly off. The _specific_ something reasonable about ignoring evidence generated by those you do not trust on account of their beliefs, is the assumption that those who have beliefs you disagree with are following [a _process_ that produces systematically misleading evidence](https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception). In this model, that assumption is just _wrong_. The problem isn't that the updating strategy used by our agents is individually "defensible" (what does that mean?) but produces inaccuracy "when used on the community level" (what does that mean?); the problem is that you get the wrong answer if your degree of trust doesn't match agents' actual trustworthiness. Still, it's enlighteningly disturbing to see specifically how the "distrust those who disagree" heuristic descends into the madness of factions.

[(Full source code.)](https://gist.github.com/zackmdavis/49539816ee1018e524a6f5a811b5b224)
