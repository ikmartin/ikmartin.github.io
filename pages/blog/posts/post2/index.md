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

*Background: some toric and log geometry.*

Toric varieties are quite nice. They make blowups, class group and many other things exceedingly simple and concrete. Much of their niceties emerge from the combinatorial structure whence they are wrought, and likewise, attempts at generalizing the setup attach combinatorial objects to the relevant geometry. In this little blog post, I'll be trying to understand and expound upon section 2.1 in [Decomposition of Degenerate Gromov-Witten Invariants](https://arxiv.org/pdf/1709.09864.pdf), in which cone complexes are associated to logarithmic stacks.

*Notation*: $N = \bZ^n$ is a lattice, $M = \Hom_{\text{Gp}}(N,\bZ)\cong \bZ^n$ is the cocharacter lattice and we set $N_\bR = N\otimes_\bZ \bR \cong \bR^n$ and $M_\bR = M\otimes_\bZ \bR \cong \bR^n$.

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
* **rational**: the coordinates of the vectors which generate $\sigma_\bR$ all lie in $N_\BR$.

  Why do we require "*strictly* convex" rather than "convex"? Recall that the typical way one builds an affine toric variety is by first writing down a cone before dualizing and taking Spec:
  \begin{align*}
    \sigma_\bR \subset N_\bR ~\xrightarrow{\text{dualize}} ~\sigma^\vee \subseteq M_\bR ~\xrightarrow{\text{obtain ring}}~ \bC[\sigma^\vee \cap M] ~\xrightarrow{\text{take Spec}}~ X_\sigma = \Spec(\bC[\sigma^\vee \cap M]).
  \end{align*}
  
  Here, the dual cone $\sigma_\bR^\vee$ is the subset of $M_\bR$ consisting of cocharacters $m \in \Hom(N_\bR,\bR)$ which are strictly nonnegative on $\sigma_\bR$. Taking the dual has a pleasing graphical interpretation: draw all the vectors orthogonal to one of the $v_i$ comprising $\sigma_\bR$ and check if it is nonnegative on the other $v_j$. It looks something like this:

  ![strictly convex rational polyhedral cone](/pages/blog/posts/post2/fig1.png)

  However, if the original cone is not strictly convex, the dual cone is no longer top dimensional:

  ![non-strictly convex rational polyhedral cone](/pages/blog/posts/post2/fig2.png)




