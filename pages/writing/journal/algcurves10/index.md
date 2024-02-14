+++
title = "Algebraic Curves Lecture 10: Hurwitz bound and hyperelliptic curves."
hascode = true
description = "The 10th lecture of algebraic curves with Karl Christ"
tags = ["blog"]
date = "2024-02-14"
published = true
public = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{ title }}

> {{ description }}

\toc

---

### Proof of Hurwitz Bound
Last time we ended with the Hurwitz bound:

\begin{cor}
    *(Hurwitz bound).* &nbsp; Suppose $X$ has genus $\geq 2$ and finitely many automorphisms. Then $|\Aut(X)| \leq 84(g - 1)$.
\end{cor}
Note that if $X$ is genus $0$ or $1$ then it will never have finitely many automorphisms.
\begin{proof}
let $f_i$ be the number of points of ramification index $r_i$ over a point $p_i$ in the base. Orbit stabilizer theorem says that $|\Aut(X)| = f_ir_i$. Let $h$ denote the genus of $X/\Aut(X)$. Riemann-Hurwitz says that
\begin{align*}
    2g(X) - 2 &= |\Aut(X)| \cdot (2h - 2) + \sum_{i,j}(e_{i,j} - 1) \\
    &= |\Aut(X)| \cdot (2h - 2) + \sum_{i=1}^bf_i(r_i - 1)
    &= |\Aut(X)| \cdot \left(2h - 2 - \sum_{i=1}^b(1 - \frac{1}{r_i})\right).
\end{align*}
Set $c = \left(2h - 2 - \sum_{i}(1 - \frac{1}{r_i})\right)$. We'll come up with a lower bound on $c$ by examining a few cases:

**Case 1:** $h \geq 2$. Then $c \geq 2$ and $|\Aut(X)| \leq g - 1$.

**Case 2:** $h = 1$. Then $b \geq 1$ (remember, $b$ is the number of branch points) and $c \geq \frac{1}{2}$. Thus $|\Aut(X)|\leq 4(g - 1)$.

**Case 3:** $h = 0$. 

**Case 3.1:** If $b\geq 5$, then $c \geq \frac{1}{2}$ and so $|\Aut(X) \leq 4(g - 1)$. 

**Case 3.2:** If $b = 4$ then not all $r_i$ can be equal to $2$. Then
\begin{align*}
    c \geq -2 \frac{3}{2} = \frac{g + 4 - 12}{6} = \frac{1}{6} \implies |\Aut(X)| \leq 12(g - 1).
\end{align*}

**Case 3.3:** The case that $b \leq 2$ is not possible since $g$ is at least $2$.

**Case 3.4:** If $b = 3$ then suppose $r_1\leq r_2 \leq r_3$ without loss of generality. Now MORE subcases:

**Case 3.4.1:** If $r_1\geq 3$, then not all $r_i$ can be equal to $3$, so
\begin{align*}
    c \geq -2 + \frac{2}{3} + \frac{2}{3} + \frac{3}{4} = \frac{-24 + 16 + 9}{12} = \frac{1}{12},
\end{align*}
from which it follows that $|\Aut(X)| \leq 24(g - 1)$.

**Case 3.4.2:** If $r_1 = 2$ then $r_2 > 4$ and $r_3 \geq 5$. Then
\begin{align*}
    c \geq -2 + \frac12 + \frac34 + \frac 45 = \frac{-40 + 10 + 15 + 16}{20} = \frac{1}{20}
\end{align*}
so $|\Aut(X)| \leq 40(g - 1)$.

**Case 3.4.3:** If $r_1 = 2$, $r_2 = 3$ and then $r_3 \geq 7$. Then
\begin{align*}
    c \leq -2 + \frac{1}{2} + \frac34 + \frac67 = \frac{1}{42}
\end{align*}
so $|\Aut(X)| \leq 84(g - 1)$, which is exactly the Hurwitz bound.

So in all cases, if $X$ is a genus $\geq 2$ curve, then $|\Aut(X)| \leq 84(g - 1)$. 

\end{proof}

### Hyperelliptic curves

A curve $X$ is called **hyperelliptic** if it admits a $g^1_2$, that is, a degree $2$ map $X\to \mathbb P^1$.

@@revindentblock
1. If $g = 0$ (meaning $X \cong \mathbb P^1$) then $h^0(\mathcal O_{\mathbb P^1}(2)) = 3$. Any 2-dimensional subspace $V\subset H^0(\mathcal O_{\mathbb P^1}(2))$ gives a $g^1_2$.
1. If $g \geq 1$ and $X$ is hyperelliptic, then the g$1_2$ needs to be complete.
1. If $g = 1$, then any degree 2 line bundle gives a $g^1_2$ (Riemann-Roch).
1. If $g = 2$, then the canonical divisor has degree equal to $2g - 2 = 2$, and its space of global sections is $h^0(K_X) = g = 2$. From Riemann-Roch we can deduce that this is the unique $g^1_2$.
@@
As a reminder:
\begin{lem}
    If $X$ has genus $g \geq 1$ and $L$ has degree $2g - 2$ then $h^0(L) \leq g$ and equality holds if and only if $L\cong K_X$.
\end{lem}
\begin{proof}
    \begin{align*}
        h^0(L) - h^0(K_X - L) = 2g - 2 - g + 1 = g - 1.
    \end{align*}
\end{proof}

\begin{prop}
    If $X$ is a hyperelliptic curve with $g\geq 2$ then $K_X\cong L^{\otimes g - 1}$ where $L$ is a $g^1_2$.
\end{prop}
\begin{proof}
    $L$ induces a map $\varphi_L:X\to \mathbb P^1$. Consider the Veronese embedding of $\mathbb P^1$, i.e. the map $\mathbb P^1 \to \mathbb P^{g - 1}$ induced by $\mathcal O_{\mathbb P^1}(g - 1)$: $[x,y] \mapsto [x^3, x^2y, xy^2, y^3]$. Then
    \begin{align*}
        \varphi^*_L\mathcal O_{\mathbb P^1}(1)\cong L
    \end{align*}
    and
    \begin{align*}
        \mathcal O_{\mathbb P^1}(g - 1) \cong \mathcal O_{\mathbb P^1}(1)^{\otimes g - 1}.
    \end{align*}
    Thus $\varphi\circ \varphi_L:X\to \mathbb P^{g - 1}$ given by $L^{\otimes g - 1}$. In particular, $h^0(L^{\otimes g-1})$ and $\deg(L^{\otimes g-1}) = 2g -2$, hence $L^{g-1}\cong K_X$.
\end{proof}

\begin{thm}
    Let $g \geq 2$. Then $K_X$ is base point free and
1. very ample if $X$ is not hyperelliptic
1. a $2:1$ cover of a rational normal curve in $\mathbb P^{g-1}$ if $X$ is hyperelliptic.
\end{thm}
\begin{proof}
Let $p\in X$.
\begin{align*}
    h^0(K_X - p) - h^0(\mathcal O_X(p)) = 2g - 3 - g + 1 = g - 2.
\end{align*}
We previously saw that $h^0(\mathcal O_X(p)) = 1$ in this case (I forgot why this is true) so $h^0(K_X - p) = g - 1 = h^0(K_X) - 1$.
1. Since $h^0(\mathcal O_X O(p + q) = 1$ \begin{align*}h^0(K_x - p - q) - &h^0(\mathcal O_X O(p + q)) = 2g - 4 - g + 1 = g-2 \\ &\implies h^0(K_x - p - q) = g - 2.\end{align*}
1. This was the previous proposition.
\end{proof}

\begin{prop}
    If $X$ is a hyperelliptic curve of genus $\geq 2$ then the $g^1_2$ is unique.
\end{prop}
\begin{proof}
    Consider $\varphi_{K_X}:X\to \mathbb P^{g -1}$. By the previous proposition, this is a $2:1$ cover of its image which is a rational curve. Conversely, give any $g^1_2$ on $X$ and it defines this cover. This implies the $g^1_2$ is unique.
\end{proof}
