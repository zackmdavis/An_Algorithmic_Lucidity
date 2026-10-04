Title: Dance, Dance
Date: 2027-01-01
Status: draft
Category: psychology
Tags: dance

As a brash but anxious young programmer in the before-time, I affected a standoffish attitude on the topic of _games_. Why would I learn to play a game as a human, I said, when I could just write a program to do it? [When an office chess game got started at my workplace](/blog/2019/May/minimax-search-and-the-structure-of-cognition/), I [wrote](/blog/2016/Jan/ideas-have-expirations/) [a chess engine](https://github.com/zackmdavis/Leafline) (a standard minimax search with α–β pruning) rather than learn anything about strategy or tactics. When my insufficiently requited love started hosting a meetup to play [Zendo](https://en.wikipedia.org/wiki/Zendo_(game))—a deduction game in which one player makes up a rule to positively or negatively classify arrangements of plastic pyramids, while the others submit arrangements to be classified to help them guess the rule—I wrote [a program](https://github.com/zackmdavis/Mezzanine) to efficiently propose examples to deduce a true rule from dozens of candidates. (Given a distribution over hypotheses, it generated an arrangement whose positive or negative classification would eliminate half the remaining probability-mass.)

Now, in my old age (and the present end-time in which custom software is no longer such a flex), I no longer feel the need to pretend not to understand the appeal of games. I even [learned](https://www.chess.com/member/zackmdavis/stats?time=0) [chess](https://lichess.org/@/zackmdavis) properly back in 'twenty-four.

The one that's captured my interest lately is the arrow-stomping game—known by a couple other brand names in addition to the original, whose inessential differences of implementation accentuate rather than obscure its fundamental nature as the same game. (Except the South Korean one is trash because the timing windows and letter grades are too lenient.)

The arrow-stomping game is notable for being trivial from the perspective of my before-time impulse to write a program for it. When programming (say) chess, the implementation of the rules of the game is quite different from the implementation of the tree search agent to play the game. Moreover, a chess program is an exercise in logic: the program need only represent the abstract structure of the game; robotics to move physical pieces on a physical board would be considered superfluous if they were considered at all.

The arrow-stomping game is just the opposite. If you implemented the game as a sequence of timers (expect Left in 2.0 seconds, Up in 2.25 seconds, Right in 2.5 seconds ...), then the natural implementation of an agent to play the game would be—the same sequence of timers (input Left in 2.0 seconds, _&c_.). Arrow-stomping is _only_ interesting as a "robotics" problem: the struggle of an embodied agent to convert visual cues to timing information and a motor plan to deliver a force to the appropriate panel or panels at the requested moment. It is thus particularly suited to the present end-time as an illustration of Moravec's paradox. The games that endure are sports, which appear cognitively trivial only because the form of cognition demanded is more ancient than language, with the effect that we can't talk about it and the pretraining set (for all the vastness of webtext) doesn't cover it.

A related way in which the pre-linguistic nature of arrow-stomping seems suited to the present end-time has to do with how the process of learning it gives the lie to 



[TODO—
The appeal is that it's a Moravec-proof game!

And rather than writing a GOFAI program (as I did with chess or Zendo) the learning method is modern— the judgements give you a very clear gradient. (StepManiaX Perfect!!/Perfect/Late/Early/Miss has Late/Early as first-class judgements, but there's a config option to make DDR show Late/Early, too—that's important for gradient information. And the less we say about the South Korean game with the inflated grades and timing windows, the better.)

Contrast to chess where ratings can be flat for years of play—you have to study; you don't necessarily learn enough from experience. Contrast to gymnastics where I didn't have enough of a gradient to learn a handstand. 

There are a few verbal tips that can be given (try to alternate feet; at the beginning, I tried to treat the center as "home base"), but mostly, you play, and the judgements give you a gradient, and the levels give you a very smooth loss progression (patterns show up, then blue notes at level 6, and you get used to seeing the patterns as chunks and loading them as one motor program). You don't linguistically reason about where to put your feet, you just get a sense of it. (The pattern-chunking isn't a taught technique, it's a natural solution to the learning problem.)

You can tell that you're not reading individual notes, because when you get out of sync with the beat, you miss a lot of consecutive notes correlatedly (as contrasted to the individual Gaussian error that tightens up and lets you get Great Fullcombos when previously a regular Fullcombo seemed hard). 
]

[TODO: not sure how to tie off the piece?]
