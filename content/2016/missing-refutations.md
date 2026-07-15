Title: Missing Refutations
Date: 2016-02-17 00:21
Status: published
Category: social science
Tags: chess, politics
Slug: missing-refutations

It [looks like](https://github.com/swiftstack/Chesswork/commit/681085b3) the opposing all-human team is winning the exhibition game of me and [my it's-not-chess engine](http://zackmdavis.net/blog/2016/01/ideas-have-expirations/) (as White) _versus_ everyone in the office who (unlike me) actually knows something about chess (as Black). I mean, naïvely, my team is up a bishop right now, but our king is pretty exposed, and the [principal variation](https://en.wikipedia.org/w/index.php?title=Variation_%28game_tree%29&oldid=545070873#Principal_variation) that generated one of our recent moves (16. Bxb4 Bf5 17. Kd1 Qxd4+ 18. Kc1 Ng3 19. Qxc7 Nxh1) looks _dreadful_.

Real chess aficionados (chessters? chessies?) will laugh at me, but it actually took me a while to understand why Ng3 was in that principal variation (I might even have invoked the engine again to help). The position after Ng3 looks like

```text
    a b c d e f g h
 8 ♜       ♜   ♚   
 7 ♟ ♟ ♟     ♟ ♟ ♟ 
 6                 
 5           ♝     
 4   ♗   ♛         
 3 ♙           ♞   
 2   ♙ ♕     ♙ ♙ ♙ 
 1 ♖ ♘ ♔     ♗   ♖
```

and—forgive me—I didn't understand why that wasn't refuted by fxg3 or hxg3; in my novice's utter _blindness_, I somehow failed to see the discovered attack on the white queen, the necessity of evading which allows the black knight to capture the white rook, and preparation for which was clearly the purpose of 16. ..Bf5 (insofar as we—anthropomorphically?—attribute _purpose_ to a sequence of moves discovered by a minimax search algorithm which doesn't represent concepts like _discovered attack_ anywhere).

It's the little things like this that reinforce my suspicion that human cognition doesn't really work most of the time, that to the extent that we have a technological civilization with nice things in it, it's a matter of a bunch of apes, _some_ of whom are just _barely_ generally-intelligent, happening to stumble into patterns of coöperation that happened to scale, and not a matter of anyone within the system actually understanding much. It's the current year, and the current year turns out to be not only congruent to 0 mod 2, but furthermore to 0 mod _4_, which means outrage season is brewing again. I'm mostly pretty good at ignoring it, [except for](http://zackmdavis.net/blog/2012/11/i-just-want-outrage-season-to-be-over-already/) the undercurrent of contempt that I can't help but feel at how almost everyone seems to think it's _okay_ for important decisions to be made in this way.

The thing about chess is that it's a very simple game. There are these thirty-two figurines on an eight-by-eight grid, and you take turns moving the figurines subject to a few rules with a well-specified objective in mind. Simple. If you're lazy like me, you can even write a computer program to do it for you. And if you hadn't already spent many, many hours of study and practice mastering the game yourself, what such a program will surely show you (as it showed me, though I expected as much) is that your unaided attempts to make good moves will _get it wrong_. The novice thinks: checkmate is the goal, giving check is good, capturing material is good; I should look for moves that do those things. And the novice will _lose_, badly. What you actually need to do is look for your best move _given_ your opponent's best reply _given_ your best counterreply _given_ your opponent's best countercounterreply, and so on as far forward as you can afford to compute. It's not magic and it's not impossible, but it's _subtle_ and it takes _work_.

And the thing about the real world is that it is _unimaginably complicated_. There are seven billion humans on this radius-6.37·$10^6$ m planet, all haphazardly pursuing their own objectives subject to no rules except whatever high-level generalizations about the underlying fundamental physics strike you as sufficiently robust to be worth reifying as a _rule_. Unimaginable. And I feel like those appealing to the masses seeking leadership positions in the reigning institutions of governance don't properly appreciate this. You hear them or their boosters talk about how "we" obviously need to make college or healthcare free, or crush our terrorist foes, and to me it just sounds like so many shouts of "fxg3!" or "hxg3!". The _goals_ are noble: of course we _want_ America to be great, and for its people to be healthy and wealthy and knowledgeable and safe, just as a chess player _wants_ to checkmate the opposing king. But the interventions that _sound intuitively appealing_ aren't necessarily the same as the interventions that will _actually work_! "We" should hope for leaders with the courage and skepticism and _competence_ to say, "No, wait, that won't work because of ...Bxc2," and continue the search for better alternatives for our nation and its children.

But if I can _predict_ that that's not what "we" are going to choose, maybe I should continue searching for better alternative ways to spend my time than complaining about it.
