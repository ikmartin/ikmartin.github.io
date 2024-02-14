+++
title = "Algebraic Curves Lecture 7: "
hascode = true
description = "The seventh lecture of algebraic curves by Karl Christ."
tags = ["blog"]
date = "2024-02-05"
published = true
public = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{ title }}

> {{ description }}

\toc

---

## Connection to last lecture

Last time we stopped with the calculation that $K_{\mathbb P^r} = \mathcal O_{\mathbb P^r}(-r-1)$. Using this together with the following theorem is quite profitable:

\begin{thm}
    *(Adjunction formula)*. Let $X$ be smooth and $Y\subseteq X$ smooth of codimension $k$. Then we can express the canonical sheaf of $Y$ in terms of the canonical sheaf of $X$ in the following way:
    \begin{align*}
        K_Y = K_X\otimes \bigwedge^k N_{Y/X} \otimes \mathcal O_Y,
    \end{align*}
    where we include the last tensor just to ensure that this equality happens as sheaves on $Y$. I believe the tensor products are taken over $\mathbb C$.
\end{thm}
The most common situation in which we use this is where $k = 1$, in which case the adjunction formula says
\begin{align*}
    K_Y = K_X\otimes \mathcal O_X(Y) \otimes \mathcal O_Y
\end{align*}
or in the divisor notation
\begin{align*}
    K_Y = (K_X + Y)|_{Y^0}.
\end{align*}
Here's a sketch of the proof for $k=1$:
\begin{proof}
    *(Sketch).* We have an exact sequence
    \begin{align*}
        0 \to T_Y \to T_X|_{Y} \to N_{Y/X} \to 0.
    \end{align*}
    We have a picture on the board at this point which shows a curve $Y$ together with a tangent line drawn at a point on $Y$ and a normal space (a plane) at the same point.

    Dualize this to get
    \begin{align*}
        0 \to N_{Y/X}^* \to T_{X|_{Y}}^*\to T^*_{Y}\to 0
    \end{align*}
    noting that the rank of these bundles are $1$, $n$ and $n-1$ respectively. It's a general fact that if you have an exact sequence
    \begin{align*}
        0 \to \mathcal F'\to \mathcal F\to \mathcal F'' \to 0,
    \end{align*}
    then
    \begin{align*}
        \bigwedge^r \mathcal F = \bigwedge^{r'} \mathcal F' ~\otimes~\bigwedge^{r''}\mathcal F'',
    \end{align*}
    so
    \begin{align*}
        \bigwedge^n T_{X|_Y}^* = N_{Y/X}^* \otimes \bigwedge^{n-1}T_Y^*.
    \end{align*}
    The leftmost term is $K_{X|_Y}$ and the rightmost term is $K_Y$, so rearranging, we get
    \begin{align*}
        K_Y = N_{Y/X}\otimes K_X\otimes \mathcal O_Y.
    \end{align*}
\end{proof}

## Curves in $\mathbb P^2$

Let's see Bezout's theorem.

\begin{thm}
    *(Bezout's Theorem).* If $C_1$, $C_2\subseteq \mathbb P^2$ are projective curves of degree $d_1$ and $d_2$ respectively, then $C_1\cdot C_2 = d_1\cdot d_2$.
\end{thm}
\begin{proof}
    $C_1$ is linearly equivalent to a union of $d_1$ general lines; likewise, $C_2$ is linearly equivalent to a union of $d_2$ general lines. Any two linear intersect in exactly one point, and $C_1\cdot C_2$ is well-defined on linear equivalence classes. Thus, counting intersection of lines gives $C_1\cdot C_2 = d_1\cdot d_2$.
\end{proof}

Remember: $C_1$ and $C_2$ are divisors of $\mathbb P^2$ and two divisors $C$ and $D$ are linearly equivalent ($C\sim D$) if and only if $C - D = \div(f)$. The statement that every curve of degree $d$ is linearly equivalent to a union of lines is something like saying that every polynomial of degree $d$ factors as a product of $d$ linear terms.

\begin{prop}
    *(genus-degree formula)*. If $C\subseteq \mathbb P^2$ is a smooth plane curve of degree $d$ and genus $g$, then
    \begin{align*}
        g = \frac{(d-1)(d-2)}{2}.
    \end{align*}
\end{prop}
\begin{proof}
    Recall that we saw, as a corollary of Riemann Roch, that $\deg(K_C) = 2g - 2$. By adjunction we get
    \begin{align*}
        K_C = (K_{\mathbb P^2} + C)_{|_C} 
        &= \left(\mathcal O_{\mathbb P^2}(-3) \otimes \mathcal O_{\mathbb P^2}(d)\right)_{|_C} \\
        &= \left(\mathcal O_{\mathbb P^2}(d - 3)\right)_{|_C}
    \end{align*}
    which implies
    \begin{align*}
        \deg(K_C) = (d-3)\cdot d = d^2 - 3d = 2g - 2.
    \end{align*}
    Solving for $g$ gives the result.
\end{proof}

## Curves in $\mathbb P^1\times \mathbb P^1$

A curve on $\mathbb P^1\times \mathbb P^1$ (take coordinates $[u_0:u_1]\times [v_1\times v_2]$) is given by a bi-homogeneous polynomial of bi-degree $(d_1, d_2)$; that is, a polynomial in $u_0,u_1,v_0,v_1$ which is homogeneous of degree $d_1$ in $u_0,u_1$ and homogeneous of degree $d_2$ in $v_0, v_1$. For instance, $u_0^2 \cdot u_1 \cdot v_0 \cdot v_1 + u_1^3 \cdot v_0^2$ has bidegree $(3, 2)$.

**Fact:** $C\sim D\subseteq \mathbb P^1\times \mathbb P^1$ if and only if $C$ and $D$ have the same bi-degree.

\begin{prop}
    Let $C_1$ and $C_2$ be curves of bidegrees $(d_1,e_1)$ and $(d_2,e_2$). Then
    \begin{align*}
        C_1\cdot C_2 = d_1e_2 + d_2 e_1
    \end{align*}
\end{prop}
The proof is, again, done by counting the intersections of lines. Omitted.

Now consider an arbitrary curve $C$ in $\mathbb P^1\times \mathbb P^1$ of bi-degree $(d_1,d_2)$. It has canonical divisor
\begin{align*}
    K_C = (K_{\mathbb P^1\times \mathbb P^1} + C)_{|_C}
\end{align*}
by the adjunction formula. Once you know that $K_{\mathbb P^1\times \mathbb P^1} = \mathcal O_{\mathbb P^1\times \mathbb P^1}(-2)$ (see below for this computation) the above equality implies that $\textrm{bideg}(K_Q) = (-2, -2)$.

Here are two ways of seeing that $K_{\mathbb P^1\times \mathbb P^1} = \mathcal O_{\mathbb P^1\times \mathbb P^1}(-2)$.

@@revindentblock
*Method 1:* We realize $Q = \mathbb P^1\times \mathbb P^1$ as a smooth quadric in $\mathbb P^3$ (in fact, [every smooth quadric in $\mathbb P^3$ is isomorphic to $\mathbb P^1\times \mathbb P^1$](https://math.stackexchange.com/questions/1334097/show-that-any-quadric-in-mathbbp3-is-isomorphic-to-mathbbp1-times-m)). To see this, take the Segre embedding $[u_0:u_1]\times [v_0:v_1]\mapsto [u_0v_0:u_0v_1:u_1v_0:u_1v_1]$ and notice that this is exactly the surface $xy = zw$ in $\mathbb P^3$ after choosing homogeneous coordinates $[x:y:z:w]$. 

Now apply adjunction:
\begin{align*}
    K_Q = (K_{\mathbb P^3} + Q)_{|_Q} = (\mathcal O_{\mathbb P^3}(-4) + \mathcal O_{\mathbb P^3}(2))_{|_Q} = (\mathcal O_{\mathbb P^3}(-2))_{|_Q}.
\end{align*}
@@

@@revindentblock
    *Method 2:* (Thanks Abhishek!) We can instead calculate $K_{\mathbb P^1\times \mathbb P^1}$ without considering an embedding into $\mathbb P^3$ by applying the adjunction formula to one copy of $\mathbb P^1$ inside of $\mathbb P^1\times \mathbb P^1$. Adjunction says
    \begin{align*}
        K_{\mathbb P^1} = (K_{\mathbb P^1\times \mathbb P^1} + \mathbb P^1).
    \end{align*}

    We know $K_{\mathbb P^1} = \mathcal O_{\mathbb P^1}(-2)$ since $K_{\mathbb P^r} = \mathcal O_{\mathbb P^r}(-r - 1)$. 
@@

Applying the Corollary about $\deg(K_C)$ to our curve $C$ of bi-degree $(d_1,d_2)$, we have
\begin{align*}
    2g - 2 &= \deg(K_C) = \deg((K_{\mathbb P^1\times \mathbb P^1} + C)_{|_C}) \\
    &= (d_1 - 2)\cdot d_2 ~+~ (d_2 - 2)\cdot d_1 \\
    &= 2d_1d_2 - 2d_2-2d_1,
\end{align*}
which implies $g = (d_1-1)(d_2 - 1)$.

This leads to the following proposition.
\begin{prop}
    If $C$ is a smooth curve of bi-degree $(d_1,d_2)$ on $\mathbb P^1\times \mathbb P^1$, then
    \begin{align*}
        g(C) = (d_1 - 1)(d_2 - 1).
    \end{align*}
\end{prop}

Comparing the genus/degree formulas for curves in $\mathbb P^2$ and $\mathbb P^1\times \mathbb P^1$ warrants the following remark.
\begin{rmk}
1. For some $g$ (e.g. g = 2) there exists no smooth plane curve of that genus, simply because $d\mapsto \frac{(d-1)(d-2)}{2}$ is not a surjective map on $\mathbb N$.
1. In contrast, for any $g$ there exists a smooth curve of genus $g$ on $\mathbb P^1\times\mathbb P^1$. For example, a smooth curve of bi-degree $(g-1, 2)$.
\end{rmk}
