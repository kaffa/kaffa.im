Racket Programming the Fun Way
########################################################

:date: 2024-10-28 00:47
:author: Kaffa
:category: book
:tags: racket
:slug: racket-programming-the-fun-way
:summary: Racket 是一种直观的适合教学使用的 lisp
:image: /static/img/2024/hero.png
:subject_url: https://neodb.social/book/4UmS679GD5IRTgopUJqOov


评分
====================

⭐⭐⭐⭐⭐
⭐⭐⭐
8 / 10


说明
====================

Racket 的优势是，将 lisp + 常用数据类型 + 绘图 + GUI，因此可以很方便做出很多 2D 图形游戏。

适合作为讲述通用编程思想的语言。

在实战中，lisp 的表达能力确实强于 python、js，但 Python 视觉上更简洁，少了许多视觉障碍，而 Js 也可能是最开始学的 C 教学的缘故，大家也习惯大括号。

主要内容：讲解了 lisp 基础，比如

- 原子类型 Atomic Data，number 和 strings
- Lists
- S-Expressions
- List Functions

  - length
  - reverse
  - sort
  - append
  - range
  - make-list
  - null?
  - index-of
  - member

- Defines, Assigns and Variables
- Symbols, Identifiers and Keywords
- Equality
- Strings, Things
- String Functions

  - string-length
  - substring
  - string-titlecase
  - string-upcase
  - string-downcase
  - string<=?
  - string=?
  - string-replace
  - string-contains?
  - string-split
  - string-trim

- String Conversion and Formatting Functions
- Vectors
- Struct
- Controlling output

  - write
  - display
  - print

- Arithmetic

  - Booleans
  - Integers
  - Rationals
  - Reals
  - Complex Numbers

- Numeric Comparison
- Built-in Functions

  - abs
  - ceiling
  - floor
  - tan
  - atan
  - cos
  - sqrt
  - srq
  - log
  - exp
  - expt

- Function
- 绘图
- GUI
- 算法

很多 Python 书也是这种思路了。

本书的最大特点就和 Racket 一样，非常学术，实现了扑克牌游戏、A* 算法、Dijkstra 算法、八皇后问题、数独，甚至还有我喜欢的 15-Puzzle，也是用 A* 搞定的。

.. image:: /static/img/2024/the-golden-spiral.png
    :alt: Racket 画个黄金螺线，那是最擅长的

Racket 就像一个老教授或一个顶级 Geek 一样，可以实现一切算法。但将 Racket 用到 Real world 中，会遇到现实粗砺的坑，现实会用人性打败他，会用数据量打败它，会用缺少必要中间件、分布式组件打败它，让 Racket 呆在它的教学领域是最好的选择。

精通的 Racket，能很快适应现代语言的基础特性，毕竟编程语言的爷爷在这里，比如新语言中出现 match 等，而反过来就不成立。
