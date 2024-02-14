+++
title = "Algebraic Curves Lecture 5: Corollaries to Riemann-Roch"
hascode = true
description = "The 5th lecture of algebraic curves by Karl Christ."
tags = ["blog"]
date = "2024-01-31"
published = true
public = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{ title }}

> {{ description }}

\toc

---

## More Riemann-Roch

Recall that for a divisor $D$ on a curve $X$, if we write

- $\ell(D) = h^0(X,\mathcal O_X(D))$
- $i(D) = h^0(X,K_X\otimes \mathcal O_X(D)^{-1}) = h^1(X,\mathcal O_X(D))$ (here $h^0(X,K_X\otimes \mathcal O_X(D)^{-1})$ is called the "index of speciality")

Then Riemann-Roch says $\ell(D) - i(D) = d - g + 1$ where $d$ is the degree of the line bundle. Today we'll collect some easy Corollaries of Riemann Roch.

\begin{defn}
    $\mathcal O_X(D)/D$ is **special** if $\ell(D) > 0$ and $i(D) > 0$.
\end{defn}

\break

\begin{details}
    \begin{summary}
        \begin{cor}
            Let $K_X$ be the canonical sheaf. Then $h^0(K_X) = g$ and $\deg(K_X) = 2g - 2$.
        \end{cor}
    \end{summary}
    \begin{proof}
        Apply Riemann-Roch to $\mathcal O_X$. Then $h^0(\mathcal O_X) = 1$ since the only global regular functions on $X$ are constant, $h^0(K_X\otimes \mathcal O_X^{-1}) = h^0(K_X)$ and $d = 0$ since the degree of $\mathcal O_X$ is $0$. Then
        \begin{align*}
            h^0(K_X) = g.
        \end{align*}
        Now applying Riemann-Roch to $K_X$ gives us $\deg(K_X) = 2g - 2$.
    \end{proof}
\end{details}

\break

\begin{details}
    \begin{summary}
        \begin{cor}
            If $\deg(L) < 0$ or $\deg(L) > 2g- 2$ then $L$ is not special and
            \begin{align*}
                h^0(L) =
                \begin{cases}
                    0 & \text{if} \deg(L) < 0 \\
                    d - g + 1 &\text{if} \deg(L) > 2g - 2
                \end{cases}
            \end{align*}
        \end{cor}
    \end{summary}
    \begin{proof}
        The first case where $\deg(L) < 0$ was already established, so assume $\deg(L) > 2g - 2$. Then $h^0(L) - h^0(K_X - L) = d - g + 1$.

        Karl says that $h^0(K_X - L) = 0$, I'm not sure why, but this gives you the result.
    \end{proof}
\end{details}

\break

\begin{details}
\begin{summary} 
\begin{cor}
    The Hilbert Polynomial of a degree d subcurve of $\mathbb P^n$ $h_X(m) = d\cdot m - g + 1$.
\end{cor}
\end{summary}
\begin{proof}
    By definition the Hilbert function is the function
    \begin{align*}
        f_X(m) = h^0(X,\mathcal O_X(m)).
    \end{align*}
    Applying Riemman-Roch gives us
    \begin{align*}
        h^0(X,\mathcal O_X(m)) - h^1(X,\mathcal O_X(m)) = dm - g + 1.
    \end{align*}
    For $m \gg 0$, $h^1(X,\mathcal O_X(m)) = 0$.
\end{proof}
\end{details}

\break

\begin{details}
\begin{summary}
    \begin{cor}
        $X$ is rational (i.e. isomorphic to $\mathcal P^1$) if and only if $g = 0$. That is, there is only one genus $0$ curve up to isomorphism.
    \end{cor}
\end{summary}
\begin{proof}
    Suppose $g=0$. We now want to construct a map to $\mathbb P^1$, Pick $p\in X$ and consider $\mathcal O_X(p) = L$. By Riemann-Roch, $h^0(X,L) \geq d - g + 1 = 2$ since $g = 0$ and $d = \deg(\mathcal O_X(p) = 1$. This gives us a degree 1 map $X \dashrightarrow \mathcal P^1$, which implies $X\cong \mathbb P^1$.

    Now suppose that $X\cong \mathbb P^1$. Then $h_X(m) = h^0(\mathcal O_{\mathbb P^1}(m)) = m + 1.$ Then the previous corollary concerning the Hilbert polynomial means $d\cdot m - g + 1 = m + 1$, and since $d = 1$ (viewing $X$ as a curve with a degree 1 embedding in $\mathbb P^1$) we have $g = 0$.
\end{proof}
\end{details}

\break

\begin{details}
    \begin{summary}
        \begin{cor}
            For any line bundle $L$, $h^0(L) \leq \deg(L) + 1$. With equality if and only if $X$ is rational.
        \end{cor}
    \end{summary}
    \begin{proof}
        Suppose $h^0(L) > \deg(L) + 1$. Let $D$ be an effective divisor of degree $d + 1$. Then $h^0(L(-D))\geq 0$. But $0 > \deg(L(-D))$, which is a contradiction.

        If $X$ is rational, $L$ has degree d. Then $h^0(L) \geq d + 1$. Then $h^0(L)\geq d + 1$ since $h^1(L) = 0$. Conversely, suppose there is a line bundle $L$ of degree $d > 0$ and space of global sections $h^0(L) = d + 1$.
    \end{proof}
\end{details}

Now let $D$ be an effective divisor of degree $d - 1$. Then $h^0(L(-D)) \geq 2$ and the degree of $L(-D)$ is $1$ (since $L$ is degree $d$ and $-D$ is of degree $1 - d$). This again gives a map $X\dashrightarrow \mathbb P^1$ of degree $1$ and hence $X\cong \mathbb P^1$.

Now for the most important corollary:

\begin{details}
    \begin{summary}
        \begin{cor}
1. Any line bundle of degree $2g$ is base point free 
1. Any line bundle of degree $2g + 1$ is very ample.
        \end{cor}
    \end{summary}
    \begin{proof}
        If $\deg(L) \geq 2g$, then $h^0(L) = d - g + 1$ and $h^0(L(-p)) = d - 1$ for all $p$. This implies there are no base points.

        If $\deg(L)\geq 2g + 1$ then $h^0(L) = h^0(L(-p-q)) + 2$ for all $p,q$.
    \end{proof}
\end{details}
