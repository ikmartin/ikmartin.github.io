+++
title = "Algebraic Curves Lecture 2: Basic Notions"
hascode = true
description = "A discussion of the fundamental notions of algebraic curves: definition of a curve, facts about maps between smooth curves, divisors."
tags = ["algebraic-geometry"]
date = "2024-01-19"
published = true
public = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{ title }}

> {{ description }}

\toc

---

Let $k$ be an algebraically closed field (unless otherwise stated) of characteristic 0. 

\begin{rmk}
    Whenever you have these two hypotheses (algebraically closed and characteristic 0), you don't lose anything by simply taking $\mathbb C$ to be the complex numbers. This is the Lefschetz principle. This isn't *strictly* true, but is a good slogan.
\end{rmk}

\begin{defn}
    A **curve** is a scheme of pure dimension 1 over $k$. This is often called an **abstract curve**. Unless otherwise stated we will always assume that a curve is smooth and connected.
\end{defn}

In particular, our curves will always be irreducible (this follows from the connected hypothesis + Zariski topology weirdness).

### Two alternative ways to view curves

1. The category of curves is equivalent to that of Riemann-surfaces, i.e. complete 1-dimensional $\mathbb C$-manifolds. (Included here is a picture of a genus 2 surface.) I was unfamiliar with the term "complete manifold", so here's a [convenient link](https://en.wikipedia.org/wiki/Geodesic_manifold) to the Wikipedia page.
1. The category of curves is equivalent to the category of finitely generated field extensions of $K$ of transcendence degree 1. This is given simply by associating to a curve its field of rational functions.

The second statement above is equivalent to saying that the field of rational functions of a curve entirely determine the curve's isomorphism class. This in particular fails for higher dimensional varieties; any two birational varieties have isomorphic fields of rational functions. Thus
\begin{cor}
    Any birational morphism $f:X\to Y$ between (smooth) curves is an isomorphism.
\end{cor}
Again, this clearly fails for non-smooth curves. Take the cuspoidal cubic $C = V(x^3 = y^2)$ for instance; it is birationally equivalent to $K = \mathbb A^1$ via $t \mapsto (t^2, t^3)$ (one should projectivize this argument but you get the idea). Alternatively, take a nodal cubic and blow up at the node to resolve it. The blowup map is then an isomorphism away from the singularity.

### Some facts about projective varieties

\begin{thm}
    Let $f:X\to Y$ be a morphism of projective varieties $X$ and $Y$. Then $f$ is closed.
\end{thm}
\begin{cor}
    Any non-constant morphism $f:X\to Y$ between projective curves $X$ and $Y$ if finite and surjective.
\end{cor}

Recall the difference betwen finite and finite type: it's about generation as an algebra vs as a module. A morphism $f:X\to Y$ is *finite type* if it is affine and if over each affine $U\subseteq Y$ $f_*\mathcal O_X(U)$ is a finitely generated *algebra* of $\mathcal O_Y(U)$. The morphism is *finite* if it is affine and if over each affine $U\subseteq Y$ $f_*\mathcal O_X(U)$ is finitely generated *module* of $\mathcal O_Y(U)$.

\begin{defn}
    The **genus** of a curve $X$ is
    \begin{align*}
        g = 1 - \chi(\mathcal O_X) = 1 - h^0(\mathcal O_X) + h^1(\mathcal O_X) = h^1(\mathcal O_X).
    \end{align*}
\end{defn}
The three equalities above represent the equivalence of arithmetic and geometric genus for smooth curves.

### Divisors

A divisor on a curve is a formal linear combination of points on $X$:
\begin{align*}
    D = \sum_{P\in X} D_P\cdot P
\end{align*}
where $D_P \in \mathbb Z$ and only finitely many $D_P \neq 0$.

- The **degree** of a divisor is $\sum_{P\in X} D_P$. 
- A divisor is called **effective** if $D_P\geq 0$ for all $P\in X$.

\begin{rmk}
    Effective divisors correspond uniquely to 0-dimensional subschemes of $X$.
\end{rmk}

If $f:X\to Y$ is a non-constant morphism of curves $X$ and $Y$, then
\begin{align*}
    f^*Y = \sum_{x\in X} \text{val}_{\mathcal O_{X,x}}(\pi)\cdot x \in \operatorname{Div}(X)
\end{align*}
where $\pi$ is a local parameter of $\mathcal O_Y,y$ (also known as the **uniformizer**. Extending this linearly gives us a pullback of divisors on $Y$ to divisors on $X$:
\begin{align*}
    f^*:\operatorname{Div}(Y)\to \operatorname{Div}(X)
\end{align*}

\begin{rmk}
    Analytically, $f$ is given around $x$ as $z\mapsto z^n$. Then $n = \operatorname{val}_{\mathcal O_{X,x}}(\pi).$
\end{rmk}

\begin{prop}
    If $f:X\to Y$ is a non-constant morphism of curves, then
    \begin{align*}
        \deg(f^*D) = \deg(\pi)\cdot \deg(D).
    \end{align*}
\end{prop}

### Principal divisors
Let $f\in K(X)$ [i.e. $f:X\to \mathbb P^1$] then define
\begin{align*}
    \div(f) = f^*(0 - \infty).
\end{align*}
\begin{cor}
    For $f$ above, $\deg(\div(f)) = 0$.
\end{cor}

Any divisor $D = \div(f)$ is called a **principal divisor**. Two divisors $D$ and $E$ are **linearly equivalent** if $D - E$ is principal. In this case, we write $D \sim E$.

**Vague Note:** We call this "linearly equivalence" because the two divisors vary by a linear family, since $\mathbb P^1$ is our prototype of a "line".

To any divisor $D$ we can associate an invertible sheaf, denoted $\mathcal O_X(D)$, defined to be the sheaf of rational functions $f$ such that $D + \div(f)$ is effective. This is invertible
