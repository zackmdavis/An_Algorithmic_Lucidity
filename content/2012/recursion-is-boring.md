Title: Recursion Is Boring
Date: 2012-09-13 05:00
Status: published
Category: computing
Tags: Emacs, Git
Slug: recursion-is-boring

What the utter novice finds brilliant and fascinating, the slightly-more-experienced novice finds obvious and boring.

When you're trying to think of cool things to do with a system, one of the obvious things to try is to abuse self-reference for all the world as if you were Douglas fucking Hofstadter—but it's not cool, precisely because it is so obvious, and you're not Douglas Hofstadter.

Once I made a Git repository and a Mercurial repository living in the same directory, tracking each other endlessly, one going out of date the moment you committed to the other ...

But that's not interesting.

You can run Emacs inside a terminal, and you can run a terminal inside Emacs—in fact, you can run two (_M-x term_, _M-x ansi-term_). Therefore you can run two instances of Emacs within Emacs. Each of those Emacsen could run some natural number of other nested Emacsen, and therefore (to a certain perverse sort of mind) could be said to _represent_ that natural number, which I presume could be determined programmatically (via recursion). [Two-counter machines are Turing-complete](http://en.wikipedia.org/wiki/Counter_machine#Two-counter_machines_are_Turing_equivalent_.28with_a_caveat.29). So, in principle, if you didn't run out of memory, you could build a computer out of instances of Emacs running on your computer ...

But that's boring.
