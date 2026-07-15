Title: $
Date: 2015-07-19 22:45
Status: published
Category: computing
Tags: Clojure, Python, Ruby

I used to think of `$` in regular expressions as matching the end of the string. I was wrong! It actually might do something more subtle than that, depending on what regex engine you're using. In my [native](http://zackmdavis.net/blog/2014/11/native-tongue/) Python's [`re` module, `$`](https://docs.python.org/3/library/re.html)

> [m]atches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline.

Note! The end of the string, _or just before the newline at the end of the string_.

```text
In [2]: my_regex = re.compile("foo$")

In [3]: my_regex.match("foo")
Out[3]: <_sre.SRE_Match object; span=(0, 3), match='foo'>

In [4]: my_regex.match("foo\n")
Out[4]: <_sre.SRE_Match object; span=(0, 3), match='foo'>
```

I guess I can see the motivation—we often want [to use](https://docs.python.org/3/library/stdtypes.html#str.splitlines) the newline character as a terminator of lines (by definition) or files (by [sacred tradition](http://unix.stackexchange.com/a/18789)), without wanting to think of `\n` as really part of the content of interest—but the disjunctive behavior of `$` can be a source of treacherous bugs in the fingers of misinformed programmers!

It happened to me while I was doing speculative pre-development of the speculative pre-prototype for my speculative [Glitteral programming language](https://github.com/zackmdavis/Glitteral), specifically in the lexical analyzer—the part of a compiler that recognizes strings of source code as representing _tokens_ that mean something in the language's grammar: this is a language keyword, that's an integer literal, this is an identifier, and so forth. My makeshift lexical analyzer (inspired by, but diverging significantly from, the more sophisticated thing that textbook said to do—I was in a hurry) involved deciding if a segment of source code could represent a particular token (or prefix thereof) by checking if it matched the regular expression defining each token class (or a regex describing prefixes of that token class). I had prudently (but not prudently enough, as you see) anchored each of my token class regexes with `$`, so that, for example, the source fragment `fore` could not be erroneously recognized as the language keyword `for`. But that just left me with a bug in which a newline immediately following a token would be recognized as part of the token: for example, you could end up lexing the string `3\n` as an integer literal, even though the integer literal was supposed to be just `3`. After [my first crude fix](https://github.com/zackmdavis/Glitteral/commit/abfe411b) later proved to be inadequate, I ended up [fixing it by augmenting the `$`s with the negative lookahead assertion `(?!\n)` immediately thereafter](https://github.com/zackmdavis/Glitteral/commit/832285a8), in effect saying, "match the end of the string or just before the newline at the end of the string, _but_ not just before a newline," the negative lookahead assertion canceling out the interpretation of `$` that I didn't want. And then later I [replaced all those `$(?!\n)`s with `\Z`s](https://github.com/zackmdavis/Glitteral/commit/b5961d66) (which _actually_ match the end of the string, like I wanted in the first place), after it was brought to my attention that `\Z` was a thing.

But I'm not the only one who was confused! (Note: the previous sentence should be read in a tone of terror and despair at the tightness of the cruel grip of ignorance on our fragile world, _not_ relief that other people are as dumb as me.) The famous Django web application framework recently released patch versions [1.8.3](https://docs.djangoproject.com/en/1.8/releases/1.8.3/), [1.7.9](https://docs.djangoproject.com/en/1.8/releases/1.7.9/), and [1.4.21](https://docs.djangoproject.com/en/1.8/releases/1.4.21/) due to security concerns, one of which being [validators failing to guard against possible header injection vulnerabilities](https://www.djangoproject.com/weblog/2015/jul/08/security-releases/#s-header-injection-possibility-since-validators-accept-newlines-in-input) owing to [the use of `$` instead of `\Z` in regular expressions](https://github.com/django/django/commit/574dd5e0).

All this that I have said about `$` in regexes concerns the Python world. Apparently [Perl is the same way](http://perldoc.perl.org/perlre.html#Regular-Expressions) (maybe we got it from them?). But other regex engines don't have the "or just before the newline" semantic flourish in their interpretation of `$`. [In Java, for example](http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) (and therefore, more importantly from my point of view, Clojure),

> [b]y default, the regular expressions `^` and `$` ignore line terminators and only match at the beginning and the end, respectively, of the entire input sequence.

```text
user=> (re-matches #"foo$" "foo")
"foo"
user=> (re-matches #"foo$" "foo\n")
nil
```

[Whereas in Ruby](http://ruby-doc.org/core-2.2.0/Regexp.html#class-Regexp-label-Anchors), `$` is explicitly the end of _line_ anchor (like in Python's `MULTILINE` mode), `\Z` matches the end of the string or just before the newline if the string ends with a newline (like Python's default), and `\z` is for the end of the string!

I guess the moral is that if you want to write a kind of regular expression that you're not already intimately familiar with, you should think carefully and read the owner's manual of your chosen regex engine. What you find there may surprise you!
