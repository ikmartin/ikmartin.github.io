+++
title = "Algebraic Curves Lecture 1"
hascode = true
description = "The first day of Algebraic Curves taught by Karl Christ. We briefly discussed the course structure and Karl gave a brief overview of the type of math we can expect to see."
tags = ["algebraic-geometry", "algebraic-curves"]
date = "2024-01-17"
published = true
public = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{title}}

> {{description}}

\toc

---

## Organizational Matters
Instructor: Karl Christ

References:
- Harshorne Chapter IV
- Arbasello, Corualla, Griffiths, Harris: *Geometry of Algebraic Curves*, Vol I (maybe Vol II also)
- Eisenbud and Harris: *The practice of algebraic curves* (Draft)

Grade: 
There is no regular homework. There is a final exam, which is an oral exam. You can get extra credit by handing in up to 2 papers about 5-10 pages each. Topic can be anything from the class.

Office Hours: 15:30 - 17:00 on Monday. Can also talk after class on Wednesday at department coffee.

## Overview of Algebraic Curves

The most natural (first) way to study algebraic curves is by interpreting them as the zero sets of polynomials. These are **embedded** algebraic curves. These have been studied almost since the inception of mathematics, the Ancient Greeks studied them for instance. We will typically interpret embedded algebraic curves as subsets of $\mathbb P^r$ or more concretely in $\mathbb P^r_{\mathbb C}$.

We will also study **abstract curves** i.e. **one-dimensional schemes** i.e. **compact 1-dimensional complex manifolds** (Riemann surfaces).

The main theme of this course will be the study of an algebraic curve $C$ together with a map $C\to \mathbb P^r_{\mathbb C}$. This allows us to study both abstract and embedded curves simultaneously.

Perhaps the first thing to not is that this adds nothing new to the theory.

\begin{rmk}
    Every abstract smooth curve over $\mathbb C$ can be embedded in $\mathbb P^3$.
\end{rmk}

Note that this fails for singular curves; the dimension of the Zariski tangent space can be arbitrarily large at a singularity and any embedding of a curve must map to a space whose dimension is at least as large as this dimension. You can find singularities whose Zariski tangent space is of arbitrarily large dimension.

The map $\varphi:C\to \mathbb P^r$ is given by a line bundle $L$ on $C$ and a vector subspace $V$ of $H^0(C,L)$ of dimension $r+d$, where $d$ is the **degree of $\varphi$.**

### Genus

We thus far have two invariants: $r$ the dimension of the ambient projective space $\mathbb P^r$ and $d$ the degree of the embedding $\varphi:C\to \mathbb P^r$. The third primary invariant we consider is the **genus** $g$ of $C\to \mathbb P^r$. A natural question is this: given $d$ and $r$, what are the possible values of $g$?

\begin{defn}
    Let $X$ be a curve. 
- The **arithmetic genus** of $X$ is $p_a(X) = 1 - P_X(0)$ where $P_X$ is the Hilbert polynomial of $X$.
- The **geometric genus** of $X$ is $p_g(X) = \dim_k\Gamma(X,\omega_X)$ where $\omega_X$ is the canonical sheaf $\omega_X = \bigwedge_{i=1}^n \Omega_X$.

These two notions agree for curves and are equal to $H^1(X,\mathcal O_X)$ by Serre duality. We therefore simply refer to the **genus** of $X$ and denote it $g = H^1(X,\mathcal O_X)$.
\end{defn}

**For $r = 2$** we have the degree-genus formula: $g = \frac{(d-1)(d-2)}{2}$.

**For $r = 3$** it is no longer true that $g$ depends solely on $d$.
- Castelnnovo's bound gives an upper bound to $g$
- A classification was given by Hartshorne.

**For any $r$** there is a generalization of Castelnnovo's bound, but giving the possible values is an open problem.

### Rank

Let's instead ask a different question: given fixed $g$ and $d$, what are the possible values of $r$?

**Riemann-Roch**: $r(L) - r(K_C - L) = d - g + 1$, which implies $r(L) \geq \max \{-1, d - g + 1\}$. **This gives a lower bound on $r(L)$.**

**Clifford Theorem**: $r(L) \leq \frac{d}{2}$ if $0 \leq d \leq 2g - 2$. This gives an upper bound on $r(L)$.

When $d \geq 2g - g$, the lower bound and upper bound of $r$ coincide, and then $d$ fully determines $g$. For $0\leq d\leq 2g - 2$ however, the upper and lower bounds for $r$ do not coincide giving a "special region of line bundles". This region is exactly what the Brill Noether theorem describes.

\begin{thm}
    *(Brill Noether Theorem).* If $C$ is a general curve of genus $g$ then there exists a line bundle $g^d_r$ on $C$ if and only if
    \begin{align*}
        \rho(g,r,d) = g - (r + 1)(g - d + r) \geq 0.
    \end{align*}
\end{thm}

There's an even stronger theorem:

\begin{thm}
    The locus of a line bundle $g^r_d$ in $Pic(X)$ has dimension $\rho$ and is smooth and irreducible.
\end{thm}
