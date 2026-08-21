# FCC Python

*Learning documentation*

This repo holds the labs, workshops, and certification projects I've worked through for freeCodeCamp's **Python** certification. It's organized as one folder per topic, roughly in the order the course introduces them. Starting with the basics of the language and ending up in data structures and algorithms territory.

## Structure

- `01. Basics`
- `02. Loops and Sequences`
- `03. Dictionaries and Sets`
- `04. Error Handling`
- `05. Classes And Objects`
- `06. Object-Oriented Programming`
- `07. Linear Data Structures`
- `08. Algorithms`
- `09. Graphs and Trees`
- `10. Dynamic Programming`

Each folder contains the `.py` files written for that topic — labs, workshop exercises, and, further along, the actual certification projects.

### 01. Basics

Variables, data types, operators, basic I/O, the usual basics. Not much to say here except this is where the syntax stopped feeling foreign.

### 02. Loops and Sequences

`for` and `while` loops, lists, strings as sequences. The begining of thinking in terms of iteration instead of (the trivial) writing everything out by hand.

### 03. Dictionaries and Sets

Moving past ordered sequences into key-value data and uniqueness: dictionaries, sets, and the kinds of problems that they were designed for. This topic got a lot easier once I stopped reaching for a list by default.

### 04. Error Handling

`try`/`except`/`finally`, raising and catching exceptions, and writing code that fails on purpose instead of just crashing.

### 05. Classes And Objects

The first real step into object-oriented thinking: defining classes, instantiating objects, attributes vs. methods, and `__init__`.

### 06. Object-Oriented Programming

Building on the previous topic with the bigger OOP concepts — inheritance, encapsulation, polymorphism — and structuring programs around objects instead of just functions and data. This is were the language started to become real fun.

### 07. Linear Data Structures

Stacks, queues, linked lists. Implementing the data structures that usually get taken for granted, which makes it a lot clearer what's actually happening under the hood of things like Python's own `list`.

### 08. Algorithms

Classic algorithm territory: searching, sorting, and the kind of problems where the *how* matters as much as the *what*. Time and space complexity start became 'the thing' to focus on.

### 09. Graphs and Trees

Non-linear data structures. Trees, binary search trees, graphs, and the traversal algorithms (BFS, DFS) that come with them.

### 10. Dynamic Programming

The last stop: breaking problems down into overlapping subproblems, memoization, and tabulation. This was the point where brute-force solutions stopped being 'good enough' and I had to actually think about the structure of the problem before writing a single line of code.

## What I Learned

A few things that carried across the whole repo, not just one folder:

- **Core Python fluency**: Going from "looking up syntax" to actually thinking in Python. Comfortable with the language's built-in data types and control flow.
- **OOP fundamentals**: Structuring code around classes and objects instead of just scripts, and understanding why that structure helps as programs grow.
- **Data structures from scratch**: Implementing stacks, queues, linked lists, trees, and graphs myself instead of just using Python's built-ins, which made it a lot clearer what those built-ins are actually doing.
- **Algorithmic thinking**: Moving from "does this work" to "how efficiently does this work," and picking up dynamic programming as a way to avoid solving the same subproblem twice (or even a million times :P).

Each folder's code is a snapshot of where my Python was at when I wrote it, so earlier folders are rougher than later ones. Which is honestly the most useful part of keeping this repo around, kind of like a landmark of what was.
