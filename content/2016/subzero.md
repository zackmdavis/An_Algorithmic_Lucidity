Title: Subzero
Date: 2016-04-06 22:05
Status: published
Category: computing
Tags: Python

Python has this elegant destructuring-assignment iterable-unpacking syntax that every serious Pythonista and her dog tends to use whereëver possible. So where a novice might write

```python
split_address = address.split(':')
host = split_address[0]
port = split_address[1]
```

a serious Pythonista (_and_ her dog) would instead say

```python
host, port = address.split(':')
```

which is clearly superior on grounds of succinctness and beauty; we don't want our vision to be cluttered with this ugly sub-zero, sub-one notation when we can just declare a sequence of names.

Consider, however, the somewhat-uncommon case where we have an iterable that, for whatever reason, we happen to _know_ contains only one element, and we want to assign that one element to a variable. Here, I've seen people who ought to know better fall back to indexing:

```python
if len(jobs) == 1:
   job = jobs[0]
```

But there's _no reason_ to violate the æsthetic principle of "use a length-_n_ ([or smaller](https://www.python.org/dev/peps/pep-3132/)) tuple of identifiers on the left side of a destructuring assignment in order to name the elements of a length-_n_ iterable" just because _n_ happens to be one:

```python
if len(jobs) == 1:
   job, = jobs
```
