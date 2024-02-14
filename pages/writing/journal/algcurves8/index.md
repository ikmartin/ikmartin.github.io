+++
title = "Algebraic Curves Lecture 8:"
hascode = true
description = "The 8th lecture of algebraic curves by Karl Christ"
tags = ["blog"]
date = "2024-02-07"
published = true
public = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{ title }}

> {{ description }}

\toc

---

## Complete Intersection Curves in $\mathbb P^n$

Take $C = S_1 \cap S_2\subseteq \mathbb P^3$ to be a complete intersection and let $d_i = \deg S_i$. Adjunction gives us
\begin{align*}
    K_C = K_{\mathbb P^3} \otimes \bigwedge_{i=1}^2 N_{C / \mathbb P^3},
\end{align*}
and the normal bundle of $C$ over $\mathbb P^3$ can be written
\begin{align*}
    N_{C/\mathbb P^3} = T_{\mathbb P^3}/T_C, N_{S_i} = T_{\mathbb P^3}/T_{S_i}.
\end{align*}
We then have a map $\varphi:N_C\to N_{S_1} \oplus N_{S_2}$. Since $C$ is smooth, $T_C = T_{S_1}\cap T_{S_2}$ which implies that $\varphi$ is injective. Since $\textrm{rank}(N_C) = \textrm{rk}(N_{S_1} \oplus N_{S_2}$, it follows that $\varphi$ is an isomorphism. Thus
\begin{align*}
    N_C \cong \mathcal O_{\mathbb P^3}(d_1) \oplus \mathcal O_{\mathbb P^3}(d_2)
\end{align*}
and
\begin{align*}
    \bigwedge^2 N_C = \bigwedge^2 \mathcal O_{\mathbb P^3}(d_1) \oplus \mathcal O_{\mathbb P^3}(d_2) = \mathcal O_{\mathbb P^3}(d_1 + d_2).
\end{align*}
The last equality above follows from the standard trick we introduced [last lecture](pages/writing/journal/algcurves7/index.md): if you have a short exact sequence
\begin{align*}
    0 \to \mathcal F\to \mathcal F \to \mathcal F'' \to 0
\end{align*}
where each term has rank $r$, $r'$ and $r''$ respectively, then
\begin{align*}
    \bigwedge^{r'}\mathcal F' = \bigwedge^{r}\mathcal F \otimes \bigwedge^{r''}\mathcal F''.
\end{align*}
In our case we have the somewhat trivial exact sequence
\begin{align*}
    0 \to \mathcal O_{\mathbb P^3}(d_1) \to \mathcal O_{\mathbb P^3}(d_1)\oplus \mathcal O_{\mathbb P^3}(d_2) \to \mathcal O_{\mathbb P^3}(d_2)\to 0,
\end{align*}
which gives us the final equality above after messing around with tensors and direct sums.

\break

Examining the formula $2g - 2 = \deg (K_C)$ and noting that $\deg(C) = d_1\cdot d_2$, we have
\begin{align*}
    2g - 2 = \deg(K_C) &= \deg\big((\mathcal_{\mathbb P^3}(-4) \otimes \mathcal )_{\mathbb P^3}(d_1 + d_2)_{|_C}\big) \\
    &= d_1\cdot d_2 \cdot (d_1+d_2 - 4).
\end{align*}
Thus $g = \frac{1}{2}(d_1\cdot d_2 \cdot (d_1 + d_2 - 4)) + 1$.

\begin{rmk}
1. If $d_2 = 1$ then we get the correct formula:
\begin{align*}
    g = \frac{1}{2}(d_1\cdot (d_1 - 3)) + 1 = \frac{(d_1 - 1)(d_1 - 2)}{2}
\end{align*}
1. For the intersection of $n-1$ hypersurfaces in $\mathbb P^n$ we get analogously
\begin{align*}
    \bigwedge^{n-1}N_C = \mathcal O_{\mathbb P^3}\left(\sum d_i\right) \text{~ and ~} g = \frac{1}{2}\left(\prod_i d_i~\cdot~ (\sum d_i - n - 1)\right) + 1.
\end{align*}
\end{rmk}

Up to $n = 10$, the possible values of $g$ for complete intersection curves are
\begin{align*}
    0,1,3,4,5,6,9,10.
\end{align*}
For a plane curve, they are $0,1,3,6$.

@@revindentblock
    **Example:** &nbsp; Take $C = Q_1\cap Q_2 \subseteq \mathbb P^3$ to be a smoooth curve where each $Q_i$ is a smooth quadric. Our formula gives us
    \begin{align*}
        g(C) = \frac12 (4 \cdot ( 0 ) ) + 1 = 1,
    \end{align*}
    so we get a genus 1 curve.

    Conversely, any genus 1 curve can be realized as the intersection of two quadrics in $\mathbb P^3$. If $X$ is a genus 1 curve, then Riemann-Roch gives us
    \begin{align*}
        h^1(\mathcal O_X(4p)) = d - g + 1 = 4
    \end{align*}
    which means $\mathcal O_X(4p)$ gives an embedding into $X\to \mathcal P^3$. We therefore have a map
    \begin{align*}
        H^0(\mathbb P^3,\mathcal O_{\mathbb P^3}(2)) \to H^0(X,\mathcal O_X(2)).
    \end{align*}
    The left term above has dimension $\binom{3+2}{2} = 10$ while the right term has dimension $8 - 1 + 1$ (by Riemann-Roch), so the kernel of this map is at least 2. So $X$ is the intersection of at least $2$ quadrics in $\mathbb P^3$, and by dimension considerations we can choose two of those and they will still cut out $X$.
@@

@@revindentblock
    **Example 2:** Consider $\mathbb P^1 \to \mathbb P^3$ given by $V = \{t&4, t^3s, ts^3, s^4\} \subseteq H^0(\mathbb P^1, \mathcal O_{\mathbb P^1}(4))$. Observe that there are smooth curves of genus 0 and genus 1 in $\mathbb P^3$. Note that the image of this map must lie on a quadric as a bidegree $(1,4)$ curve; we can see this by first passing through an embedding $\mathbb P^1\to \mathbb P^1\times \mathbb P^1$.
@@

Observation: No smooth non-degenerate rational curve $C\subseteq \mathbb P^3$ can be a complete intersection. Remember that $2g - 2 = d_1\cdot d_1 \cdot (d_1 + d_2 - 4)$, if $g = 0$, then this means $d_1 + d_2 \leq 3$. The only options are $d_1 = d_2 = 1$ which implies we have a line or $d_1 = 1$ and $d_2 = 2$ which implies we have a cubic in $\mathbb P^2$, both of which are degenerate.

## Covers and Riemann Hurwitz Theorem (start)

A cover (or covering) is a surjective map $f:Y\to X$ between two smooth curves $X$ and $Y$. 

The **degree** of $f$ is the number of preimages in a general fibre; or more algebraically, its the degree of the field extension $K(Y)/K(X)$.

The **ramification index** of $f$ at $p\in Y$ is $v_p(t) - 1$ where $t$ is a local parameter at $f(p)$. A "local parameter" at $f(p) = q$ is a function which vanishes to order $1$ at $q$. It lives in $\mathcal O_{X,q}$ and we take the valuation in $K(Y)$ under the embeddings
\begin{align*}
    \mathcal O_{X,q} \hookrightarrow K(X) \hookrightarrow K(Y).
\end{align*}
