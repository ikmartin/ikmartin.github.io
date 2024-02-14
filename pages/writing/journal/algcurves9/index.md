+++
title = "Algebraic Curves Lecture 9:"
hascode = true
description = "The 9th lecture of Algebraic Curves by Karl Christ"
tags = ["blog"]
date = "2024-02-09"
published = true
public = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{ title }}

> {{ description }}

\toc

---

## Coverings

Let $f:Y\to X$ be a map of curves, $p\in Y$, $q = f(p)$. 

The **ramification index** at $p$ is $v_p(t)$.

If $v_p(t) = 1$ we say that $f$ is **unramified** at $p$. Otherwise $p$ is a **ramification point** of $f$, in which case we say that $q$ is a **branch point**.

The **ramification divisor** of $f$ is
\begin{align*}
    R = \sum_{p\in Y} (v_p(t) - 1)\cdot p.
\end{align*}
Implicit in this definition is the fact that $f$ has finitely many ramification points. Our first theorem is the Riemann-Hurwitz formula.

\begin{thm}
    In this situation in characteristic $0$,
    \begin{align*}
        K_Y = f^*K_X + R
    \end{align*}
    and in particular
    \begin{align*}
        2g(Y) - 2 = d(2g(X) - 2) + \sum_{p\in Y}(v_p(t) - 1)
    \end{align*}
    where $d = \deg(t)$.
\end{thm}
\break
\begin{rmk}
    We say that $f$ is separable if the induced field extension $K[Y]/K[X]$ is separable. In positive characteristic
1. If $f$ is not separable then it is ramified along all of $Y$
2. Even if it is separable the formula might fail if the ramification is not tame (meaning the ramification index is divisible by the characteristic of the base field).
\end{rmk}
\break
\begin{proof}
    *(Sketch of an analytic proof.)* &nbsp; Let $\omega$ be a meromorphic 1-form on $X$ the target curve. Pulling it back by $f$ gives us a 1-form on $Y$. Away from branch points, $f$ is a local isomorphism (here we have a drawing of a stack of analytic disks in $Y$ over an analytic disk around the point $q$ in $X$) and thus any zero or pole of $\omega$ is given $d$ zeros or $d$ poles on $Y$.

    At a ramification point $p$, $f$ is given analytic locally be $z\mapsto z^{v_p(t)}$. On the other hand, $\omega$ is locally given by $dt = dz^{v_p(t)} = (v_p(t))z^{v_p(t)-1}dz$ on $Y$.
\end{proof}
We can see where this fails when the ramification is not tame; if the characteristic of the base field divides $v_p(t)$ then $\omega$ vanishes on $Y$.

\begin{cor}
    There is no nontrivial étale cover $Y\to \mathbb P^1$.
\end{cor}
\break
\begin{proof}
    Recall that étale = flat + unramified. Any finite surjective map of nonsingular varieties is flat, but a cover $f:Y\to \mathbb P^1$ will always fail to be unramified. Indeed, suppose $f$ is étale. Riemann-Hurwitz says that
    \begin{align*}
        2g(Y) - 2 = -2\cdot d + \deg(R) = -2d
    \end{align*}
    which implies $g(Y) = 0, d = 1$. The important part is that $\deg(f) = d=1$, hence $f$ is an isomorphism on function fields. hence $f$ is an isomorphism. The only étale map is therefore trivial.
\end{proof}
\break
\begin{cor}
    If $f:Y\to X$ is a cover then $g(Y) \geq g(X)$.
\end{cor}
\begin{proof}
    
If $g(X) = 0$ then there is nothing to show. Otherwise, we get by Riemann-Hurwitz that
    \begin{align*}
        &2g(Y) - 2 = d\cdot (2g(X) - 2) + \deg(R) \\
        &\implies g(Y) = d(g(X) - 1) + \frac{\deg(R)}{2} + 1 \\
        &\implies g(Y) = g(X) + (d-1)(g(X) - 1) + \frac{\deg(R)}{2}.
    \end{align*}
If $g(X) > 0$ then $(d-1)(g(X) - 1)\geq 0$ and $\frac{\deg(R)}{2}\geq 0$ so the claim follows.
\end{proof}

\begin{cor}
    $\deg(R)$ is even.
\end{cor}
\begin{cor}
    If $g\geq 2$ and $g(X) = g(Y) = g$ then any cover $f:Y\to X$ is an isomorphism.
\end{cor}
\begin{proof}
    $2g - 2 = d\cdot (2g - 2) + \deg(R)$ which implies $d = 1$ and hence $f$ is an isomorphism.
\end{proof}

@@revindentblock
    *Example:* Take $f:\mathbb P^1\xrightarrow{2:1} \mathbb P^1$. Then
    \begin{align*}
        -2 = 2\cdot (-2) + \deg(R) \implies \deg(R) = 2
    \end{align*}
    and so $f$ is ramified at two points with ramification index $2$: $[x:y] \mapsto [x^2:y^2]$.
@@

\begin{cor}
    *(Hurwitz bound).* &nbsp; Suppose $X$ has genus $\geq 2$ and finitely many automorphisms. Then $|\Aut(X)| \leq 84(g - 1)$.
\end{cor}
\break
\begin{rmk}
1. This bound is sharp in the sense that it is achieved for infinitely many $g$, but not all of them. For example, up to $g = 6$ it is achieved only in $g = 3$ by the Klein quartic:
\begin{align*}
    \{x^3y + y^3z + z^3 x = 0\} \subseteq \mathbb P^2
\end{align*}
2. The upshot is that if you fix $g$, there is a bound on the automorphisms of ALL curves of that genus. A priori, it might be the case that for fixed genus $g$ you could find curves of that genus whose automorphism group has arbitrarily large size.
3. The Hurwitz bound fails in positive characteristic.
\end{rmk}
\begin{proof}
    You can check that $X/\Aut(X) = Y$ is again a curve. So you get a covering $X\to Y$ of degree $\Aut(X)|$. Ramification points of this cover are the points with non-trivial stabilizers.

    Denote by $r_{i,j}$ the ramification points lying over a branch point $p_i$ for $1\leq i\leq b$. (A picture of a line representing the base curve $Y$ with a tick for point $p_i$ lying in $Y$. Above $p_i$ is a loopy curved line representing $X$ so that each point $r_{i,j}$ is a ramification point. Each $r_{i,1}, r_{i,2}, r_{i,3}$ is a place where the fiber is "tangent to the curve $X$")

    Over $p_i$ all points in the fiber $f^{-1}(p_i)$ have the same ramification index $f_i$. If $r_i = |f^{-1}(p_i)|$ then $f_i\cdot r_i = |\Aut(X)|$. Then Riemann-Hurwitz says
    \begin{align*}
        2g(X) - 2 &= |\Aut(X)| \cdot (2g(Y) - 2) + \sum_{i}r_i\cdot (f_i - 1) \\
        &= |\Aut(X)| \cdot (2g(Y) - 2) + \sum_{r_{i,j}}(f_i - 1)
    \end{align*}
\end{proof}
