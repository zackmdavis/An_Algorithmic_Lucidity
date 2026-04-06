Title: Beauty Is Truthiness, Truthiness Beauty?
Date: 2021-04-20 22:55
Status: published
Category: computing
Tags: Python
Slug: beauty-is-truthiness-truthiness-beauty

Imagine reviewing Python code that looks something like this.
\_\_\_PRE\_BLOCK\_0\_\_\_
You might look at the conditional, and disapprove: `None` and empty collections are both falsey, so there's no reason to define that `has_items` variable; you could just say `if items:`.

But, wouldn't it be weird for `do_stuff`'s `has_items` kwarg to take a collection rather than a boolean? I think it would be weird: even if the function's internals can _probably_ rely on mere truthiness rather than needing an actual boolean type for some reason, why leave it to chance?

So, _maybe_ it's okay to define the `has_items` variable for the sake of the function kwarg—and, having done so anyway, to use it as an `if` condition.

You might object further: but, but, `None` and the empty collection are _still both falsey_. Even if we've somehow been conned into defining a whole variable, shouldn't we say `has_items = bool(items)` rather than spelling out `is not None and len(items) > 0` like some _rube_ [(or Rubyist)](https://stackoverflow.com/a/23068894) who doesn't know Python?!

Actually—maybe not. Much of Python's seductive charm comes from its friendly readability ("executable pseudocode"): it's _intuitive_ for `if not items` to mean "if `items` is empty". English, and not the formal truthiness rules, are all ye need to know. In contrast, it's only if you _already_ know the rules that `bool(items)` becomes meaningful. Since we care about good code and don't care about testing the reader's Python knowledge, spelling out `items is not None and len(items) > 0` is very arguably the _right thing to do_ here.
