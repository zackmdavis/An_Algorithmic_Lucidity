Title: Dance, Dance
Date: 2026-10-05
Status: draft
Category: psychology
Tags: dance

As a brash but anxious young programmer in the before-time, I affected a standoffish attitude on the topic of _games_. Why would I learn to play a game as a human, I said, when I could just write a program to do it? [When an office chess game got started at my workplace](/blog/2019/May/minimax-search-and-the-structure-of-cognition/), I [wrote](/blog/2016/Jan/ideas-have-expirations/) [a chess engine](https://github.com/zackmdavis/Leafline) (a standard [minimax search](https://en.wikipedia.org/wiki/Negamax) with [α–β pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)) rather than learn anything about strategy or tactics. When my insufficiently requited love started hosting a meetup to play [Zendo](https://en.wikipedia.org/wiki/Zendo_(game))—a deduction game in which one player makes up a rule to positively or negatively classify arrangements of plastic pyramids, while the others submit arrangements to be classified to help them guess the rule—I wrote [a program](https://github.com/zackmdavis/Mezzanine) to efficiently propose examples to deduce a true rule from dozens of candidates. (Given a distribution over hypotheses, it generated an arrangement whose positive or negative classification would eliminate half the remaining probability-mass.)

Now, in my old age (and the present end-time in which custom software is no longer such a flex), I no longer feel the need to pretend not to understand the appeal of games. I even [learned](https://www.chess.com/member/zackmdavis/stats?time=0) [chess](https://lichess.org/@/zackmdavis) properly back in 'twenty-four.

The one that's captured my interest lately is the arrow-stomping game—known by a couple other brand names in addition to the original, whose inessential differences of implementation accentuate rather than obscure its fundamental nature as the same game. (Except the South Korean one is trash because the timing windows and letter grades are too lenient.)

<video class="alignright" poster="{static}/images/dance_dance-poster.jpg" width="340" autoplay loop 
  muted playsinline>
   <source src="{static}/images/dance_dance.mp4" type="video/mp4">
</video>

The arrow-stomping game is notable for being trivial from the perspective of my before-time impulse to write a program for it. When programming (say) chess, the implementation of the rules of the game is quite different from the implementation of the tree search agent to play the game. Moreover, a chess program is an exercise in logic: the program need only represent the abstract structure of the game; robotics to move physical pieces on a physical board would be considered superfluous if they were considered at all.

The arrow-stomping game is just the opposite. If you implemented the game as a sequence of timers (expect Left in 2.0 seconds, Up in 2.25 seconds, Right in 2.5 seconds ...), then the natural implementation of an agent to play the game would be—the same sequence of timers (input Left in 2.0 seconds, _&c_.). Arrow-stomping is _only_ interesting as a robotics problem: the struggle of an embodied agent to convert visual cues to timing information and a motor plan to deliver a force to the appropriate panel or panels at the requested moment. It is thus particularly suited to the present end-time as an illustration of [Moravec's paradox](https://en.wikipedia.org/wiki/Moravec%27s_paradox). The games that endure are sports, which appear cognitively trivial only because the form of cognition demanded is more ancient than language, with the effect that we can't talk about it and the pretraining set (for all the vastness of webtext) doesn't cover it.

A related way in which the pre-linguistic nature of arrow-stomping seems thematically suited to the present end-time has to do with how the process of learning it [casts doubt on the dream of an intelligence shaped like Reason itself](https://minihf.com/posts/2023-10-16-hermes-lecture-3-why-do-cognitive-scientists-hate-llms/). In the before-time, people thought that the end-times would be brought about by "good old fashioned" engineering turned on itself: [the code that writes the code that writes the code that ends the world](https://unremediatedgender.space/2019/Dec/i-want-to-be-the-one/).

To be clear, that's still plausible as a theoretical possibility for a later end-time, but it turned out to be unnecessary for the beginning of the end-times. For now, we don't know how to write the code that writes the code. We can only write code to train networks that write code. The kind of legible symbolic reasoning embodied in a chess engine is the output of a process that doesn't seem to natively have the shape of legible symbolic reasoning.

Likewise the solution to the robotics problem. Every arrow summons a _judgment_. In the original-brand implementation, they are Marvelous (±17 ms), Perfect (±34 ms), Great (±84 ms), Good (±124 ms), and Miss. (Apparently historical contingency forces us to suffer "Perfect" not being the best judgment. The American one at least has the decency to call the best judgment "Perfect!!" with two exclamation points, as distinguished from "Perfect".)

The judgments are a densely supervised training signal. Beyond a few words of high-level advice (try to alternate your feet), one does not "study" arrow-stomping. In principle, we could imagine a mind inspecting a sequence of upcoming arrows and searching for a motor plan to fit them, like a chess engine calculating variations. As a human, there's no time for that. One can only let one's policy be shaped by the rewards of the judgments. (The American-brand implementation provides gradient information by displaying "Early" or "Late" as part of the on-screen judgment; in the original, you have to toggle a config option.)

Arrows often come in patterns (like Left–Right–Left or Right–Up–Right), which can be "chunked" and loaded as one motor program, rather than read as individual notes. The chunking theory correctly predicts that losing the rhythm often results in correlated poor judgements on consecutive notes, in contrast to the independent "Gaussian" error on every step. A Great Fullcombo (completing a song with only Great or better judgments) isn't overwhelmingly harder than a Fullcombo (no Miss judgements): both imply having held the rhythm the whole way, with the Great Fullcombo ["only" (only)](https://zackmdavis.net/blog/2012/Oct/the-quieted-scare-convention/) requiring a tighter Gaussian variance.

The levels of the game provide a smooth progression. As the player masters simpler patterns, higher difficulty levels provide new ones. On level 6 of the original-brand implementation, notes spaced at closer intervals (shown in different colors) become common.

[TODO—

Patterns like Left–Down–Right imply

either breaking 

(Left with left foot, Down with right foot, Right with _left_ foot)

, in contrast to the 


Contrast to chess where ratings can be flat for years of play—you have to study; you don't necessarily learn enough from experience. Contrast to gymnastics where I didn't have enough of a gradient to learn a handstand. 

at the beginning, I tried to treat the center as "home base"), but mostly, you play, and the judgments give you a gradient, and the levels give you a very smooth loss progression (patterns show up, then blue notes at level 6, and you get used to seeing the patterns as chunks and loading them as one motor program). You don't linguistically reason about where to put your feet, you just get a sense of it. (The pattern-chunking isn't a taught technique, it's a natural solution to the learning problem.)

]

A revolution.