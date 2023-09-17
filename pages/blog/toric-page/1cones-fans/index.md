+++
title = "Week 1: Cones, fans and toric varieties (DRAFT)"
hascode = true
description = "Notes covering Fulton chapter 1"
tags = ["toric-geometry", "polyhedral-geometry"]
date = "2023-01-31"
+++

# Cones, fans and toric varieties

\toc

---

These notes correspond to the first meeting of the spring 2023 toric geometry learning seminar at UT Austin. For more information on the topics found here, please reference Fulton's _An Introduction to Toric Varieties_.

## Definition of Toric Variety

Recall from the primer that $(C^\times)^n = \Spec \bC[x_1,...,x_n]_{x_1x_2...x_n}$ is called the _algebraic torus_. Qualitatively, toric varieties are varieties over $\bC$ which 1. contain a copy of $(\bC^\times)^n$ and 2. whose geometry is largely determined by the torus. Here is a definition:

@@defn-box
**Definition:** A _toric variety_ is a variety $X$ together with an open dense subset $T \subseteq X$ isomorphic to $(\bC^\times)^n$ for some $n$ such that the natural action $T\times T\to T$ extends to an action $T\times X\to X$ of $T$ on $X$.
@@

Some authors, including Fulton, require that toric varieties be _normal_. This is because the category of normal toric varieties is equivalent to the category of rational polyhedral fans, and the study of toric varieties is really about moving between these two categories. By omitting the _normal_ hypothesis we get a slightly weaker correspondence, discussed later.

@@indent-block
**Example 1:** $(\bC^\times)^n$ is of course itself an affine toric variety. The natural torus action is simply coordinate wise multiplication and the corresponding ring map is given by _comultiplication_:
$$T\times X\to X\hspace{1em};\hspace{1em}(t_1,...,t_n)\cdot (s_1,...,s_n)\mapsto (t_1s_1,...,t_ns_n)$$
$$\bC[t_1^{\pm},...,t_n^{\pm}] \to \bC[y_1^{\pm},...,y_n^{\pm}]\otimes_{\bC}\bC[y_1^{\pm},...,y_n^{\pm}]\hspace{1em};\hspace{1em}t_i \mapsto x_i \otimes y_i$$

**Example 2:** $\bC^n$ is an affine toric variety, where the torus action $T\times X\to X$ is again given by pointwise multiplication on coordinates.

**Example 3:** $\bP^n_{\bC}$ is a toric variety. The torus is $T = \left\{[z_0:...:z_n] ~\mid~ z_i\neq 0\right\}$ and the torus action is again given by pointwise multiplication, this time on homogeneous coordinates.
@@

It should be remarked that a toric variety is actually a package $$(X, T \xrightarrow{\text{open}}X, T\times X \to X)$$
consisting of the variety itself, a dominant open embedding of the torus and a specified torus action. There are typically _many_ choices of embeddings and actions for any given toric variety, so it is standard practice to fix a choice of each before doing anything else.

## Motivation for Fans

Fix $T \cong (\bC^\times)^n$ and consider the group of _cocharacters_ or _1-parameter subgroups_:$$N = \Hom_{\text{Grp}}(\bC^\times, T).$$ It turns out that $N \cong \bZ^n$, as proved in Humphrey's _Linear Algebraic Groups_ in section 16.2 for instance. Given $u = (u_1,...,u_n) \in \bZ^n = N$ the corresponding 1-parameter subgroup is

$$\lambda_u:\bC^\times\to T, \hspace{1em} t \mapsto (t^{u_1},...,t^{u_{n}}).$$

If we now take a toric variety $X$, we can consider the extension of $\lambda_u$ to $X$ given by composing with the torus embedding:
$$\bC^\times_t \xrightarrow{\lambda_u} T \hookrightarrow X$$
where here the subscript on $\bC^\times_t$ is simply there to emphasize that we have chosen a coordinate $t$ on $\bC^\times$ with respect to which $\lambda_u$ is defined. If we now consider extending $\lambda_u$ to $\bC$ we can ask: what is the limit as $t\to 0$?

@@indent-block
**Example:** Suppose $X = \bP^2_{z_0,z_1,z_2}$ and choose $u = (a,b) \in \bZ^2$. We have several different cases to consider:

- If $u_0,u_1 > 0$ then $[t^{u_0}:t^{u_1}:1] \xrightarrow{t\to 0} [0:0:1]$.
- If $u_0 > u_1, u_1 < 0$ then $[t^{u_0}:t^{u_1}:1] = [t^{u_0 - u_1}:1:t^{-u_1}]\xrightarrow{t\to 0} [0:1:0]$
- If $u_0 < u_1, u_0 < 0$ then $[t^{u_0}:t^{u_1}:1] = [1:t^{u_1 - u_0}:t^{-u_0}]\xrightarrow{t\to 0} [1:0:0]$
- If $u_0 > u_1, u_1 = 0$ then $[t^{u_0}:t^{u_1}:1] = [t^{u_0}:1:1] \xrightarrow{t\to 0} [0:1:1]$
- If $u_0 = 0, u_1 > u_0$ then $[t^{u_0}:t^{u_1}:1] = [1:t^{u_1}:1] \xrightarrow{t\to 0} [1:0:1]$
- If $0 > u_0 = u_1$ then $[t^{u_0}:t^{u_1}:1] = [t^{u_0 - u_1}:t^{u_1 - u_1}:t^{-u_1}] \xrightarrow{t\to 0} [1:1:0]$
- If $u_0 = u_1 = 0$ then $[t^{u_0}:t^{u_1}:1] = [1:1:1]$.

If we partition $N = \bZ^2$ into regions where choices of $u$ give the same limit point, then we get a _fan_:

![The fan of $\bP^2_{\bC}$](/pages/blog/toric-page/1cones-fans/fan-P2.png)

We can dually write this object as a convex polytope:
![Convex polytope of fan of P2](/pages/blog/toric-page/1cones-fans/triangle-P2.png)

Now consider the torus orbit of each of these points. We write down three of them:

- $T\cdot [0:0:1] = \{[0:0:z_0] \mid z_0 \neq 0\} = [0:0:1]$,
- $T \cdot [1:0:1] = \{[z_0:0:z_2] \mid z_0, z_2 \neq 0\}$,
- $T \cdot [1:1:1] = \{[z_0:z_1:z_2] \mid z_0, z_1, z_2 \neq 0\}$ etc.

In particular, the torus orbits of these seven points do not intersect and their union covers $\bP^2_{\bC}$. The fan tells us how the torus action partitions the underlying toric variety!

There is one other thing I'd like to point out here. Notice how there are three "2-dimensional" components of the fan, three "1-dimensional" components and one "0-dimensional" component namely the origin. These components are called _cones_, and their dimension relates to the dimension of their torus orbits in the following way. If $\sigma$ is a $d$-dimensional cone with a corresponding point $P_{\sigma}$, then $T\cdot P_{\sigma}$ is a $\dim X - \dim \sigma$ subspace of $X$. In our case, the orbits of the points corresponding to the 2-dimensional cones are just points, the orbits of the 1-dimensional cones become copies of $\bP^1_{\bC}$ and the action of $T$ on the origin recovers the entire torus. This phenomenon will be explored further when we discuss the "orbit cone correspondence".
@@

## Rational Polyhedral Cones

I hope that you are now adequately convinced that fans connect in some interesting way to toric varieties. In this section, we'll cover the basics of the polyhedral geometry needed to understand this connection.

Fix a lattice $N \cong \bZ^n$ and let $N_{\bR} = N \otimes_{\bZ} \bR\cong \bR^n$. We first define polyhedral cones:
@@defn-box
**Definition:** A **convex polyhedral cone** in $N_{\bR}$ is a set
$$\sigma = \{a_1v_1+...+a_sv_s \in N_{\bR} ~\mid~ a_i \geq 0\}$$
generated by any finite set of vectors $v_1,...,v_s \in N_{\bR}$. Such vectors are called the _generators_ of $\sigma$, and we sometimes write $\text{span}_{\bR_{\geq 0}}(v_1,...,v_s)$ to denote $\sigma$. In addition, $\sigma$ is said to be

- _rational_ if each generator has integer coordinates, i.e. if $v_i \in N$ for all $1\leq i\leq s$
- _strictly convex_ if $\sigma$ does not contain a line
  The _dimension_ of $\sigma$ is denoted $\dim \sigma$ and is defined to be the dimension of $\bR \cdot \sigma = \sigma + (-\sigma)$ as a linear space over $\bR$.
  @@

Note that the word "polyhedra" refers to the finite generating set of $\sigma$: this assumption disallows cones which look like ice cream cones.

![a](./cones-noncones.png)

In the above image, only the left cone is polyhedral.

We also make frequent use of the dual lattice $M = \Hom_{\bZ}(N,\bZ)\cong \bZ^n$ and the dual vector space $M_\bR = M\otimes_\bZ \bR\cong \bR^n$. This is where the _dual cone_ lives:

@@defn-box
**Definition:** If $\sigma$ is a convex polyhedral cone in $N_\bR$, then the _dual cone_ is the set
\begin{align*}
\sigma^\vee := \left\{u \in M\_{\bR} ~\mid~ \langle u,v \rangle\geq 0 \text{ for all } v \in \sigma\right\}.
\end{align*}
@@

The following fact from the theory of convex sets is crucial:

@@fact-box
**Fact:** If $\sigma$ is a convex polyhedral cone and $v_0 \not\in \sigma$ then there is some $u_0 \in \sigma^\vee$ such that $\langle u_0,v_0 \rangle < 0$.
@@

From here we can immediately get the duality theorem.

@@thm-box
**Theorem (Duality Theorem):** If $\sigma$ is a convex polyhedral cone, then $(\sigma^\vee)^\vee = \sigma$.
@@

We now run through a few more basic definitions and facts regarding polyhedral cones.

@@defn-box
**Definition:** Let $\sigma$ be a polyhedral cone. A _face_ of $\sigma$ is the intersection of $\sigma$ with any supporting hyperplane:
$$\tau = \sigma \cap u^{\perp} = \{v \in \sigma ~\mid~ \langle u,v \rangle = 0\}$$ for some $u\in \sigma^\vee$.
@@

Any face $\tau$ of $\sigma$ is again a polyhedral cone. A cone $\sigma$ is a face of itself, as seen by taking $u = 0$ in the above definition, while every other face is referred to as a _proper_ face.

@@fact-box
**Fact:** Any intersection of faces is also a face.
@@
@@indent-block
_Proof:_ $$\bigcap (\sigma \cap u_i^{\perp}) = \sigma \cap \left(\sum u_i\right)^\perp.$$

~~~<div style="text-align:right"> ~~~ $\square$ ~~~</div> ~~~
@@
The final fact we will need is the following:
@@fact-box
**Fact:** If $\sigma$ is a rational convex polyhedral cone then $\sigma^\vee$ is a rational convex polyhedral cone.
@@

This is not difficult to prove; one can easily find a procedure by which to find generators for $\sigma^\vee$ given the generators of $\sigma$ and use this to prove both rationality and convexity. We refer the reader to page 12 of Fulton's book.

This gives us Gordan's lemma, which will be critical to our construction of toric varieties from cones.

@@thm-box
**Proposition (Gordon's Lemma):** If $\sigma$ is a rational convex polyhedral cone, then $S_\sigma = \sigma^\vee \cap M$ is a finitely generated semigroup.
@@
