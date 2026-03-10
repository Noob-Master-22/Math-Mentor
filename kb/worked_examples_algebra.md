1. Quadratic Equations
Problem 1: Roots with a Special Relationship

Question: If one root of the equation x^2 - 5x + k = 0 is the square of the other, find the value of k.

Approach: Let the roots be a and a^2. Use the relations between roots and coefficients: Sum = -b/a and Product = c/a.

Working:

Sum of roots: a + a^2 = 5
Rearrange: a^2 + a - 5 = 0
Using quadratic formula for a: a = (-1 +/- sqrt(1 - 4(1)(-5))) / 2 = (-1 +/- sqrt(21)) / 2

Product of roots: a * a^2 = k
So, k = a^3

Substitute the value of a:
k = [(-1 +/- sqrt(21)) / 2]^3

Cubing the expression:
k = [(-1)^3 + (+/- sqrt(21))^3 + 3(-1)^2(+/- sqrt(21)) + 3(-1)(+/- sqrt(21))^2] / 8
k = [-1 +/- 21*sqrt(21) +/- 3*sqrt(21) - 63] / 8
k = [-64 +/- 24*sqrt(21)] / 8
k = -8 +/- 3*sqrt(21)

Final Answer: k = -8 + 3*sqrt(21) or k = -8 - 3*sqrt(21)

Problem 2: Real Roots Range

Question: Find the set of values of m for which the equation (m-1)x^2 - (m+1)x + (m+1) = 0 has real roots.

Approach: For real roots, the Discriminant (D) must be >= 0. Also, check the condition where the coefficient of x^2 is zero.

Working:

D = b^2 - 4ac >= 0
[-(m+1)]^2 - 4(m-1)(m+1) >= 0

Factor out (m+1):
(m+1) [ (m+1) - 4(m-1) ] >= 0
(m+1) [ m + 1 - 4m + 4 ] >= 0
(m+1) [ -3m + 5 ] >= 0

Multiply by -1 (flip the inequality):
(m+1)(3m - 5) <= 0

Use the wavy curve method. The roots are -1 and 5/3.
The inequality is satisfied when m is between these values.
m belongs to [-1, 5/3]

Check m=1: If m=1, the equation becomes -2x + 2 = 0, which is a linear equation with one real root. So m=1 is included.

Final Answer: m belongs to [-1, 5/3]

2. Arithmetic & Geometric Progressions
Problem 3: Sum of an Infinite AGP

Question: Find the sum of the infinite series: S = 1 + 4/5 + 7/25 + 10/125 + ...

Approach: This is an Arithmetico-Geometric Progression (AGP). The standard method is to multiply the sum by the common ratio (r = 1/5) and subtract it from the original sum.

Working:

S = 1 + 4/5 + 7/25 + 10/125 + ... (Eq 1)

(1/5)S = 1/5 + 4/25 + 7/125 + ... (Eq 2)

Subtract (Eq 2) from (Eq 1):
S - (1/5)S = 1 + (4/5 - 1/5) + (7/25 - 4/25) + (10/125 - 7/125) + ...
(4/5)S = 1 + 3/5 + 3/25 + 3/125 + ...

Notice that from the second term onwards, it's an infinite GP:
(4/5)S = 1 + [ (3/5) / (1 - 1/5) ]
(4/5)S = 1 + [ (3/5) / (4/5) ]
(4/5)S = 1 + 3/4 = 7/4

Solve for S:
S = (7/4) * (5/4) = 35/16

Final Answer: 35/16

Problem 4: Relation between AP and GP

Question: If a, b, c are in AP and a, b, d are in GP, find d in terms of a and b.

Approach: Use the definitions: 2b = a + c (AP) and b^2 = ad (GP).

Working:

From GP: b^2 = a * d

Isolate d: d = b^2 / a

Note: The value of c is irrelevant here as the question only asks for d in terms of a and b.

However, if the question implied a, b, c, d were part of a larger sequence logic, we'd check if c was needed. Given the constraints, the direct GP relationship is sufficient.

Final Answer: d = b^2 / a

3. Logarithms
Problem 5: Logarithmic Equation with Base Change

Question: Solve for x: log_2(x) + log_4(x) + log_16(x) = 21/4

Approach: Change all logs to base 2 using the formula log_{a^n}(x) = (1/n) * log_a(x).

Working:

Rewrite terms:
log_2(x) = log_2(x)
log_4(x) = log_{2^2}(x) = (1/2) * log_2(x)
log_16(x) = log_{2^4}(x) = (1/4) * log_2(x)

Sum them up:
log_2(x) * [1 + 1/2 + 1/4] = 21/4

Simplify the bracket:
log_2(x) * [7/4] = 21/4

Solve for log_2(x):
log_2(x) = (21/4) * (4/7) = 3

Convert to exponential form:
x = 2^3 = 8

Final Answer: x = 8

Problem 6: Logarithmic Inequality (The Domain Trap)

Question: Solve for x: log_0.5 (x - 1) > 2

Approach: When the base of a log is between 0 and 1, the inequality sign flips when removing the log. Also, check the domain constraint.

Working:

Domain Constraint: The argument must be positive.
x - 1 > 0 => x > 1

Solve Inequality:
log_0.5 (x - 1) > 2
x - 1 < (0.5)^2 (Sign flipped because base 0.5 < 1)
x - 1 < 0.25
x < 1.25

Combine with Domain:
1 < x < 1.25

Final Answer: x belongs to (1, 1.25)

4. Complex Numbers
Problem 7: Power of a Complex Number

Question: Find the value of [ (1 + i) / sqrt(2) ]^8 + [ (1 - i) / sqrt(2) ]^8.

Approach: Convert to polar/Euler form. (1+i)/sqrt(2) is cos(pi/4) + i*sin(pi/4) = e^(i*pi/4).

Working:

Let z1 = e^(i*pi/4) and z2 = e^(-i*pi/4)

Use De Moivre's Theorem: (e^(i*theta))^n = e^(i*n*theta)

(z1)^8 = [e^(i*pi/4)]^8 = e^(i * 8 * pi / 4) = e^(i * 2*pi)
e^(2*pi*i) = cos(2*pi) + i*sin(2*pi) = 1 + 0 = 1

(z2)^8 = [e^(-i*pi/4)]^8 = e^(-i * 2*pi)
e^(-2*pi*i) = cos(-2*pi) + i*sin(-2*pi) = 1 + 0 = 1

Sum: 1 + 1 = 2

Final Answer: 2

Problem 8: Maximum Modulus

Question: If |z - 3 + 2i| = 4, find the maximum value of |z|.

Approach: This equation represents a circle with center C(3, -2) and radius r = 4. The maximum value of |z| (distance from origin) is Distance(Origin to Center) + radius.

Working:

Center C = (3, -2). Origin O = (0, 0).

Distance OC = sqrt((3-0)^2 + (-2-0)^2)
OC = sqrt(9 + 4) = sqrt(13)

Max value of |z| = OC + r
Max |z| = sqrt(13) + 4

Final Answer: 4 + sqrt(13)