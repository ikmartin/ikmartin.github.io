+++
title = "Squeeze Theorem"
hascode = true
description = "asdf"
tags = ["calculus", "limits", "squeeze_theorem"]
date = "2023-09-29"
published = true
+++

@def mintoclevel=2
@def maxtoclevel=4

# Using the Squeeze Theorem to Show \begin{align*}\lim_{x\to 0}\frac{\sin(x)}{x} = 0\end{align*}

> This was written for my Fall 2023 calculus students in M408C, "Differential and Integral Calculus".
>
\toc

In one of the recitation classes a while back we needed to either use the following fact:

\begin{align} 
    \lim_{x\to 0}\frac{\sin(x)}{x} = 1. 
\end{align}

At the time, I forgot how to calculate this limit without using l'Hopital's rule, Taylor Series or the "Small Angle Approximation". This is a problem, because:

- We hadn't seen l'Hopital's rule yet, and worse, it requires knowing that $\dfrac{d}{dx} \sin(x) = \cos(x)$. As far as I'm aware, calculating the derivative of $\sin(x)$ requires knowing the above limit, so this method is circular!
- Taylor Series don't show up until Calculus II and they also require the derivative of $\sin (x)$.
- The small angle approximation says that when $x$ is small, $\sin(x) \approx x$. This is quite useful in physics, but is imprecise. To make it precise, you might say that as $x$ gets super small, $\sin(x) = x + \epsilon$ where $\epsilon$ is some error term, and that $\epsilon$ shrinks faster than $x$ does as $x \to 0$ (meaning that the percentage error in the approximation $\sin(x) \approx x$ goes to zero as $x\to 0$). However, this is a fancy way of saying $\frac{\sin(x)}{x} \to 1$ as $x\to 0$, so this is *also* circular! 

The *correct* way to calculate this limit, or at least, *a* correct way to calculate it, is by using the Squeeze Theorem. It's a fantastic fact and a wonderful computation tool. It's doubly embarrassing that I forgot it that day, especially because we used it that same worksheet to find a very similar limit: $\lim_{x\to 0} x\sin(1/x)$! I wrote this post explaining the solution to this problem and delving into a lot of detail about the squeeze theorem, lest you forget it like I did.

*Thanks to **Catherine Chi** for reminding me of this solution and for suggesting we use the areas of triangles to come up with good bounds for the function $\sin(x)/x$*.

## The squeeze theorem

@@colbox-blue \thmtitle{Theorem}{(The Squeeze Theorem)}   Let $f$, $g$ and $h$ be real valued functions on some interval containing the real number $a$. Suppose there exists some $\epsilon > 0$ such that for all $a\neq x \in (a - \epsilon, a + \epsilon)$ we have [\begin{align} g(x) \leq f(x) \leq h(x). \end{align}\ If $\lim_{x\to a} g(x) = \lim_{x\to a} h(x) = L$, then $\lim_{x\to a} f(x) = L$ as well.
@@

This may be hard to parse, so let's go over the statement of this theorem in more detail.

- "Let $f$, $g$ and $h$ be real valued functions on some interval containing the real number $a$" means that $f$, $g$ and $h$ are all functions whose domain includes an interval $(u,v) \subseteq \mathbb R$ and whose codomain is the real numbers $\mathbb R$. That is, the functions you're used to thinking about. It also names a special number $a$ that is between $u$ and $v$.
- "Suppose there exists some $\epsilon$ such that for all $a\neq x\in (a-\epsilon, a+\epsilon)$ we have..." is a fancy way of saying "for all points close to $a$ but not equal to $a$...". The number $\epsilon>0$ can be super small, as long as it's still positive, and thus $(a - \epsilon, a + \epsilon)$ is a small interval centered at $a$. We call this "a small neighborhood around $a$" informally. This sort of language shows up in the formal definition of a limit, but that's a story for another time. 
- The statement $g(x) \leq f(x) \leq h(x)$ simply means that we want $g$ and $h$ to be lower and upper bounds of $f$ respectively. At this point we can see that the last portion of the statement actually gives us more freedom; we don't need $g$ and $h$ to bound $f$ *everywhere*, just around $a$. Note that we don't need $g$ and $h$ to bound $f$ at $a$ itself; limits don't care about what happens at the limit point. As per usual we are only interested in what's happening *around* $a$. 
- "If $\lim_{x\to a} g(x) = \lim_{x\to a} h(x) = L$..." means, "If the limits of g and h as $x$ approaches $a$ both *exist* and *are equal*..."
*   "...then $\lim_{x\to a} f(x) = L$ as well," means "then the limit of $f$ as $x$ approaches $a$_exists_ and _is equal to $L$_".

That's still a big wall of text, and while it's convincing, perhaps you still don't *feel* the truth of the squeeze theorem. Here are two final things that hopefully help you *feel* it's truth.

### Feeling the truth in your gut

Here's a slogan for you:

@@colbox-red 
    **Slogan:**    Limits preserve non-strict inequalities.
@@

This means that if $g(x) \leq f(x) \leq h(x)$ as above, then $\lim_{x\to a} g(x)\leq \lim_{x\to a} f(x) \leq \lim_{x\to a} h(x)$. You have to be careful: if we have strict inequalities $g(x) < f(x) < h(x)$, then we can only say that $\lim_{x\to a} g(x)\leq \lim_{x\to a} f(x) \leq \lim_{x\to a} h(x)$; limits turn strict inequalities into non-strict inequalities. If this fact is giving you pause, draw some pictures (perhaps some example graphs of $g$, $f$ and $h$) and try to convince yourself that it is true!

If we accept this fact, then in the scenario that $\lim_{x\to a} g(x) = \lim_{x\to a} h(x) = L$ we simply get that

\begin{align} g(x) \leq f(x) \leq h(x) \implies L \leq \lim_{x\to a} f(x) \leq L. \end{align}

The only way something can be simultaneously smaller and bigger than something else is if they're equal! [This is one of Terry Tao's problem solving strategies](https://terrytao.wordpress.com/2010/10/21/245a-problem-solving-strategies): break up equalities into inequalities).

### Feeling the truth in your gut with a picture

Remember this weird function?

\figenv{squeeze1.png}{*The graph of $y = x\sin(1/x)$ in red, $y = |x|$ in blue and $y = -|x|$ in green.*}{width:100%}

While $f(x) = x\sin(1/x)$ looks bizarre, it's bounded above by $|x|$ and below by $-|x|$, as you can see from the graph. At $x = 0$, we get $|x| = -|x| = 0$, and so visually, it looks like $f(x)$ is being squeezed into $0$. Nonetheless, let's carefully write down a calculation of the limit as $x\to 0$ using the squeeze theorem.

### A careful calculation

@@lineblock *Proof:* Remember that $-1 \leq \sin(x) \leq 1$ for all possible values of $x$. This means the inequality still holds if we replace $x$ with $1/x$: $-1 \leq \sin(1/x) \leq 1$. We now want to multiply $x$ into these inequalities, but if $x$ is negative then all the inequalities will flip. Therefore, we break this into cases.

@@revindentblock \thmtitle{Case 1}{($x \geq 0$)}   As long as $x > 0$, then we're free to multiply it into the inequality without changing anything: 
\begin{align} 
    -1 \leq \sin(x) \leq 1 \implies -x \leq x\sin(x) \leq x. 
\end{align}

Since $x$ is positive in this case, we can replace it with $|x|$ wherever we want. Doing that gives us 
\begin{align} 
    -|x| \leq x\sin(x) \leq |x|. 
\end{align}
If that last step confused you, try to explain it to yourself: why does $-x \leq x\sin(x) \leq x$ imply that $-|x| x\leq \sin(x) \leq |x|$ when $x \geq 0$? If you're wondering why we use $|x|$ at all, read through the next case.
@@

@@revindentparagraph \thmtitle{Case 2}{($x < 0$)}  If $x < 0$, then we need to flip the inequalities: 
\begin{align} 
    -1 \leq \sin(x) \leq 1 \implies -x \geq x\sin(x) \geq x. 
\end{align}
Since $x$ is negative, we have that $-|x| = x$, hence 
\begin{align} 
    -(-|x|) \geq x\sin(x) \geq -|x|. 
\end{align} 
or, after rearranging, 
\begin{align} 
    -|x| \leq x\sin(x) \leq |x|. 
\end{align} 
@@
Now you see why we used the absolute value signs: it's a clever way to get upper and lower bounds on $x\sin(x)$ that work when $x\geq 0$  *and* when $x < 0$. Now, if we set 
\begin{align*}
g(x) = -|x| \hspace{1em}\text{and}\hspace{1em} h(x) = |x|,
\end{align*}
then clearly $\lim_{x\to a}g(x) = \lim_{x\to a}h(x) = 0$. By what we just shown,
\begin{align*}
    g(x) \leq x\sin(1/x) \leq h(x)
\end{align*}
for all $x$ (no need to look at a small neighborhood, these are *global* bounds). By the squeeze theorem, we immediately get $\lim_{x\to a}x\sin(x) = 0$. Done!
@@

Notice what happened here: we spent all our work finding upper and lower bounds. Once we had them, the calculation of the limit was immediate.

**Takeaway:** *The squeeze theorem lets you replace the problem of calculating a difficult limit with the problem of finding nice upper and lower bounds*.

## A solution to the problem

Let's turn to the problem at hand.

**Show the following is true:**

\begin{align} 
    \lim_{x\to 0} \frac{\sin(x)}{x} = 1. 
\end{align}

Our strategy is to find functions $g$ and $h$ which bound $\sin(x)/x$ near $0$ and which have the same limit at $0$. Finding functions which bound $\sin(x)/x$ is easy; the tricky part is ensuring they have the same limit.

### Step 1: Convince ourselves the limit exists and is 1.

\figenv{thefunction.png}{*Graph of the function* $f(x) = \sin(x)/x$.}{width:100%}

I'm convinced.

### Step 2: Try the first bounds you can think of

We know that $-1 \leq \sin(x)\leq 1$, so maybe we can copy our strategy from the $x\sin(1/x)$ example. If we do that, then we get

\begin{align} 
    -\frac{1}{|x|} \leq \frac{\sin(x)}{x} \leq \frac{1}{|x|}.
\end{align}

Great! Only trouble is, as $x\to 0$, our lower bound goes to $-\infty$ and our upper bound goes to $\infty$, so we now only know that if the limit exists,

\begin{align}
    -\infty\leq \lim_{x\to 0}\frac{\sin(x)}{x}\leq \infty.
\end{align}

Not exactly helpful.

\figenv{dumb_bound.png}{*Graph of $y = \sin(x)/x$ in red, $y = 1/|x|$ in blue and $y=-1/|x|$ in green. Not a good helpful bound.*}{width: 100%;}

**Note:** You *can* use these bounds to prove that $\lim_{x\to -\infty} \frac{\sin(x)}{x} = \lim_{x\to -\infty}\frac{\sin(x)}{x} = 0$. You have to modify the squeeze theorem a bit though to make sense of limits at infinity.

### Step 3: Get clever.

As suggested by Catherine, we're breaking out some triangles and circles. Consider the normal setup on the unit circle, only this time we're adding a second, bigger triangle (seen in green):

\figenv{maincircle.jpg}{*A triangle with hypotnuse 1, a wedge of the circle and a triangle with adjacent side 1; all with angle $\theta$.*}{width:100%;}

We're going to compare the areas of these three shapes.

\figenv{shapes.jpg}{*Name the orange triangle $A$, name the wedge $B$ and name the green triangle $C$.*}{width:100%;}


#### Area of the small triangle

Using the formula $\text{Area of Triangle} = \frac 12 \text{(base)}\cdot \text{(height)}$, we get that the area of the small triangle is

\begin{align}
    \operatorname{Area}(A) = \frac12 \cos\theta\sin\theta.
\end{align}

#### Area of the wedge

Recall that the fraction of the area taken up by a circle wedge is $\theta/2\pi$:

\figenv{wedge.jpg}{*Finding the area of the wedge*}{width:100%}

This means that

\begin{align}
    \operatorname{Area}(B) = \frac{\theta}{2}.
\end{align}

#### Area of the large triangle

From the diagram, it's

\begin{align}
    \operatorname{Area}(C) = \frac 12 \cdot \tan\theta.
\end{align}

#### Comparing the areas

Based on the construction of these three shapes in the original picture, we see that $A$ sits inside $B$ and $B$ sits inside $C$. Thus

\begin{align}
    \operatorname{Area}(A) \leq \operatorname{Area}(B) \leq \operatorname{Area}(C).
\end{align}

\figenv{shapes.jpg}{*The shapes sit inside each other: $A\subseteq B\subseteq C$.*}{widht:100%;}

#### Doing some algebra

Substituting the formulas we found in for the areas in inequality (15), we get

\begin{align}
    \frac12 \cos\theta\sin\theta \leq \frac{\theta}{2} \leq \frac12 \tan\theta.
\end{align}

Multiply by $2$ to get

\begin{align}
    \cos\theta\sin\theta \leq \theta \leq \tan\theta = \frac{\sin\theta}{\cos\theta}.
\end{align}

Now we make some restrictions. We're eventually going to be applying the squeeze theorem at $\theta = 0$, so we may as well restrict our possible values of $\theta$. Let's say that $-\pi/2 < \theta < \pi/2$; if you look at the statement of the squeeze theorem, we have chosen $\epsilon = \pi/2$. Now we're working in the interval $\left(-\frac\pi2, \frac\pi2\right)$.

**Note:** We actually already implicitly made this restriction to $\theta$. If $\theta$ was any larger, then the triangles wouldn't have angles that sum to $\pi$ radians.

I'd like to divide by $\sin\theta$, but in order to control what happens to the inequalities, I need to break into the cases $\sin\theta > 0 $ and $\sin\theta < 0$.

@@revindentblock \thmtitle{Case 1}{($\theta > 0$)}   This means $\sin\theta > 0$ as well, so I can divide by it without affecting the inequalities. Dividing everything in equation (17) by $\theta$ gives me 
\begin{align} 
    \cos\theta\sin\theta \leq \theta \leq \tan\theta = \frac{\sin\theta}{\cos\theta}\hspace{1em}\leadsto\hspace{1em}\cos\theta \leq \frac{\theta}{\sin\theta} \leq \frac{1}{\cos\theta}.
\end{align} 
Now I've got $\frac{\theta}{\sin\theta}$, the opposite of what I want. Can I flip everything? Again, I need to verify that the signs behave well. Recall that, when $a$ and $b$ have matching signs, we get

\begin{align}
    a < b \iff \frac{1}{a} > \frac{1}{b}
\end{align}

(play with some positive numbers to convince yourself of this if it's unfamiliar). As long as $0 < \theta < \pi/2$, as we have assumed is the case, then everything in these inequalities is positive. Taking the reciprocal of everything in (18) gives me 
\begin{align} 
    \frac{1}{\cos\theta} \geq \frac{\sin\theta}{\theta} \geq \cos\theta,
\end{align}

and magically, we have arrived at upper and lower bounds for $\frac{\sin\theta}{\theta}$ on the interval $\theta\in \left(0,\frac{\pi}{2}\right)$!
@@

@@revindentblock\thmtitle{Case 2}{($\theta < 0$)} This means $\sin\theta < 0$ as well, so when I divide by it I need to change the directions of the inequalities. This gives me

\begin{align}
    \cos\theta \geq \frac{\theta}{\sin\theta} \geq \frac{1}{\cos\theta}.
\end{align}

We're in the interval $\theta\in \left(-\frac{\pi}{2},0\right)$. Here, $\cos\theta$ is positive, $\sin\theta$ is negative and $\theta$ is negative. This means $\sin\theta/\theta$ is positive, all sides of the inequalities in (21) have matching sign. This means I flip the inequalities *again* when I take reciprocals, leaving me with 
\begin{align}
    \frac{1}{\cos\theta} \geq \frac{\sin\theta}{\theta} \geq \cos\theta.
\end{align}
This is the *same* pair of lower and upper bounds as in the other case.
@@

#### Appling the squeeze theorem

We're now ready to apply the squeeze theorem. Set $g(\theta) = \cos\theta$ and $h(\theta) = \frac{1}{\cos\theta}$. By what we have just shown with a lovely combination of geometry and algebra is that, whenever $\theta \in \left(-\frac\pi2,\frac\pi2\right)$, we have

\begin{align} 
    g(\theta) \leq \frac{\sin\theta}{\theta}\leq h(\theta).
\end{align}

Taking limits, we get

\begin{align}
    \lim_{\theta\to 0} g(\theta) = \lim_{\theta\to 0} \cos\theta = \cos(0) = 1, 
\end{align}
\begin{align} 
    \lim_{\theta\to 0} h(\theta) = \lim_{\theta\to 0} \frac{1}{\cos\theta} = \frac{1}{\cos(0)} = 1,
\end{align}

and hence by the squeeze theorem we get

\begin{align} 
    \lim_{\theta\to 0}\frac{\sin\theta}{\theta} = 1. 
\end{align}

We're done! Here's a last graph to illustrate that these bounds do indeed work, in case you don't trust the algebra.

\figenv{thebounds.png}{*The graph of $y=\frac{\sin x}{x}$ in red, of $y=\cos x$ in blue and $y = \frac{1}{\cos x}$ in green restricted to the domain $x \in \left(-\frac\pi2, \frac\pi2\right)$*}{width:100%}

\figenv{fulldomainbounds.png}{Full domain of all functions. Luckily we only care what's happening near $x=0$}{width:100%}

