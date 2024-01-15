+++
title = "Finite Fields: Existence and Galois Theory"
hascode = true
description = "A post about finite fields. Starts by proving the existence of finite fields and concludes by stating core results about their properties as Galois extensions."
tags = ["blog"]
date = "2023-12-24"
published = true
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{title}}

> {{description}}

\toc

---
I've found the basic theory of finite fields to be slippery. A month or two after I relearn it, I inevitably forget the order in which facts appear and are proven. I suspect this is partly because my main reference, Dummit and Foote, mixes results about finite fields in with broader topics of field and ring theory. If I was writing a textbook I'd do the same; but nonetheless, when you're drilling bookwork questions on finite fields specifically, it'd be nice to have all the facts in one place. This is my attempt to do just that.

My treatment isn't exhaustive, but it does cover the main points necessary to answer finite field questions on the UT Austin Algebra II prelim exam, I think.

**Note:** I haven't figured out a good way to achieve theorem numbering yet, which makes citing facts a little awkward. Instead, each theorem, lemma, proposition or corollary is cited as a link, and clicking said link will jump you to the point of the page where the cited fact first appears.

## Important Preliminary Results

Before we begin we'll need two basic facts.

\details{
    \prop{\label{prop_field_characteristic}Every field $K$ has characteristic $0$ or $p$ for some prime number $p$.}
}{
    \proof{The characteristic $n\in \mathbb Z$ of a field $K$ is the unique nonnegative generator of $\ker\varphi$ where $\varphi$ is the unique map $\varphi:\mathbb Z \to K$. This gives us an embedding $\mathbb Z/(n) \to K$. Since $K$ is a field, $\mathbb Z/(n)$ must be a domain. This only occurs if $(n)$ is a prime ideal, giving us the result.}
}
\break
The following is a trivial (but important) corollary:

\cor{\label{cor_finite_fields_have_prime_characteristic}Finite fields have prime characteristic.}

We now prove a vital criterion for the separability of a polynomial:
\details{
    \prop{\label{prob_separability_criterion}
        Let $K$ be a field. A polynomial $f \in K[x]$ is separable if and only if $(f,f') = 1$ where $f'$ is the formal derivative of $f$.
    }
}{
    \proof{Let $L$ be the splitting field of $f$ throughout. If $f$ is inseparable then it has a repeated root in $L$, and hence can be written
    \begin{align*}
        f(x) = (x - \alpha)^2g(x)
    \end{align*}
    for some $g\in L[x]$ and $\alpha \in L$. Then
    \begin{align*}
        f'(x) = 2(x-\alpha)g(x) + (x-\alpha)^2g'(x),
    \end{align*}
    which clearly has $0$ as a root. Thus $f'(x)$ and $f(x)$ share a common factor and $(f,f')\neq 1$ as an ideal in $L[x]$. Pulling back to $K[x]$ under the inclusion $K[x] \hookrightarrow L[x]$ demonstrates that $(f,f')\neq 1$ in $K[x]$ too.
    \break
    \break
    Suppose now that $(f, f') \neq 1$. This means that $f$ and $f'$ share a root $\alpha$ in $L$. Let $f(x) = (x-\alpha)h(x)$ be a factorization of $f$ in $L$. Taking the derivative, we see
    \begin{align*}
        f'(x) = h(x) - (x-\alpha)h'(x).
    \end{align*}
    Since $\alpha$ is a root of $f'(x)$ by assumption, it must be the case that $h$ is divisible by $(x-\alpha)$. This implies $f$ is divisible by $(x-\alpha)^2$, hence it has a repeated root and is not separable.
    }
}

## Construction of Finite Fields as Splitting Fields

Here we prove that finite fields exist and construct the field $\mathbb F_{p^n}$ of order $p^n$ as the splitting field of the polynomial $x^{p^n}-x$, where $p$ is the characteristic of the finite field and $n$ is some positive integer. We begin with two lemmas.
\details{
    \lem{\label{lem_order_of_finite_fields}If $K$ is a finite field of prime characteristic $p>0$, then $|K| = p^n$ for some positive integer $n$.}
}{
    \proof{
        Since $K$ has prime characteristic $p$, there is a unique inclusion $\mathbb F_p \hookrightarrow K$. Hence $K$ is a finite extension of $\mathbb F_p$, so $K$ is an $n$-dimensional vector space with basis $\mathbf b_1,...,\mathbf b_n$ over $\mathbb F_p$ where $[K:\mathbb F_p] = n$. Every element in $K$ can therefore be written uniquely as $a_1\mathbf b_1 + ... + a_n\mathbf b_n$ with $a_i \in \mathbb F_p$, giving us $p^n$ elements in $K$.
    }
}


\details{
    \lem{\label{lem_finite_field_polynomial_separable}If $K$ is a field of prime characteristic $p > 0$, then the polynomial $f(x) = x^{p^n} - x$ is separable.}
}{
    \proof{The derivative of $f$ is $f'(x) = p^{n}x^{p^n - 1} - 1 = -1$, so $(f,f') = 1$. By the Lemma above, $f$ is separable.}
}

From this Lemma we can immediately deduce the existence of finite fields.
\details{
    \prop{\label{prop_existence_of_finite_fields}*(Existence of Finite Fields).* &nbsp; Finite fields exist. Furthermore, if $K$ is a finite field, then it has prime characteristic $p$ for some $p>0$ and is the splitting field of $x^{p^n} - x$ over $\mathbb F_p$ where $n =  [K:\mathbb F_p]$.}
}{
\proof{
    We prove the existence of finite fields by showing that the roots of $f(x) = x^{p^n} - x$ form a field. With this in mind, let $K$ be the splitting field of $f$ over $\mathbb F_p$. By the above [Lemma](#lem_finite_field_polynomial_separable), $f$ is separable over $\mathbb F_p$ and hence has distint roots. Furthermore, $0$ and $1$ are roots of $f$, and if $\alpha$ and $\beta$ are any other roots of $f$, then $\alpha^{p^n} = \alpha$ and $\beta^{p^n} = \beta$ imply that $(\alpha\beta)^{p^n} = \alpha\beta$. This means
    \begin{align*}
        f(\alpha\beta) = (\alpha\beta)^{p^n} - \alpha\beta = 0,
    \end{align*}
    \begin{align*}
        $\alpha^{-1})^{p^n} = \alpha^{-1}$
    \end{align*}
    and by the freshman's dream,
    \begin{align*}
        f(\alpha + \beta) 
        &= (\alpha + \beta)^{p^n} - \alpha - \beta
        = \alpha^{p^n} - \alpha + \beta^{p^n} - \beta = 0.
    \end{align*}
    Thus the roots of $f$ form a field, and since the splitting field $K$ is the minimal field containing all roots of $f$, it is precisely the $p^n$ distinct roots of $f$.
    \break
    Now suppose that $K$ is a finite field. Then it must be of order $p^n$ by the above [Lemma](#lem_order_of_finite_fields). The group $K^\times$ is then of order $p^n-1$, meaning that for any nonzero element $\alpha \in K$, $\alpha^{p^n - 1} = 1$. This implies $\alpha^{p^n} = \alpha$ for any element in $K$, hence every element of $K$ is a root of $f(x) = x^{p^n} - x$. Since $f$ can have at most $p^n$ roots, $K$ contains all the roots of $f$ and is hence the splitting field of $f$.
    }
}

Since any two choices of a splitting field of a polynomial are isomorphic, any two finite fields of the same cardinality are isomorphic. This justifies the following remark:

\rmk{\label{rmk_Fpn}We denote by $\mathbb F_{p^n}$ the finite field of order $p^n$.}

## Galois theory of finite fields

In the last section we showed that finite fields exist and are all isomorphic to the splitting field of a separable polynomial over $\mathbb F_p$; see the [linked Proposition](#prop_existence_of_finite_fields). We therefore obtain the following immediate Corollary:

\details{
    \cor{\label{cor_finite_field_over_Fp_is_Galois}The extension $\mathbb F_{p^n}/\mathbb F_p$ is a Galois extension.}
}{\justification{Recall that $L/K$ is a Galois extension if and only if $L$ is the splitting field of a separable polynomial over $K$.}
}

It's Galois group has exceedingly nice structure; in fact, it is cyclic and generated by the Frobenius endomorphism $F$.

\details{
    \prop{\label{prop_frobenius_generates_galois_group}The Galois group $\operatorname{GaL}(\mathbb F_{p^n}/\mathbb F)$ is cyclic and generated by the Frobenius endomorphism $F:x \mapsto x^p$.}
}{
    \proof{
        We first note that $F$ is an automorphism of $\mathbb F_{p^n}$ which fixes $\mathbb F$. Indeed, it is injective since it is an endomorphism of fields and is hence also surjective by the finiteness of $\mathbb F_{p^n}$. It fixes $\mathbb F_p$ by Fermat's little theorem: $\alpha^p = \alpha$ for all $\alpha\in \mathbb F_p$.
        \break
        \break
        Since $F \in \Gal(\mathbb F_{p^n}/\mathbb F)$ and $\Gal(\mathbb F_{p^n}/\mathbb F)| = [\mathbb F_{p^n}:\mathbb F_p] = n$, we know that $F^n$ is the identity on $\mathbb F_{p^n}$. We need only that $n$ is the minimal such integer which makes this true. Suppose then that there were a positive integer $d$ smaller than $n$ such that $F^d = \id$. Each $\alpha \in \mathbb F_{p^n}$ would then satisfy $\alpha^{p^d} = \alpha$, and hence the polynomial $x^{p^d} - x$ would have $p^n$ roots. This is impossible, so $n$ must be the smallest positive integer such that $F^n = \id$. We conclude that the Frobenius endomorphism generates of the Galois group of $\mathbb F_{p^n}/\mathbb F_p$. .
    }
}

Note that this means $\Gal(\mathbb F_{p^n}/\mathbb F_n) = \mathbb Z/n\mathbb Z$. Quite a nice Galois group, all things considered. For one thing, it's Abelian, and hence all subextensions of $\mathbb F_{p^n}/\mathbb F_p$ are Galois extensions of $\mathbb F_p$ by the Fundamental Theorem. For another, we understand all the subgroups of $\mathbb Z_n\mathbb Z$ -- they're generated by integers $d$ which divide $n$ -- and hence the subgroups of $\Gal(\mathbb F_{p^n}/\mathbb F_p)$ are $\langle F^d\rangle$ for integers $d$ which divide $n$ since $F$ generates the Galois group. Hence for every divisor $d$ of $n$ there is exactly one subfield of $\mathbb F_{p^n}$ over $\mathbb F_p$ of order $d$, namely the fixed field of the subgroup generated by $F^{n/d}$, and it is isomorphic to $\mathbb F_{p^d}$. The following theorem summarizes what we've shown thus far.

\details{
    \thm{\label{thm_finite_fields_summary}
        Let $K$ be a finite field of prime characteristic $p>0$. Then
- $K$ is a finite extension of $\mathbb F_{p}$
- $K \cong \mathbb F_{p^n}$, where $\mathbb F_{p^n}$ is the splitting field of $x^{p^n} - x$ and $n = [K:\mathbb F_p]$
- $\mathbb F_{p^n}/\mathbb F_p$ is Galois of order $n$ with cyclic Galois group generated by the Frobenius endomorphism
- Every subextension of $\mathbb F_{p^n}/\mathbb F_p$ is isomorphic to $\mathbb F_{p^d}/\mathbb F_p$ for some $d$ dividing $n$.
    }
}{
\begin{graybox}
    *Justification:* &nbsp; See the paragraph immediately above this.
\end{graybox}
}

## Further important facts

Given what we now know, we can retroactively construct $\mathbb F_{p^n}$ as a simple extension of $\mathbb F_p$. Doing this will yield some interesting results; for instance, we'll realize that $x^{p^n} - x$ is actually the product of all irreducible polynomials of order $d$ over $\mathbb F_p$ with $d$ varying over the divisors of $n$.

### Finite fields are simple extensions

To show that $\mathbb F_{p^n}$ is a simple extension of $\mathbb F_p$, we need to find an element of $\mathbb F_{p^n}$ which is algebraic of order $n$ over $\mathbb F_p$.

\details{
    \prop{\label{prop_finite_fields_are_simple}
        For each $n$, there is an element $\alpha \in \mathbb F_{p^n}$ of order $n$ over $\mathbb F_p$. Hence $\mathbb F_{p^n} \cong \mathbb F_p(\alpha)$.
    }
}{
    \proof{Fix some integer $n$ and let $\alpha$ be a generator of $\mathbb F_{p^n}^\times$, noting that every finite subgroup of the multiplicative subgroup of *any* field is cyclic ([see the below lemma](#lem_finite_subgroup_of_multiplicative_subgroup_of_field)). Then
    \begin{align*}
        \mathbb F_{p^n} = \mathbb F^\times_{p^n} \cup \{0\} = \langle \alpha \rangle \cup \{0\} = \mathbb F_p(\alpha).
    \end{align*}
    }
}

This proposition could also be stated as follows: for each integer $n$, there is an irreducible polynomial of order $n$ over $\mathbb F_p$. Quotienting $\mathbb F_p[x]$ by this irreducible polynomial would then produce a finite field of order $p^n$ which, as we've seen, is necessarily $\mathbb F_{p^n}$.

The following Lemma is included for completeness. It is Proposition 9.18 in Dummit and Foote.

\details{
    \lem{\label{lem_finite_subgroup_of_multiplicative_subgroup_of_field}Let $K$ be any field and let $G\subseteq K^\times$ be a subgroup of $K^\times$. If $G$ is finite then it is cyclic.}
}{
    \proof{The group $K^\times$ is Abelian, hence so is $G$. By the Structure Theorem of Abelian groups there exist integers $n_1 ~|~ n_2 ~|~ ... ~|~ n_k$ such that
    \begin{align*}
        G \cong \mathbb Z/n_1 \mathbb Z \times ... \times \mathbb Z/n_k \mathbb Z.
    \end{align*}
    Since $n_i ~|~ n_k$ for each $1\leq i\leq k$, every element of $G$ is a root of the polynomial $x^{n_k} - 1$. If $k > 1$, this would imply that there is a polynomial over $K$ whose order is strictly less than the number of its roots, which is impossible. Hence $k=1$ and we conclude that $G$ is cyclic.
    }
}

### Counting irreducible polynomials over $\mathbb F_p$

As a corollary to the [Proposition from the previous section](#prop_finite_fields_are_simple) we obtain the following:
\details{
    \cor{\label{cor_all_irreducible_polynomials}The polynomial $x^{p^n} - x$ is the product of all irreducible polynomials of order $d$ over $\mathbb F_p$, where $d$ ranges over the divisors of $n$.}
}{
    \proof{
        By [the linked Theorem](#thm_finite_fields_summary) we know $\mathbb F_{p^n}$ contains a copy of $\mathbb F_{p^d}$ for each $d$ dividing $n$, and hence also contains a primitive element $\alpha_d$ of order $d$. Since $f(x) = x^{p^n} - x$ vanishes at $\alpha_d$, the minimal polynomial of $\alpha_d$ must divide $x^{p^n} - x$.
        \break
        \break
        Conversely, if $g$ is an irreducible polynomial of order $d$ dividing $n$ with root $\alpha$, then $\mathbb F_p(\alpha)\cong \mathbb F_{p^d}$ is a subfield of $\mathbb F_{p^n}$, and hence $g$ divides $x^{p^n} - x$.
    }
}

### Example: An irreducible polynomial over $\mathbb Z$ which is reducible modulo every prime $p$

Recall that a polynomial which is irreducible over $\mathbb F_p$ for every prime is irreducible over $\mathbb Q$. We end with an example which demonstrates the converse is not true.

\details{
    \example{\label{ex_irreducible_over_Z_recucible_over_Fp}The polynomial $x^4 + 1$ is irreducible over $\mathbb Z$ but is reducible modulo every prime.}
}{
    \solution{The polynomial $x^4 + 1$ can easily be seen to be irreducible over $\mathbb Z$ by applying Eisenstein to $(x+1)^4 + 1$. It is reducible module $2$ since
    \begin{align*}
        x^4 + 1 \equiv (x + 1)^4 \mod 2.
    \end{align*} 
    Suppose then that $p$ is an odd prime. We'll argue that all the roots of $x^4 + 1$ are in $\mathbb F_{p^2}$, and since this is a degree 2 extension of $\mathbb F_p$, it must be the case that $x^4 + 1$ factors into (at least) quadratics over $\mathbb F_p$. Notice first that $p^2$ is either $1$, $3$, $5$ or $7$ modulo 8. All of these square to $1$ in $\mathbb Z/8\mathbb Z$; hence $8 ~|~ p^2 - 1$. It is a general fact that $d ~|~ n$ if and only if $x^d - 1 ~|~ x^n - 1$, since
    \begin{align*}
        d ~|~ n ~\iff ~ \text{every root of } ~x^d - 1 ~\text{ is a root of } ~x^n - 1 ~\iff x^d - 1 ~|~ x^n - 1,
    \end{align*}
    and hence $x^8 - 1$ divides $x^{p^2 - 1} - 1$. This gives us the following divisibility chain:
    \begin{align*}
        x^4 + 1 ~|~ x^8 - 1 ~|~ x^{p^2 - 1} - 1 ~|~ x^{p^2} - x,
    \end{align*}
    which implies that $x^4 + 1$ splits over $\mathbb F_{p^2}$. Since $[\mathbb F_{p^2}:\mathbb F_p] = 2$, the roots of $x^4 + 1$ are order $2$ over $\mathbb F_p$, implying $x^4 + 1$ factors into quadratics modulo $p$.
    }
}

## Exercises

Here I complete some of the exercises in Section 14.3 of Dummit and Foote. Consider these to be examples.

\details{
    \prob{1}{Factor $x^8 - x$ into irreducibles in $\mathbb Z[x]$ and in $\mathbb F_2[x]$.}
}{
    \solution{Over $\mathbb Z$ this polynomial factors as
    \begin{align*}
        x^8 - x = x(x - 1)(x^6 + x^5 + x^4 + x^3 + x^2+ x+1).
    \end{align*}
    The rightmost factor is the $7$th cyclotomic polynomial, and is hence irreducible over $\mathbb Z$.
    \break
    \break
    Over $\mathbb F_2$, $x^8 - x = x^{2^3} - x$ is the product of all irreducible polynomials of order either 1 or 3, since these are the two numbers dividing 3. Using the factorization we found above, we see that
    \begin{align*}
        \frac{x^8 - x}{x(x-1)} = x^6 + x^5+x^4+x^3+x^2+x+1,
    \end{align*}
    hence there are exactly 2 irreducible polynomials of order 3 over $\mathbb F_2$. They both must have nonzero cubic and constant term, leaving only 4 options depending on whether or not $x$ and $x^2$ are present.
- $x^3 + x^2 + x + 1 = (x^2 + 1)(x + 1)$, hence it is not irreducible.
- $x^3 + 1$ has a root modulo $\mathbb F_2$, hence is not irreducible.
    This implies $x^3 + x^2 + 1$ and $x^3 + x + 1$ are the two irreducible cubics over $\mathbb F_2$, and hence
    \begin{align*}
        x^8 - x = x(x - 1)(x^3 + x^2 + 1)(x^3 + x + 1) \mod 2
    \end{align*}}
}

\details{
    \prob{3}{Prove that an algebraically closed field must be infinite.}
}{
    \solution{Suppose $K$ is an algebraically closed field. If $K$ has characteristic $0$, then it contains $\mathbb Q$ and is hence infinite. If it is of prime characteristic $p$ then it contains $\mathbb F_p$. If $K$ were finite, then $[K:\mathbb F_p] = n$ for some integer $n$. However, it must then be the case that $x^{p^{n+1}} - x$ doesn't factor into linear terms over $K$, as this would imply $[K:\mathbb F_p] = n+1$. Hence $K$ must be infinite.}
}
