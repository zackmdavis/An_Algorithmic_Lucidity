Title: Computing the Powerset
Date: 2013-12-10 05:00
Status: published
Category: computing
Tags: Clojure, combinatorics
Slug: computing-the-powerset

Suppose we want to find the powerset of a given set, that is, the set of all its subsets. How might we go about it? Well, the powerset of the empty set is the set containing the empty set.

$$\mathcal{P}(\emptyset)=\{\emptyset\}$$

And the powerset of the union of a set _S_ with a set containing one element _e_, is just the union of the powerset of _S_ with the set whose elements are like the members of the powerset of _S_ except that they also contain _e_.

$$\mathcal{P}(S\cup\{e\})=\mathcal{P}(S)\cup\{t\cup\{e\}\}\_{t\in\mathcal{P}(S)}$$

So in Clojure we might say

```clojure
(require 'clojure.set)

(defn include-element [collection element]
  (map (fn [set] (clojure.set/union set #{element}))
       collection))

(defn powerset [set]
  (if (empty? set)
    #{#{}}
    (let [subproblem (powerset (rest set))]
      (clojure.set/union subproblem
                         (include-element subproblem
                                          (first set))))))
```
