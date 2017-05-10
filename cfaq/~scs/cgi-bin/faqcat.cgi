<!DOCTYPE HTML PUBLIC "-//W3O//DTD W3 HTML 2.0//EN">
<!-- This collection of hypertext pages is Copyright 1995-2005 by Steve Summit. -->
<!-- Content from the book "C Programming FAQs: Frequently Asked Questions" -->
<!-- (Addison-Wesley, 1995, ISBN 0-201-84519-9) is made available here by -->
<!-- permission of the author and the publisher as a service to the community. -->
<!-- It is intended to complement the use of the published text -->
<!-- and is protected by international copyright laws. -->
<!-- The on-line content may be accessed freely for personal use -->
<!-- but may not be published or retransmitted without explicit permission. -->
<!-- -->
<!-- this page built Sat Dec 24 21:47:45 2005 by faqproc version 2.7 -->
<!-- from source file all.sgml dated Wed Dec 21 15:28:12 2005 -->
<!-- corresponding to FAQ list version 4.0 -->
<html>
<head>
<base href="http://c-faq.com/index.html">
<meta name=GENERATOR content="faqproc">
<title>comp.lang.c Frequently Asked Questions</title>
</head>
<body bgcolor="#ffffff">
&nbsp;
<a href="index.html"><img src="images/buttontop.gif" alt="top/contents"></a>
<a href="search.html"><img src="images/buttonsrch.gif" alt="search"></a>
<hr>
<H1>comp.lang.c Frequently Asked Questions</H1>
















<p>This collection of hypertext pages is Copyright 1995-2005 by Steve Summit.
Content from the book "C Programming FAQs: Frequently Asked Questions"
(Addison-Wesley, 1995, ISBN 0-201-84519-9) is made available here by
permission of the author and the publisher as a service to the community.
It is intended to complement the use of the published text 
and is protected by international copyright laws.
The on-line content may be accessed freely for personal use
but may not be published or retransmitted without explicit permission.
</p><p>This page is the top of an HTML version of the Usenet
comp.lang.c Frequently Asked Questions list
(also known as the "clc FAQ").
An FAQ list is a collection of questions commonly asked on Usenet,
together with presumably definitive answers,
provided in an attempt to keep repeated questions
on the newsgroup
down to a low background drone
so that discussion can move on to more interesting matters.
Since they distill knowledge gleaned from many sources
and answer questions which are demonstrably Frequent,
FAQ lists serve as useful references
outside of their originating Usenet newsgroups.
This list is, I dare to claim, no exception,
and the HTML version you're looking at now,
as well as other versions referenced
just below
are intended to be useful to C programmers everywhere.
</p><p>Several
<a href="versions.html">other versions</a>
of this FAQ list are available,
including a
<a href="http://www.awl.com/cseng/titles/0-201-84519-9">book-length version</a>
published by
<a href="http://www.aw.com/cseng/">Addison-Wesley</a>.
(The book, though longer,
also has a few more errors;
I've prepared an
<a href="http://www.eskimo.com/~scs/C-faq/book/Errata.html">errata list</a>.)
See also question <a href="misc/faqavail.html">20.40</a>.
</p><p>These pages are synchronized with
the posted Usenet version
and the Addison-Wesley book version.
Since not all questions appear in all versions,
the question numbers are not always contiguous.
</p><p>[Note to web authors, catalogers, and bookmarkers:
the URL &lt;http://www.c-faq.com/&gt; is
the right way to link to these pages.
All other URL's implementing this collection
are subject to change.]
</p><p>You can browse these pages in several ways.
The table of contents below is of the list's major
sections; these links lead to sub-lists of the questions for
those sections.
The ``all questions'' link leads to a list of
all the questions; each question is (obviously) linked to its answer.
The ``question at a time'' link
arranges that
each question/answer pair be
downloaded to your browser on
its own page,
rather than having
all the questions in a section concatenated together.
In either case,
the ``read sequentially'' link leads to the first
question; you can then follow the ``next'' link at
the bottom of each question's page to read through all of the
questions and answers sequentially.
</p><p><a href="http://www.eskimo.com/~scs/">Steve Summit</a>
<br><a href="mailto:scs@eskimo.com"><TT>scs@eskimo.com</TT></a>
</p><hr><a href="../index.html">question at a time</a>

<hr>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=decl" rel=subdocument>1. Declarations and Initializations</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=struct" rel=subdocument>2. Structures, Unions, and Enumerations</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=expr" rel=subdocument>3. Expressions</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=ptrs" rel=subdocument>4. Pointers</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=null" rel=subdocument>5. Null Pointers</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=aryptr" rel=subdocument>6. Arrays and Pointers</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=malloc" rel=subdocument>7. Memory Allocation</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=charstring" rel=subdocument>8. Characters and Strings</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=bool" rel=subdocument>9. Boolean Expressions and Variables</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=cpp" rel=subdocument>10. C Preprocessor</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=ansi" rel=subdocument>11. ANSI/ISO Standard C</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=stdio" rel=subdocument>12. Stdio</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=lib" rel=subdocument>13. Library Functions</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=fp" rel=subdocument>14. Floating Point</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=varargs" rel=subdocument>15. Variable-Length Argument Lists</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=strangeprob" rel=subdocument>16. Strange Problems</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=style" rel=subdocument>17. Style</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=resources" rel=subdocument>18. Tools and Resources</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=osdep" rel=subdocument>19. System Dependencies</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=misc" rel=subdocument>20. Miscellaneous</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=sx1" rel=subdocument>Glossary</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=sx2" rel=subdocument>Bibliography</a></p>
<p><a href="/~scs/cgi-bin/faqcat.cgi?sec=sx3" rel=subdocument>Acknowledgements</a></p>
<hr>
<p><a href="questions.html">All Questions</a>
<hr>
<p>
<a href="decl/inttypes.html" rel=precedes>Read Sequentially</a>
<hr>
<p>
<a href="questions.html"><img src="images/buttontop.gif" alt="contents"></a>
<a href="search.html"><img src="images/buttonsrch.gif" alt="search"></a>
<br>
<a href="about.html">about this FAQ list</a>
&nbsp;
<a href="eskimo.html">about eskimo</a>
&nbsp;
<a href="search.html">search</a>
&nbsp;
<a href="feedback.html">feedback</a>
&nbsp;
<a href="copyright.html">copyright</a>
<p>
Hosted by
<a href="http://www.eskimo.com/"><img src="http://www.eskimo.com/img/link/eskitiny.gif" alt="Eskimo North"></a>
</p>
</body>
</html>
