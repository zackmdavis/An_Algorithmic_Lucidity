Title: Firming Up Not-Lying Around Its Edge-Cases Is Less Broadly Useful Than One Might Initially Think
Date: 2019-12-26 21:09
Status: published
Category: philosophy
Tags: rationality, honesty
Slug: firming-up-not-lying-around-its-edge-cases-is-less-broadly-useful-than-one-might-initially-think

[(originally published at _Less Wrong_)](https://www.lesswrong.com/posts/MN4NRkMw7ggt9587K/firming-up-not-lying-around-its-edge-cases-is-less-broadly)

**Reply to**: [Meta-Honesty: Firming Up Honesty Around Its Edge-Cases](https://www.lesswrong.com/posts/xdwbX9pFEr7Pomaxv/meta-honesty-firming-up-honesty-around-its-edge-cases)

Eliezer Yudkowsky, listing advantages of a "wizard's oath" ethical code of "Don't say things that are literally false", writes—

> Repeatedly asking yourself of every sentence you say aloud to another person, "Is this statement actually and literally true?", helps you build a skill for navigating out of your internal smog of not-quite-truths.

I mean, that's _one_ hypothesis about the psychological effects of adopting the wizard's code.

A potential problem with this is that human natural language contains a _lot_ of ambiguity. Words can be used in many ways depending on context. Even the specification "literally" in "literally false" is less useful than it initially appears when you consider that the way people _ordinarily_ speak when they're being truthful is actually pretty dense with metaphors that we typically don't _notice_ as metaphors because they're common enough to be recognized legitimate uses that all fluent speakers will understand.

For example, if I want to convey the meaning that our study group has covered a lot of material in today's session, and I say, "Look how far we've come today!" it would be _pretty weird_ if you were to object, "_Liar!_ We've been in this room the whole time and haven't physically moved at all!" because in this case, it really is obvious to all ordinary English speakers that that's not what I meant by "how far we've come."

Other times, the "intended"[^intended] interpretation of a statement is not only not obvious, but speakers can even mislead by motivatedly equivocating between different definitions of words: the immortal Scott Alexander has written a lot about this phenomenon under the labels ["motte-and-bailey doctrine"](https://slatestarcodex.com/2014/11/03/all-in-all-another-brick-in-the-motte/) (as [coined by Nicholas Shackel](https://philpapers.org/archive/SHATVO-2.pdf)) and ["the noncentral fallacy"](https://www.lesswrong.com/posts/yCWPkLi8wJvewPbEp/the-noncentral-fallacy-the-worst-argument-in-the-world).

[^intended]: I'm scare-quoting "intended" because this process isn't necessarily conscious, and probably usually isn't. Internal distortions of reality in [imperfectly deceptive social organisms](https://intelligence.org/files/CFAI.pdf#page=48) can be [adaptive for the function of deceiving conspecifics](https://www.lesswrong.com/posts/DSnamjnW7Ad8vEEKd/trivers-on-self-deception).

For example, Zvi Mowshowitz has written about how [the claim that "everybody knows" something](https://www.lesswrong.com/posts/BNfL58ijGawgpkh9b/everybody-knows)[^fake] is often used to establish fictitious social proof, or silence those attempting to tell the thing to people who really don't know, but it feels weird (to my intuition, at least) to [call it a "lie"](https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist), because the speaker can just say, "Okay, you're right that not literally[^lit] everyone knows; I meant that _most_ people know but was using a common hyperbolic turn-of-phrase and I reasonably expected you to figure that out."

[^fake]: If I had written this post, I would have titled it "Fake [Common Knowledge](https://www.lesswrong.com/posts/9QxnfMYccz9QRgZ5z/the-costly-coordination-mechanism-of-common-knowledge)" (following in the tradition of ["Fake Explanations"](https://www.lesswrong.com/posts/fysgqk4CjAwhBgNYT/fake-explanations), ["Fake Optimization Criteria"](https://www.lesswrong.com/posts/i6fKszWY6gLZSX2Ey/fake-optimization-criteria), ["Fake Causality"](https://www.lesswrong.com/posts/RgkqLqkg8vLhsYpfh/fake-causality), _&c._)

[^lit]: But it's worth noting that the "Is this statement actually and literally true?" test, taken literally, should have caught this, even if my intuition still doesn't want to call it a "lie."

So the question "Is this statement actually and literally true?" is itself potentially ambiguous. It could mean either—

 * "Is this statement actually and literally true _as the audience will interpret it?_"; or,
 * "Does this statement _permit an interpretation under which_ it is actually and literally true?"

But while the former is complicated and hard to establish, the latter is ... not necessarily that strict of a constraint in most circumstances?

Think about it. When's the last time you needed to consciously tell a bald-faced, _unambiguous_ lie?—something that could realistically be _outright proven false_ in front of your peers, rather than dismissed with a "reasonable" amount of language-lawyering. (Whether "Fine" is a lie in response to "How are you?" depends on exactly what "Fine" is understood to mean in this context. ["Being acceptable, adequate, passable, or satisfactory"](https://en.wiktionary.org/wiki/fine#Adjective)—to what standard?)

Maybe I'm _unusually_ honest—or possibly unusually bad at remembering when I've lied!?—but I'm not sure I even _remember_ the last time I told an outright unambiguous lie. The kind of situation where I would need to do that just _doesn't come up that often_.

Now ask yourself how often your speech has been partially optimized for any function _other_ than providing listeners with information that will help them [better anticipate their experiences](https://www.lesswrong.com/posts/a7n8GdKiAZRX86T5A/making-beliefs-pay-rent-in-anticipated-experiences). The answer is, "Every time you open your mouth"[^mouth]—and if you disagree, then you're lying. (Even if you only say true things, you're more likely to pick true things that make you look good, rather than your most embarrassing secrets. That's [optimization](https://www.lesswrong.com/posts/D7EcMhL26zFNbJ3ED/optimization).)

[^mouth]: Actually, that's not literally true! You often open your mouth to breathe or eat without saying anything at all! Is the referent of this footnote then a blatant lie on my part?—or can I expect you to _know what I meant_?

In the study of AI alignment, it's a truism that failures of alignment [can't be fixed by deontological "patches"](https://arbital.greaterwrong.com/p/patch_resistant). If your AI is exhibiting [weird and extreme](https://arbital.greaterwrong.com/p/edge_instantiation) behavior (with respect to what you _really wanted_, if not what you actually programmed), then adding a penalty term to exclude _that specific behavior_ will just result in the AI executing the "nearest unblocked" strategy, which will probably also be undesirable: [if you prevent your happiness-maximizing AI from administering heroin to humans](https://arbital.greaterwrong.com/p/nearest_unblocked#exampleproducinghappiness), it'll start administering cocaine; if you hardcode a list of banned happiness-producing drugs, it'll start researching new drugs, or just _pay_ humans to take heroin, _&c._

Humans are also intelligent agents. (Um, sort of.) If you don't genuinely have the [intent to inform](http://benjaminrosshoffman.com/honesty-and-perjury/#Intent_to_inform) your audience, but consider yourself ethically bound to be honest, but your conception of _honesty_ is simply "not lying", you'll naturally gravitate towards the nearest unblocked [cognitive algorithm](https://www.lesswrong.com/posts/HcCpvYLoSFP4iAqSz/rationality-appreciating-cognitive-algorithms) [of deception](https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception).[^promise]

[^promise]: A similar phenomenon may occur with other attempts at ethical bindings: for example, confidentiality promises. Suppose Open Opal tends to [wear her heart on her sleeve](https://en.wiktionary.org/wiki/wear_one%27s_heart_on_one%27s_sleeve) and more specifically, believes in lies of omission: if she's talking with someone _she_ trusts, and she has information [_relevant_](https://www.lesswrong.com/posts/GSz8SrKFfW7fJK2wN/relevance-norms-or-gricean-implicature-queers-the-decoupling) to that conversation, she finds it _incredibly psychologically painful_ to _pretend not to know_ that information. If Paranoid Paris has _much_ stronger [privacy](https://www.lesswrong.com/posts/v3Nnsm5HgvEBBDpEZ/privacy) intuitions than Opal and wants to message her about a sensitive subject, Paris might demand a promise of secrecy from Opal ("Don't share the content of this conversation")—only to spark conflict later when Opal construes the literal text of the promise more narrowly than Paris might have hoped ("'Don't share the content' means don't share the _verbatim text_, right? I'm still allowed to paraphrase things Paris said and attribute them to an anonymous correspondent when I think that's relevant to whatever conversation I'm in, even though that hypothetically [leaks entropy](https://www.gwern.net/Death-Note-Anonymity) if Paris has implausibly determined enemies, right?").

So _another_ hypothesis about the psychological effects of adopting the wizard's code is that—however noble your initial conscious _intent_ was—in the face of sufficiently strong incentives to deceive, you just end up accidentally training yourself to get _really good_ at misleading people with a variety of [not-technically-lying](https://www.lesswrong.com/posts/PrXR66hQcaJXsgWsa/not-technically-lying) rhetorical tactics (motte-and-baileys, false [implicatures](https://plato.stanford.edu/entries/implicature/), [stonewalling](https://www.lesswrong.com/posts/wqmmv6NraYv4Xoeyj/conversation-halters), [selective reporting](https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting), [clever rationalized arguments](https://www.lesswrong.com/posts/9f5EXt8KNNxTAihtZ/a-rational-argument), [gerrymandered category boundaries](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries), _&c._), all the while congratulating yourself on how "honest" you are for never, ever emitting any "literally" "false" individual sentences.

-----

Ayn Rand's novel _Atlas Shrugged_[^fiction] portrays a world of crony capitalism in which politicians and businessmen claiming to act for the "common good" (and not consciously lying) are actually using force and fraud to temporarily enrich themselves while destroying the [credit-assignment mechanisms](https://www.lesswrong.com/posts/Ajcq9xWi2fmgn8RBJ/the-credit-assignment-problem) Society needs to coordinate production.[^rand]

[^fiction]: I know, [fictional evidence](https://www.lesswrong.com/posts/rHBdcHGLJ7KvLJQPk/the-logical-fallacy-of-generalization-from-fictional), but I claim that the _kind of deception_ illustrated in quoted passage to follow is _entirely_ realistic.

[^rand]: Okay, that's probably not _exactly_ how Rand or [her acolytes](https://www.lesswrong.com/posts/96TBXaHwLbFyeAxrg/guardians-of-ayn-rand) would put it, but that's [how I'm interpreting it](https://tvtropes.org/pmwiki/pmwiki.php/Main/DeathOfTheAuthor).

In one scene, Eddie Willers (right-hand man to our railroad executive heroine Dagny Taggart) expresses horror that the government's official scientific authority, the State Science Institute, has issued a hit piece denouncing the new alloy, Rearden Metal, with which our protagonists have been planning to use to build a critical railroad line. (In actuality, we later find out, the Institute leaders want to spare themselves the embarrassment—and therefore potential loss of legislative funding—of the innovative new alloy having been invented by private industry rather than the Institute's own metallurgy department.)

> "The State Science Institute," he said quietly, when they were alone in her office, "has issued a statement warning people against the use of Rearden Metal." He added, "It was on the radio. It's in the afternoon papers."
>
> "What did they say?"
>
> "Dagny, they didn't say it! ... They haven't really said it, yet it's there—and it—isn't. That's what's monstrous about it."
>
> [...] He pointed to the newspaper he had left on her desk. "They haven't said that Rearden Metal is bad. They haven't said it's unsafe. What they've done is ..." His hands spread and dropped in a gesture of futility.
>
> She saw at a glance what they had done. She saw the sentences: "It may be possible that after a period of heavy usage, a sudden fissure may appear, though the length of this period cannot be predicted. ... The possibility of a molecular reaction, at present unknown, cannot be entirely discounted. ... Although the tensile strength of the metal is obviously demonstrable, certain questions in regard to its behavior under unusual stress are not to be ruled out. ... Although there is no evidence to support the contention that the use of the metal should be prohibited, a further study of its properties would be of value."
>
> "We can't fight it. It can't be answered," Eddie was saying slowly. "We can't demand a retraction. We can't show them our tests or prove anything. They've said nothing. They haven't said a thing that could be refuted and embarrass them professionally. It's the job of a coward. You'd expect it from some con-man or blackmailer. But, Dagny! It's the State Science Institute!"

I think Eddie is right to feel horrified and betrayed here. At the same time, it's notable that with respect to wizard's code, _no lying has taken place_.

I like to imagine the statement having been drafted by an idealistic young scientist in the [moral maze](https://www.lesswrong.com/posts/45mNHCMaZgsvfDXbw/quotes-from-moral-mazes) of Dr. Floyd Ferris's office at the State Science Institute. Our scientist knows that his boss, Dr. Ferris, expects a statement that will make Rearden Metal look bad; the negative consequences to the scientist's career for failing to produce such a statement will be severe. (Dr. Ferris didn't _say_ that, but [he didn't have to](https://www.lesswrong.com/posts/9fB4gvoooNYa4t56S/power-buys-you-distance-from-the-crime).) But the lab results on Rearden Metal came back with flying colors—by every available test, the alloy is superior to steel along every dimension.

Pity the dilemma of our poor scientist! On the one hand, scientific integrity. On the other hand, [the incentives](https://www.lesswrong.com/posts/5nH5Qtax9ae8CQjZ9/no-it-s-not-the-incentives-it-s-you).

He decides to follow a rule that he thinks will preserve his "inner agreement with truth which allows ready recognition": after every sentence he types into his report, he will ask himself, "Is this statement actually and literally true?" For that is his mastery.

Thus, his writing process goes like this—

"It may be possible after a period of heavy usage, a sudden fissure may appear." Is this statement actually and literally true? _Yes!_ It [_may be possible!_](https://www.lesswrong.com/posts/ooypcn7qFzsMcy53R/infinite-certainty)

"The possibility of a molecular reaction, at present unknown, cannot be entirely discounted." Is this statement actually and literally true? _Yes!_ The _possibility_ of a molecular reaction, at present unknown, _cannot be entirely discounted_. Okay, so there's [not enough](https://www.lesswrong.com/posts/nj8JKFoLSMEmD3RGp/how-much-evidence-does-it-take) evidence to [single out](https://www.lesswrong.com/posts/MwQRucYo6BZZwjKE7/einstein-s-arrogance) that possibility as [worth paying attention to](https://www.lesswrong.com/posts/X2AD2LgtKgkRNPj2a/privileging-the-hypothesis). [But there's still a chance, right?](https://www.lesswrong.com/posts/q7Me34xvSG3Wm97As/but-there-s-still-a-chance-right)

"Although the tensile strength of the metal is obviously demonstrable, certain questions in regard to its behavior under unusual stress are not to be ruled out." Is this statement actually and literally true? _Yes!_ The lab tests demonstrated the metal's unprecedented tensile strength. But certain questions in regard to its behavior under unusual stress are _not to be ruled out_—the [probability isn't _zero_](https://www.lesswrong.com/posts/QGkYCwyC7wTDyt3yT/0-and-1-are-not-probabilities).

And so on. You see the problem. Perhaps a member of the general public who _knew_ about the corruption at the State Science Institute could read the report and [infer the existence of hidden evidence](https://www.lesswrong.com/posts/kJiPnaQPiy4p9Eqki/what-evidence-filtered-evidence): "Wow, even when trying their hardest to trash Rearden Metal, _this_ is the worst they could come up with? Rearden Metal must be pretty great!"

_But they won't_. An institution that proclaims to be dedicated to "science" is asking for a _very high_ level of trust—and [in the absence of a trustworthy auditor](https://en.wikipedia.org/wiki/Quis_custodiet_ipsos_custodes%3F), they might get it. Science is complicated enough and natural language is ambiguous enough, that that kind of trust that can be _betrayed_ without lying.

I want to emphasize that I'm _not_ saying the report-drafting scientist in the scenario I've been discussing is a "bad person." (As it is written, [almost no one is evil; almost everything is broken.](https://blog.jaibot.com/)) Under more favorable conditions—in a world where metallurgists had the academic freedom to speak the truth as they see it [(even if their voice trembles)](https://www.lesswrong.com/posts/pZSpbxPrftSndTdSf/honesty-beyond-internal-truth) without being threatened with ostracism and starvation—the _sort of person_ who finds the wizard's oath appealing, wouldn't even be _tempted_ to engage in these kinds of not-technically-lying shenanigans. But the point of the wizard's oath is to constrain you, to have a _simple_ bright-line rule to _force_ you to be truthful, _even when other people are making that genuinely difficult_. Yudkowsky's meta-honesty proposal is a clever attempt to strengthen the foundations of this ethic by formulating a more complicated theory that can account for the edge-cases under which even unusually honest people typically agree that lying is okay, usually due to extraordinary coercion by an adversary, as with the proverbial murderer or Gestapo officer at the door.

And yet it's _precisely_ in adversarial situations that the wizard's oath is most constraining (and thus, arguably, most useful). You probably don't _need_ special [ethical inhibitions](https://www.lesswrong.com/posts/cyRpNbPsW8HzsxhRK/ethical-inhibitions) to tell the truth to your friends, because [you should expect to _benefit_ from friendly agents having more accurate beliefs](http://benjaminrosshoffman.com/humility-argument-honesty/).

But an enemy who wants to use information to hurt you is most constrained if the worst they can do is [selectively report](https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting) harmful-to-you _true_ things, rather than just making things up—and therefore, by symmetry, if you want to use information to hurt an enemy, _you_ are most constrained if the worst you can do is selectively report harmful-to-the-enemy true things, rather that just making things up.

Thus, while the study of how to minimize information transfer to an adversary under the constraint of not lying is certainly _interesting_, I argue that this "firming up" is of limited practical utility given [the ubiquity](https://unstableontology.com/2019/09/10/truth-telling-is-aggression-in-zero-sum-frames/) of _other_ kinds of deception. A theory of under what conditions conscious explicit unambiguous outright lies are acceptable doesn't help very much with combating _intellectual_ dishonesty—and I fear that intellectual dishonesty, plus sufficient intelligence, is enough to destroy the world all on its own, without the help of conscious explicit unambiguous outright lies.

Unfortunately, I do not, at present, have a superior alternative ethical theory of honesty to offer. I don't _know_ how to unravel the web of deceit, rationalization, excuses, disinformation, bad faith, fake news, phoniness, gaslighting, and fraud that threatens to consume us all. But one thing I'm pretty sure _won't_ help much is _clever logic puzzles about implausibly sophisticated Nazis_.

_(Thanks to Michael Vassar for feedback on an earlier draft.)_
