+++
title = "Algebraic Curves Lecture 3: Line bundles and linear series"
hascode = true
description = "The third class of algebraic curves. We discussed line bundles and linear series on smooth curves. We stated the fact that linear series classify maps from the curve to projective space."
tags = ["algebraic-curves,", "algebraic-geometry"]
date = "2024-01-22"
published = true
public = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{ title }}

> {{ description }}

\toc

---

$X$ is still a smooth curve over an algebraically closed field $K$.

## Brief Follow-up from Previous Class

We discussed "finite type" vs "finite" last class. A map $f:x\to Y$ is

**quasi finite** if it has finitely many points in each fiber

**finite** if there exists an affine cover $U_\alpha$ of $Y$ such that for
\begin{align*}
    f|_{f^{-1}(U_\alpha)}: f^{-1}(U_\alpha) \to U_\alpha
\end{align*}
the corresponding inclusion $A\rightarrow B$ realizes $B$ as a finitely generated $A$-module; where $U_\alpha = \Spec A$ and $f^{-1}(U_\alpha) = \Spec B$.

\begin{thm}
    A map as above is finite if and only if it is quasi-finite and proper.
\end{thm}

\begin{example}
    Take the inclusion $\mathbb A^1 \setminus \{0\} \to \mathbb A^1$. It is not finite type because $K[x,x^{-1}]$ is not finitely generated as a module over $K[x]$.
\end{example}

## Line bundles and linear series

We ended last class by defining the sheaf $\mathcal O_X(D)$ to be the sheaf of rational functions $f$ of $X$ such that $\div (f) + D$ is effective.

\begin{example}
    $\mathcal O_{\mathbb P^1}(2P - 3Q)$ is the sheaf of regular functions which have a zero of order 3 or greater at $Q$, a pole of order at most $2$ at $P$ and no poles anywhere else on $\mathbb P^1$.
\end{example}

We have the following facts immediately.
1. $\mathcal O_X(D) \cong \mathcal O_X(D') \iff D\sim D'$
1. Conversely, any invertible sheaf $L$ is of the form $\mathcal O_X(D)$ for some divisor $D$

We call $L$  **effective** if there exists $D$ effective such that $L\cong \mathcal O_X(D)$ which happens if and only if $h^0(X,L) > 0$. Note that there are effective sheaves which are not invertible in general.

### Linear series
The **degree** of a line bundle $L\cong \mathcal O_X(D)$ is the degree of $D$. Furthermore, $\mathcal O_X(D + D') = \mathcal O_X(D)\otimes \mathcal O_X(D')$. We can now define linear series, objects which classify maps $X\to \mathbb P^r$.

\begin{defn}
    A linear series is a subspace $V$ of $H^0(X,L)$. 
- It has degree equal to the degree of $L$. 
- It has rank equal to $\dim(V) - 1$. 
- The linear series is called **complete** if $V = H^0(X,L).$
- A **base point** of a linear series $(L,V)$ is a point $P$ such that $\dim(V) = \dim(V(-P))$. 
A linear series of degree $d$ and rank $r$ is called a $g^r_d$.
\end{defn}
Why do we care about linear series? It turns out they classify maps to $\mathbb P^r$.

Given a $g^r_d$ $(L,V)$ that is base point free, we obtain a map $\varphi_V:X\to \mathbb P^r$ given by
\begin{align*}
    P\mapsto \{s ~\mid~ s(P) = 0\} \in \mathbb PV^* \cong \mathbb P^r.
\end{align*}
Note that $V^*$ is the dual space here. This is the coordinate free version, but if we choose a basis $s_0,...,s_r$ of $V$ (remember that $V$ is $r+1$ dimensional) then we can write this map more concretely as
\begin{align*}
    P\mapsto [s_0(P): ... : s_r(P)].
\end{align*}

A question was asked: why does $\{s\in V ~\mid~ s(P) = 0\}$ specify an element in the dual space of $V$? It's because the condition $s(P) = 0$ specifies a hyperplane in $V$, a subspace of codimension 1, and hence is given by an element of the dual space.

In the situtation $\varphi_V:V\to \mathbb P^r$ above, we have $L\cong \varphi_V^*\mathcal O_{\mathcal P^r}(1)$; in other words, we can recover $L$ from the map $\varphi_V$. To summarize:

\begin{prop}
    There is a bijective correspondence between maps $f:X\to \mathbb P^r$ up to the action of $\operatorname{PGL}_{r + 1}$ with non-degenerate image and a base-point free linear series.
\end{prop}
**Notes:** By non-degenerate we just mean that the image of $f$ above isn't contained in any linear subspace of $\mathbb P^r$. This isn't the case with the map $\varphi_V$ we defined above -- if it were, then $s_0(P), ...,s_r(P)$ would have a nontrivial linear relation, which isn't the case since they were chosen to be a basis. If $f:X\to \mathbb P^r$ *did* have image lying in some linear subspace, then we'd simply decrease the value of $r$.

\begin{rmk}
    If $D\in \operatorname{Div}(X)$ is the base locus of $V$, then the map $\varphi_V$ is defined to be the map induced by $V(-D)$.
\end{rmk}
\begin{rmk}
    If the $g^r_d$ $(V,L)$ has degree $d$ then
    \begin{align*}
        d = \deg(\varphi_V) \cdot \deg(\varphi_V(X)) + \deg(D).
    \end{align*}
\end{rmk}

### Ampleness

$L$ is called **very ample** if $\varphi_L$ is an embedding. $L$ is called **ample** if $L^{\otimes n}$ is very ample for some $n > 0$.

\begin{prop}
    $L$ is very ample if and only if it is effective and
1. $h^0(X,L(-P)) = h^0(X,L) - 1$ for all $P\in X$
1. $h^0(X,L(-P - Q)) = h^0(X.L) - 2$ for all $P,Q\in X$.
\end{prop}

The example we'll discuss next time to have in mind is the following:
\begin{example}
    $\mathbb P^1 \to \mathbb P^3$, $(s,t) \mapsto (s^3 : st^2: t^3)$.
\end{example}








