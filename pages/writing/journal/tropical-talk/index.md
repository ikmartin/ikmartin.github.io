+++
title = "Tropical Geometry Notes for the Gross-Siebert Program Seminar"
hascode = true
description = "Notes for a talk given in the mirror symmetry seminar organized by Suraj Dash"
tags = ["tropical-geometry", "algebraic-geometry", "gross-siebert-program"]
date = "2023-09-17"
+++

@def mintoclevel=2
@def maxtoclevel=3

# Notes on Tropical Geometry for the Gross-Siebert Program Seminar

These notes accompany a talk I gave at the virtual Gross-Siebert Program Seminar, organized by Suraj Dash.

\toc

## Conventions and Reference List
- [*Tropical Geometry and Mirror Symmetry* by Mark Gross](https://www.math.utah.edu/~yplee/teaching/7800f15/Gross_Kansas_cropped.pdf). Chapter 1 of this book is the main reference.
- ["First Steps in Tropical Geometry" by Richter-Gerbert, Sturmfels, Theobald](https://arxiv.org/abs/math/0306366). Gross says chapter 1 of his book mostly follows this reference. I looked at it a few times while prepping these notes.
- [*Introduction to Tropical Geometry* by Maclagan and Sturmfels](https://bookstore.ams.org/gsm-161). Used to cross-reference the more opaque definitions in Gross's book. This is a little more down-to-earth and typically provides enlightening examples.

Note that we use $M \cong \mathbb Z^n$ and $N \cong \Hom(M, \bZ)$. This is the opposite of the convention I'm used to, but it's what Gross uses in his book. As always $M_\bR = M\otimes_\bZ \bR$ and $N_\bR = \Hom_\mathbb{Z}(M,\mathbb R)$.

## Parameterized Tropical Curves

We skip over the basics of tropical polynomials, tropical curves in $\bR^n$ and fans and go straight to section 1.3 of Gross's book, where we first encounter generalized tropical curves built from the data of *weighted graphs* and *marked graphs*. I gave a (bad) introduction to [cones and fans here](/pages/blog/toric-page/1cones-fans/), but the unfamiliar reader should either check out section 1.2 of Gross's book or look at Fulton's *Introduction to Toric Varieties*. Note that any tropical curve $V(f)$ locally looks like a fan around every vertex after translating to the origin.

### Balancing condition
We first need to discuss the *balancing condition*. Let $\Sigma \subset \bR^n$ be a one-dimensional rational fan; i.e. a fan comprised only of the origin and a collection of $s$ rays. Let $v_i$ be the first lattice point of the $i$th ray in $\Sigma$. We give $\Sigma$ the structure of a *weighted fan* by assigning a positive integer $m_i \in \mathbb Z$ to $v_i$, and we say that $\Sigma$ is *balanced* if
$$ \sum m_i v_i = 0.$$

Here's an example from Maclagan and Sturmfels page 111:

\figenv{images/balanced-rational-fan.png}{A balanced rational fan in $\mathbb R^2$.}{}

Before we generalize this, let's review some terminology.

- A **polyhedron** $P\subset \bR^n$ is the intersection of finitely many closed half-spaces.
- A **face** of a polyhedron $P$ is determined by a linear functional $\lambda \in \mathbb (\bR^n)^\vee$ like so. (Note that the codimension 1 faces of $P$ occur on the of a single supporting hyperplane, the codimension 2 faces occur on the intersection of two supporting hyperplanes, etc.) $$ \operatorname{face}_\lambda(P) = \{x \in P ~\mid~ \lambda(x) \leq \lambda(y) \text{ for all } y \in P\}.$$
- A **polyhedral complex** $\Sigma$ is a collection of polyhedra such that 
    - if $P\in \Sigma$ then every face of $P$ is also in $\Sigma$ and
    - if $P, Q\in \Sigma$ then $P\cap Q \in \Sigma$.
  The polyhedra of $\Sigma$ are called *cells*. Cells which aren't faces of any larger cell are called *facets*. Notice that all the facts need not have the same dimension, which is why...
- ...we say that $\Sigma$ is *pure of dimension $d$* if every facet of $\Sigma$ has the same dimension.
- The *affine span* of a polyhedron $P$ is the smallest affine subset of $\mathbb R^n$ which contains $P$. The *relative interior* of $P$ is the interior of $P$ inside its affine span.

There are two more definitions we need, included here for reference.

@@lineblock \thmtitle{Definition 1}{Normal Fan} Let $P\subset \mathbb R^n$ be a polyhedron. The *normal fan* of $P$ is the polyhedral fan $\mathcal N_P$ consisting of the cones $$\mathcal N_P(F) = \operatorname{cl}(\{w \in \mathbb (R^n)^\vee ~\mid~ \operatorname{face}_w(P) = F\}),$$ as $F$ varies over the faces of $P$.
@@

\break

\figenv{images/normal-fan.png}{A quadrilateral on the left with its normal fan on the right.}{width: 80%;}

@@lineblock \thmtitle{Definition 2}{Star of a Cell} Let $\Sigma$ be a polyhedral complex in $\mathbb R^n$ and let $\sigma$ be a cell in $\Sigma$. The **star** of $\sigma \in \Sigma$ is a fan in $\mathbb R^n$ denoted $\operatorname{star}_\Sigma(\sigma)$. Its cones are indexed by those cells $\tau \in \Sigma$ which contain $\sigma$ as a face. The cone of $\operatorname{star}_\Sigma(\sigma)$ which is indexed by $\tau$ is the subset $$ \overline{\tau} = \{\lambda(x - y) ~\mid~ \lambda\geq 0, x\in \tau, y\in \sigma\}.$$
@@

Definition 2 above is taken directly from Maclagan and Sturmfels. Note that they don't ask that polyhedral fans contain a zero-dimensional cone, so it's fine that $\overline{\sigma}$ is the minimal dimensional cone of $\operatorname{star}_\Sigma(\sigma)$.

\figenv{images/star-of-cell.jpg}{The star of a 1-dimensional cell of a polyhedral complex $\Sigma$.}{width: 100%;}

We can now extend the balancing condition to arbitrary fans.

@@lineblock \thmtitle{Definition 3}{Balancing Condition} Let $\Sigma$ be a rational fan in $\mathbb R^n$, pure of dimension $d$, and suppose we have a weighting function $m$ which assigns weights $m(\sigma) \in \mathbb N$ for all the maximal cones $\sigma$. Given $\tau \in \Sigma$ of dimension $d-1$, let $L$ be the linear space parallel to $\tau$. The abelian group $L_\mathbb{Z} = L\cap \mathbb Z^n$ is free of rank $d-1$ since $\tau$ is a rational cone, and then $N(\tau) = \mathbb Z^n/L_\mathbb Z \cong \mathbb Z^{n-d+1}$.

Now, for each maximal cone $\sigma$ with $\tau \subsetneq \sigma$, the set $(\sigma +L)/L$ is a one-dimensional cone in $N(\tau)\otimes_\mathbb{Z} \mathbb R$ -- it's just the projection of $\sigma$ onto $L$. Take $v_\sigma$ to be the first lattice point on this ray. Then $\Sigma$ is *balanced at $\tau$* if $$\sum m(\sigma) v_\sigma = 0,$$iterating over all $\sigma$ containing $\tau$. We say that the fan $\Sigma$ is *balanced* if it's balanced at all codimension ($d-1$)-cones.

If we instead have a rational polyhedral complex $\Sigma$ of pure dimension $d$ with weights $m(\sigma)\in \mathbb N$ on all maximal cells, then for each $\tau \in \Sigma$ the fan $\operatorname{star}_{\Sigma}(\tau)$ inherits the weighting function $m$. We therefore say that $\Sigma$ is balanced if $\operatorname{star}_{\Sigma}(\tau)$ is balanced for all $(d-1)$-dimensional cells $\tau$.
@@

### Tropical curves from graphs

We can use the balancing condition to define tropical curves in a more abstract setting than in $\mathbb R^n$. Let $\overline{\Gamma}$ be a connected graph with no bivalent vertices (i.e. no vertices with exactly two connected edges). We denote by $\overline{\Gamma}^{[0]}$ and $\overline{\Gamma}^{[1]}$ the set of vertices and edges respectively of $\overline{\Gamma}$. It's convenient to freely switch back and forth between thinking of $\overline{\Gamma}$ as the purely combinatorial object defined by $\overline{\Gamma}^{[0]}$ and $\overline{\Gamma}^{[1]}$ and as a topological space given a union of closed line segments.

Denote by $\overline{\Gamma}^{[0]}_\infty$ the set of univalent vertices of $\overline{\Gamma}$, and write $$\Gamma = \overline{\Gamma} \setminus \overline{\Gamma}^{[0]}_\infty.$$
Thinking of $\Gamma$ and $\overline{\Gamma}$ as topological spaces, we see that $\Gamma$ is a "graph with some non-compact edges", i.e. "legs" or "half-edges" and $\overline{\Gamma}$ is its closure. This explains the notation, especially if we consider the univalent vertices of $\overline{\Gamma}$ to occur at infinity. 

Here are some rapid-fire definitions.
- We let $\Gamma^{[1]}_\infty$ denote the non-compact edges of $\Gamma$.
- A *flag* of $\Gamma$ is a vertex/edge pair $(V,E)\in\Gamma^{[0]}\times \Gamma^{[1]}$ with $V \in E$.
- A *weight function* is a map assigning positive integer weights to the edges of $\Gamma$: $$w:\Gamma^{[1]} \to \mathbb N.$$
- A *marked graph* is a tuple $(\Gamma, x_1, ..., x_k)$ where $\Gamma$ is as above and $x_1,...,x_k$ are labels assigned to the non-compact edges with weight $0$, i.e. $\{E_{x_1},...,E_{x_k}\} \subseteq \Gamma^{[1]}_\infty$ is precisely the set of non-compact edges such that $w(E_{x_i}) = 0$.

And finally the actual definition to which we've been building.

@@lineblock \thmtitle{Definition 4}{Parameterized Tropical Curve} A *marked parameterized tropical curve* 
\begin{equation}
  h:(\Gamma, x_1,...,x_k)\to M_\bR
\end{equation}
is a continuous map $h$ satisfying the following two properties:
1. If $E\in \Gamma^{[1]}$ and $w(E) = 0$, then $h|_E$ is constant; otherwise, $h|_E$ is a proper embedding of $E$ into a line of rational slope in $M_\mathbb R$.
2. *The balancing condition*. Let $V\in \Gamma^{[0]}$ and let $E_1,...,E_\ell\in \Gamma^{[1]}_\infty$ be the edges adjacent to $V$. Let $m_i \in M$ be a primitive tangent vector to $h(E_i)$ pointing away from $h(V)$. Then
\begin{equation}
  \sum_{i = 1}^\ell w(E_i) m_i = 0.
\end{equation}
If $h:(\Gamma, x_1,...,x_n)\to M_\bR$ is a marked parameterized tropical curve, we write $h(x_i)$ for $h(E_{x_i})$. The *genus* of $h$ is $b_1(\Gamma)$.
@@

Here are some pictures justifying the idea that as long as $\overline{\Gamma}$ is not bivalent and the balancing condition is satisfied, then $\operatorname{img}(h)$ does indeed look like a tropical curve.

\figenv{images/no-bivalent.JPG}{Convexity is ruined when $\overline{\Gamma}$ is not bivalent.}{width: 100%}
\figenv{images/needs-to-be-weighted.JPG}{If $h$ can't be weighted to satisfy the balancing condition, then $\operatorname{img}(h)$ won't locally look like a rational polyhedral fan.}{width: 100%}
\figenv{images/looks-tropical.JPG}{If the hypotheses are satisfied then $\operatorname{img}$ looks like a tropical curve.}{width: 100%}

We call these *parameterized* tropical curves because the image $\operatorname{img}(h)$ of $h$ is a tropical curve in $M_\mathbb R$ and $h$ parameterizes each "edge" of the tropical curve according to condition (1) in the definition.

We say that two marked parameterized tropical curves $h:(\Gamma,x_1,...,x_k)\to M_\bR$ and $h':(\Gamma',x_1',...,x_k')\to M_\mathbb R$ are *equivalent* if there is a homeomorphism $\varphi:\Gamma \to \Gamma'$ with $\varphi(E_{x_i}) = E_{x_i'}$ and $h = h'\circ \varphi$. We define a *marked tropical curve* to be an equivalence class of parameterized marked tropical curves.
