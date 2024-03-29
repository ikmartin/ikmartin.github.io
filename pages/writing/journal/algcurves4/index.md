+++
title = "Algebraic Curves Lecture 4: Riemann Roch"
hascode = true
description = "The fourth lecture of the algebraic curves class"
tags = ["blog"]
date = "2024-01-29"
published = true
public = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{ title }}

> {{ description }}

\toc

---

Last time we stopped with the following characterization of "very ampleness":

\begin{prop}
    Let $L$ be a line bundle on a curve $X$. Then

1. $L$ is base point free if and only if $h^0(X,L) = h^0(X,L(-p)) + 1$ for all $p\in X$.
1. $L$ is very ample if $h^0(X,L) = h^0(X,L(-p-q))+2$ for all $p,q \in X$.
\end{prop}

\break

\begin{rmk}
    The same is true for linear series, and the definitions (of base point, of very ample) are the same as well.
\end{rmk}

\break

\begin{example}
    Take a map $\mathbb P^1 \to \mathbb P^2$ given by $(s:t) \mapsto (s^3:st^2:t^3)$. Take the linear series $V = \mathrm{span}\{s^3,st^2,t^3\} \subseteq H^0(\mathbb P^1, \mathcal O_{\mathbb P^1}(3))$. In the affine chart $r\mapsto (r^2, r^3)$ this is given by the equation $x^3 - y^2$; it's the cuspoidal cubic. The linear series $V$ is NOT very ample because at the singularity the differential is not injective: the sections in $V$ that vanish at $0$ are of the form $a\cdot r^2 + b\cdot t^3 = r^2\cdot (a+b\cdot r)$, meaning
    \begin{align*}
        \dim(V(-0)) = \dim(V(-2\cdot 0)).
    \end{align*}
    Here $0$ is the origin $(0,0)$, the divisor.

    Here are other ways to see that $(0,0)$ is singular in the the image:
1. $k\mapsto (2r \cdot k, 3r^2 \cdot k)$
2. Jacobi's criterion
3. If you have a plane curve you can directly read off the equation of the Zariski tangent space at the origin -- the equation of the Zariski tangent space at the origin is the linear term in the equation. In the case of $x^3 - y^2 = 0$ we don't have a linear term, hence singular at the origin.
4. You can also use the definition of a singularity; show that the dimension of the Zariski tangent space is larger than the dimension of the ring. In our case,
\begin{align*}
    \dim_{\mathbb C}\left(\frac{(x,y)}{(x^2,xy,y^2)} = 2 \neq 1.\right)
\end{align*}
\end{example}

Note that the equation for the *tangent cone* is given by the lowest order terms. The tangent cone to an affine variety $X$ given by an ideal $I$ at the origin is the Zariski closed subset corresponding to the ideal $in(I)$, the ideal generated by all the lowest degree terms of elements in $I$.

## Riemann Roch

\begin{lem}
1. If $\deg(L) < 0$ then $h^0(X,L) = 0$.
1. If $\deg(L) = 0$ and $h^0(X,L) > 0$ then $L\cong \mathcal O_X$.
\end{lem}
\begin{proof}
1. Assume $h^0(X,L) > 0$. We know that $L\cong \mathcal O_X(D)$ for some $D\in \textrm{Div}(X)$. If $h^0(X,L) > 0$, then $D\sim D'$ with $D'$ effective which then implies that $\deg(D') = \deg(L) \geq 0$.
1. This follows since the only effective divisor of degree $0$ is 0 (all coefficients equal to 0 in the divisor).
\end{proof}

\begin{defn}
    We denote by $K_X$ the **canonical sheaf** on $X$. Analytically, the sheaf of holomorphic one forms.
\end{defn}

\begin{thm}
    *(Serre Duality)*.
    \begin{align*}
        H^1(X,L) \cong H^0(X,K_X\otimes L^{-1}).
    \end{align*}
\end{thm}
Note that we call $K_X\otimes L^{-1}$ the **residual of $\mathbf{L}$**.

\begin{thm}
    *(Riemann Roch).*
    \begin{align*}
        h^0(X,L) - h^0(X,K_X\otimes L^{-1}) = d - g + 1.
    \end{align*}
\end{thm}

\begin{proof}
    By Serre Duality, we need to show that
    \begin{align*}
        h^0(X,L) - h^1(X,L) = d - g + 1.
    \end{align*}
    We prove this by induction, and we write $h^i(-)$ for $h^i(X,-)$ to simplify notation a bit.
\break
    *Base case:* The claim is true for $L = \mathbb O_X$:
    \begin{align*}
        h^0(\mathcal O_X) = 1, ~h^1(\mathcal O_X) = g, ~d = 0.
    \end{align*}
    We show that equality holds for $L$ if and only if it holds for $L(-p)$.
    \break
    We have a short exact sequence
    \begin{align*}
        0\to L(-p)\to L\to L|_p \to 0
    \end{align*}
    where $L|_p$ denotes the skyscraper sheaf of $L$ at $p$. I can then pass to the long exact sequence of cohomology to get
    \begin{align*}
        0 \to H^0(L(-p)) \to H^0(L) \xrightarrow{\mathrm{ev}} K \to H^1(L(-p)) \to H^1(L) \to 0
    \end{align*}
    noting that $H^0(L|_p) = K$ and $H^1(L|_p) = 0$. From this long exact sequence we have that 

\begin{align*}
    h^0(L) = h^0(L(-p)) + \dim(\ker \mathrm{ev})
\end{align*} 
and
\begin{align*}
    h^1(L(-p)) &= h^1(L) + \textrm{codim}(\ker \mathrm{ev}) \\
    &= h^1(L) + 1 - \dim(\ker\textrm{ev}).
\end{align*}
This implies
\begin{align*}
    h^0(L) - h^0(L(-p)) = h^1(L) + 1 - h^1(L(-p))
\end{align*}
and then
\begin{align*}
    h^0(L) - h^1(L) = h^0(L(-p)) - h^1(L(-p)) + 1.
\end{align*}
\end{proof}
