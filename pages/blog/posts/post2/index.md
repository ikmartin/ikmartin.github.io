+++
title = "Associating cones to logarithmic stacks"
hascode = true
date = Date(2022, 11, 12)
rss = "Detailed description of section 2.1 in [Decomposition of Degenerate Gromov-Witten Invariants](https://arxiv.org/pdf/1709.09864.pdf). Goal is to understand how one can attach combinatorial structure (strictly rational polyhedral cones) to logarithmic schemes."

tags = ["tropical-geometry", "algebraic-geometry", "log-geometry"]
+++

# Associating cones to logarithmic stacks

\toc

---

Toric varieties are quite nice. They make blowups, class group and many other things exceedingly simple and concrete. Much of their niceties emerge from the combinatorial structure whence they are wrought, and likewise, attempts at generalizing the setup attach combinatorial objects to the relevant geometry. In this little blog post, I'll be trying to understand and expound upon section 2.1 in [Decomposition of Degenerate Gromov-Witten Invariants](https://arxiv.org/pdf/1709.09864.pdf), in which cone complexes are associated to logarithmic stacks.


*Required background*: some toric and log geometry.

*Notation*: $N = \bZ^n$ is a lattice, $M = \Hom_{\text{Gp}}(N,\bZ)\cong \bZ^n$ is the cocharacter lattice and we set $N_\bR = N\otimes_\bZ \bR \cong \bR^n$ and $M_\bR = M\otimes_\bZ \bR \cong \BR^n$.

---

## Category of Cones

Let us recall the basic combinatorial setup of toric geometry. There are a few different equivalent characterizations of toric varieties, but the most interesting formulation is that of _normal, separated toric varieties_ as these correspond uniquely to combinatorial objects known as _fans_. This correspondence goes deeper than a mere bijection of sets, however. Just as varieties are built from gluing affine varieties, so too are fans built from "gluing" simpler combinatorial objects known as _cones_, and these objects correspond in a neat way.

The category of cones is denoted $\Cones$. The objects of $\Cones$ are pairs $\sigma = (\sigma_{\bR},N)$ where $N \cong \bZ^n$ is a lattice and $\sigma_\bR \subseteq N_\bR = N\otimes_\bR \bR$ is a top-dimensional strictly convex rational polyhedral cone. Here are some definitions to shed some light on these adjectives:

- **cone**: a cone $\sigma_\bR$ given by $v_1,...,v_m \in N_\bR$, where
  \begin{align*}

  \cone(v_1,...,v_m) = \left\{\sum_{i = 1}^m c_i v_i ~:~ c_i \in \bR\_{\geq 0}\right\}.

  \end{align*}

* **top dimensional**: has the same dimension as the ambient topological space
* dimension of cone: $\dim(\sigma_\bR) = \dim(\sigma_\bR + (-\sigma_\bR)) = \dim(\vspan(\sigma_\bR))$, i.e. the dimension of the vector space spanned by the cone
* **strictly convex**: doesn't contain a linear subspace of $N_\bR$, i.e. no lines
* **rational**: the coordinates of the vectors which generate $\sigma_\bR$ all lie in $N_\bR$.

  Why do we require "*strictly* convex" rather than "convex"? Recall that the typical way one builds an affine toric variety is by first writing down a cone before dualizing and taking Spec:
  \begin{align*}
    \sigma_\bR \subset N_\bR ~\xrightarrow{\text{dualize}} ~\sigma^\vee \subseteq M_\bR ~\xrightarrow{\text{obtain ring}}~ \bC[\sigma^\vee \cap M] ~\xrightarrow{\text{take Spec}}~ X_\sigma = \Spec(\bC[\sigma^\vee \cap M]).
  \end{align*}
  
  Here, the dual cone $\sigma_\bR^\vee$ is the subset of $M_\bR$ consisting of cocharacters $m \in \Hom(N_\bR,\bR)$ which are strictly nonnegative on $\sigma_\bR$. Taking the dual is easy if done graphically: draw all the vectors orthogonal to one of the $v_i$ comprising $\sigma_\bR$ and check if it is nonnegative on the other $v_j$. It looks something like this:

  ![strictly convex rational polyhedral cone](/pages/blog/posts/post2/fig1.png)

  However, if the original cone is not strictly convex, the dual cone is no longer top dimensional:

  ![non-strictly convex rational polyhedral cone](/pages/blog/posts/post2/fig2.png)

  @@colbox-blue
    A **morphism of cones** $\varphi:\sigma_1\to \sigma_2$ is a homomorphism $\varphi:N_1\to N_2$ which takes $\sigma_{1\bR}$ to $\sigma_{2\bR}$. We call this a **face morphism** if $\sigma_{1\bR}$ is identified with a face of $\sigma_{2\bR}$ and $N_1$ is with a saturated sublattice of $N_2$, i.e. $n\cdot v \in \varphi(N_1)$ implies $v \in \varphi(N_1)$.
  @@

  *Fans* are collections of cones residing in the same ambient $N_\bR$ which satisfy some additional compatibility conditions, and they are the object that yields a correspondence between toric geometry and polyhedral geometry (at least if you consider only normal separated toric varieties). However, the category of cones doesn't itself admit colimits, which means that if you want to, say, glue cones together along faces to generalize the idea of a fan, you've got to enlarge your category.

## Cone and Polyhedra Complexes

### Cone complexes

*Cone complexes* are the first way one might try to enlarge $\Cones$. Here's the definition given in [ACP15]: 
@@colbox-blue
A **rational cone complex with integral structure** is a topological space $\Sigma$ together with a finite collection of closed subspaces $V_1,...,V_n$ together with identifications/homeomorphisms from each $V_i$ to a rational cone with integral structure $\sigma_i$ such that the intersection of two cones is a union of faces of each.
@@

In other words, it is the colimit of a poset in $\Cones$ in which each morphism is an isomorphism onto proper faces. The paper [Pay09, Section 2](https://arxiv.org/pdf/math/0605537.pdf) is a good reference for further details.

A *morphism* of cone complexes $f:\Sigma\to \Sigma'$ of cone complexes is a continuous map of topological spaces such that for each cone $\sigma \subseteq \Sigma$ there is a cone $\sigma' \subset \Sigma'$ so that $f|_\sigma$ factors through a morphism of cones $\sigma\to \sigma'$.

### Generalized cone complexes
A still **more** general "fan" is called a generalized cone complex. We replace "poset" in the definition of a cone complex with "arbitrary finite diagram" and "isomorphism onto proper faces" with "face map".

@@colbox-blue
  A **generalized cone complex** $\Sigma$ is the colimit of an arbitrary finite diagram in $\Cones$ where all maps are face maps. We denote by $|\Sigma|$ the underlying topological space corresponding to $\Sigma$. A **morphism** $f:\Sigma\to \Sigma'$ of generalized cone complexes is a continuous map $f:|\Sigma|\to |\Sigma'|$ such that for each $\sigma_\bR \in \Sigma$ the induced map $\sigma \to |\Sigma'|$ factors through a morphism $\sigma \to \sigma' \in \Sigma$.
@@

Two generalized cone complexes can be isomorphic and yet have different presentations.


## References

- [[ACP15]](https://arxiv.org/pdf/1212.0373.pdf)

- "Punctured Logarithmic Maps", Abramovich, Chen, Gross, Siebert. [[arXiv:2009.07720]](https://arxiv.org/pdf/2009.07720.pdf)

- [[Pay09, Section 2]](https://arxiv.org/pdf/math/0605537.pdf)
