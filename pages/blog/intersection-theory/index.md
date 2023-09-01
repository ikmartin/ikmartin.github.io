+++
title = "Notes Following Early Chapters of Fulton's Intersection Theory"
hascode = true
description = "Thoughts following the early chapters of Fulton's Intersection Theory"
tags = ["algebraic-geometry"]
date = "2023-08-30"
+++

@def mintoclevel=2
@def maxtoclevel=3

# The early chapters of Fulton's *Intersection Theory*: \\Thoughts from

\toc

---

I'm reading some early chapters of Fulton's *Intersection Theory*.

## Notation and Terms

- $\mathcal O_{V,X}$: when $V$ is a subvariety of $X$, this is the stalk of the structure sheaf $\mathcal O_X$ of $X$ at the generic point of $V$.
- $R(V)$: the function field of a variety $V$. When $V$ is a subvariety of $X$, $R(V) = \mathcal O_{V,X}/\mathfrak m_{V,X}$. **Note:** the local ring $\mathcal O_{X,V}$ consists of all rational functions on $X$ whose denominators don't vanish on $V$ and quotienting by $\mathfrak m_{V,X}$ eliminates all rational functions which vanish on $V$, hence $R(V)^\times$ is precisely all rational functions of $X$ which are neither all zero or all infinite on $V$.

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

#### Properties of intersection multiplicity

The following properties of intersection multiplicity are immediate:

1. $i(P,G\cdot F) = i(P,F\cdot G)$
2. $i(P,(F_1 + F_2)\cdot G) = i(P,F_1\cdot G) + i(P, F_2\cdot G)$ where $F_1 + F_2$ is ~~~<br>~~~the plane curve defined by $f_1f_2$
3. $i(P,F'\cdot G) = i(P,F\cdot G)$ where $F'$ is defined by $f+gh$ for some $h\in K[x,y]$
4. $i(P,F\cdot G) = 0$ if $P\not\in F\cap G$ and $i(P,F\cdot G) = \infty$ if $F$ and $G$ have a common component through $P$. Otherwise $i(P,F\cdot G)$ is finite and positive.
5. $i(P,F\cdot G) = 1$ if $f = x - a$ and $g = y - b$ and $P = (a,b)$, or more generally if the Jacobian $\frac{\partial (f,g)}{\partial (x,y)}$ is not zero at $P$.
6. $i(P,G\cdot H)\geq \min (i(P,F\cdot G), i(P,F\cdot H))$ if $P$ is a simple point on $F$ and $F$ has no common component with $G$ or $H$ through $P$.

### Orders of Zeros and Poles

The setup: $X$ is a variety with a subvariety $V$ of codimension 1. Thus the local ring $A = \mathcal O_{V,X}$ is a one-dimensional local domain. Our goal is to define the *order of vanishing* of a rational function $r\in R(X)^\times$ along $V$. This should be a homomorphism $R(X^*) \to \mathbb Z$:
\begin{equation*}
    \operatorname{ord}_V(rs) = \operatorname{ord}_V(r) + \operatorname{ord}_V(s),
\end{equation*}
and since $r = a/b$ for some $a,b\in A$, we'll necessarily have that
\begin{equation*}
    \operatorname{ord}_V(r) = \operatorname{ord}(a) - \operatorname{ord}(b).
\end{equation*}
When $X$ is nonsingular along $V$ then $A$ is a DVR, and so any $a\in A$ can be written $ut^m$ for some unit $u\in A^\times$ and a unique $m\in \mathbb Z_{\geq0}$, where $t$ is a generator of the maximal ideal. Defining $\operatorname{ord}_V(a) = m$ then extends to a definition on all of $R(X)^*$.

Generalizing this definition requires removing both the codimension 1 and the nonsingular hypothesis. In the special case that $X$ is a curve over a field $K$ and $V$ is a point, our "valuation" definition coincides with $\dim_K A/(a)$ when $a\in A$, but the latter formula works in singular cases too. However, $A/(a)$ is not a finite $K$-vector space in higher dimensions. According to Fulton, the correct definition is that
\begin{equation*}
    \operatorname{ord}(a) = l_A(A/(a))
\end{equation*}
where $l_A(A/(a))$ is the length of $A/(a)$ as an $A$-module. Fulton also write $e_A(a,A)$ for $l_A(A/aA)$.

If $\operatorname{ord}_V(r)$ is positive, then $r$ is zero along $V$. If $\operatorname{ord}_V(r)$ is negative, then $r$ "has $V$ as a pole", i.e. the denominator of $r$ vanishes along $V$.

There are many useful examples in Fulton in this section, some of which confuse me. I may come back to them at some point.

### Cycles and Rational Equivalence

We now promptly arrive at cycles. A *k-cycle* on a scheme $X$ is a finite formal sum
\begin{equation*}
    \sum n_i [V_i]
\end{equation*}

where each $V_i$ is a $k$-dimensional subvariety of $X$ and the $n_i$ are integers. For any $(k+1)$-dimensional subvariety $W$ of $X$ and any $r\in R(W)^*$, we can define a $k$-cycle $[\operatorname{div}(r)]$ by
\begin{equation*}
    [\operatorname{div}(r)] = \sum \operatorname{ord}_V(r)[V],
\end{equation*}
taking the sum over all $k$-dimensional subvarieties of $W$ and noting $\operatorname{ord}_V(r)$ is zero except at finitely many $V$. Now we can define rational equivalence. We first say that a $k$-cycle is *rationally equivalent to zero* and write $\alpha \sim 0$ if there exist finitely many $(k+1)$-dimensional subvarieties $W_i$ of $X$ and $r_i \in R(W_i)^\times$ such that
\begin{equation*}
    \alpha = \sum ~ [\operatorname{div}(r_i)].
\end{equation*}
We then say that two $k$-cycles $\alpha, \beta$ are *rationally equivalent* if $\alpha - \beta \sim 0$ and write $\alpha \sim \beta$. Now for some notation:
- $Z_kX$ is the group of all $k$-cycles on $X$
- $\operatorname{Rat}_kX$ is the group of all $k$-cycles on $X$ rationally equivalent to $0$
- $A_kX = Z_kX / \operatorname{Rat}_k X$ is the group of all $k$-cycles up to rational equivalence.

Furthermore, we define
\begin{equation*}
    Z_*X = \bigoplus_{k =0}^{\dim X} Z_kX, \hspace{2em} A_*X = \bigoplus_{k=1}^{\dim X} A_kX.
\end{equation*}
We call elements of $Z_*X$ *cycles* and elements of $A_*X$ *cycle classes*. We denote by $\{\alpha\}_k$ the component of a class $\alpha$ in $A_kX$.

Having defined all this, Fulton runs through what I call "far reaching" or "general" examples. For instance, he shows
\begin{equation*}
    A_k(X) \cong A_k(X_{\text{red}})
\end{equation*}
and when $X$ is the disjoint union of schemes $X_1,...,X_n$
\begin{equation*}
    A_k(X) \cong \bigoplus_{i=1}^n A_k(X_i).
\end{equation*}
See page 11 of Fulton for those. Instead, let's examine some concrete examples.

#### Example: $X = \mathbb A^2_K$.

I claim that $A_0(X) = A_1(X) = 0$ and $A_2(X) = \mathbb Z$.

*Dimension 2:* $k = 2$. Since $X$ is irreducible it is its own unique dimension 2 subvariety, and hence $Z_2(X) = X\mathbb Z$. As there are no dimension $3$ subvarieties of $X$, $\operatorname{Rat}_2(X) = 0$ vacuously. Thus
\begin{equation*}
    A_2(X) \cong \mathbb Z.
\end{equation*}

*Dimension 1:* $k = 1$. Every codimension 1 subvariety of $X$ is given by the vanishing of some function $f\in \mathcal O_X(X)$. We can therefore write an arbitrary $1$-cycle as 
\begin{equation*}
    \alpha = \sum_i n_i F_i
\end{equation*}
where $F_i = V(f_i)$. Each $f_i$ is an element of $R(X)^*$ which vanishes only on $F_i$ by definition, hence
\begin{equation*}
    \alpha = \sum_i n_i F_i = \sum_i [\operatorname{div}(f_i^{n_i})].
\end{equation*}

*Dimension 0:* $k=0$. In this case an arbitrary cycle is a finite sum of closed points in $X$, namely
\begin{equation*}
    \alpha = \sum_i n_i P_i.
\end{equation*}
Choose a line $\ell_i$ for each $i$ such that $\ell_i$ passes through $P_j$ if and only if $i = j$. Let $t_i$ be the coordinate for $\ell_i$ under the isomorphism $\ell_i \cong \mathbb A^1_K$ which sends $P_i$ to $0$, interpreted as a function on $\ell_i$. Then $t_i$ is a function in $R(\ell_i)^\times$ which vanishes only at $P_i$ with order 1, hence
\begin{equation*}
    \alpha = \sum_{i} n_i P_i = \sum_i [\operatorname{div}(t_i^{n_i})].
\end{equation*}

Since every 1-cycle and 0-cycle is rationally equivalent to 0, we have that $A_2(X) \cong \mathbb Z$ and $A_0(X) = A_1(X) = 0$. We can generalize this argument to conclude that
\begin{equation*}
    A_k(\mathbb A^n_K) = \begin{cases}
        \mathbb Z & k = n \\
        0 & \text{otherwise}
    \end{cases}.
\end{equation*}















