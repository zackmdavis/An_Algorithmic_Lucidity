Title: Convention
Date: 2014-07-13 23:11
Status: published
Category: computing
Tags: Clojure

```console
$ lein new 3lg2048
Project names must be valid Clojure symbols.
$ lein new Thirty-Three
Project names containing uppercase letters are not recommended 
and will be rejected by repositories like Clojars and Central. 
If you're truly unable to use a lowercase name, please set the 
LEIN_BREAK_CONVENTION environment variable and try again.
$ LEIN_BREAK_CONVENTION=1
$ lein new Thirty-Three
Project names containing uppercase letters are not recommended 
and will be rejected by repositories like Clojars and Central. 
If you're truly unable to use a lowercase name, please set the 
LEIN_BREAK_CONVENTION environment variable and try again.
$ export LEIN_BREAK_CONVENTION="fuck you"
$ lein new Thirty-Three
```
