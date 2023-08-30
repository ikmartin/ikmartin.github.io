+++
title = "Notes Following Early Chapters of Fulton's Intersection Theory"
hascode = true
description = "Thoughts following the early chapters of Fulton's Intersection Theory"
tags = ["algebraic-geometry"]
date = "2023-08-30"
+++

@def mintoclevel=2
@def maxtoclevel=3

# Notes following the early chapters of Fulton's *Intersection Theory*

\toc

---

I'm reading some of the early chapters of Fulton's *Intersection Theory*.

## Chapter 1: Rational Equivalence

This first chapter introduces some of the most basic concepts of intersection theory, cycles and rational equivalence. The primary result proves that rational equivalence pushes forward under proper morphisms of schemes.

### Notation and Conventions

Here Fulton establishes his conventions. Schemes are all algebraic schemes over a field, varieties are integral schemes, subvarieties of schemes are always closed subschemes which are varieties and a *point* on a scheme is always a closed point. He does include a single example in this section, and I'd like to go over it in more detail.

#### Example 1.1 
This example introduces the notion of *intersection number*, at least for plane curves. Let $f, g\in K[x,y]$ be polynomials defining affine plane curves $F$ and $G$ respectively, and define $Z = Z(f,g)\subseteq \mathbb A^2_K$ to be the *intersection subscheme* of $F$ and $G$. We then define the **intersection multiplicity** of $F$ and $G$ at a point $P \in \mathbb A^2_K$ to be
\begin{equation*}
    i(P,F\cdot G) = \operatorname{dim}_K\mathcal O_{P,Z} = \operatorname{dim}_K \frac{\mathcal O_{P,\mathbb A^2_K}}{(f,g)}.
\end{equation*}
My commutative algebra is currently rusty, so I found it useful to examine some examples.

**Example (a):** &nbsp; Denote by $P = (a,b)$ an arbitrary closed point in $\mathbb A^2_K$ and consider $f(x,y) = x$ and $g(x,y) = y$. The maximal ideal corresponding to $P$ is then given by $(x-a, y-b)$ and so $\mathcal O_{P,\mathbb A^2_K} = K[x,y]_{(x - a, ~y - b)}$. If either $a$ or $b$ is nonzero, then one of $f$ and $g$ is invertible in $\mathcal O_{P,\mathbb A^2_K}$ and hence
\begin{equation*}
    \operatorname{dim}_K \frac{\mathcal O_{P,\mathbb A^2_K}}{(f,g)} = \operatorname{dim}_K \{0\} = 0.
\end{equation*}
If $(a,b) = (0,0)$ however, then
\begin{equation*}
    \operatorname{dim}_K \frac{\mathcal O_{P,\mathbb A^2_K}}{(f,g)} = \operatorname{dim}_K K = 1,
\end{equation*}
giving us an intersection multiplicity of $1$ at $(0,0)$ and $0$ otherwise. This aligns with our expectations from the graph of $f\cdot g$.

**Example (b):** &nbsp; Again set $P = (a,b)$ but let $f(x,y) = x^2 - y$ and $g(x,y) = y - b$ for some $b\in K$. Following a similar calculation from before, we get that $\mathfrak m_P = (x - a, y - b)$ contains a unit in $\mathcal O_{P,\mathbb A^2}$ whenever $P$ is not in $Z(f\cdot g)$. We thus have three cases to consider:

- *Case (i):* &nbsp; Suppose $b < 0$. Then $Z(f\cdot g) = \emptyset$, so $I(P,F\cdot G) = 0$ for all $P\in \mathbb A^2$.
- *Case (ii):* &nbsp; Suppose $b > 0$. Then $Z(f\cdot g) = \{(-\sqrt{b},b), (\sqrt{b},b)\}$, and for $P\in Z(f\cdot g)$ we get 
\begin{equation*}
    I(P,F\cdot G) = \dim_K \mathcal O_{P,\mathbb A^2}/\mathfrak m_{P} = \dim_K K = 1.
\end{equation*}
- *Case (iii):* &nbsp; Suppose $b = 0$. This is our first instance of degeneracy: $Z(f\cdot g) = \{(0,0)\}$. Set
\begin{equation*}
    R = \mathcal O_{P,\mathbb A^2}/\mathfrak m_{P} = K[x,y]_{(x,y)}/(x^2 - y, y).
\end{equation*}
Because $y = 0$ in $R$, $R \cong K[x]_{(x)}/x^2$ via the map $y \mapsto 0$. This is a two dimensional vector space over $K$ with basis $1, x$, hence
\begin{equation*}
    I((0,0), F\cdot G) = 2.
\end{equation*}
This demonstrates that $I(P,F\cdot G)$ *is* able to account for some degeneracy.




















