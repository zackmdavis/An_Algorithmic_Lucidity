## Discontinuous Linear Functions?!

We know what linear functions are. A function _f_ is linear iff it satisfies _additivity_ _f_(_x_ + _y_) = _f_(_x_) + _f_(_y_) and _homogeneity_ _f_(_ax_) = _af_(_x_).

We know what continuity is. A function _f_ is continuous iff for all ε there exists a δ such that if |_x_ − _x_<sub>0</sub>| < δ, then |_f_(_x_) − _f_(_x_<sub>0</sub>)| < ε.

An equivalent way to think about continuity is the sequence criterion: _f_ is continuous iff a sequence (_x_<sub>_k_</sub>) converging to _x_ implies that (_f_(_x_<sub>_k_</sub>)) converges to _f_(_x_). That is to say, if for all ε there exists an _N_ such that if _k_ ≥ _N_, then |_x_<sub>_k_</sub> − _x_| < ε, then for all ε, there also exists an _M_ such that if _k_ ≥ _M_, then |_f_(_x_<sub>_k_</sub>) − _f_(_x_)| < ε.

Sometimes people talk about discontinuous linear functions. You might think: that's crazy. I've seen many linear functions in my time, and they were definitely all continuous. _f_(_x_): ℝ → ℝ := _ax_ is continuous for any _a_ ∈ ℝ. _T_(**x⃗**): ℝ² → ℝ² := $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \boldsymbol{\vec{v}}$ is continuous no matter what the entries in the matrix are. Stop being crazy!!

Actually, it's not crazy. It's just that all the discontinuous linear functions live in infinite-dimensional spaces.

Take, say, the space C<sup>1</sup>(ℝ) of continuously differentiable functions ℝ → ℝ with the uniform norm. (The uniform norm means that the "size" of a function for the purposes of continuity is the least upper bound of its absolute value.) If you think of a vector in the _n_-dimensional ℝ<sup>_n_</sup> as a function from {1...n} to ℝ, then you can see why a function from a continuous (not even countable) domain would be infinite-dimensional.

Consider the sequence of functions (_f_<sub>_k_</sub>) = $(\frac{\sin kx}{k})_{k=1}^{\infty}$ in C<sup>1</sup>(ℝ). The sequence converges to the zero function: for any ε, we can take $k := \lceil \frac{1}{\varepsilon} \rceil$ and then $\frac{\sin kx}{k} \le \frac{1}{\lceil \frac{1}{\varepsilon} \rceil} \le \frac{1}{\frac{1}{\varepsilon}} = \varepsilon$.

Now consider that the sequence of derivatives is $(\frac{k \cos kx}{k})_{k=1}^{\infty} = (\cos kx)_{k=1}^{\infty}$, which doesn't converge. But the function D: C<sup>1</sup>(ℝ) → C<sup>0</sup>(ℝ) that maps a function to its derivative is linear. (We have additivity because the derivative of a sum is the sum of the derivatives, and we have homogeneity because you can "pull out" a constant factor from the derivative.)

By exhibiting a function _D_ and a sequence (_f_<sub>_k_</sub>) for which (_f_<sub>_k_</sub>) converges but (_D_(_f_<sub>_k_</sub>)) doesn't, we have shown that the derivative mapping _D_ is a discontinuous linear function, because the sequence criterion for continuity is not satisfied. If you know the definitions and can work with the definitions, it's not crazy to believe in such a thing!

The infinite-dimensionality is key to grasping the ultimate sanity of what would initially have appeared crazy. One way to think about continuity is that a function not having any "jumps" implies that it can't have an "infinitely steep" slope: a small change in the input can't correspond to an arbitrarily large change in the output.

Consider a linear transformation _T_ on a finite-dimensional vector space; for simplicity of illustration, suppose it's diagonalizable with eigenbasis {**u⃗**<sub>_j_</sub>} and eigenvalues {λ<sub>_j_</sub>}. Then for input **x⃗** = Σ<sub>_j_</sub> _c_<sub>_j_</sub>**u⃗**<sub>_j_</sub>, we have _T_(**x⃗**) = Σ<sub>_j_</sub> _c_<sub>_j_</sub>λ<sub>_j_</sub>**u⃗**<sub>_j_</sub>: the eigencoördinates of the input get multiplied by the eigenvalues, so the amount that the transformation "stretches" the input is bounded by max<sub>_j_</sub> |λ<sub>_j_</sub>|. The linearity buys us the "no arbitrarily large change in the output" property which is continuity.

In infinite dimensions, linearity doesn't buy that. Consider the function _T_(_x_<sub>1</sub>, _x_<sub>2</sub>, _x_<sub>3</sub>, ...) = (_x_<sub>1</sub>, 2<em>x</em><sub>2</sub>, 3<em>x</em><sub>3</sub>, ...) on sequences finitely many nonzero elements, under the uniform norm. The effect of the transformation on any given dimension is linear and bounded, but there's always another dimension that's getting stretched more. A small change in the input can result in an arbitrarily large change in the output, by making the change sufficiently far in the sequence (where the input is getting stretched more and more).
