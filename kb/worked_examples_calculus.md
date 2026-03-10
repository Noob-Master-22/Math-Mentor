1. Limits (L'Hopital's Rule)
Problem 1: The Exponential Limit

Question: Evaluate lim_{x -> 0} (e^x - e^{-x} - 2x) / (x - sin x).

Approach: Direct substitution gives (1 - 1 - 0) / (0 - 0) = 0/0. We apply L'Hopital's Rule repeatedly until the indeterminacy is removed.

Working:

First Differentiation:
Num' = e^x + e^{-x} - 2
Den' = 1 - cos x
Limit = lim_{x -> 0} (e^x + e^{-x} - 2) / (1 - cos x) (Still 0/0)

Second Differentiation:
Num'' = e^x - e^{-x}
Den'' = sin x
Limit = lim_{x -> 0} (e^x - e^{-x}) / sin x (Still 0/0)

Third Differentiation:
Num''' = e^x + e^{-x}
Den''' = cos x
Limit = lim_{x -> 0} (e^x + e^{-x}) / cos x

Final Substitution:
(e^0 + e^0) / cos(0) = (1 + 1) / 1 = 2

Final Answer: 2

Problem 2: Limit involving Logarithms

Question: Find lim_{x -> 1} (1 - x + ln x) / (1 - sqrt(2x - x^2)).

Approach: Substitution gives (1 - 1 + 0) / (1 - 1) = 0/0. Apply L'Hopital's Rule.

Working:

Differentiate Numerator: d/dx(1 - x + ln x) = -1 + 1/x

Differentiate Denominator: d/dx(1 - (2x - x^2)^{0.5}) = -0.5 * (2x - x^2)^{-0.5} * (2 - 2x)
Simplify Denominator: -(1 - x) / sqrt(2x - x^2)

Re-evaluate Limit:
lim_{x -> 1} [(-1 + 1/x)] / [-(1 - x) / sqrt(2x - x^2)]
lim_{x -> 1} [(1 - x) / x] / [(1 - x) / sqrt(2x - x^2)] (Notice the (1-x) cancels!)
lim_{x -> 1} sqrt(2x - x^2) / x

Substitute x = 1:
sqrt(2(1) - 1^2) / 1 = 1 / 1 = 1

Final Answer: 1

2. Derivatives (Chain Rule)
Problem 3: Nested Square Roots

Question: Find dy/dx if y = sqrt(x + sqrt(x + sqrt(x))).

Approach: Use the chain rule d/dx(sqrt(u)) = (1 / (2*sqrt(u))) * du/dx.

Working:

Let u = x + sqrt(x + sqrt(x)). Then y = sqrt(u).
dy/dx = (1 / 2*sqrt(u)) * d/dx(x + sqrt(x + sqrt(x)))

d/dx(x + sqrt(x + sqrt(x))) = 1 + (1 / 2*sqrt(x + sqrt(x))) * d/dx(x + sqrt(x))

d/dx(x + sqrt(x)) = 1 + 1 / (2*sqrt(x))

Combine everything:
dy/dx = [1 / 2*sqrt(x + sqrt(x + sqrt(x)))] * [1 + (1 / 2*sqrt(x + sqrt(x))) * (1 + 1 / 2*sqrt(x))]

Final Answer: [1 / 2y] * [1 + (1 / 2*sqrt(x + sqrt(x))) * (1 + 1/(2*sqrt(x)))]

Problem 4: Trig-Log Combination

Question: If y = ln(tan(pi/4 + x/2)), prove dy/dx = sec x.

Approach: Chain rule: Differentiate ln(u), then tan(v), then (pi/4 + x/2).

Working:

dy/dx = [1 / tan(pi/4 + x/2)] * [sec^2(pi/4 + x/2)] * [1/2]

Convert to sin and cos:
dy/dx = [cos(pi/4 + x/2) / sin(pi/4 + x/2)] * [1 / cos^2(pi/4 + x/2)] * [1/2]
dy/dx = 1 / [2 * sin(pi/4 + x/2) * cos(pi/4 + x/2)]

Use 2 sin A cos A = sin 2A:
dy/dx = 1 / sin(2 * (pi/4 + x/2))
dy/dx = 1 / sin(pi/2 + x)

Since sin(pi/2 + x) = cos x:
dy/dx = 1 / cos x = sec x

Final Answer: sec x

3. Definite Integrals
Problem 5: The King's Property

Question: Evaluate I = Integral_{0}^{pi/2} [ (sin^{10} x) / (sin^{10} x + cos^{10} x) ] dx.

Approach: Apply the King's Property: Integral_{a}^{b} f(x) dx = Integral_{a}^{b} f(a+b-x) dx.

Working:

I = Integral_{0}^{pi/2} [ (sin^{10} x) / (sin^{10} x + cos^{10} x) ] dx (Eq 1)

Use x -> pi/2 - x:
sin(pi/2 - x) = cos x, cos(pi/2 - x) = sin x
I = Integral_{0}^{pi/2} [ (cos^{10} x) / (cos^{10} x + sin^{10} x) ] dx (Eq 2)

Add (Eq 1) and (Eq 2):
2I = Integral_{0}^{pi/2} [ (sin^{10} x + cos^{10} x) / (sin^{10} x + cos^{10} x) ] dx
2I = Integral_{0}^{pi/2} 1 dx

2I = [x]_{0}^{pi/2} = pi/2

I = pi/4

Final Answer: pi/4

Problem 6: Fractional Part Integration

Question: Evaluate Integral_{0}^{2} [x^2] dx, where [.] is the greatest integer function.

Approach: Break the integral at points where x^2 becomes an integer (x = 1, x = sqrt(2), x = sqrt(3), x = 2).

Working:

Range 0 to 1: x^2 is 0 to 1, so [x^2] = 0.

Range 1 to sqrt(2): x^2 is 1 to 2, so [x^2] = 1.

Range sqrt(2) to sqrt(3): x^2 is 2 to 3, so [x^2] = 2.

Range sqrt(3) to 2: x^2 is 3 to 4, so [x^2] = 3.

Sum of integrals:
I = Integral_{0}^{1} 0 dx + Integral_{1}^{sqrt(2)} 1 dx + Integral_{sqrt(2)}^{sqrt(3)} 2 dx + Integral_{sqrt(3)}^{2} 3 dx
I = 0 + (sqrt(2) - 1) + 2(sqrt(3) - sqrt(2)) + 3(2 - sqrt(3))

Simplify:
I = sqrt(2) - 1 + 2*sqrt(3) - 2*sqrt(2) + 6 - 3*sqrt(3)
I = 5 - sqrt(2) - sqrt(3)

Final Answer: 5 - sqrt(2) - sqrt(3)

4. Optimization (Maxima/Minima)
Problem 7: Maximum Volume of a Cylinder

Question: A cylinder is inscribed in a sphere of radius R. Find the maximum volume of the cylinder.

Approach: Let cylinder radius be r and height be h. Use r^2 + (h/2)^2 = R^2. Maximize V = pi * r^2 * h.

Working:

r^2 = R^2 - h^2/4

V(h) = pi * (R^2 - h^2/4) * h = pi * R^2 * h - (pi/4) * h^3

Differentiate wrt h: dV/dh = pi * R^2 - (3*pi/4) * h^2

Set dV/dh = 0: pi * R^2 = (3*pi/4) * h^2 => h^2 = 4*R^2 / 3 => h = 2R / sqrt(3)

Find max volume: V = pi * (R^2 - (4*R^2/3)/4) * (2R/sqrt(3))
V = pi * (R^2 - R^2/3) * (2R/sqrt(3)) = pi * (2R^2/3) * (2R/sqrt(3))
V = 4 * pi * R^3 / (3 * sqrt(3))

Final Answer: (4 * pi * R^3) / (3 * sqrt(3))

Problem 8: Shortest Distance

Question: Find the point on the curve y^2 = 4x which is nearest to the point (2, 1).

Approach: Minimize the square of the distance D^2 = (x - 2)^2 + (y - 1)^2. Substitute x = y^2/4.

Working:

f(y) = (y^2/4 - 2)^2 + (y - 1)^2

Differentiate wrt y: f'(y) = 2(y^2/4 - 2)(2y/4) + 2(y - 1)
f'(y) = (y^2/4 - 2)(y/2) + 2y - 2 = y^3/8 - y + 2y - 2 = y^3/8 + y - 2

Set f'(y) = 0: y^3 + 8y - 16 = 0

By inspection, y = 2 is a root: 8 + 16 - 16 = 8 (No). Let's re-check y^3/8 + y - 2 = 0.
If y = 1.something... let's test y=2 again. 2^3/8 + 2 - 2 = 1.
Wait, let's solve y^3 + 8y - 16 = 0 more carefully. For y=1.5: 3.375 + 12 - 16 = -0.625.
Close to y=1.5. In a typical JEE problem, this would solve to a clean integer. Let's assume the question meant point (2, 0).
If P = (2, 0), then f'(y) = y^3/8 + y = 0 => y = 0.
With (2, 1), the point is approximately (0.6, 1.55).

Final Answer: Point (x, y) where y^3 + 8y - 16 = 0 and x = y^2/4