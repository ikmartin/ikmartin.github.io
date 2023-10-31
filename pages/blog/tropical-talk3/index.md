+++
title = "Tropicalization of the moduli space of curves"
hascode = true
description = "Tropicalization of Mgn bar"
tags = ["tropical-geometry,", "algebraic-geometry,", "curves"]
date = "2023-10-30"
published = true
+++

@def mintoclevel=2
@def maxtoclevel=3

# Tropicalization of the Moduli Space of Curves

\toc

---

## Reminder

Fix an algebraically closed field $k$. An $n$-pointed nodal curve $(C, P_1,...,P_n)$ of genus $g$ over $k$ is a projective curve with arithmetic genus $g$ and at most nodal singularities. The curve is **stable** if it is connected and the automorphism group $\Aut(C, P_1,...,P_n)$ is finite. The space $\overline{\mathcal M}_{g,n}$ is the moduli space of all $n$-pointed curves of genus $g$. Note that this is a Deligne-Mumford stack because all $n$-pointed curves have finitely many automorphisms.

@@revindentblock
    \thmtitle{Definition 1}{} For each $n$-pointed curve with at most nodes as singularities over $\overline{k}$, we can assign it a **weighted dual graph $G_C = (V,E,L,h)$** given by

1. the set of verticies $V = V(G)$ is the set of irreducible components of $C$ and
1. the set of edges $E = E(G)$ is the set of nodes of $C$ where an edge $e \in E$ is incident to verticies $v_1,.v_2$ if the corresponding node lies in the intersection of the corresponding components. Note that a node contained in only one component corresponds to a loop.
1. The ordered set of legs $L = L(G)$ correponds to the marked points. These are sometimes called "half edges", they're homeomorphic to an unbounded ray in $\mathbb R$.
1. the function $h:V\to \mathbb N$ is the genus function, $h(v)$ is the geometric genus of the component $v\in V$.
    This produces a weighted unbounded graph.
@@

## Tropical curves and their moduli
A **tropical curve** is a metric weighted graph $\Gamma = (G, \ell) = (V,E,L,h,\ell)$ where $\ell: E\to \mathbb R+{> 0}$. One realizes a tropical curve as an **"extended"** metric space by realizing an edge $e$ as an interval of length $\ell(e)$, and you realize a leg as a copy of $\mathbb R_{\geq 0}\cup \{\infty\}$, where $0$ is attached to its incident vertex.

We denote $\Aut(\Gamma)\subset \Aut(G)$ as the subgroup of symmetries preserving the length function $\ell$. An **extended tropical curve** is an **extended metric weighted graph** $(G,\ell)$ with $\ell:E\to \mathbb R \cup \{\infty\}$. The **extended cone** $\overline{\sigma_G^\circ} = (\mathbb R_{>0}\cup \{\infty\})^E$ is a fine moduli space for extended tropical curves whose underlying graph is exactly $G$. $\overline{\mathcal{M}_G}^{trop} = \overline{\sigma}_G^\circ / \Aut(G)$.

One of the things that modding out by $\Aut(G)$ does is delete the zero length edges. Xianyu drew a picture here of an extended weighted graph with three edges here and noted that, when the edge connecting two of the vertices has length zero, it is equivalent to an extended weighted graph with two vertices.

We know that the length function $\ell$ actually comes from the valuation $K\to \mathbb R$. 



