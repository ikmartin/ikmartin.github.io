+++
title = "Thoughts on Sheafification"
hascode = true
description = "Sheafification felt opaque to me when I first saw it, but it really isn't"
tags = ["algebraic-geometry", "sheaves"]
date = "2023-09-13"
+++

@def mintoclevel=2
@def mastic level=3

# Thoughts on Sheafification
\author

Sheafification felt opaque to me when I first learned it from Hartshorne, I'll admit. I reviewed it recently to recover from summer rustiness and wanted to make the argument that it is, in fact, actually pretty straightforward.

There are two additional axioms a presheaf $\mathcal F$ on $X$ must satisfy to be a sheaf:

1. (*Locality*) &nbsp;Let $U$ be covered by $U_i$. If $s,t \in \mathcal F(U)$ satisfy $s|_{U_i} = t|_{U_i}$ for all $i$, then $s = t$.
2. (*Gluing*)  &nbsp;&nbsp; Again let $U$ be covered by $U_i$. If there exist sections $s_i \in \mathcal F(U_i)$ such that $s_i|_{U_i\cap U_j} = s_j|_{U_i \cap U_j}$ then there exists some $s \in \math cal F(U)$ such that $s|_{U_i} = s_i$.

Thus, there are two ways a sheaf can fail to be a presheaf: it can violate locality by having *extra* sections which are equal locally but not globally or it can violate gluing by having *too few* sections to glue stuff together. Sheafification therefore consists of removing all sections which violate locality and adding extra sections to ensure gluing is possible. There's an excellent mathoverflow post this: [here's a link](https://mathoverflow.net/questions/45212/how-should-one-think-about-sheafification-and-the-difference-between-a-sheaf-and). It also motivated this entry.

\fancyhr{gradient}{Examples}

Examples of presheaves which violate gluing are pretty natural; lots of properties are easy or even trivial to satisfy locally but are much harder to satisfy globally.

@@revindentparagraph
  \thmtitle{Example 1}{(Violating Gluing)} Let $X = \mathbb C$ and define $\mathcal F(U)$ to be the collection of all polynomials bounded on $U$. If we additionally define $\mathcal F(\emptyset) = 0$ (see the Appendix) then $\mathcal F$ is a presheaf. As long as $U$ itself is bounded and nonempty, $\mathcal F(U) = \mathbb C[z]$, but Louiville's theorem tells us that the only bounded holomorphic functions on all of $\mathbb C$ are constant. In particular, if $D_r$ is the open disk of radius $r$ centered at $0$, then $f(z) = z$ is bounded on $D_r$, but there is no section $g \in \mathcal F(\mathbb C) = \mathbb C$ such that $g|_{D_r}(z) = f(z)$. Sheafification applied to $\mathcal F$ therefore adds in the extra functions; it just expands $\mathcal F(U)$ so that it too is $\mathbb C[z]$. The sheafification of $\mathcal F$ is therefore the constant sheaf associated to $\mathbb C[z]$.
@@

*Takeaway: A function can be simultaneously be bounded locally and unbounded globally. Hence the 'bounded' condition is removed.*

@@revindentparagraph
  \thmtitle{Example 2}{(Violating Gluing)} Let $X = S^1$, and pick two distinct points $p \neq q \in S^1$. For any $U\subseteq S^1$ define $\mathcal F(U)$ to be all continuous functions $f:U\to \mathbb R$ such that $f(p) = f(q)$. Whenever $U$ includes $p$ but not $q$, this equality condition disappears and $\mathcal F(U)$ is the set of *all* continuous functions on $U$. Therefore if $U$ is a neighborhood of $p$ which avoids $q$ and $V$ a neighborhood of $q$ which avoids $p$, then two sections $f\in \mathcal F(U)$ and $g\in \mathcal F(V)$ only glue if they agree on $U\cap V$ and if $f(p) = g(q)$. Sheafification of $\mathcal F$ adds in all these extra sections, and thus the sheafification of $\mathcal F$ is the sheaf of continuous functions on $S^1$.
@@

*Takeaway: The property $f(p) = f(q)$ is not a local property, hence it is removed.*

Examples of locality violation feel less natural to me because it's hard to construct them by imposing conditions on sets of functions. After all, if two functions are equal in every neighborhood of a space, then they're equal everywhere. It feels better to think about "equivalence", in my opinion. I can easily imagine two things which are "similar locally" but are not similar globally. Here's an example utilizing the boundedness example from earlier.

@@revindentblock
\thmtitle{Example 3}{(Violating Locality)} Again let $X = \mathbb C$, let $\mathcal F$ be the sheaf of holomorphic functions and let $\mathbb G$ be the presheaf of bounded holomorphic functions. Now define a presheaf $\mathcal H(U) = \mathcal F(U)/\mathcal G(U)$. At any $x\in X$ we get $\mathcal H_x = 0$, since any holomorphic function defined at $x$ is bounded in a suitably small neighborhood of $x$. However, functions like $f(z) = z$ are not in the class of zero in $\mathcal H(X)$, since they are not bounded globally. Contrast these two sets:
- $\mathcal H_x = \{0\}$ for reasons described above
- $\mathcal H(X) = \{\text{entire functions}\}/\mathbb C$, since the only bounded functions on $X$ are the constant functions.

The set $\mathcal H(U)$ is kind of like "unbounded functions on $U$ up to boundedness". Two functions $f$ and $g$ can both be bounded on a small set $U$, but for a strictly larger set $f$ might become unbounded while $g$ remains bounded. The sheafification of $\mathcal H$ throws away all sections for which local equivalence doesn't imply global equivalence. Since all holomorphic functions are equivalent to a bounded function on a sufficiently small set, this is just the constant zero sheaf.

*Takeaway: Locally bounded doesn't imply globally bounded for all sections, so all sections which are only locally bounded are thrown out.*
@@
\fancyhr{gradient}{The Image Sheaf}

##
