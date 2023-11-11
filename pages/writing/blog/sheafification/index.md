+++
title = "Thoughts on Sheafification"
hascode = true
description = "Sheafification felt opaque to me when I first saw it, but it really isn't"
tags = ["algebraic-geometry", "sheaves"]
date = "2023-09-13"
published = true
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
  \thmtitle{Example 1}{(Violating Gluing)} Let $X = S^1$, and pick two distinct points $p \neq q \in S^1$. For any $U\subseteq S^1$ define $\mathcal F(U)$ to be all continuous functions $f:U\to \mathbb R$ such that $f(p) = f(q)$. Whenever $U$ includes $p$ but not $q$, this equality condition disappears and $\mathcal F(U)$ is the set of *all* continuous functions on $U$. Therefore if $U$ is a neighborhood of $p$ which avoids $q$ and $V$ a neighborhood of $q$ which avoids $p$, then two sections $f\in \mathcal F(U)$ and $g\in \mathcal F(V)$ only glue if they agree on $U\cap V$ and if $f(p) = g(q)$. Sheafification of $\mathcal F$ adds in all these extra sections, and thus the sheafification of $\mathcal F$ is the sheaf of continuous functions on $S^1$.
@@

*Takeaway: The property $f(p) = f(q)$ is not a local property, hence it is removed.*
@@revindentparagraph
  \thmtitle{Example 2}{(Violating Gluing)} Let $X = \mathbb C$ and define $\mathcal F(U)$ to be the collection of all polynomials bounded on $U$. If we additionally define $\mathcal F(\emptyset) = 0$ (see the Appendix) then $\mathcal F$ is a presheaf. As long as $U$ itself is bounded and nonempty, $\mathcal F(U) = \mathbb C[z]$, but Louiville's theorem tells us that the only bounded holomorphic functions on all of $\mathbb C$ are constant. In particular, if $D_r$ is the open disk of radius $r$ centered at $0$, then $f(z) = z$ is bounded on $D_r$, but there is no section $g \in \mathcal F(\mathbb C) = \mathbb C$ such that $g|_{D_r}(z) = f(z)$. Sheafification applied to $\mathcal F$ therefore adds in the extra functions; it just expands $\mathcal F(U)$ so that it too is $\mathbb C[z]$. The sheafification of $\mathcal F$ is therefore the constant sheaf associated to $\mathbb C[z]$.
@@

*Takeaway: A function can be simultaneously be bounded locally and unbounded globally. Hence the 'bounded' condition is removed.*

Examples of locality violation feel less natural to me because it's hard to construct them by imposing conditions on sets of functions. After all, if two functions are equal in every neighborhood of a space, then they're equal everywhere. It feels better to think about "equivalence", in my opinion. I can easily imagine two things which are "similar locally" but are not similar globally. Here's an example utilizing the boundedness example from earlier.

@@revindentblock
\thmtitle{Example 3}{(Violating Locality)} Again let $X = \mathbb C$, let $\mathcal F$ be the sheaf of holomorphic functions and let $\mathbb G$ be the presheaf of bounded holomorphic functions. Now define a presheaf $\mathcal H(U) = \mathcal F(U)/\mathcal G(U)$. At any $x\in X$ we get $\mathcal H_x = 0$, since any holomorphic function defined at $x$ is bounded in a suitably small neighborhood of $x$. However, functions like $f(z) = z$ are not in the class of zero in $\mathcal H(X)$, since they are not bounded globally. Contrast these two sets:
- $\mathcal H_x = \{0\}$ for reasons described above
- $\mathcal H(X) = \{\text{entire functions}\}/\mathbb C$, since the only bounded functions on $X$ are the constant functions.

The set $\mathcal H(U)$ is kind of like "unbounded functions on $U$ up to boundedness". Two functions $f$ and $g$ can both be bounded on a small set $U$, but for a strictly larger set $f$ might become unbounded while $g$ remains bounded. The sheafification of $\mathcal H$ throws away all sections for which local equivalence doesn't imply global equivalence. Since all holomorphic functions are equivalent to a bounded function on a sufficiently small set, this is just the constant zero sheaf.

*Takeaway: Locally bounded doesn't imply globally bounded for all sections, so all sections which are only locally bounded are thrown out.*
@@
Now let's look at some more general examples that show up immediately after you define sheafification. These sheafification examples are imperative to understand, since we use the sections of these sheaves *all the time*. If you fall back on the universal property of sheafification in these cases to avoid thinking about sections, then you're robbing yourself of valuable intuition and insight.
\fancyhr{gradient}{Kernel, Image and Cokernel Shaves}
Say we have a map $\varphi:\mathcal F\to \mathcal G$ of sheaves on a topological space $X$. We can immediately define kernel, image and cokernel presheaves on $X$:
- $\ker^p \varphi (U) = \ker(\varphi(U): \mathcal F(U)\to \mathcal G(U))\subseteq \mathcal F(U)$
- $\im^p \varphi (U) = \im(\varphi(U): \mathcal F(U)\to \mathcal G(U))\subseteq \mathcal G(U)$
- $\coker^p \varphi(U) = \coker(\varphi(U): \mathcal F(U)\to \mathcal G(U))$

These are presheaves, but are they sheaves? Fix $U\subseteq X$ and a cover $\{U_i\}$ of $U$.

#### The kernel presheaf is a sheaf

@@revindentparagraph *Locality:* Everything is happening in $\mathcal F(U)$, so this is easy. Given a section $s\in \ker^p\varphi(U)$ whose restriction $s|_{U_i} = 0$ is zero for all $i$, we automatically have that $s = 0$ on $U$ since  $s|_{U_i} \in \mathcal F(U_i)$, $s\in \mathcal F(U)$ and $\mathcal F$ is a sheaf.
@@

@@revindentblock *Gluing:* Given $s_i \in \mathcal \ker^p\varphi(U_i)$ so that $s_i|_{U_i\cap U_j} = s_j|_{U_i\cap U_j}$, we want to find a section $s\in \ker^p\varphi(U)$ whose restriction to $U_i$ recovers $s_i$. Such a section certainly exists in $\mathcal F(U)$ because $\mathcal F$ is a sheaf, but is this in the kernel of $\varphi$? Yes, it is -- we need to move over to $\mathcal G$ to see it. The map $\varphi$ commutes with restrictions, so $$\varphi(s)|_{U_i} = \varphi(s|_{U_i}) = \varphi(s_i) = 0$$ in $\mathcal G(U_i)$ by the assumption that $s_i\in \ker^p\varphi(U_i) = \ker(\varphi(U_i))$. But $\mathcal G$ is also a sheaf, hence satisfies locality and thus $\varphi(s) = 0$ in $\mathcal G(U)$. This implies $s\in \ker^p\varphi(U)$.
@@

Therefore $\ker^p\varphi$ is indeed a sheaf, so we remove the $p$ and define $\ker\varphi := \ker^p\varphi$.

#### The image presheaf fails gluing

We're not so lucky in the case of the image presheaf. It *does* satisfy locality:

@@revindentparagraph *Locality:* Take $s\in \im^p\varphi(U)$ whose restriction to each $U_i$ is zero. By virtue of being a section of $\mathcal G(U)$, this immediately implies $s = 0$ because $\mathcal G$ is a sheaf.
@@
But notice what goes wrong when we try to glue:
@@revindentparagraph *Gluing:* Given a collection of $s_i \in \im^p\varphi(U_i)$ which agree on overlaps, we want a section $s \in\im^p\varphi(U)$ which restricts to $s_i$ at each $U_i$. Again, because $\mathcal G$ is a sheaf, there is a unique section of $\mathcal G(U)$ which satisfies this. However, unless $\varphi(U)$ is surjective, we can't guarantee that this $s$ is in $\im^p\varphi(U)$. Thus $\im^p\varphi$ isn't a sheaf *unless* $\varphi(U)$ is surjective for each $U$.
@@

A sheaf which satisfies locality but not gluing is called a **separated presheaf**. To obtain an image sheaf, we simply sheafify: $\im\varphi := (\im^p\varphi)^\sim$.

All we've done is add the missing sections from $\mathcal G(U)$ into $\im^p\varphi(U)$, so $\im\varphi$ is most definitely still a subsheaf of $\mathcal G$.

#### The cokernel presheaf fails locality

If we look back at the bounded holomorphic sections examples, you'll notice that the failure of locality in Example 3 was actually due to the failure of gluing in Example 2. This is a more general fact; if we take the quotient of a presheaf (or sheaf) by a presheaf which doesn't have the gluing property, then the resulting quotient presheaf won't have the locality property. To see what I mean, let's look at why locality fails for the cokernel presheaf:

@@revindentparagraph *Locality:* Same setup as always, we've got a $s\in \coker^p\varphi(U) = \mathcal G(U)/\im(\varphi(U))$ whose restrictions are all zero. This means $s|_{U_i}$ is contained in $\im(\varphi(U_i))$, but if we wish to conclude $s = 0$ too, we'd need $s \in \im(\varphi(U))$. This doesn't happen in general, exactly because the image presheaf doesn't glue!
@@
The cokernel doesn't actually satisfy gluing either.
@@revindentblock *Gluing:* Standard setup by now: $s_i \in \coker^p\varphi(U_i)$ are sections which agree on intersections $U_i\cap U_j$. Each $s_i$ is represented by some 
@@

##
