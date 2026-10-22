Title: San Francisco State University in Twilight
Date: 2026-10-17
Status: draft
Category: mathematics
Tags: analysis, artificial intelligence

I've been crashing [Prof. Lai](https://sites.google.com/view/chunkitlai/)'s "Advanced Topics" class this semester, on Fourier analysis plus enough functional analysis to get by (since the University can't afford to offer functional analysis as a regular class anymore). It's not obviously a good use of my time, but now that I've started, I have to see it through. I could try to tell a story about _impact_: I am leveling up my math chops, which will be useful for understanding natural abstractions or singular learning theory or mechanistic explanation, which will be useful for—but maybe it's less embarrassing to not try to sell a story. Call it luxury consumption during garbage time. I've lived a good life, in some ways if not others. I could choose to drown in oceans of regret over all the songs I never finished and stories I never wrote and math I never learned when I was young, in the before-time when there was still enough clock in the timeline for these things to matter—or I could choose to do something with the time I have now, which doesn't.

Only it's not quite the same as it was in the before-time. Part of the glamor of learning math in the before-time lay in the irreplaceability of expensive human capital investment. Textbooks contained information, but information could only become living knowledge through uncounted hours of laborious struggle, whose pain could only be tolerated on the promise that it expanded the reach of one's intellect and kept the flame of civilization alive.

It's not completely different now. What's still true is that information can only become _human_ knowledge through uncounted hours of laborious struggle. And as far as the production of human knowledge goes, the present end-time should be much superior to anything that came before. Anything you would have done in the before-time, you can still do. Nothing has been taken away. It's just that now you have the option of chatting with an indefatigably patient tutor who knows everything, is always online, and works for $20 a month.

It should be much superior. Some of the struggle to compile information into human knowledge is intrinsic to the endeavor (one aspires to learn to solve problems, not merely be told how to solve problems), but too much of the struggles of the before-time were clearly unnecessary. Think of all the moments when a minimal well-timed hint from a tutor could have converted the deathly suffering of being _stuck_ to the life-affirming suffering of productive struggle, but no tutor was available until scheduled office hours—or at all. (Say, if you wanted to learn functional analysis but didn't serve an institution offering a "class" on it.) Having the tutor live in your phone should amount to a fantastic efficiency gain.

[TODO:
summation by parts tutoring
the connection to my anti-school 
https://x.com/jd_pressman/status/1882407537917804759
the flame survives
assembly language 
]

On 16 September, the class had its first examination. (When I had dropped by office hours the other day, Prof. Lai had said I could take it, but that he might not grade it.) I hadn't prepped enough and did poorly, blanking on two parts. I didn't hand in the paper, but GPT-6 Astra later gave it 58%.

![torso of man wearing purple אוניברסיטת המדינה בסן פרנסיסקו המחלקה למתמטיקה shirt]({static}/images/sfsu_math_dept_shirt.jpg){: width="300" .alignright }

After enjoying lunch and [dancing](/blog/2026/Oct/dance-dance/) at the [mall](https://en.wikipedia.org/wiki/Stonestown_Galleria), I walked back to campus for the math department's occasional [seminar](https://sites.google.com/view/sfsuagc/fall-2026). On a whim, I had recently ordered a custom branded department tee (in Hebrew, with the thought of trolling the other analysis professor, who is a big free-Palestine guy), which I was sure to wear for the occasion. (Ordering custom T-shirts online was already a thing in the before-time, but my modest [GIMP](https://en.wikipedia.org/wiki/GIMP) skills would not have yielded as attractive a result in as little effort.) [Aida Abiad](https://aidaabiad.win.tue.nl/) of the Eindhoven University of Technology was speaking on coding theory applications of spectral graph theory, a topic of nonzero interest to me. (In October 2009, I had ordered a copy of _An Introduction to the Theory of Graph Spectra_, which sat mostly untouched among my textbook collection for the intervening seventeen years.)

The talk was pretty accessible, as these things go. The independence number $\alpha$ of a graph is the maximum size of [a set of non-adjacent vertices](https://en.wikipedia.org/wiki/Independent_set_(graph_theory)). The exact independence number of a graph is [hard to compute](https://en.wikipedia.org/wiki/NP-hardness), but back in the 1970s, people had come up with some upper bounds in terms of the [eigenvalues](/blog/2012/Dec/eigencritters/) of the graph's [adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix). Abiad explained her work on extending such techniques to bound the _k_-independence number $\alpha_k$ (the maximum size of a set of vertices with graph distance greater than _k_ from each other). Once you have a bound in terms of powers of the eigenvalues, it's natural to ask, what about a polynomial?—and then, which polynomial is the best? Then there are applications: if you're constructing a code, then an isomorphism between a graph and a metric space on your set of possible codewords helps you answer, what's the largest code you can construct whose codewords are at least a given distance apart?

For the most part, it felt like that talk in that room could have taken place any time in the past seventeen or twenty-seven years. (Much further back than that, and it's harder to believe that SFSU would have had a digital projector rather than still being on [transparencies](https://en.wikipedia.org/wiki/Transparency_(projection)).) Abiad discussed bound improvements published in 2016, 2019, and 2022, but as far as I could tell as a non-specialist, there was no reason the same results couldn't have been reached in 2006 or 2009 or 2012 except that no one had gotten around to it yet. Besides the paper dates, the relative timelessness of the moment was only betrayed by a few odd remarks Abiad made, like, "Now probably the artificial intelligence gives you the graph invariants if you ask for it."

Afterwards, I took the 28 bus back to Daly City BART station. At the station, the bus stopped before pulling all the way up to the curb. Apparently a car was in the way: the bus driver honked a few times, then more frequently, then in one long, continuous honk. Why wasn't the car moving? "It's a Waymo!" one of the passengers said. "Fucking Waymo," said someone else. "Bring back human drivers!" said a man. The bus driver gave up and opened the doors, still short of the curb. Walking to the station among the throng, I saw that the offending Waymo had moved out of the way; it was unclear what had aroused it to motion.

On the train home, inspiration struck. Recently, one Levent Alpöge of Anthropic (and before that, someplace called "Harvard") had been in everyone's feed for Tweeting AI-assisted solutions to famous open problems. I didn't have access to the frontier magic that Alpöge had, but I wondered if there was more low-hanging fruit accessible to the public models that hadn't been plucked yet just because there were few enough math people monitoring the AI situation that no one had spent the tokens yet. (My impression from hanging out at SFSU had been that everyone knew about LLMs as a way for students to cheat on homework—that's why Prof. Lai couldn't give take-home exams anymore—or for researchers to look up graph invariants, but that few were looking at the bigger picture.)

When I got home, I tasked Claude Opus 5 in Claude Code with going through the papers of [Prof. Emily Clader](https://sites.google.com/site/emilyclader/) (who had let me [crash her "Topics" class on algebraic topology this time last year](http://zackmdavis.net/docs/algebraic_topology-01.pdf)) to look for "open problems that might be interesting to her that might be scoopable with an LLM (so, like, stuff where you can compute a checkable counterexample, which would have been a master's student project)". I said that scooping the result would "probably demand expensive Fable tokens, although Opus is probably fine" for the literature search.

[TODO: fill in context about moduli spaces and log-concavity from the papers]

Opus downloaded the LaTeX sources of Clader's papers and grepped for phrases like "open problem", "conjecture" and "future work." After 84 seconds, it reported, "Found a promising one already: CDLR (arXiv:2208.05463) conjectures that the Betti numbers of $\overline{\mathcal{L}}^r_n$ are log-concave." Another 52 seconds later, it had written a Python program to reproduce the table of Betti numbers in the paper. Eighteen seconds later, it had written another Python program to empirically check the log-concavity of the Betti numbers—and whether the their generating polynomial had real roots, which would imply log-concavity. Thirty-nine seconds later, it concluded, "No counterexamples turned up — every case is log-concave and real-rooted, so real-rootedness likely implies log-concavity here."

It had recognized the generating polynomial as related 



http://zackmdavis.net/docs/betti_numbers_form_a_log-concave_sequence.pdf
http://zackmdavis.net/docs/log_concavity_Lrn.pdf


[TODO—
https://terrytao.wordpress.com/2026/09/24/were-gonna-need-a-lot-more-mathematicians/
https://arxiv.org/abs/2609.28603
]