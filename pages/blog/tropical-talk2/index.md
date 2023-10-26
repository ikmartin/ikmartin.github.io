+++
title = "Tropicalization of Abstract Curves"
hascode = true
description = "Notes from Abhishek's talk on the tropicalization of abstract curves for our tropical geometry learning seminar"
tags = ["tropical-geometry,", "algebraic-geometry,", "curves"]
date = "2023-10-23"
published = true
+++

@def mintoclevel=2
@def maxtoclevel=3

# Tropicalization of Abstract Curves

\toc

---

Today Abhishek Koparde spoke on the tropicalization of abstract curves. These are some rough notes taken during the talk.

Main reference: [Tropical geometry and correspondence theorems via toric stacks](https://arxiv.org/abs/1001.1554).
Link to Abhishek's notes: not yet obtained.

## Conventions
$K$ is algebraicaly closed, $R$ is a complex DVR with residue field $k$ and fraction field $F$. We let $\overline F$ be the separable closure of $F$ and $v$ is a normalized valuation on $\overline F$ so that $v(F^*) = \mathbb Z$.

Graphs are finite connected with the usual notations.

Curves are denoted by $(C,D)$, are assumed to be complete with marked points $(q_1,...,q_{|D|})$ over $\overline F$, and $(C_{R_L}, D_{R_L})$ is the nodal model ($F \subset L\subset \overline F$ is an intermediate field extension). $C_{R_L} \to \Spec R_{L}$ is a proper curve and $L/F$ is finite separable. $D_{R_L}$ is a finite set of $R_L$ points and the total space $C_{R_L}$ is normal. $(C_{R_L},D_{R_L}) \times_{\Spec R_{L}} \Spec k$ is nodal and $(C_{R_L}, D_{R_L})\times_{\Spec_{R_L}} \Spec \overline F \cong (C,D)$.

## Tropical Curves

A tropical curve $\Gamma$ is a topological graph with a complete (possibly degenerate) metric. (Note that a degenerate metric is one where $d(x,y) = 0$ does not necessarily imply that $x = y$. I think this is sometimes called a pseudo-metric.)
- (s1) Vertices of $\Gamma$ are divided into finite vertices and infinite vertices
- (s2) $V^\infty(\Gamma)$ is equipped with a total order and $V^f(\Gamma)$ is just a set.
- (p1) $\Gamma$ has finitely many vertices and edges
- (p2) any infinite vertex has valency 1 and is connected to a finite vertex by an edge called an "unbounded edge". We denote by $E^b(\Gamma)$ those edges between finite vertices and by $E^\infty(\Gamma)$ those edges between a finite and infinite vertex.
- (p3) Any bounded edge $e$ is isometric to the interval $[0,|e|]$ (read $|e|$ as "the length of $e$") where $|e| \in \mathbb R_{\geq 0}$ and an unbounded edge is isometric to $[0,\infty]$  where $0$ maps to the finite vertex and $\infty$ maps to the infinite vertex.

These axioms describe a **general tropical curve**. We say
- a **$\mathbb Q$-tropical curve** if $|e| \in \mathbb Q$ for any $e\in \Gamma^b(\Gamma)$ 
- a tropical curve is **irreducible** if $\Gamma$ is connected 
- the **genus** of a tropical curve is $g(\Gamma) = 1 - |V(\Gamma)| + |E(\Gamma)|$
- we say a curve is **stable** if all finite vertices have valency at least $3$
- An isomorphism of tropical curves is an isomorphism of the underlying metric graphs.

### Algorithm
The following modifications made to a general tropical graph will not change the genus:
- Operation 1: Divide each bounded edge $e$ into finitely many pieces
- Operation 2: Subdivide each unbounded edge into finitely many pieces
- Operation 3: Attach rooted metric trees at some finite vertices such that all edges (but maybe not some leaves of that metric tree) are bounded

Claim: Let $\Gamma$ be an irreducible tropical curve satisfying $g(\Gamma) + \frac{|V^\infty(\Gamma)| + 1}{2} \geq 2$. Then there exists a unique stable tropical curve $\Gamma^{st}$ such that $V^\infty(\Gamma) = V^\infty(\Gamma^{st})$ and $\Gamma$ can be obtained from $\Gamma^{st}$ and $\Gamma$ can be obtained from $\Gamma^{st}$ by using finitely many of the above steps. We call $\Gamma^{st}$ the **stabilization** of $\Gamma$.

### A $\mathbb Q$-tropical curve associated to $(C,D)$
Consider a curve $(C,D)$ and remember that $(C_{R_L},D_{R_L})$ is the nodal model and $C_{R_L} \times_{\Spec R_L} \Spec k$ is the fiber over the base. Irreducible components will correspond to finite vertices, nodes will correspond to edges between finite vertices and $D_{R_L}'s$ which specialize to $C_V$ will correspond to infinite edges. This should determine a tropical curve, and we call this tropical curve the **tropicalization** of the curve.

At this point Abhishek included a picture of a sphere identified with a torus at a point corresponding a tropical curve with two finite vertices, one finite edge and three infinite edge. One finite vertex has valence 3 and the other has valence 2. In particular, this means the tropicalization is not stable.

There was some ambiguity about what it means to say "$(C,D)$ is stable". At first, we thought it might mean that there exists a nodal model $(C_{R_L},D_{R_L})$ such that its special fiber is stable, but this is true of any curve because of the stable reduction theorem, so it must be something else.

### Parameterized Tropical Curves

Let $N$ be a lattice, $N_\mathbb R = N\otimes \mathbb R$. A parameterized tropical curve is a pair $(\Gamma, h_\Gamma)$ where $h_\Gamma:V(\Gamma) \to N_\mathbb R$ is a map such that $h_\Gamma(v) \in N$ for $v\in V^\infty(\Gamma)$ and
\begin{align}
    \frac{1}{|e|}(h_\Gamma(v) - h_\Gamma(v')) \in N.
\end{align}
We also require that it satisfies the balancing condition:
\begin{align}
    v \in V^f(\Gamma) \implies \sum_{v'\in V^f(\Gamma), e\in E_{vv'}(\Gamma)} \frac{1}{|e|}(h_\Gamma(v) - h_\Gamma(v')) ~+~ \sum_{v' \in V^\infty(\Gamma), e\in E_{v,v'}(\Gamma)} h_\Gamma(v') ~=~ 0.
\end{align}
If $h_\Gamma(v) \in N_\mathbb Q$ for all $v$ then we say $\Gamma$ is a $N_\mathbb Q$-parameterized $\mathbb Q$-tropical curve. For the duration of today we'll attempt to justify the balancing condition.

Suppose that you have a map $f:C\setminus D \to T_{N, \overline F}$ and let $(C_{R_L}, D_{R_L})$ be a nodal model. Here $T_{N,\overline F}$ is the algebraic torus of dimension equal to the rank of $N$. There's a diagram that I'd like to draw but can't because of tikzcd support in markdown, but its rows look like $C\setminus D \to T_{N,\overline F}$ and $C_{R_L}\setminus D_{R_L} \to T_{N,R_L}$.

In this picture, given a character $\chi^m$ on $T_{N,R_L}$, I can pull back to obtain a character on $C_{R_L}\setminus D_{R_L}$. I can evaluate the order of this on an irreducible component $V$ of $C$, and arrive at the following definition for $h_\Gamma$:
$$ 
    h_\Gamma(V) := \frac{1}{|e|} \operatorname{ord}_{V} f^*(\chi^m).
$$

The character $\chi^m$ is a linear function of $m$ for some $m\in M = N^\vee$, so in particular, $\frac{1}{|e|} \operatorname{ord}_{V} f^*(\chi^m) \in N_\mathbb Q$. Furthermore,
$$
\operatorname{ord}_{V} f^*(\chi^{m + m'}) = \operatorname{ord}_{V} f^*(\chi^m) + \operatorname{ord}_{V} f^*(\chi^{m'}),
$$
so this definition of $h_\Gamma(V)$ is linear. We also need that $\frac{1}{|e|}(h_\Gamma(v) - h_\Gamma(v')) \in N_\mathbb Q$ for any bounded edge $v$.

We completed the proof that $h_\Gamma$ does indeed satisfy the balancing condition, but I wasn't able to get all of it down. Please see the end of Abhishek's notes.
