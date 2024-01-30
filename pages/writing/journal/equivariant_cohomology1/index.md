+++
title = "Some notes on Equivariant Cohomology"
hascode = true
description = "Me taking notes on some stuff I'm learning about equivariant cohomology and localization"
tags = ["blog"]
date = "2024-01-24"
published = true
public = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{ title }}

> {{ description }}

\toc

---

## References

- *Introduction to Equivariant Cohomology in Algebraic Geometry* notes by David Anderson
- Chapter 7 and 8 of *An Invitation to Enumerative Geometry* by Andrea T. Ricolfi
- *Introduction to actions of algebraic groups* notes by Michel Brion

## Primer on principal $G$-bundles, $\mathbb EG$ and $\mathbb BG$

Our goal is to understand equivariant cohomology and localization in the category of algebraic varieties over $\mathbb C$, but it's informative to first work in a more flexible category. We'll therefore first discuss principal $G$-bundles over topological spaces.

### Principal $G$-bundles

Let $G$ be a topological group. The category of $G$-spaces has objects given by pairs $(X,\sigma)$ where $X$ is a topological space with a left or right $G$ action $\sigma:G\times X\to X$ (continuous, of course). Morphisms in this category are $G$-equivariant continuous maps $\varphi: X\to Y$ which commute with the $G$-action of $X$ and $Y$. We require homotopies in this category to be equivariant as well with $G$ acting trivially on $[0,1]$.

\begin{defn}
    Let $p:E\to S$ be a fiber bundle in the category of $G$-spaces where $E$ has a right $G$-action and $S$ has a trivial $G$-action[^1]. We say $(E,p)$ is a principal $G$-bundle over $S$ if $p$ is $G$-equivariantly locally trivial; if $S$ has a local trivialization $\{S_i\}$ with $G$-equivariant homeomorphisms $p^{-1}(S_i)\xrightarrow{\sim}S\times G$ where $(s,h)\cdot g := (s,hg)$.

    [^1]: This means $p$ is automatically equivariant
\end{defn}

\begin{rmk}
    Since the action of $G$ on $S\times G$ is free and $E$ is locally isomorphic to $S\times G$, the action of $G$ on $E$ is necessarily also free when $(E,p)$ is a principal $G$-bundle. Furthermore there exists a canonical homeomorphism
    \begin{align*}
        E/G\xrightarrow{\sim} S.
    \end{align*}
    This consequently implies that every fiber of $p$ is isomorphic to $G$.
\end{rmk}

A map between principal $G$-bundles $p:E\to X$ and $q:F\to S$ is a continuous equivariant map $\varphi:E\to F$ which commutes with projection to the base space.
\begin{rmk}
    Every morphism $\varphi:(E,p)\to (F,q)$ of principal $G$-bundles over a space $S$ is an isomorphism. Thus the category of principal $G$-bundles over $S$ is a groupoid.
\end{rmk}

### The functor $\mathrm{Bun}_G$

Suppose we have a continuous map $\alpha:S'\to S$ and a principal $G$-bundle $(E,p)$. Pullback via $\alpha^*$ gives us a principal $G$-bundle over $S'$,
\begin{align*}
    \alpha^*E = \{(e,s')\in E\times S' ~\mid~ \alpha(s') = p(e)\},
\end{align*}
and it comes equipped with an equivariant map $\alpha^*E\to E$ given by projection onto the first coordiante. This means we can define a functor
\begin{align*}
    \mathrm{Bun}_G:\mathsf{Top}^{op} \to \mathsf{Set}
\end{align*}
given by sending a space $S$ to the set of isomorphism classes of principal $G$-bundles over $S$. It's contravariant because we send the isomorphism class of a bundle $E$ to $\alpha^*E,$ reversing the direction of the arrows.

However, pullbacks of homotopic maps are isomorphic:
\begin{prop}
    If $\alpha,\beta:S'\to S$ are homotopy equivalent, then $\alpha^*E\cong \beta^*E$.
\end{prop}
...which means we can upgrade $\mathrm{Bun}_G$ by only defining it up to homotopy: 
\begin{align*}
    \mathrm{Bun}_G:\mathsf{HTop}^{op} \to \mathsf{Set}.
\end{align*}

This functor is represented by a topological space $\mathbb BG$: $\mathrm{Bun}_G(-) = \Hom(-,\mathbb BG)$. In other words, specifying a principal $G$-bundle $p:E\to S$ up to isomorphism is equivalent to specifying a continuous map $S\to \mathbb BG$.

### Construction of $\mathbb BG$
Fill in later

## Equivariant Cohomology

### The Borel Construction

Let $G$ be a complex linear algebraic group ("complex" here meaning that it is a complex algebraic variety) and let $X$ be a complex algebraic group with a left $G$-action. Define
\begin{align*}
    \mathbb EG \times^G X:= (\mathbb EG\times X)/(e\cdot g, x)\sim (e,g\cdot x).
\end{align*}
We then define the **equivariant cohomology** of $X$ to be
\begin{align*}
    H^i_G(X) := H^i(\mathbb EG\times^G X),
\end{align*}
where the right term is singular cohomology. The point of using $\mathbb EG \times^G X$ instead of the orbit space $X/G$ is that $\mathbb EG \times X$ is homotopy equivalent to $X$ since $\mathbb EG$ is contractible but the $G$ action on $\mathbb EG\times X$ is free. Essentially this "fixes" the action of $G$ on $X$ by making it free without changing the homotopy type. In particular, if the $G$-action on $X$ was already free, then $H^i_G(X)$ is just the singular cohomology $H^i(X/G)$.

### Equivariant cohomology of a point

In the special case that $X = \{pt\}$, then $\mathbb EG \times^G X = \mathbb EG/G = \mathbb BG$, and so
\begin{align*}
    H^i_G(\mathsf{pt}) = H^i(\mathbb BG).
\end{align*}
There are two things to note:
1. Very often $\mathbb BG$ has nontrivial topology, so $H^*_G(\mathsf{pt}) \neq \mathbb Z$ in most cases. This is a key feature of equivariant cohomology.
1. The ring $H^*_G(\mathsf{pt}) = H^*(\mathbb BG)$ is typically interpreted as the ring of characteristic classes for principal $G$-bundles.

### Examples with explanations

\begin{example}
    Let $G = \mathbb C^*$. In this case $\mathbb EG = \mathbb C^\infty\setminus \{0\}$ and so $\mathbb BG = \mathbb EG/G = \mathbb P^\infty$. Recall that
    \begin{align*}
        H^i(\mathbb P^\infty_{\mathbb C}) =
        \begin{cases}
            0 & \text{$i$ is odd} \\
            \mathbb Z & \text{$i$This has cohomology of $\mathbb Z$ in each even degree and trivial cohomology in every odd degree. As a ring, it is generated by the  is even}
        \end{cases}
    \end{align*}
    and that the ring $H^*(\mathbb P^\infty_{\mathbb C})$ is generated in degree 2. We then see that
    \begin{align*}
        \mathbb ^*_{\mathbb C^*}(\mathsf{pt}) = H^*\mathbb P^\infty_{\mathbb C} \cong \mathbb Z[t]
    \end{align*}
    where $t = c_1(\mathcal O_{\mathbb P^\infty}(-1)$ is the first Chern class of the tautological bundle.
\end{example}
