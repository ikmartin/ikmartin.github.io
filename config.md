<!--
Add here global page variables to use throughout your website.
-->

+++
author = "Isaac Martin"
mintoclevel = 2

# Add here files or directories that should be ignored by Franklin, otherwise
# these files might be copied and, if markdown, processed by Franklin which
# you might not want. Indicate directories by ending the name with a `/`.
# Base files such as LICENSE.md and README.md are ignored by default.

ignore = ["node_modules/", "config/"]

# RSS (the website\_{title, descr, url} must be defined to get RSS)

generate_rss = true
website_title = "Isaac Martin's Homepage"
website_descr = "Homepage of Isaac Martin"
website_url = "https://lwkatzen.github.io"
+++

<!--
#########################################################
Add here global commands to be used throughout your pages
#########################################################
-->

<!-- ==================================================================
     HTML FUNCTIONS
================================================================== -->

<!-- Make the text sansserif -->
\newcommand{\sansserif}[1]{~~~<span style="font-family: 'Fira', 'Helvetica-Neue', sans-serif">~~~ #1 ~~~</span>~~~}

<!-- Text Alignment -->
\newenvironment{right}{@@right}{@@}
\newenvironment{center}{@@center}{@@}
\newenvironment{left}{@@left}{@@}

<!-- Indentation -->
\newenvironment{indent}{@@indentblock}{@@}
\newenvironment{noindent}{@@noindent}{@@}

<!-- Quality of life -->
\newcommand{\break}[]{~~~<br>~~~}
\newcommand{\comment}[1]{<!-- #1 -->}
\newcommand{\open}[1]{~~~<#1>~~~}
\newcommand{\close}[1]{~~~</#1>~~~}

<!-- The markdown2html parser does unpredictable things to '---' -->
\newcommand{\hline}{~~~<hr>~~~}
\newcommand{\hrule}{~~~<hr>~~~}

<!-- ==================================================================
     TEXT MACROS
================================================================== -->

\newcommand{\author}[]{~~~<p style='font-style: italic;text-align: center;'>by <a href='/'>Isaac</a> on {{date}} </p>~~~}
\newcommand{\thmtitle}[2]{~~~<span><strong>#1:</strong> <em>~~~#2~~~</em>&nbsp;&nbsp;</span>~~~}
\newcommand{\fancyhr}[2]{~~~<div class="#1"><span class="fancytext">#2</span></div>~~~}


<!-- FIGURES -->

\newcommand{\figenv}[3]{
~~~
<figure style="text-align:center;">
<img src="!#1" style="padding:0;#3" alt="#1"/>
<figcaption>~~~#2~~~</figcaption>
</figure>
~~~
}

<!--
############################################################
Add here global latex commands to use throughout your pages.
############################################################
-->

<!--
Operator Names
-->


\newcommand{\ker}{\operatorname{ker}}
\newcommand{\im}{\operatorname{im}}
\newcommand{\coker}{\operatorname{coker}}
\newcommand{\cone}{\operatorname{cone}}
\newcommand{\dim}{\operatorname{dim}}
\newcommand{\fchar}{\operatorname{char}}
\newcommand{\det}{\operatorname{det}}
\newcommand{\id}{\operatorname{id}}
\newcommand{\vspan}{\operatorname{span}}
\newcommand{\Spec}{\operatorname{Spec}}
\newcommand{\Maxspec}{\operatorname{Maxspec}}
\newcommand{\GL}{\operatorname{GL}}
\newcommand{\SL}{\operatorname{SL}}
\newcommand{\Sym}{\operatorname{Sym}}

<!--
Categories
-->

\newcommand{\Ab}{\mathsf{Ab}}
\newcommand{\Cones}{\mathsf{Cones}}
\newcommand{\Grp}{\mathsf{Grp}}
\newcommand{\Set}{\mathsf{Set}}

<!--
Functors
-->

\newcommand{\Hom}{\operatorname{Hom}}
\newcommand{\Aut}{\operatorname{Aut}}
\newcommand{\Gal}{\operatorname{Gal}}
\newcommand{\Spec}{\operatorname{Spec}}

<!--
mathbb
-->

\newcommand{\bA}{\mathbb{A}}
\newcommand{\bB}{\mathbb{B}}
\newcommand{\bC}{\mathbb{C}}
\newcommand{\bD}{\mathbb{D}}
\newcommand{\bE}{\mathbb{E}}
\newcommand{\bF}{\mathbb{F}}
\newcommand{\bG}{\mathbb{G}}
\newcommand{\bH}{\mathbb{H}}
\newcommand{\bI}{\mathbb{I}}
\newcommand{\bJ}{\mathbb{J}}
\newcommand{\bK}{\mathbb{K}}
\newcommand{\bL}{\mathbb{L}}
\newcommand{\bM}{\mathbb{M}}
\newcommand{\bN}{\mathbb{N}}
\newcommand{\bO}{\mathbb{O}}
\newcommand{\bP}{\mathbb{P}}
\newcommand{\bQ}{\mathbb{Q}}
\newcommand{\bR}{\mathbb{R}}
\newcommand{\bS}{\mathbb{S}}
\newcommand{\bT}{\mathbb{T}}
\newcommand{\bU}{\mathbb{U}}
\newcommand{\bV}{\mathbb{V}}
\newcommand{\bW}{\mathbb{W}}
\newcommand{\bX}{\mathbb{X}}
\newcommand{\bY}{\mathbb{Y}}
\newcommand{\bZ}{\mathbb{Z}}
\newcommand{\ba}{\mathbb{a}}
\newcommand{\bb}{\mathbb{b}}
\newcommand{\bc}{\mathbb{c}}
\newcommand{\bd}{\mathbb{d}}
\newcommand{\be}{\mathbb{e}}
\newcommand{\bf}{\mathbb{f}}
\newcommand{\bg}{\mathbb{g}}
\newcommand{\bh}{\mathbb{h}}
\newcommand{\bi}{\mathbb{i}}
\newcommand{\bj}{\mathbb{j}}
\newcommand{\bk}{\mathbb{k}}
\newcommand{\bl}{\mathbb{l}}
\newcommand{\bm}{\mathbb{m}}
\newcommand{\bn}{\mathbb{n}}
\newcommand{\bo}{\mathbb{o}}
\newcommand{\bp}{\mathbb{p}}
\newcommand{\bq}{\mathbb{q}}
\newcommand{\br}{\mathbb{r}}
\newcommand{\bs}{\mathbb{s}}
\newcommand{\bt}{\mathbb{t}}
\newcommand{\bu}{\mathbb{u}}
\newcommand{\bv}{\mathbb{v}}
\newcommand{\bw}{\mathbb{w}}
\newcommand{\bx}{\mathbb{x}}
\newcommand{\by}{\mathbb{y}}
\newcommand{\bz}{\mathbb{z}}

<!--
mathcal
-->

\newcommand{\cA}{\mathcal{A}}
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cC}{\mathcal{C}}
\newcommand{\cD}{\mathcal{D}}
\newcommand{\cE}{\mathcal{E}}
\newcommand{\cF}{\mathcal{F}}
\newcommand{\cG}{\mathcal{G}}
\newcommand{\cH}{\mathcal{H}}
\newcommand{\cI}{\mathcal{I}}
\newcommand{\cJ}{\mathcal{J}}
\newcommand{\cK}{\mathcal{K}}
\newcommand{\cL}{\mathcal{L}}
\newcommand{\cM}{\mathcal{M}}
\newcommand{\cN}{\mathcal{N}}
\newcommand{\cO}{\mathcal{O}}
\newcommand{\cP}{\mathcal{P}}
\newcommand{\cQ}{\mathcal{Q}}
\newcommand{\cR}{\mathcal{R}}
\newcommand{\cS}{\mathcal{S}}
\newcommand{\cT}{\mathcal{T}}
\newcommand{\cU}{\mathcal{U}}
\newcommand{\cV}{\mathcal{V}}
\newcommand{\cW}{\mathcal{W}}
\newcommand{\cX}{\mathcal{X}}
\newcommand{\cY}{\mathcal{Y}}
\newcommand{\cZ}{\mathcal{Z}}
