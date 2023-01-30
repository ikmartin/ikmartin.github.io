+++
title = "Week 2: Local Properties (DRAFT)"
hascode = true
description = "Week 2 of toric varieties learning seminar"
tags = ["toric-geometry,algebraic-geometry"]
+++

# Week 2: Local Properties of Toric Varieties (DRAFT)

\toc

---
These notes correspond to the second week of the toric geometry learning seminar, presented by Abhishek Koparde.

## Distinguished points in $X_\sigma$
Let's start with a lemma.

@@thm-box
**Lemma.** There exists a bijective correspondence
$$\big\{~\text{closed points of } X_\sigma~\big\} \leftrightarrow \big\{~\text{semi group homomorphisms } S_\sigma \to \bC~\big\}.$$
@@
@@prf-box **Proof:** By definition, each closed point of $X_\sigma$ is a morphism $\varphi:\Spec\bC \to \Spec \bC[S_\sigma]$ and each of these corresponds to a map of rings $\varphi_*:\Spec\bC[S_\sigma] \to \bC$. Given such a ring map, we obtain a semigroup homomorphism $\psi:S_\sigma \to \bC$ by sending $\psi(s) = \varphi(x^s)$.

Conversely, given a semigroup homomorphism $\psi:S_\sigma \to \bC$, we obtain a ring homomorphism $$\varphi_*:\bC[S_\sigma] \to \bC$$ by defining $\varphi_*(x^s) = \psi(s)$ for each $s \in S_\sigma$ and extending linearly. Note that in each case we take $\bC$ to be a semigroup with respect to multiplication, NOT addition. $\hspace{19.5em}\square$
@@

For each cone in a toric variety there is a particular closed point in which we'll be interested. Consider the semigroup morphism $\varphi_\sigma: S_\sigma \to \bC$ defined
$$
\varphi_\sigma(m) =
\begin{cases}
1 & \text{if } ~m\in \sigma^\perp \\
0 & \text{else}
\end{cases},
$$

where $\sigma^\perp = \{m \in M ~\mid~ \langle m,u\rangle = 0 \text{ for all } u \in \sigma\}$.
