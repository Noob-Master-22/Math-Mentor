Limits & Derivatives

lim(x->0) [sin(x) / x] = 1

lim(x->0) [(e^x - 1) / x] = 1

lim(x->0) [ln(1+x) / x] = 1

lim(x->0) (1+x)^(1/x) = e

d/dx(log_a x) = 1 / (x * ln a)

d/dx(a^x) = a^x * ln a

Chain Rule: dy/dx = (dy/du) * (du/dx)

Product Rule: (uv)' = u'v + uv'

Quotient Rule: (u/v)' = (u'v - uv') / v^2

Parametric: dy/dx = (dy/dt) / (dx/dt)

Integration

Integral [ 1 / sqrt(a^2 - x^2) ] dx = arcsin(x/a) + C

Integral [ 1 / (a^2 + x^2) ] dx = (1/a) * arctan(x/a) + C

Integral [ 1 / (x * sqrt(x^2 - a^2)) ] dx = (1/a) * arcsec(x/a) + C

Integral [ tan(x) ] dx = ln|sec x| + C

Integral [ sec(x) ] dx = ln|sec x + tan x| + C

Integral [ sqrt(a^2 - x^2) ] dx = (x/2)sqrt(a^2-x^2) + (a^2/2)arcsin(x/a) + C

Integral [ e^x (f(x) + f'(x)) ] dx = e^x * f(x) + C

King's Prop: Integral(a to b) f(x) dx = Integral(a to b) f(a+b-x) dx

Leibniz Rule: d/dx [ Integral(u(x) to v(x)) f(t) dt ] = f(v(x))v'(x) - f(u(x))u'(x)

Differential Equations

Linear Form: dy/dx + Py = Q

Integrating Factor (I.F.) = e^(Integral P dx)

Solution: y * (I.F.) = Integral (Q * I.F.) dx + C

## Limits: L'Hôpital's Rule
- **Rule:** - LaTeX: $\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}$
  - ASCII: lim f/g = lim f'/g' (for 0/0 or inf/inf)
  - **Common Mistakes:** Applying the rule when the form is NOT $0/0$ or $\infty/\infty$. Differentiating using the Quotient Rule instead of differentiating numerator and denominator separately.

## Differentiation: Chain Rule
- **Formula:** - LaTeX: $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$
  - ASCII: dy/dx = (dy/du) * (du/dx)
  - **Common Mistakes:** Forgetting to differentiate the "inner" function.

## Integration: Power Rule
- **Formula:** - LaTeX: $\int x^n dx = \frac{x^{n+1}}{n+1} + C$ for $n \neq -1$
  - ASCII: integral x^n dx = (x^(n+1))/(n+1) + C
  - **Common Mistakes:** Applying this to $1/x$ (where $n=-1$). Forgetting the constant of integration $+ C$.

## Integration: Logarithmic Form
- **Formula:** - LaTeX: $\int \frac{1}{x} dx = \ln |x| + C$
  - ASCII: integral (1/x) dx = ln|x| + C
  - **Common Mistakes:** Forgetting the absolute value $|x|$. Attempting to use the power rule and getting division by zero.

# Calculus

Calculus is the mathematical study of continuous change, in the same way that geometry is the study of shape and algebra is the study of generalizations of arithmetic operations.
Originally called infinitesimal calculus or the calculus of infinitesimals, it has two major branches, differential calculus and integral calculus. Differential calculus analyses instantaneous rates of change and the slopes of curves; integral calculus analyses accumulation of quantities and areas under or between curves. These two branches are related to each other by the fundamental theorem of calculus. Calculus uses convergence of infinite sequences and infinite series to a well-defined mathematical limit. 
Calculus is the "mathematical backbone" for solving problems in which variable quantities change with time or another reference value. It has also been called "the basic instrument of physical science".
In the late 17th century, Isaac Newton and Gottfried Wilhelm Leibniz each independently formulated infinitesimal calculus. Later work, including codifying the idea of limits, put calculus on a more solid conceptual footing. The concepts and techniques of calculus have broad applications in science, engineering, and other branches of mathematics.

Etymology
In mathematics education, calculus is an abbreviation of both infinitesimal calculus and integral calculus, which denotes courses of elementary mathematical analysis. 
In Latin, the word calculus means “small pebble”, (the diminutive of calx, meaning "stone"), a meaning which still persists in medicine. Because such pebbles were used for counting out distances, tallying votes, and doing abacus arithmetic, the word came to be the Latin word for calculation. In this sense, it was used in English at least as early as 1672, several years before the publications of Leibniz and Newton, who wrote their mathematical texts in Latin.

In addition to differential calculus and integral calculus, the term is also used for naming specific methods of computation or theories that imply some sort of computation. Examples of this usage include propositional calculus, Ricci calculus, calculus of variations, lambda calculus, sequent calculus, and process calculus. Furthermore, the term "calculus" has variously been applied in ethics and philosophy, for such systems as Bentham's felicific calculus, and the ethical calculus.

History
Modern calculus was developed in 17th-century Europe by Isaac Newton and Gottfried Wilhelm Leibniz (independently of each other, first publishing around the same time). Elements of it first appeared in ancient Egypt and later Greece, then in China and the Middle East, and still later again in medieval Europe and India.

Ancient precursors
Egypt
Calculations of volume and area, one goal of integral calculus, can be found in the Egyptian Moscow papyrus (c. 1820 BC), but the formulae are simple instructions, with no indication as to how they were obtained.

Greece
Laying the foundations for integral calculus 

---
## Derivative (from Wikipedia)

In mathematics, the derivative is a fundamental tool that quantifies the sensitivity to change of a function's output with respect to its input. The derivative of a function of a single variable at a chosen input value, when it exists, is the slope of the tangent line to the graph of the function at that point. The tangent line is the best linear approximation of the function near that input value. The derivative is often described as the instantaneous rate of change, the ratio of the instantaneous change in the dependent variable to that of the independent variable. The process of finding a derivative is called differentiation.

There are multiple different notations for differentiation. Leibniz notation, named after Gottfried Wilhelm Leibniz, is represented as the ratio of two differentials, whereas prime notation is written by adding a prime mark. Higher order notations represent repeated differentiation, and they are usually denoted in Leibniz notation by adding superscripts to the differentials, and in prime notation by adding additional prime marks. Higher order derivatives are used in physics; for example, the first derivative  with respect to time of the position of a moving object is its velocity, and the second derivative is its acceleration.

Derivatives can be generalized to functions of several real variables. In this case, the derivative is reinterpreted as a linear transformation whose graph is (after an appropriate translation) the best linear approximation to t

### Continuity and differentiability

⁠. As an example, choose a point

be the step function that returns the value 1 for all

⁠, and returns a different value 10 for all

is on the low part of the step, so the secant line from

tends to zero, the slope tends to infinity. If

is on the high part of the step, so the secant line from

has slope zero. Consequently, the secant lines do not approach any single slope, so the limit of the difference quotient does not exist. However, even if a function is continuous at a point, it may not be differentiable there. For example, the absolute value function given by

⁠, but it is not differentiable there. If

is positive, then the slope of the secant line from 0 to

is negative, then the slope of the secant line from

⁠.  This can be seen graphically as a "kink" or a "cusp" in the graph at ⁠

⁠. Even a function with a smooth graph is not differentiable at a point where its tangent is vertical: For instance, the function given by

⁠. In summary, a function that has a derivative is continuous, but there are continuous functions that do not have a derivative.

Most functions that occur in practice have derivatives at all points or almost every point. Early in the history of calculus, many mathematicians assumed that a continuous function was differentiable at most points. Under mild conditions (for example, if the function is a monotone or a Lipschitz function), this is true. However, in 1872, Weierstrass found the first example of a function that is continuous everywhere but differentiable nowhere.  This example is now known as the Weierstrass function. In 1931, Stefan Banach proved that the set of functions that have a derivative at some point is a meager set in the space of all continuous functions. Informally, this means that hardly any random continuous functions have a derivative at even one point.

### Rules of computation

In principle, the derivative of a function can be computed from the definition by considering the difference quotient and computing its limit. Once the derivatives of a few simple functions are known, the derivatives of other functions are more easily computed using rules for obtaining derivatives of more complicated functions from simpler ones. This process of finding a derivative is known as differentiation.

### Antidifferentiation

An antiderivative of a function

is a function whose derivative is ⁠

⁠. Antiderivatives are not unique: if

is any constant, because the derivative of a constant is zero. The fundamental theorem of calculus shows that finding an antiderivative of a function gives a way to compute the areas of shapes bounded by that function. More precisely, the integral of a function over a closed interval is equal to the difference between the values of an antiderivative evaluated at the endpoints of that interval.

### Higher-order derivatives

Higher-order derivatives are the result of differentiating a function repeatedly. Given that

is a differentiable function, the derivative of

is the first derivative, denoted as ⁠

is the second derivative, denoted as ⁠

is the third derivative, denoted as ⁠

⁠. By continuing this process, if it exists, the ⁠

⁠th derivative is the derivative of the ⁠

⁠th derivative or the derivative of order ⁠

⁠. As has been discussed above, the generalization of derivative of a function

successive derivatives is called

-th derivative is continuous, then the function is said to be of differentiability class ⁠

⁠. A function that has infinitely many derivatives is called infinitely differentiable or smooth. Any polynomial function is infinitely differentiable; taking derivatives repeatedly will eventually result in a constant function, and all subsequent derivatives of that function are zero.

One application of higher-order derivatives is in physics. For example, if the function ⁠

⁠ represents an object's position with respect to time, ⁠

⁠ represents the object's velocity, ⁠

⁠ represents the object's acceleration, and ⁠

⁠ represents the object's jerk.

### Generalizations

The concept of a derivative can be extended to many other settings. The common thread is that the derivative of a function at a point serves as a linear approximation of the function at that point.

An important generalization of the derivative concerns complex functions of complex variables, such as functions from (a domain in) the complex numbers

⁠. The notion of the derivative of such a function is obtained by replacing real variables with complex variables in the definition. If

⁠ then a differentiable function from

is certainly differentiable as a function from

(in the sense that its partial derivatives all exist), but the converse is not true in general: the complex derivative only exists if the real derivative is complex linear and this imposes relations between the partial derivatives called the Cauchy–Riemann equations – see holomorphic functions.

Another generalization concerns functions between differentiable or smooth manifolds. Intuitively speaking such a manifold

is a space that can be approximated near each point

by a vector space called its tangent space: the prototypical example is a smooth surface in ⁠

⁠. The derivative (or differential) of a (differentiable) map

⁠, is then a linear map from the tangent space of

⁠. The derivative function becomes a map between the tangent bundles of

⁠. This definition is used in differential geometry.

Differentiation can also be defined for maps between vector space, such as Banach space, in which those generalizations are the Gateaux derivative and the Fréchet derivative.

One deficiency of the classical derivative is that very many functions are not differentiable. Nevertheless, there is a way of extending the notion of the derivative so that all continuous functions and many other functions can be differentiated using a concept known as the weak derivative. The idea is to embed the continuous functions in a larger space called the space of distributions and only require that a function is differentiab



---
## Integral (from Wikipedia)

In mathematics, an integral is the continuous analog of a sum, and is used to calculate areas, volumes, and their generalizations. The process of computing an integral, called integration, is one of the two fundamental operations of calculus, along with differentiation. Integration was initially used to solve problems in mathematics and physics, such as finding the area under a curve, or determining displacement from velocity. Usage of integration expanded to a wide variety of scientific fields thereafter.

A definite integral computes the signed area of the region in the plane that is bounded by the graph of a given function between two points in the real line. Conventionally, areas above the horizontal axis of the plane are positive while areas below are negative. Integrals also refer to the concept of an antiderivative, a function whose derivative is the given function; in this case, they are also called indefinite integrals. The fundamental theorem of calculus relates definite integration to differentiation and provides a method to compute the definite integral of a function when its antiderivative is known; differentiation and integration are inverse operations.

Although methods of calculating areas and volumes dated from ancient Greek mathematics, the principles of integration were formulated independently by Isaac Newton and Gottfried Wilhelm Leibniz in the late 17th century, who thought of the area under a curve as an infinite sum of rectangles of infinitesimal width.

### Terminology and notation

In general, the integral of a real-valued function f(x) with respect to a real variable x on an interval [a, b] is written as

The integral symbol ∫ represents integration. The symbol dx, called the differential of the variable x, indicates that the variable of integration is x.  The function f(x) is called the integrand, the points a and b are called the limits (or bounds) of integration, and the integral is said to be over the interval [a, b], called the interval of integration.

A function is said to be integrable if its integral over its domain is finite. If limits are specified, the integral is called a definite integral.

When the limits are omitted, as in

the integral is called an indefinite integral, which represents a class of functions (the antiderivative) whose derivative is the integrand. The fundamental theorem of calculus relates the evaluation of definite integrals to indefinite integrals. There are several extensions of the notation for integrals to encompass integration on unbounded domains and/or in multiple dimensions (see later sections of this article).

In advanced settings, it is not uncommon to leave out dx when only the simple Riemann integral is being used, or the exact type of integral is immaterial. For instance, one might write

^(c_f+c_g)=c_\int _^f+c_\int _^g}

to express the linearity of the integral, a property shared by the Riemann integral and all generalizations thereof.

### Interpretations

Integrals appear in many practical situations. For instance, from the length, width and depth of a swimming pool which is rectangular with a flat bottom, one can determine the volume of water it can contain, the area of its surface, and the length of its edge. But if it is oval with a rounded bottom, integrals are required to find exact and rigorous values for these quantities. In each case, one may divide the sought quantity into infinitely many infinitesimal pieces, then sum the pieces to achieve an accurate approximation.

As another example, to find the area of the region bounded by the graph of the function f(x) =

between x = 0 and x = 1, one can divide the interval into five pieces (0, 1/5, 2/5, ..., 1), then construct rectangles using the right end height of each piece (thus √0, √1/5, √2/5, ..., √1) and sum their areas to get the approximation

}}\left(}-0\right)+}}\left(}-}\right)+\cdots +}}\left(}-}\right)\approx 0.7497,}

which is larger than the exact value. Alternatively, when replacing these subintervals by ones with the left end height of each piece, the approximation one gets is too low: with twelve such subintervals the approximated area is only 0.6203. However, when the number of pieces increases to infinity, it will reach a limit which is the exact value of the area sought (in this case, 2/3). One writes

which means 2/3 is the result of a weighted sum of function values, √x, multiplied by the infinitesimal step widths, denoted by dx, on the interval [0, 1].

### Formal definitions

There are many ways of formally defining an integral, not all of which are equivalent. The differences exist mostly to deal with differing special cases which may not be integrable under other definitions, but are also occasionally for pedagogical reasons. The most commonly used definitions are Riemann integrals and Lebesgue integrals.

### Fundamental theorem of calculus

The fundamental theorem of calculus is the statement that differentiation and integration are inverse operations: if a continuous function is first integrated and then differentiated, the original function is retrieved. An important consequence, sometimes called the second fundamental theorem of calculus, allows one to compute integrals by using an antiderivative of the function to be integrated.

### Applications

Integrals are used extensively in many areas. For example, in probability theory, integrals are used to determine the probability of some random variable falling within a certain range. Moreover, the integral under an entire probability density function must equal 1, which provides a test of whether a function with no negative values could be a density function or not.

Integrals can be used for computing the area of a two-dimensional region that has a curved boundary, as well as computing the volume of a three-dimensional object that has a curved boundary. The area of a two-dimensional region can be calculated using the aforementioned definite integral. The volume of a three-dimensional object such as a disc or washer can be computed by disc integration using the equation for the volume of a cylinder,

is the radius. In the case of a simple disc created by rotating a curve about the x-axis, the radius is given by f(x), and its height is the differential dx. Using an integral with bounds a and b, the volume of the disc is equal to:

Integrals are also used in physics, in areas like kinematics to find quantities like displacement, time, and velocity. For example, in rectilinear motion, the displacement of an object over the time interval

is the velocity expressed as a function of time. The work done by a force

(given as a function of position) from an initial position

Integrals are also used in thermodynamics, where thermodynamic integration is used to calculate the difference in free energy between two given states.



---
## L'Hôpital's rule (from Wikipedia)

L'Hôpital's rule ( loh-pee-TAHL), also known as Bernoulli's rule, is a mathematical theorem that allows evaluating limits of indeterminate forms using derivatives. Application (or repeated application) of the rule often converts an indeterminate form to an expression that can be easily evaluated by substitution. The rule is named after the 17th-century French mathematician Guillaume de l'Hôpital. Although the rule is often attributed to de l'Hôpital, the theorem was first introduced to him in 1694 by the Swiss mathematician Johann Bernoulli.

L'Hôpital's rule states that for functions

which are defined on an open interval

for a (possibly infinite) accumulation point

### General form

The general form of l'Hôpital's rule covers many cases. Let

be extended real numbers: real numbers, as well as positive and negative infinity. Let

(for a two-sided limit) or an open interval with endpoint

(for a one-sided limit, or a limit at infinity if

throughout, the limits may also be one-sided limits (

In the second case b), the hypothesis that

diverges to infinity is not necessary; in fact, it is sufficient that

appears most commonly in the literature, but some authors sidestep this hypothesis by adding other hypotheses which imply

. For example, one may require in the definition of the limit

must be defined everywhere on an interval

. Another method is to require that both

be differentiable everywhere on an interval containing

### Necessity of conditions: Counterexamples

All four conditions for l'Hôpital's rule are necessary:

are differentiable on an open interval

except possibly at the limit point

Non-zero derivative of denominator:

Existence of limit of the quotient of the derivatives:

Where one of the above conditions is not satisfied, l'Hôpital's rule is not valid in general, and its conclusion may be false in certain cases.

### Examples

In the following computations, each application of l'Hôpital's rule is indicated by the symbol

Here is a basic example involving the exponential function, which involves the indeterminate form

-1}+x}}\  }}\ \lim _}(e^-1)}}(x^+x)}}=\lim _}}=1.}

This is a more elaborate example involving

. Applying l'Hôpital's rule a single time still results in an indeterminate form. In this case, the limit may be evaluated by applying the rule three times:

\lim _}&\  }}\ \lim _}\\[4pt]&\  }}\ \lim _}\\[4pt]&\  }}\ \lim _}=}=6.}}

x^\cdot e^=\lim _}}}\  }}\ \lim _}}}=n\cdot \lim _}}}.}

Repeatedly apply l'Hôpital's rule until the exponent is zero (if

is fractional) to conclude that the limit is zero.

Here is an example involving the indeterminate form

(see below), which is rewritten as the form

}x\ln x=\lim _}}}\  }}\ \lim _}}}}}}=\lim _}-x=0.}

Here is an example involving the mortgage repayment formula and

be the principal (loan amount),

the interest rate per period and

is zero, the repayment amount per period is

(since only principal is being repaid); this is consistent with the formula for non-zero interest rates:

}-1}}\  }}\ P\lim _+rn(1+r)^}}}=}.}

One can also use l'Hôpital's rule to prove the following theorem. If

is twice-differentiable in a neighborhood of

and its second derivative is continuous on this neighborhood, then

\lim _}}&=\lim _}\\[4pt]&=\lim _}\\[4pt]&=f''(x).}}

Sometimes l'Hôpital's rule is invoked in a tricky way: suppose

converges to positive or negative infinity. Then:

f(x)=\lim _\cdot f(x)}}}\  }}\ \lim _f(x)+f'(x)}}}=\lim _f(x)+f'(x),}

(This result remains true without the added hypothesis that

converges to positive or negative infinity, but the justification is then incomplete.)

### Complications

Sometimes L'Hôpital's rule does not reduce to an obvious limit in a finite number of steps, unless some intermediate simplifications are applied. Examples include the following:

Two applications can lead to a return to the original expression that was to be evaluated:

+e^}-e^}}\  }}\ \lim _-e^}+e^}}\  }}\ \lim _+e^}-e^}}\  }}\ \cdots .}

This situation can be dealt with by substituting

goes to infinity; with this substitution, this problem can be solved with a single application of the rule:

+e^}-e^}}=\lim _}}}\  }}\ \lim _}}}=}=1.}

Alternatively, the numerator and denominator can both be multiplied by

at which point L'Hôpital's rule can immediately be applied successfully:

+e^}-e^}}=\lim _+1}-1}}\  }}\ \lim _}}}=1.}

An arbitrarily large number of applications may never lead to an answer even without repeating:

}+x^}}}}-x^}}}}\  }}\ \lim _}x^}}-}x^}}}}x^}}+}x^}}}}\  }}\ \lim _}x^}}+}x^}}}}x^}}-}x^}}}}\  }}\ \cdots .}

This situation too can be dealt with by a transformation of variables, in this case

}+x^}}}}-x^}}}}=\lim _}}}\  }}\ \lim _}}}=}=1.}

Again, an alternative approach is to multiply numerator and denominator by

before applying L'Hôpital's rule:

}+x^}}}}-x^}}}}=\lim _}\  }}\ \lim _}=1.}

A common logical fallacy is to use L'Hôpital's rule to prove the value of a derivative by computing the limit of a difference quotient. Since applying l'Hôpital requires knowing the relevant derivatives, this amounts to circular reasoning or begging the question, assuming what is to be proved. For example, consider the proof of the derivative formula for powers of x:

Applying L'Hôpital's rule and finding the derivatives with respect to

as expected, but this computation requires the use of the very formula that is being proven. Similarly, to prove

, applying L'Hôpital requires knowing the derivative of

in the first place; a valid proof requires a different method such as the squeeze theorem.

### Other indeterminate forms

Other indeterminate forms, such as

, can sometimes be evaluated using L'Hôpital's rule. We again indicate applications of L'Hopital's rule by

For example, to evaluate a limit involving

, convert the difference of two functions to a quotient:

\lim _\left(}-}\right)&=\lim _}\\[6pt]&\  }}\ \lim _}+\ln x}}\\[6pt]&=\lim _}\\[6pt]&\  }}\ \lim _}=}.}}

L'Hôpital's rule can be used on indeterminate forms involving exponents by using logarithms to "move the exponent down". Here is an example involving the indeterminate form

\!}x^=\lim _\!}e^)}=\lim _\!}e^=\lim _\!}\exp(x\cdot \ln x)=\exp(\!\!}\,x\cdot \ln x}).}

It is valid to move the limit inside the exponential function because this function is continuous. Now the exponent

has been "moved down". The limit

is of the indeterminate form 0 · ∞ dealt with in an example above: L'Hôpital may be used to determine that

The following table lists the most common indeterminate forms and the transformations which precede applying l'Hôpital's rule:

### Stolz–Cesàro theorem

The Stolz–Cesàro theorem is a similar result involving limits of sequences, but it uses finite difference operators rather than derivatives.

### Geometric interpretation: parametric curve and velocity vector

Consider the parametric curve in the xy-plane with coordinates given by the continuous functions

. The slope of the tangent to the curve at

. The tangent to the curve at the point

. L'Hôpital's rule then states that the slope of the curve at the origin (

) is the limit of the tangent slope at points approaching the origin, provided that this is defined.

### Corollary

A simple but very useful consequence of L'Hopital's rule is that the derivative of a function cannot have a removable discontinuity. That is, suppose that

in some open interval containing

Thus, if a function is not continuously differentiable near a point, the derivative must have an essential discontinuity at that point.



---
## Chain rule (from Wikipedia)

In calculus, the chain rule is a formula that expresses the derivative of the composition of two differentiable functions z and y in terms of the derivatives of z and y. More precisely, if

for every x, then the chain rule is, in Lagrange's notation,

The chain rule may also be expressed in Leibniz's notation. If a variable z depends on the variable y, which itself depends on the variable x (that is, y and z are dependent variables), then

### Intuitive explanation

Intuitively, the chain rule states that knowing the instantaneous rate of change of z relative to y and that of y relative to x allows one to calculate the instantaneous rate of change of z relative to x as the product of the two rates of change.

As put by George F. Simmons: "If a car travels twice as fast as a bicycle and the bicycle is four times as fast as a walking man, then the car travels 2 × 4 = 8 times as fast as the man."

The relationship between this example and the chain rule is as follows. Let z, y and x be the (variable) positions of the car, the bicycle, and the walking man, respectively. The rate of change of relative positions of the car and the bicycle is

So, the rate of change of the relative positions of the car and the walking man is

The rate of change of positions is the ratio of the speeds, and the speed is the derivative of the position with respect to the time; that is,

which is also an application of the chain rule.

### Statement

The simplest form of the chain rule is for real-valued functions of one real variable. It states that if g is a function that is differentiable at a point c (i.e. the derivative g′(c) exists) and f is a function that is differentiable at g(c), then the composite function

is differentiable at c, and the derivative is

The rule is sometimes abbreviated as

If y = f(u) and u = g(x), then this abbreviated form is written in Leibniz notation as:

The points where the derivatives are evaluated may also be stated explicitly:

}\right|_=\left.}\right|_\cdot \left.}\right|_.}

Carrying the same reasoning further, given n functions

\circ (f_\circ \cdots (f_\circ f_))\!}

is differentiable at its immediate input, then the composite function is also differentiable by the repeated application of Chain Rule, where the derivative is (in Leibniz's notation):

### Higher derivatives

Faà di Bruno's formula generalizes the chain rule to higher derivatives. Assuming that y = f(u) and u = g(x), then the first few derivatives are:

}&=}}\\y}}}&=y}}}\left(}\right)^+}u}}}\\y}}}&=y}}}\left(}\right)^+3\,y}}}}u}}}+}u}}}\\y}}}&=y}}}\left(}\right)^+6\,y}}}\left(}\right)^u}}}+y}}}\left(4\,}u}}}+3\,\left(u}}}\right)^\right)+}u}}}.}}

### Multivariable case

The full generalization of the chain rule to multi-variable functions (such as

) is rather technical. However, it is simpler to write in the case of functions of the form

As this case occurs often in the study of functions of a single variable, it is worth describing it separately.

### Further generalizations

All extensions of calculus have a chain rule. In most of these, the formula remains the same, though the meaning of that formula may be vastly different.

One generalization is to manifolds. In this situation, the chain rule represents the fact that the derivative of f ∘ g is the composite of the derivative of f and the derivative of g. This theorem is an immediate consequence of the higher dimensional chain rule given above, and it has exactly the same formula.

The chain rule is also valid for Fréchet derivatives in Banach spaces. The same formula holds as before. This case and the previous one admit a simultaneous generalization to Banach manifolds.

In differential algebra, the derivative is interpreted as a morphism of modules of Kähler differentials. A ring homomorphism of commutative rings f : R → S determines a morphism of Kähler differentials Df : ΩR → ΩS which sends an element dr to d(f(r)), the exterior differential of f(r). The formula D(f ∘ g) = Df ∘ Dg holds in this context as well.

The common feature of these examples is that they are expressions of the idea that the derivative is part of a functor. A functor is an operation on spaces and functions between them. It associates to each space a new space and to each function between two spaces a new function between the corresponding new spaces. In each of the above cases, the functor sends each space to its tangent bundle and it sends each function to its derivative. For example, in the manifold case, the derivative sends a Cr-manifold to a Cr−1-manifold (its tangent bundle) and a Cr-function to its total derivative. There is one requirement for this to be a functor, namely that the derivative of a composite must be the composite of the derivatives. This is exactly the formula D(f ∘ g) = Df ∘ Dg.

There are also chain rules in stochastic calculus. One of these, Itō's lemma, expresses the composite of an Itō process (or more generally a semimartingale) dXt with a twice-differentiable function f. In Itō'



---
## Integration by parts (from Wikipedia)

In calculus, and more generally in mathematical analysis, integration by parts or partial integration is a process that finds the integral of a product of functions in terms of the integral of the product of their derivative and antiderivative. It is frequently used to transform the antiderivative of a product of functions into an antiderivative for which a solution can be more easily found. The rule can be thought of as an integral version of the product rule of differentiation; it is indeed derived using the product rule.

The integration by parts formula states:

### Visualization

. Assuming that the curve is locally one-to-one and integrable, we can define

x(y)&=f(g^(y))\\y(x)&=g(f^(x))}}

Similarly, the area of the red region is

The total area A1 + A2 is equal to the area of the bigger rectangle, x2y2, minus the area of the smaller one, x1y1:

}^}x(y)\,dy} ^}+\overbrace }^}y(x)\,dx} ^}\ =\ x\cdot y(x)_}^}\ =\ y\cdot x(y)_}^}}

}^}x(t)\,dy(t)+\int _}^}y(t)\,dx(t)\ =\ x(t)y(t)_}^}}

Or, in terms of indefinite integrals, this can be written as

Thus integration by parts may be thought of as deriving the area of the blue region from the area of rectangles and that of the red region.

This visualization also explains why integration by parts may help find the integral of an inverse function f−1(x) when the integral of the function f(x) is known. Indeed, the functions x(y) and y(x) are inverses, and the integral ∫ x dy may be calculated as above from knowing the integral ∫ y dx. In particular, this explains use of integration by parts to integrate logarithm and inverse trigonometric functions. In fact, if

is a differentiable one-to-one function on an interval, then integration by parts can be used to derive a formula for the integral of

. This is demonstrated in the article, Integral of inverse functions.

### Repeated integration by parts

Considering a second derivative of

in the integral on the LHS of the formula for partial integration suggests a repeated application to the integral on the RHS:

Extending this concept of repeated partial integration to derivatives of degree n leads to

\int u^v^\,dx&=u^v^-u^v^+u^v^-\cdots +(-1)^u^v^+(-1)^\int u^v^\,dx.\\[5pt]&=\sum _^(-1)^u^v^+(-1)^\int u^v^\,dx.}}

This concept may be useful when the iterated integrals of

are readily available (e.g., plain exponentials or sine and cosine, as in  Laplace or Fourier transforms), and when the nth derivative of

vanishes (e.g., as a polynomial function with degree

). The latter condition stops the repeating of partial integration, because the RHS-integral vanishes.

In the course of the above repetition of partial integrations the integrals

v^\,dx\quad 1\leq m,\ell \leq n}

get related. This may be interpreted as arbitrarily "shifting" derivatives between

within the integrand, and proves useful, too (see Rodrigues' formula).

### Higher dimensions

Integration by parts can be extended to functions of several variables by applying a version of the fundamental theorem of calculus to an appropriate product rule. There are several such pairings possible in multivariate calculus, involving a scalar-valued function u and vector-valued function (vector field) V.

The product rule for divergence states:

)\ =\ u\,\nabla \cdot \mathbf  \ +\ \nabla u\cdot \mathbf  .}

with a piecewise smooth boundary

with respect to the standard volume form

, and applying the divergence theorem, gives:

u\mathbf  \cdot  }}\,d\Gamma \ =\ \int _\nabla \cdot (u\mathbf  )\,d\Omega \ =\ \int _u\,\nabla \cdot \mathbf  \,d\Omega \ +\ \int _\nabla u\cdot \mathbf  \,d\Omega ,}

is the outward unit normal vector to the boundary, integrated with respect to its standard Riemannian volume form

u\,\nabla \cdot \mathbf  \,d\Omega \ =\ \int _u\mathbf  \cdot  }}\,d\Gamma -\int _\nabla u\cdot \mathbf  \,d\Omega ,}

u\,\operatorname  (\mathbf  )\,d\Omega \ =\ \int _u\mathbf  \cdot  }}\,d\Gamma -\int _\operatorname  (u)\cdot \mathbf  \,d\Omega .}

The regularity requirements of the theorem can be relaxed. For instance, the boundary

need only be Lipschitz continuous, and the functions u, v  need only lie in the Sobolev space

