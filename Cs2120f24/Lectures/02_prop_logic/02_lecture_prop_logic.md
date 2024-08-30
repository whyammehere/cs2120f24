# Propositional Logic

Propositional logic is a formal language of expressions, each
expressing a proposition, that you already understand from your
introduction to programming. Propositional logic is essentially
identical to the simplest of languages of Boolean expressions.

## Languages of Commands and Expressions

An *imperative* language, such as Python, Java, or C, is a
language of *state-changing commands*. For example, *X = 5*:
this is an assignment command to ensure that right after this
command runs,, the state of the computation will be just as it
was right before the command runs, except that the value for X
after it runs will now be 5 (overwriting the previous value).

Expression languages are simpler than command languages, and
they also often appear as sub-languages embedded within more 
complex languages. For example, any common imperative programming 
language has expression sub-languages for Boolean and arithmetic
expressions, among others (e.g., *X && Y* and *N + 1*).

## The Formal Language of Propositional Logic, Informally

Propositional logic is an *expression language*. In fact it is
*isomorphic* (essentially identical) to the language of Boolean
expressions you will find in any old imperative language. We give
names to a few more binary operations, and use different notation,
but otherwise, you've already got this.

### Syntax

We define the syntax of expressions in propositional logic (PL)
*inductively*. That means we allow for larger expressions to be
constructed from smaller ones, starting with some smallest ones
as *base cases*. Here's the syntax.

#### Abstract Syntax

We define the type of expressions in PL as follows:

- base cases
  - given any (b : Bool), (lit b) is an expression (base case)
  - given any (v : Variable), (var v) is an expression (base case)
- inductive cases
  - given any expression e and any *unary* operator, op, \op e is an expression 
    - the only *unary* operator we consider for now is \not
    - thus, for any e, the only unary operator expression we define is (not e)
  - if e1 and e2 are expressions and op is a *binary* connective, then (\op e1 e2) is an expression
    - the binary connectives we consider here for now are: and, or, implies, iff
    - so the following are also all expressions in propositional logic:
      - (and e1 e2)
      - (or e1 e2)
      - and some others
        - (imp e1 e2)
        - (iff e1 e2)
        - etc

#### Concrete Syntax

We'll use \top and \bottom as notations for the (lit true) and (lit false) expressions.
Given any variable, v, we'll use {v} as a variable expression and will allow shorthands such as X := {v}
Given any expression, e, we'll use \not e as a notation for \not e
Given any expressions, e1 and e2, we'll use *infix* notation e1 \and e2, etc.

##### Operator Precedence

When using concrete infix instead of abstract prefix notations we run into
questions of order or operations. The ideas should be familiar from arithmetic.
For example you know that X x Y + Z means (X x Y) + 2. The reason is that x is
defined to have higher precedence, to *bind more tightly,* than +. When we define
infix operators for and and or and implies etc., we similarly need to specify
operator precedences.

##### Operator Associativity

Now consider the arithmetic expression, 5 - 3 - 1. What does it mean? It would
not be ambiguous if we'd used prefix notation. It's either (sub 5 (sub 3 1)), or
it's (sub (sub 5 3) 1). If we *parse* 5 - 3 - 1 as 5 - (3 - 1) we get 5 - 2 = 3.
If we parse it as (5 - 3) - 1, we get 2 - 1 = 1. Different results. So which is
it. The question is, how do expressions group, or *associate*? Is it from the
right to the left, which would give us (5 - (3 - 1)) or from the left to right:
((5 - 3) - 1). The answer is that subtraction is defined as *left-associative,*
so the correct answer is 1, not 3. Some other operators, such as *implies*, are
*right associative*. So, for example, P -> Q -> R means (P -> (Q -> R)), and not
((P -> Q) -> R).

#### Exercises

#### Conclusions

The obvious conclusions here are that (1) to use concrete notations with infix
operators, you really have to know the relative precedences and associativity
properties of all of the operators; (2) when you're *specifying* the concrete
syntax for a language (such as propositional logic) you should  make decisions
about these values based on established notations used in practice.

### Semantics

The semantic domain for any expression in PL is the set of *truth values*
of Boolean algebra: *{ true, false }*. Given expression, e, in PL, we want
to be able to mechanically compute its semantic (Boolean-valued) meaning.
So how exactly should we determine the semantic meaning of any expression
in PL?

We answer this question by presenting an *operational semantics* for PL.
An operational semantics is a *function* that takes any expression, e,
and possibly additional information, and that returns the meaning of e
in the corresponding semantic domain.

In our case, the additional data will be ab *interpretation function*, i,
that defines the Boolean meaning of each *variable expression* in e. We
now define a PL semantic evaluation function, *eval*, as follows.

The eval function is applied to an expression, e, and an interpretation,
i to obtain the meaning of e given i. The computation of the return value 
is defined by analysis of the *structure* of e: it can only be one of the
following: (literal b), (variable v), \not e, or \op e1 e2 (\op being one 
of: and, or, not, etc.)

We define *eval (e : Expr) (i : Interpretation) : Bool* more precisely as:

- if e matches (literal b), and given i, the "meaning" of e is b so return b
- if e matches (variable v), and given i (from variables to Bools), return (i v)
- if e matches (not f) where f is the rest of e, and given i, return !eval(f)
- if e matches (and e1 e2), return (eval(e1) && eval(e2))
- if e matches (or e1 e2), return (eval(e1) && eval(e2))
- if e matches (implies e1 e2), return (eval(e1) ??? eval(e2))
- if e matches (iff e1 e2), return (eval(e1) ??? (eval(e2)))

You have all the tools you need now to full and quickly understand
propositional logic.  

In Python, Java, and C, you
have state-changing *assignment* commands, sequencing of commands
into larger commands, conditional commands the run one command or
another (each possibly a larger command) depending on the value
obtained by *evaluating* a Boolean expression that specifies the
condition to branch on. Finally, such languages feature *while*
commands, where execution of the loop body occurs for as many
times as necessary to render the loop condition expression false.
The possibility for a program to iterate endlessly is inherent
in such imperative programs. It's makes a programming language
"Turing Complete," but also enables infinite loops and makes it
impossible to automatically verify in finite times whether any
given program actually goes into an infinite loop or not, or for
that matter to automatically verify in finite time almost *any*
interesting properties of programs. For example, it's impossible
to write an "always-right" program that takes any Java program
as input and that in a finite number of steps outputs the right
answer to the question, can it go into an infinite loop?

## Semantics of Expressions

## Properties of Expressions