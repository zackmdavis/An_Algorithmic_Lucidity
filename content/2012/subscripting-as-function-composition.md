Title: Subscripting as Function Composition
Date: 2012-11-02 05:00
Status: published
Category: mathematics
Tags: analysis, notation
Slug: subscripting-as-function-composition

Dear reader, don't laugh: I had thought I already understood subsequences, but then it turned out that I was mistaken. I should have noticed the vague, unverbalized discomfort I felt about the subscripted-subscript notation, $(a_{n_k})$. But really it shouldn't be confusing at all: as Bernd S. W. Schröder points out in his _Mathematical Analysis: A Concise Introduction_, it's just a function composition. If it helps (it helped me), say that $(a_n)$ is mere _syntactic sugar_ for $a(n): \mathbb{N} \to \mathbb{R}$, a function from the naturals to the reals. And $(a_{n_k})$ is just the composition $a(n(k))$, with $n(k): \mathbb{N} \to \mathbb{N}$ being a strictly increasing function from the naturals to the naturals.
