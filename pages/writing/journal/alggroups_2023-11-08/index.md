+++
title = "Some notes on actions of algebraic groups"
hascode = true
description = "This is me taking notes on the notes by Brion on the actions of algebraic groups"
tags = ["algebraic-geometry,", "group-actions"]
date = "2023-11-08"
published = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# Some notes on actions of algebraic groups
> I'm trying to understand the localization formula for equivariant Chow groups. This requires a working knowledge of algebraic groups and especially of linear algebraic groups, so I'm reading the notes "Introduction to actions of algebraic groups" by Michel Brion to get up to speed. Not coincidentally this is the same author of the paper "Equivariant Chow groups and torus actions".

\toc

## Algebraic Groups

All algebraic varieties are varieties over $\mathbb C$, and they have the Zariski topology instead of the complex topology. The algebra of regular functions on a variety is denoted by $\mathcal O_X(X)$. We start with a definition and then some examples.

@@revindentblock
\thmtitle{Definition}{(Algebraic Group).} An **algebraic group** is a variety $G$ equipped with the structure of a group such that the multiplication map
\begin{equation}
    \mu:G\times G\to G, ~ (g,h)\mapsto gh
\end{equation}
and the inverse map
\begin{align}
    \iota: G\to G, ~ g\mapsto g^{-1}
\end{align}
are morphisms of varieties. 

The **neutral component** of an algebraic group $G$ is the connected component $G^0\subseteq G$ containing the identity element (called the "neutral element" by Brion). This is also called the **identity component**.
@@

Basically all the algebraic groups I'm interested in are linear algebraic groups; subsets of $\GL_n$.

@@revindentblock 
\thmtitle{Example}{} Here are several examples of algebraic groups.

1. All finite groups are algebraic groups.
1. The **general linear group** $\GL_n$ is the subset of all $n\times n$ matrices, which as a variety is $\mathbb C^{n^2}$. It is the inverse image of the determinant map $\det:\mathbb C^{n^2} \to \mathbb C$ away from $0$; hence it is an open set and is an affine variety. Matrix multiplication is a polynomial in the coefficients of the matrices, and is hence a regular map. Likewise, inversion $A\mapsto A^{-1}$ is a polynomial in the coefficients of of $A$ and $1/\det(A)$. Thus $\GL_n$ is an algebraic group.
1. Any Zariski-closed subgroup of $\GL_n$ is also an algebraic group, for instance, $\SL_n$. We call such groups **linear algebraic groups**.
1. The **multiplicative group** $\mathbb C^*$ is an affine algebraic group. It is a linear algebraic group since $\mathbb C^* \cong \GL_1$.
1. The **algebraic torus** $T_n = (\mathbb C^*)^n$ is the diagonal subgroup of $\mathbb GL_n$ and is hence a linear algebraic group.
1. Every smooth curve of degree $3$ in $\mathbb P^2$ is an algebraic group; these are **elliptic curves**. People supposedly have studied these before.
@@

The following lemma should be reminiscent of a basic fact about Lie groups.

@@revindentparagraph
\thmtitle{Lemma}{} *Any algebraic group $G$ is a smooth variety and its (connected or irreducible) components are the cosets $gG^0$ where $g\in G$. Moreover, $G^0$ is a closed normal subgroup of $G$ and the quotient group $G/G^0$ is finite.*
@@

\\

@@lineblock
    *Proof.* &nbsp; The variety $G$ is smooth at some point $g$, and hence also at the point $gh$ for any $h\in G$ since multiplication is a morphism. This implies $G$ is smooth everywhere.

Every variety has only finitely many connected components. Since $G$ is a disjoint union of distinct cosets $gG^0$ and each of these is connected, they form the connected components. The inverse $\iota(G^0)$ is a connected component since $\iota$ is an isomorphism of varieties, and because $e_G$ is in both $G^0$ and $\iota(G^0)$ it must be that $\iota(G^0) = G^0$. For any $g\in G^0$ we then know that $g^{-1} \in G^0$, and hence both $gG^0$ and $G^0$ contain $e_G$. This means $gG^0 = G^0$ and hence $G^0$ is a closed subgroup of $G$. Likewise, $gG^0g^{-1} = G^0$ so $G^0$ is normal.

The group $G/G^0$ is equal to the number of cosets of $gG^0$, and we have already argued that there are finitely many of these.
@@

### Actions on Varieties

A **$G$-variety** is a variety $X$ equipped with an action of the algebraic group $G$
\begin{align*}
    \alpha:G\times X\to X, ~ (g,x) \mapsto g\cdot x
\end{align*}
which is also a morphism of varieties. We then say that $\alpha$ is the *algebraic $G$-action*, so this is all exactly as you might expect.

For each $g$ we have a morphism $\varphi_g:X\to X$ given by $\varphi_g(x) = gx$. This gives us a corresponding $G$-action on regular functions $f\in \mathcal O_X(X)$ defined $g\cdot f =  f\circ \varphi_{g^{-1}}$. Composing with $\varphi_{g^{-1}}$ ensures that this is a left group action, since then $h\cdot g f = f\circ \varphi_{g^{-1}}\circ \varphi_{h^{-1}}$. From this we get the following Lemma:

@@revindentblock
*With the preceeding notation, the complex vector space $\mathcal O_X(X)$ is a union of finite-dimensional $G$-stable subspaces on which $G$ acts algebraically.*
@@

\\

@@lineblock
*Proof.* &nbsp; The action morphism $\alpha:G\to X$ induces an algebra homomorphism between rings of regular functions on $X$ and $G\times X$:
\begin{align*}
    \alpha^\#: \mathcal O_X(X) \to \mathcal O_{G\times X}(G\times X), ~ f\mapsto \big( (g,x) \mapsto f(g^{-1}\cdot x)\big).
\end{align*}
Since $\mathcal O_{G\times X}(G\times X)\cong \mathcal O_G(G)\otimes_{\mathbb C}\mathcal O_{X}(X)$, we can write
\begin{align*}
    f(g^{-1}\cdot x) = \sum_{i=1}^n \varphi_i(g^{-1})\cdot \psi_i(x),
\end{align*}
where each $\varphi_i \in \mathcal O_G(G)$ and each $\psi_i \in \mathcal O_X(X)$. Then
\begin{align*}
    g\cdot f = \sum_{i=1}^n \varphi_i(g^{-1})\psi_i.
\end{align*}
Varying $g$ changes the $\varphi_i(g^{-1})$ coefficients and nothing else, so the translates $g\cdot f$ of $f$ span a finite-dimensional subspace $V\subseteq \mathcal O_G(G)$. This subspace $V$ is $G$-stable since it is closed under the action of $G$ (is this what $G$-stable means???). Moreover, the functions $h\mapsto \varphi_i(g^{-1}h^{-1})$ are all regular functions and $h\cdot (g\cdot f) = \sum_{i=1}^n \varphi_i(g^{-1}h^{-1})\psi_i$, so the $G$-action on $V$ is algebraic.
@@

This result motivates the following definition, which is what led me to these notes in the first place.

A **rational $G$-module** is a complex vector space $V$ (possibly infinite dimensional) equipped with a linear action of $G$ such that every $v\in V$ is contained in a finite-dimensional $G$-stable subspace on which $G$ acts algebraically.
