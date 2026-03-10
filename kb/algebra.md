# Algebra — JEE Formula Reference

## Quadratic Equations
- Standard form: ax^2 + bx + c = 0
- Roots: x = (-b +/- sqrt(b^2 - 4ac)) / 2a
- Sum of roots: alpha + beta = -b/a
- Product of roots: alpha * beta = c/a
- Discriminant D = b^2 - 4ac
- D > 0: two distinct real roots
- D = 0: one repeated root
- D < 0: no real roots (complex)
- If roots are equal: b^2 = 4ac

## How to Solve a Quadratic — Step by Step
1. Write in standard form ax^2 + bx + c = 0
2. Calculate D = b^2 - 4ac
3. If D >= 0, apply quadratic formula
4. Verify roots by substituting back
5. Check domain constraints

## Binomial Theorem
- (x + y)^n = sum of nCr * x^(n-r) * y^r for r = 0 to n
- nCr = n! / (r! * (n-r)!)
- Middle term: T(n/2 + 1) for even n

## Logarithm Rules
- log(xy) = log(x) + log(y)
- log(x/y) = log(x) - log(y)
- log(x^n) = n*log(x)
- log_b(a) = log(a)/log(b)  [change of base]
- log_a(a) = 1
- log(1) = 0
- ln(e) = 1

## Common Mistakes — Algebra
- Only writing one root, forgetting +/-
- Using b^2 + 4ac instead of b^2 - 4ac
- log(a + b) ≠ log(a) + log(b)
- Dividing by variable without checking it ≠ 0


Complex Numbers

z = x + iy = r(cos theta + i sin theta) = r * e^(i*theta)

|z| = sqrt(x^2 + y^2)

arg(z) = arctan(y/x)

1 + w + w^2 = 0 (Roots of unity)

w^3 = 1

De Moivre's: (cos theta + i sin theta)^n = cos(ntheta) + i sin(ntheta)

|z1 + z2| <= |z1| + |z2| (Triangle Inequality)

Quadratic Equations

Roots = [-b +/- sqrt(b^2 - 4ac)] / 2a

Sum of roots (S) = -b/a

Product of roots (P) = c/a

Equation: x^2 - Sx + P = 0

Discriminant (D) = b^2 - 4ac

Condition for common root: (a1c2 - a2c1)^2 = (a1b2 - a2b1)(b1c2 - b2c1)

Progressions

AP n-th term: a + (n-1)d

AP Sum: (n/2) * [2a + (n-1)d]

GP n-th term: a * r^(n-1)

GP Sum: a(r^n - 1) / (r - 1)

Infinite GP Sum: a / (1 - r)  [for |r| < 1]

Sum n = n(n+1)/2

Sum n^2 = n(n+1)(2n+1)/6

Sum n^3 = [n(n+1)/2]^2



## Quadratic Equations & Roots
- **General Formula:** - LaTeX: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
  - ASCII: x = (-b +/- sqrt(b^2 - 4ac)) / (2a)
  - **Common Mistakes:** Forgetting the $\pm$ sign and only providing one root. Using $b^2 + 4ac$ instead of $b^2 - 4ac$.

- **Sum and Product of Roots:**
  - LaTeX: $\alpha + \beta = -b/a, \alpha\beta = c/a$
  - ASCII: sum = -b/a, product = c/a
  - **Common Mistakes:** Swapping the signs; thinking sum is $b/a$ or product is $-c/a$.

## Progressions (AP, GP, HP)
- **AP Sum of n Terms:**
  - LaTeX: $S_n = \frac{n}{2}[2a + (n-1)d]$
  - ASCII: S_n = (n/2) * [2*a + (n-1)*d]
  - **Common Mistakes:** Using $n$ instead of $n/2$. Confusing $d$ (common difference) with $r$ (common ratio).

- **Infinite GP Sum:**
  - LaTeX: $S_\infty = \frac{a}{1-r}$ where $|r| < 1$
  - ASCII: S_inf = a / (1-r) where |r| < 1
  - **Common Mistakes:** Applying this formula when $|r| \geq 1$. Forgetting the $1-$ in the denominator.

## Logarithms
- **Change of Base:**
  - LaTeX: $\log_b a = \frac{\log_c a}{\log_c b}$
  - ASCII: log_b(a) = log(a) / log(b)
  - **Common Mistakes:** Writing $\log(a) - \log(b)$ instead of a division.

- **Product/Quotient Rules:**
  - LaTeX: $\log(xy) = \log x + \log y$
  - ASCII: log(x*y) = log(x) + log(y)
  - **Common Mistakes:** Incorrectly assuming $\log(x+y) = \log x + \log y$.

---
## Quadratic equation (from Wikipedia)

In mathematics, a quadratic equation (from Latin  quadratus 'square') is an equation that can be rearranged in standard form as

⁠ represents an unknown number, and a, b, and c represent known numbers, where a ≠ 0. (If a = 0 and b ≠ 0 then the equation is linear, not quadratic.) The numbers a, b, and c are the coefficients of the equation and may be distinguished by respectively calling them, the quadratic coefficient, the linear coefficient and the constant coefficient or free term.

⁠ that satisfy the equation are called solutions of the equation, and roots or zeros of the quadratic function on its left-hand side. A quadratic equation has at most two solutions. If there is only one solution, one says that it is a double root. If all the coefficients are real numbers, there are either two real solutions, or a real double root, or two complex solutions that are complex conjugates of each other. A quadratic equation always has two roots, if complex roots are included and a double root is counted for two. A quadratic equation can be factored into an equivalent equation

### Solving the quadratic equation

A quadratic equation whose coefficients are real numbers can have either zero, one, or two distinct real-valued solutions, also called roots. When there is only one distinct root, it can be interpreted as two roots with the same value, called a double root. When there are no real roots, the coefficients can be considered as complex numbers with zero imaginary part, and the quadratic equation still has two complex-valued roots, complex conjugates of each-other with a non-zero imaginary part. A quadratic equation whose coefficients are arbitrary complex numbers always has two complex-valued roots which may or may not be distinct.

The solutions of a quadratic equation can be found by several alternative methods.

### Examples and applications

The golden ratio is found as the positive solution of the quadratic equation

The equations of the circle and the other conic sections—ellipses, parabolas, and hyperbolas—are quadratic equations in two variables.

Given the cosine or sine of an angle, finding the cosine or sine of the angle that is half as large involves solving a quadratic equation.

The process of simplifying expressions involving the square root of an expression involving the square root of another expression involves finding the two solutions of a quadratic equation.

Descartes' theorem states that for every four kissing (mutually tangent) circles, their radii satisfy a particular quadratic equation.

The equation given by Fuss' theorem, giving the relation among the radius of a bicentric quadrilateral's inscribed circle, the radius of its circumscribed circle, and the distance between the centers of those circles, can be expressed as a quadratic equation for which the distance between the two circles' centers in terms of their radii is one of the solutions. The other solution of the same equation in terms of the relevant radii gives the distance between the circumscribed circle's center and the center of the excircle of an ex-tangential quadrilateral.

Critical points of a cubic function and inflection points of a quartic function are found by solving a quadratic equation.

In physics, for motion with constant acceleration

of a moving body can be expressed as a quadratic function of time

In chemistry, the pH of a solution of weak acid can be calculated from the negative base-10 logarithm of the positive root of a quadratic equation in terms of the acidity constant and the analytical concentration of the acid.



---
## Binomial theorem (from Wikipedia)

In elementary algebra, the binomial theorem (or binomial expansion) describes the algebraic expansion of powers of a binomial. According to the theorem, the power ⁠

⁠ expands into a polynomial with terms of the form ⁠

⁠ are nonnegative integers satisfying ⁠

⁠ of each term is a specific positive integer depending on ⁠

### Statement

According to the theorem, the expansion of any nonnegative integer power n of the binomial x + y is a sum of the form

=}x^y^+}x^y^+}x^y^+\cdots +}x^y^,}

is a positive integer known as a binomial coefficient, defined as

This formula is also referred to as the binomial formula or the binomial identity. Using summation notation, it can be written more concisely as

The final expression follows from the previous one by the symmetry of x and y in the first expression, and by comparison it follows that the sequence of binomial coefficients in the formula is symmetric,

A simple variant of the binomial formula is obtained by substituting 1 for y, so that it involves only a single variable. In this form, the formula reads

(x+1)^&=}x^+}x^+}x^+\cdots +}x^\\[4mu]&=\sum _^}x^.}}}

### Examples

The first few cases of the binomial theorem are:

(x+y)^&=1,\\[8pt](x+y)^&=x+y,\\[8pt](x+y)^&=x^+2xy+y^,\\[8pt](x+y)^&=x^+3x^y+3xy^+y^,\\[8pt](x+y)^&=x^+4x^y+6x^y^+4xy^+y^,}}

In general, for the expansion of (x + y)n on the right side in the nth row (numbered so that the top row is the 0th row):

the exponents of x in the terms are n, n − 1, ..., 2, 1, 0 (the last term implicitly contains x0 = 1);

the exponents of y in the terms are 0, 1, 2, ..., n − 1, n (the first term implicitly contains y0 = 1);

the coefficients form the nth row of Pascal's triangle;

before combining like terms, there are 2n terms xiyj in the expansion (not shown);

after combining like terms, there are n + 1 terms, and their coefficients sum to 2n.

An example illustrating the last two points:

(x+y)^&=xxx+xxy+xyx+xyy+yxx+yxy+yyx+yyy&(2^)\\&=x^+3x^y+3xy^+y^&(3+1)}}

A simple example with a specific positive value of y:

(x+2)^&=x^+3x^(2)+3x(2)^+2^\\&=x^+6x^+12x+8.}}

A simple example with a specific negative value of y:

(x-2)^&=x^-3x^(2)+3x(2)^-2^\\&=x^-6x^+12x-8.}}

### Binomial coefficients

The coefficients that appear in the binomial expansion are called binomial coefficients. These are usually written

### In abstract algebra

The binomial theorem is valid more generally for two elements x and y in a ring, or even a semiring, provided that xy = yx. For example, it holds for two n × n matrices, provided that those matrices commute; this is useful in computing powers of a matrix.

The binomial theorem can be stated by saying that the polynomial sequence  is of binomial type.



---
## Logarithm (from Wikipedia)

In mathematics, the logarithm of a number is the exponent by which another fixed value, the base, must be raised to produce that number. For example, the logarithm of 1000 to base 10 is 3, because 1000 is 10 to the 3rd power: 1000 = 103 = 10 × 10 × 10. More generally, if x = by, then y is the logarithm of x to base b, written logb x = y, so log10 1000 = 3. As a single-variable function, the logarithm to base b is the inverse of exponentiation with base b.

The logarithm base 10 is called the decimal or common logarithm and is commonly used in science and engineering. The natural logarithm has the number e ≈ 2.718 as its base; its use is widespread in mathematics and physics because of its very simple derivative. The binary logarithm uses base 2 and is widely used in computer science, information theory, music theory, and photography. When the base is unambiguous from the context or irrelevant it is often omitted, and the logarithm is written log x.

Logarithms were introduced by John Napier in 1614 as a means of simplifying calculations. They were rapidly adopted by navigators, scientists, engineers, surveyors, and others to perform high-accuracy computations more easily. Using logarithm tables, tedious multi-digit multiplication steps can be replaced by table look-ups and simpler addition. This is possible because the logarithm of a product is the sum of the logarithms of the factors:

### Motivation

Addition, multiplication, and exponentiation are three of the most fundamental arithmetic operations. The inverse of addition is subtraction, and the inverse of multiplication is division. Similarly, a logarithm is the inverse operation of exponentiation. Exponentiation is when a number b, the base, is raised to a certain power y, the exponent, to give a value x; this is denoted

For example, raising 2 to the power of 3 gives 8:

The logarithm of base b is the inverse operation, that provides the output y from the input x. That is,

if b is a positive real number. (If b is not a positive real number, both exponentiation and logarithm can be defined but may take several values, which makes definitions much more complicated.)

One of the main historical motivations of introducing logarithms is the formula

by which tables of logarithms allow multiplication and division to be reduced to addition and subtraction, a great aid to calculations before the invention of computers.

### Definition

Given a positive real number b such that b ≠ 1, the logarithm of a positive real number x with respect to base b is the exponent by which b must be raised to yield x. In other words, the logarithm of x to base b is the unique real number y such that

The logarithm is denoted "logb x" (pronounced as "the logarithm of x to base b", "the base-b logarithm of x", or most commonly "the log, base b, of x").

An equivalent and more succinct definition is that the function logb is the inverse function to the function

### Logarithmic identities

Several important formulas, sometimes called logarithmic identities or logarithmic laws, relate logarithms to one another.

### Particular bases

Among all choices for the base, three are particularly common. These are  b = 10,  b = e (the irrational mathematical constant e ≈ 2.71828183  ), and  b = 2 (the binary logarithm). In mathematical analysis, the logarithm base e is widespread because of analytical properties explained below. On the other hand, base 10 logarithms (the common logarithm) are easy to use for manual calculations in the decimal number system:

\,(\,10\,x\,)\ =\;\log _10\ +\;\log _x\ =\ 1\,+\,\log _x\,.}

Thus, log10 (x) is related to the number of decimal digits of a positive integer x: The number of digits is the smallest integer strictly bigger than   log10 (x) .

For example, log10(5986) is approximately 3.78 . The next integer above it is 4, which is the number of digits of 5986. Both the natural logarithm and the binary logarithm are used in information theory, corresponding to the use of nats or bits as the fundamental units of information, respectively.

Binary logarithms are also used in computer science, where the binary system is ubiquitous; in music theory, where a pitch ratio of two (the octave) is ubiquitous and the number of cents between any two pitches is a scaled version of the binary logarithm, or log 2 times 1200, of the pitch ratio (that is, 100 cents per semitone in conventional equal temperament), or equivalently the log base  21/1200  ; and in photography, where rescaled base 2 logarithms are used to measure exposure values, light levels, exposure times, lens apertures, and film speeds in "stops".

The abbreviation log x is often used when the intended base can be inferred based on the context or discipline, or when the base is indeterminate or immaterial. Common logarithms (base 10), historically used in logarithm tables and slide rules, are a basic tool for measurement and computation in many areas of science and engineering; in these contexts log x still often means the base ten logarithm. In mathematics log x usually refers to the natural logarithm (base e).

In 

### Analytic properties

A deeper study of logarithms requires the concept of a function. A function is a rule that, given one number, produces another number. An example is the function producing the x-th power of b from any real number x, where the base b is a fixed number. This function is written as f(x) = b x. When b is positive and unequal to 1, we show below that f is invertible when considered as a function from the reals to the positive reals.

### Calculation

Logarithms are easy to compute in some cases, such as log10 (1000) = 3. In general, logarithms can be calculated using power series or the arithmetic–geometric mean, or be retrieved from a precalculated logarithm table that provides a fixed precision. Newton's method, an iterative method to solve equations approximately, can also be used to calculate the logarithm, because its inverse function, the exponential function, can be computed efficiently. Using look-up tables, CORDIC-like methods can be used to compute logarithms by using only the operations of addition and bit shifts. Moreover, the binary logarithm algorithm calculates lb(x) recursively, based on repeated squarings of x, taking advantage of the relation

### Applications

Logarithms have many applications inside and outside mathematics. Some of these occurrences are related to the notion of scale invariance. For example, each chamber of the shell of a nautilus is an approximate copy of the next one, scaled by a constant factor. This gives rise to a logarithmic spiral. Benford's law on the distribution of leading digits can also be explained by scale invariance. Logarithms are also linked to self-similarity. For example, logarithms appear in the analysis of algorithms that solve a problem by dividing it into two similar smaller problems and patching their solutions. The dimensions of self-similar geometric shapes, that is, shapes whose parts resemble the overall picture are also based on logarithms. Logarithmic scales are useful for quantifying the relative change of a value as opposed to its absolute difference. Moreover, because the logarithmic function log(x) grows very slowly for large x, logarithmic scales are used to compress large-scale scientific data. Logarithms also occur in numerous scientific formulas, such as the Tsiolkovsky rocket equation, the Fenske equation, or the Nernst equation.

