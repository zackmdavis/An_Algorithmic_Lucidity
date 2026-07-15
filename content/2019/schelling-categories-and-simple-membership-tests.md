Title: Schelling Categories, and Simple Membership Tests
Date: 2019-08-25 19:43
Status: published
Category: philosophy
Tags: rationality, philosophy of language, game theory
Slug: schelling-categories-and-simple-membership-tests

[(originally published at _Less Wrong_)](https://www.lesswrong.com/posts/edEXi4SpkXfvaX42j/schelling-categories-and-simple-membership-tests)

**Followup to**: [Where to Draw the Boundaries?](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries)

_Or there might be social or psychological forces anchoring word usages on identifiable Schelling points that are easy for different people to agree upon, even at the cost of some statistical "fit"_ ...

The one comes to you and says, "That paragraph about Schelling points sounded interesting. What did you mean by that? Can you give an example?"

Sure. Previously on _Less Wrong_, in ["The Univariate Fallacy"](https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy), we studied points sampled from two multivariate probability distributions $P_A$ and $P_B$, and showed that it was possible to [infer with very high probability](http://zackmdavis.net/blog/2019/05/the-typical-set/) which distribution a given point was sampled from, despite significant overlap in the marginal distributions for any one variable considered individually.

From the standpoint of ["the way to carve reality at its joints, is to draw your boundaries around concentrations of unusually high probability density in Thingspace"](https://www.lesswrong.com/posts/yLcuygFfMfrfK8KjF/mutual-information-and-density-in-thingspace), the correct categorization of the points in that example is clear. We have two clearly distinguishable clusters. The [conditional independence](https://www.lesswrong.com/posts/gDWvLicHhcMfGmwaK/conditional-independence-and-naive-bayes) property is satisfied: _given_ a point's cluster-membership, knowing one of the $x_i$ doesn't tell you anything about $x_j$ for _j_ ≠ _i_. So we should draw a category boundary around each cluster. Obviously. We might ask [hypophorically](https://en.wikipedia.org/wiki/Hypophora): what could _possibly_ change this moral?

More constraints on the problem, that's what!

Suppose you needed to _coordinate_ with someone else to make decisions about these points—that is, it's important not just that you and your partner make good decisions, but also [that you make the _same_ decision](https://www.lesswrong.com/posts/9QxnfMYccz9QRgZ5z/the-costly-coordination-mechanism-of-common-knowledge#Coordination_Problems)—but that each of you only got to observe one coordinate from each point. As we saw, the predictive work we get from category-membership in this scenario is [spread across _many_ variables](https://marcodgdotnet.files.wordpress.com/2018/04/delgiudice_2017_heterogeneity_d_mbr.pdf): if you only get to observe a _few_ dimensions, you have a lot of uncertainty about cluster-membership (which carries over into additional uncertainty about the other dimensions that you haven't observed, but which affect the _ex post_ quality of your decision).

If you and your partner were both ideal Bayesian calculators who could communicate costlessly, you would [share your observations](https://www.overcomingbias.com/2009/02/share-likelihood-ratios-not-posterior-beliefs.html), work out the correct probability, and use that to make optimal decisions. But suppose you _couldn't_ do that—either because communication is expensive, or your partner was bad at math, or any other reason. Then it would be sad if you happened to see $x_9$ = 2 and said "It's an A (probably)!", and your partner happened to see $x_{27}$ = 3 and said "It's a B (I think)!", and the two of you made inconsistent decisions.

Okay, _now_ suppose that there's actually a forty-first, binary, variable that I didn't tell you about earlier, distributed like so:

$$P_A(x_{41}) = \begin{cases} 3/4 & x_{41} = 0 \\ 1/4 & x_{41} = 1 \\ \end{cases}$$

$$P_B(x_{41}) = \begin{cases} 1/4 & x_{41} = 0 \\ 3/4 & x_{41} = 1 \\ \end{cases}$$

Observing $x_{41}$ gives you $\log_2 3$ ≈ 1.585 bits of evidence about cluster-membership, which is more than the

$$\frac{1/4 + 1/16}{2} \cdot |\log_2(4)| + \frac{7/16 + 1/4}{2} \cdot |\log_2(7/4)| + \frac{1/4 + 7/16}{2} \cdot |\log_2(4/7)| + \frac{1/16 + 1/4}{2} \cdot |\log_2(4)|$$

≈ 1.18 bits you can get from any one observation of one of the $x_i$ for _i_ ∈ {1...40}.

If you and your partner can both observe $x_{41}$, you might end up wanting to base your shared categories and language on _that_—calling a point an "A" if it has $x_{41}$ = 0, even though such points actually came from $P_B$ a full quarter of the time—even if $x_{41}$ itself has no effect on the quality of your decisions, and what you _actually_ care about is wholely determined by the values of $x_1$ through $x_{40}$! It's not the [intension](https://www.lesswrong.com/posts/HsznWM9A7NiuGsp28/extensions-and-intensions) you would pick if you could make (and share) _more observations_—but _ex hypothesi_, you can't.

If you and your partner only get to observe one variable, $x_{41}$ is your best choice—the single variable that gives you the most information about the "natural" cluster-membership. That also makes it a [_Schelling point_](https://www.lesswrong.com/posts/yJfBzcDL9fBHJfZ6P/nash-equilibria-and-schelling-points)—if you and your partner didn't get to commmunicate in advance about how you want to draw your shared category boundaries, you could pick $x_{41}$ as your defining observation and be pretty confident your partner would make the same choice. We could imagine an even more pessimistic scenario in which the Schelling point category definition (a set of variables that "stuck out" from all the others) was _less_ predictive than some other candidates—but if you couldn't _coordinate_ to _pick_ one of the more predictive category systems, you might be stuck with the Schelling point.

In conclusion, the right categories to use _given_ constraints on communication and observation, might be different from the category boundaries you would draw from a "God's eye view", in part because consideration of which categories are easy for different agents to _coordinate_ on is relevant, not just raw information-theoretic expressive power. Thus, "Schelling categories."

Thanks for reading!

-------

The one says, "No, I meant, like, a _real world_ example, not some dumb math thing for nerds. What is this post _really_ about?"

It's about ... math? Or like, the relationship between math and human natural language? Like, I was wondering what "second-order" caveats or complications there might be to the basic ["carve reality at the joints" moral](https://www.lesswrong.com/posts/d5NyJ2Lf6N22AD9PB/where-to-draw-the-boundary) of our [standard Bayesian philosophy of language](https://www.lesswrong.com/posts/FaJaCgqBKphrDzDSj/37-ways-that-words-can-be-wrong), and some of the people I've been collaborating with lately had been talking a lot about the importanace of [_intersubjective_ epistemology](http://benjaminrosshoffman.com/humility-argument-honesty/)—that is, [_shared_ mapmaking](https://twitter.com/jessi_cata/status/1113677758071070720), so—

"But where's the _actionable takeaway_? What's your _real_ agenda here, huh?"

Oh. One of _those_ readers, I see. Fine, I can probably think of some—how do you say?—"applications."

Ummmm ...

Let's see ...

Okay, here's something, maybe. What's the deal with the [age of majority](https://en.wikipedia.org/wiki/Age_of_majority)?

Society needs to decide who it wants to be allowed to vote, stand trial, sign contracts, serve in the military, _&c._ Whether it's a good idea for a particular person to have these privileges presumably depends on various _relevant_ features of that person: things like cognitive ability, foresight, wisdom, relevant life experiences, _&c_. In particular, it would be _pretty weird_ for someone's fitness to vote to directly depend on _how many times the Earth has gone around the sun since they were born_. What does _that_ number have to do with anything?

It doesn't! But if Society isn't well-coordinated enough to _agree_ on the exact prerequisites for voting and how to measure them, but _can_ agree that most twenty-five-year-olds have them and most eleven-year-olds don't, then we end up choosing some arbitrary age cutoff as the criterion for our "legal adulthood" social construct. It _works_, but it's just a legal fiction—and not necessarily a particularly good fiction, as any bright teenagers reading this will doubtlessly attest.

If I told you that a particular fourteen-year-old was very "mature", that's a contentful statement: we have shared meaning attached to the word _mature_, such that my describing someone that way [constrains your anticipations](https://www.lesswrong.com/posts/a7n8GdKiAZRX86T5A/making-beliefs-pay-rent-in-anticipated-experiences). But it's a _really complicated_ meaning, a statistical signal in behavior that your brain can pick up on, but which isn't particularly verifiable to others who might have reasons to doubt my character assessment. In contrast, age is easy for everyone to agree on. We could _imagine_ some hypothetical science-fictional Society that used brain scans and some sophisticated machine-learning classifer to determine which citizens get which privileges—but in our dumber, poorer world, calendars and subtraction will have to do.

In terms of [Scott Garrabrant's taxonomy](https://www.lesswrong.com/posts/EbFABnst8LsidYs5Y/goodhart-taxonomy) of applications of [Goodhart's law](https://www.lesswrong.com/posts/YtvZxRpZjcFNwJecS/the-importance-of-goodhart-s-law), this is regressional Goodhart: Society _wants_ to select for maturity, chooses age as a proxy, and in the process, ends up granting or withholding privileges that a more discriminating Society maybe wouldn't.

The age of majority is a case of replacing a _complicated_, [illegible](https://www.ribbonfarm.com/2010/07/26/a-big-little-idea-called-legibility/) category ("maturity", the kind of abstract thing you might want to model as a cluster in a forty- or forty-one-dimensional space) with a _simple_ membership test (an age cutoff that everyone knows how to compute). Different people might make make different _subjective_ (but not [arbitrary](https://www.lesswrong.com/posts/HacgrDxJx3Xr7uwCR/arbitrary)) judgements of the complicated, illegible category, so in order to get a more intersubjectively robust verdict on category-membership, we rely on an _objective_ measurement that everyone can agree on.

If no convenient objective measurement is available, another strategy is possible: we can _delegate_ to some canonical trusted authority, whose opinion of the complicated category will take precdence over everyone else's. An example of this is [commodity grading standards](https://www.usda.gov/our-agency/about-usda/laws-and-regulations/commodity-standards-and-grades). What is a "Grade AA" egg? Well, there's a complicated definition written down in [a manual somewhere](https://www.ams.usda.gov/sites/default/files/media/Egg%20Grading%20Manual.pdf) that you could try applying yourself—but for most people, Grade AA eggs are simply "those which have been certified as Grade AA by the USDA."[^america]

[^america]: Or the analogous agency in your country.

It's even possible for the "simple objective measurement" and "delegate to an authority's subjective judgement" strategies to be combined. In ["The Ideology Is Not the Movement"](https://slatestarcodex.com/2016/04/04/the-ideology-is-not-the-movement/), the immortal Scott Alexander writes about his model of the genesis of social groups—

> Pre-existing differences are the raw materials out of which tribes are made. A good tribe combines people who have similar interests and styles of interaction _even before_ the ethnogenesis event. Any description of these differences will necessarily involve stereotypes, but a lot of them should be hard to argue. [...] There are subtle habits of thought, not yet described by any word or sentence, which atheists are more likely to have than other people. [...]
>
> The rallying flag is the explicit purpose of the tribe. It's usually a belief, event, or activity that get people with that specific pre-existing difference together and excited. Often it brings previously latent differences into sharp relief. People meet around the rallying flag, encounter each other, and say "You seem like a kindred soul!" or "I thought I was the only one!" Usually it suggests some course of action, which provides the tribe with a purpose.

Eliezer Yudkowsky's ["A Fable of Science and Politics"](https://www.lesswrong.com/posts/6hfGNLf4Hg5DXqJCF/a-fable-of-science-and-politics) depicts a fictional underground society split between two such tribes: an predominantly urban tribe that believes that the unseen sky is blue (and favors an income tax, strong marriage laws, and an Earth-centric cosmology), and predominanty rural one that believes that the sky is green (and favors merchant taxes, no-fault divorce, and a heliocentric cosmology). In this story, beliefs about the color of the sky are functioning as the "rallying flag" for tribe-formation in Alexander's model—and as a Schelling point for category definition.

We don't know how to _talk_ about the preëxisting undefinable habits of thought that make social groups work—it's hard to _explicitly_ articulate what exact statistical regularity our brains have detected in five-and-more-dimensional locale/sky-belief/tax-belief/divorce-belief/cosmology/_&c_.-space. (Although we could imagine some hypothetical science-fictional Society that _did_ know how to articulate it, and consequently had richer forms of social and political organization than our own.) It's a lot simpler to talk about whether someone has pledged allegiance to the rallying flag: just _ask_ someone, "What color do you believe the sky is?" (using sky-beliefs as as an "objective" simple membership test), or simply, "Are you a Blue or a Green?" (delegating the classification problem to _the person themselves_ as the authority whose discernment is to be trusted)—and whatever they say, that's what they are.

Well, _probably_. We've seen that objective measurements like age are subject to regressional Goodhart, but the delegation-to-authority strategy is furthermore subject to [_adversarial_ Goodhart](https://www.lesswrong.com/posts/EbFABnst8LsidYs5Y/goodhart-taxonomy): once a category-membership test has been established, some agents might have an incentive to create examples that _pass the test_, but don't have the complicated, illegible properties than made the test a useful proxy in the first place.

We've seen this, for example, with [title inflation](http://benjaminrosshoffman.com/excerpts-from-a-larger-discussion-about-simulacra/): we expect the "job title" (the words that get printed on business cards or immigration sponsorship forms) to be the canonical description of what someone "does", even if the vagaries of the workday encompass many tasks,[^booth] and an alien anthropologist tasked with observing the worksite and summarizing what each of the humans did might slice up her observations into categories with little resemblance to the company's formal org chart. But since we don't know _how_ to do [the obvious thing](http://zackmdavis.net/blog/2014/06/standard-advice/) and average over all possible alien anthropologists [weighted by simplicity](https://arbital.greaterwrong.com/p/1hh?l=1hh), we can only rely on the org chart—which people have [political incentives](https://www.lesswrong.com/posts/45mNHCMaZgsvfDXbw/quotes-from-moral-mazes) to manipulate, with the result that [everyone in the finance industry is a "vice president"](https://www.thebalancecareers.com/job-titles-1287163) of some sort or another.

[^booth]: When I worked in [a supermarket](https://www.safeway.com/), two days a week I did Tracy's bookkeeping/customer-service job while Tracy had her weekend, which entailed counting the money from last night's tills _and_ swapping in new coinmags _and_ completing the FSM report _and_ answering the phone _and_ selling money orders _and_ covering the floral stand when the floral lady was on lunch, _&c._ I'm actually not sure what official name this role had in Safeway's official org chart. We just called it "the booth."

But "Vice President" has a _literal meaning_. Or it _used to_. _Vice_, ["in place of; subordinate to."](https://en.wiktionary.org/wiki/vice#Etymology_3) _President_, one who _presides_ over some deliberative body. The adversarial-Goodhart pressures on language ["exploit[ ] the trust we have in a functioning piece of language until it's lost all meaning"](https://slatestarcodex.com/2019/07/16/against-lie-inflation/).

So for readers who demand a takeaway beyond just an edge case in the math, perhaps take away this: coordination is [_costly_](https://www.lesswrong.com/posts/9QxnfMYccz9QRgZ5z/the-costly-coordination-mechanism-of-common-knowledge). From the standpoint of language as an AI capability, the social constructions that feeble humans need in order to work together may be [unavoidably dumbed-down for mass consumption](https://www.lesswrong.com/posts/4ZvJab25tDebB8FGE/you-have-about-five-words), but that's no reason to not _aspire_ to the true precision of the [Bayes-structure](https://www.lesswrong.com/posts/QrhAeKBkm2WsdRYao/searching-for-bayes-structure) to whatever extent possible.

_(Thanks to Ben Hoffman for the etymology of "Vice President.")_
