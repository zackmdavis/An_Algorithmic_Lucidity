Title: Maybe Lying Can’t Exist?!
Date: 2020-08-22 17:36
Status: published
Category: philosophy
Tags: rationality, honesty
Slug: maybe-lying-cant-exist

[(originally published at _Less Wrong_)](https://www.lesswrong.com/posts/YptSN8riyXJjJ8Qp8/maybe-lying-can-t-exist)

How is it possible to tell the truth?

I mean, sure, you can use your larynx to make sound waves in the air, or you can draw a sequence of symbols on paper, but sound waves and paper-markings can't be _true_, any more than a leaf or a rock can be "true". Why do you [think you can](https://www.lesswrong.com/posts/rQEwySCcLtdKHkrHp/righting-a-wrong-question) tell the truth?

This is a pretty easy question. Words don't have intrinsic ontologically-basic meanings, but intelligent systems can _learn_ associations between a symbol and things in the world. If I say "dog" and point to a dog a bunch of times, a child who didn't already know what the word "dog" meant, would soon get the idea and learn that the sound "dog" _meant_ this-and-such kind of furry four-legged animal.

As a _formal_ model of how this AI trick works, [we can study sender–receiver games](https://www.lesswrong.com/posts/4hLcbXaqudM9wSeor/philosophy-in-the-darkest-timeline-basics-of-the-evolution). Two agents, a "sender" and a "receiver", play a simple game: the sender observes one of several possible states of the world, and sends one of several possible _signals_—something that the sender can vary (like sound waves or paper-markings) in a way that the receiver can detect. The receiver observes the signal, and [makes a prediction](https://www.lesswrong.com/posts/a7n8GdKiAZRX86T5A/making-beliefs-pay-rent-in-anticipated-experiences) about the state of the world. If the agents both get rewarded when the receiver's prediction matches the sender's observation, a convention evolves that assigns [common-usage](https://www.lesswrong.com/posts/9ZooAqfh2TC9SBDvq/the-argument-from-common-usage) meanings to the previously and otherwise arbitrary signals. True information is communicated; the signals become a _shared_ map that reflects the territory.

This works because the sender and receiver have a common interest in getting the same, correct answer—in [coordinating](https://www.lesswrong.com/posts/9QxnfMYccz9QRgZ5z/the-costly-coordination-mechanism-of-common-knowledge) for the signals to mean something. If instead the sender got rewarded when the receiver made _bad_ predictions, then if the receiver could use some correlation between the state of the world and the sender's signals in order to make better predictions, then the sender would have an incentive to change its signaling choices to destroy that correlation. No convention evolves, no information gets transferred. This case is not a matter of a map failing to reflect the territory. Rather, there just is no map.

------

How is it possible to _lie_?

This is ... a surprisingly less-easy question. The problem is that, in the formal framework of the sender–receiver game, the meaning of a signal is simply how it makes a receiver update its probabilities, which is determined by the conditions under which the signal is sent. If I say "dog" and four-fifths of the time I point to a dog, but one-fifth of the time I point to a tree, what should a child conclude? Does "dog" mean dog-with-probability-0.8-and-tree-with-probability-0.2, or does "dog" mean dog, and I'm just lying one time out of five? (Or does "dog" mean tree, and I'm lying four times out of five?!) Our sender–receiver game model would seem to favor the first interpretation.

Signals convey information. What could make a signal, information, _deceptive_?

Traditionally, _deception_ has been regarded as intentionally causing someone to have a false belief. As Bayesians and reductionists, however, we endeavor to [pry open](https://www.lesswrong.com/posts/HnS6c5Xm9p9sbm4a8/grasping-slippery-things) anthropomorphic black boxes like "intent" and "belief." As a _first attempt_ at making sense of deceptive signaling, let's generalize "causing someone to have a false belief" to "causing the receiver to update its probability distribution to be less accurate ([operationalized](https://plato.stanford.edu/entries/operationalism/) as [the logarithm of the probability it assigns to the true state](https://www.lesswrong.com/posts/afmj8TKAqH6F2QMfZ/a-technical-explanation-of-technical-explanation))", and [generalize "intentionally" to](https://www.lesswrong.com/posts/sXHQ9R5tahiaXEZhR/algorithmic-intent-a-hansonian-generalized-anti-zombie) "benefiting the sender (operationalized by the rewards in the sender–receiver game)".

One might ask: why require the sender to benefit in order for a signal to count as deceptive? Why isn't "made the receiver update in the wrong direction" enough?

The answer is that we're seeking an account of communication that _systematically_ makes receivers update in the wrong direction—signals that we can think of as having been [_optimized for_](https://www.lesswrong.com/posts/CW6HDvodPpNe38Cry/aiming-at-the-target) making the receiver make wrong predictions, rather than accidentally happening to mislead on this particular occasion. The "rewards" in this model should be interpreted mechanistically, not necessarily mentalistically: it's _just_ that things that get "rewarded" more, happen more often. That's all—and that's enough to shape the evolution of how the system processes information. There need not be any conscious mind that "feels happy" about getting rewarded (although that would do the trick).

Let's test out our proposed definition of deception on a concrete example. Consider a firefly of the fictional species _[P.](https://en.wikipedia.org/wiki/Photinus_(beetle)) rey_ exploring a new area in the forest. Suppose there are three possibilities for what this area could contain. With probability 1/3, the area contains another _P. rey_ firefly of the opposite sex, available for mating. With probability 1/6, the area contains a firefly of a different species, _[P.](https://en.wikipedia.org/wiki/Photuris) redator_, which eats _P. rey_ fireflies. With probability 1/2, the area contains nothing of interest.

A potential mate in the area can flash the _P. rey_ mating signal to let the approaching _P. rey_ know it's there. Fireflies evolved their eponymous ability to emit light specifically for this kind of sexual communication—potential mates have a common interest in making their presence known to each other. Upon receiving the mating signal, the approaching _P. rey_ can eliminate the predator-here and nothing-here states, and update its what's-in-this-area probability distribution from {$\frac{1}{3}$ mate, $\frac{1}{6}$ predator, $\frac{1}{2}$ nothing} to {$1$ mate}. True information is communicated.

Until "one day" (in evolutionary time), a mutant _P. redator_ [emits flashes that imitate the _P. rey_ mating signal](https://en.wikipedia.org/wiki/Aggressive_mimicry), thereby luring an approaching _P. rey_, who becomes an easy meal for the _P. redator_. This meets our criteria for deceptive signaling: the _P. rey_ receiver updates in the wrong direction (revising its probability of a _P. redator_ being present downwards from $\frac{1}{6}$ to 0, even though a _P. redator_ is in fact present), and the _P. redator_ sender benefits (becoming more likely to survive and reproduce, thereby spreading the mutant alleles that predisposed it to emit _P. rey_-mating-signal-like flashes, thereby ensuring that this scenario will _systematically_ recur in future generations, even if the first time was an accident because fireflies aren't that smart).

Or rather, this meets our criteria for deceptive signaling _at first_. If the _P. rey_ population counteradapts to make correct Bayesian updates in the new world containing deceptive _P. redators_, then in the new equilibrium, seeing the mating signal causes a _P. rey_ to update its what's-in-this-area probability distribution from  {$\frac{1}{3}$ mate, $\frac{1}{6}$ predator, $\frac{1}{2}$ nothing} to {$\frac{2}{3}$ mate, $\frac{1}{3}$ predator}. But now the counteradapted _P. rey_ is _not_ updating in the wrong direction. If both mates and predators send the same signal, than the [likelihood ratio](https://arbital.greaterwrong.com/p/likelihood_ratio) between them is one; the observation doesn't favor one hypothesis more than the other.

So ... is the _P. redator_'s use of the mating signal _no longer deceptive_ after it's been "priced in" to the new equilibrium? Should we stop calling the flashes the "_P. rey_ mating signal" and start calling it the "_P. rey_ mating and/or _P. redator_ prey-luring signal"? Do we agree with [the executive in _Moral Mazes_ who said](https://www.lesswrong.com/posts/45mNHCMaZgsvfDXbw/quotes-from-moral-mazes#L__Truth_and_Public_Relations), "We lie all the time, but if everyone knows that we're lying, is a lie really a lie?"

Some authors are willing to bite this bullet in order to preserve our tidy formal definition of _deception_. (Don Fallis and Peter J. Lewis write: "Although we agree [...] that it _seems_ deceptive, we contend that the mating signal sent by a [predator] is not _actually_ misleading or deceptive [...] not all sneaky behavior (such as failing to reveal the _whole_ truth) counts as deception".)

Personally, I don't care much about having tidy formal definitions of English words; I want to understand the general [_laws_ governing](https://www.lesswrong.com/posts/eY45uCCX7DdwJ4Jha/no-one-can-exempt-you-from-rationality-s-laws) the construction and perversion of shared maps, even if a detailed understanding requires revising or splitting some of our intuitive concepts. (Cailin O'Connor writes: "In the case of deception, though, part of the issue seems to be that we generally ground judgments of what is deceptive in terms of human behavior. It may be that there is no neat, unitary concept underlying these judgments.")

Whether you choose to _describe_ it with the signal/word "deceptive", "sneaky", [_Täuschung_](https://en.wiktionary.org/wiki/T%C3%A4uschung), הונאה, 欺瞞, or something else, _something_ about _P. redator's_ signal usage has the optimizing-for-the-inaccuracy-of-shared-maps property. There is a fundamental asymmetry underlying why we want to talk about a mating signal rather than a 2/3-mating-1/3-prey-luring signal, even if the latter is a better description of the information it conveys.

Brian Skyrms and Jeffrey A. Barrett have an explanation in light of the observation that our sender–receiver framework is a [sequential game](https://en.wikipedia.org/wiki/Sequential_game): _first_, the sender makes an observation (or equivalently, Nature chooses the type of sender—mate, predator, or null in the story about fireflies), _then_ the sender chooses a signal, _then_ the receiver chooses an action. We can separate out the _propositional_ content of signals from their informational content by taking the propositional meaning to be defined in the [subgame](https://en.wikipedia.org/wiki/Subgame_perfect_equilibrium) where the sender and receiver have a common interest—the branches of the game tree where the players are _trying_ to communicate.

Thus, we see that deception is ["ontologically parasitic" in sense that holes are](https://plato.stanford.edu/entries/holes/#Theo). You can't have a hole without some material for it to be a hole _in_; you can't have a lie without some shared map for it to be a lie _in_. And a sufficiently deceptive map, like a sufficiently holey material, collapses into noise and dust.

### Bibliography

I changed the species names in the standard story about fireflies because I can never remember which of _Photuris_ and _Photinus_ is which.

Fallis, Don and Lewis, Peter J., ["Toward a Formal Analysis of Deceptive Signaling"](http://philsci-archive.pitt.edu/13337/)

O'Connor, Cailin, _Games in the Philosophy of Biology_, §5.5, "Deception"

Skyrms, Brian, _Signals: Evolution, Learning, and Information_, Ch. 6, "Deception"

Skyrms, Brian and Barrett, Jeffrey A., ["Propositional Content in Signals"](http://philsci-archive.pitt.edu/14774/)
