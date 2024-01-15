<!-- 
#####################
Macros for boxes
#####################
-->

\newcommand{\details}[2]{
  ~~~<details>~~~ ~~~<summary class="box">~~~ #1 ~~~</summary>~~~ #2 ~~~</details>~~~
}

\newcommand{\bluebox}[1]{
@@blue-body,box3,border1
  #1
@@}
\newcommand{\redbox}[1]{
@@red-body,box3,border1
  #1
@@}
\newcommand{\greenbox}[1]{
@@green-body,box3,border1
  #1
@@}
\newcommand{\graybox}[1]{
@@gray-body,box3,border1
  #1
@@}
\newcommand{\graybasicbox}[1]{
@@gray-body,box1 #1
@@}


\newcommand{\defn}[1]{\redbox{**Definition:** #1}}
\newcommand{\rmk}[1]{\redbox{**Remark:** #1}}
\newcommand{\lem}[1]{\bluebox{**Lemma:** #1}}
\newcommand{\prop}[1]{\bluebox{**Proposition:** #1}}
\newcommand{\thm}[1]{\bluebox{**Theorem:** #1}}
\newcommand{\cor}[1]{\bluebox{**Corollary:** #1}}
\newcommand{\example}[1]{\greenbox{**Example:** #1}}
\newcommand{\prob}[2]{\graybox{**Problem #1:** #2}}
\newcommand{\proof}[1]{\graybasicbox{*Proof:* &nbsp; #1}}
\newcommand{\solution}[1]{\graybasicbox{*Solution:* &nbsp; #1}}
\newcommand{\justification}[1]{\graybasicbox{*Justification:* &nbsp; #1}}

\newenvironment{details}{~~~<details>~~~}{~~~</details>~~~}
\newenvironment{summary}{~~~<summary class="box">~~~}{~~~</summary>~~~}
\newenvironment{arrowsummary}{~~~<summary>~~~}{~~~</summary>~~~}
\newenvironment{dropdown}[1]{~~~<details><summary>~~~ #1 ~~~</summary>~~~}{~~~</details>~~~}

\newenvironment{defn}{@@red-body,box3,border1 **Definition:**}{@@}
\newenvironment{rmk}{@@red-body,box3,border1 **Remark:**}{@@}
\newenvironment{lem}{@@blue-body,box3,border1 **Lemma:**}{@@}
\newenvironment{cor}{@@blue-body,box3,border1 **Cor:**}{@@}
\newenvironment{prop}{@@blue-body,box3,border1 **Proposition:**}{@@}
\newenvironment{thm}{@@bluebody,box3,border1 **Theorem:**}{@@}
\newenvironment{example}{@@green-body,box3,border1 **Example:**}{@@}
\newenvironment{prob}{@@gray-body,box3,border1 **Problem:**}{@@}
\newenvironment{proof}{@@gray-body,box1 *Proof.* &nbsp;}{\begin{right}$\square$\end{right}&nbsp;@@}
\newenvironment{solution}{@@gray-body,box1 *Solution.* &nbsp;}{\begin{right}$\square$\end{right}&nbsp;@@}
\newenvironment{graybox}{@@gray-body,box1}{@@}
\newenvironment{redbox}{@@red-body,box3,border1}{@@}
\newenvironment{greenbox}{@@green-body,box3,border1}{@@}
\newenvironment{bluebox}{@@blue-body,box2,border1}{@@}

