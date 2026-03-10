Algebra (8 Mistakes)
1. Ignoring the "Base != 1" condition in Logs

WRONG: Solving log_x(a) by only checking x > 0.

WHY: If the base is 1, the logarithm is undefined (1 to any power is 1, not a).

CORRECT: Check x > 0, x != 1, and a > 0.

MEMORY TIP: "Base is the Boss; the Boss can't be 1."

2. Squaring Inequalities blindly

WRONG: If x > y, then x^2 > y^2.

WHY: Fails if numbers are negative. If -5 > -10, then 25 < 100.

CORRECT: Square only if both sides are confirmed positive; otherwise, use cases.

MEMORY TIP: "Negative squares flip the cares."

3. Canceling Variables from both sides

WRONG: Solving x^2 = x by dividing by x to get x = 1.

WHY: You lose the root x = 0.

CORRECT: Bring all terms to one side: x^2 - x = 0 -> x(x - 1) = 0.

MEMORY TIP: "Don't kill the x, factor the effects."

4. Forgetting the "+/-" in Square Roots

WRONG: x^2 = 9 implies x = 3.

WHY: -3 squared is also 9.

CORRECT: x = +/- 3.

MEMORY TIP: "Even power, two-way flower."

5. Assuming AM > GM for negative numbers

WRONG: Using (a+b)/2 >= sqrt(ab) for negative a, b.

WHY: The AM-GM inequality is only valid for positive real numbers.

CORRECT: Check positivity before applying AM-GM.

MEMORY TIP: "AM-GM stays Positive."

6. Misinterpreting sqrt(x^2)

WRONG: sqrt(x^2) = x.

WHY: If x is -3, sqrt(9) is 3, not -3.

CORRECT: sqrt(x^2) = |x|.

MEMORY TIP: "Root of a square is a Mod-pair."

7. Forgetting "a != 0" in Quadratics

WRONG: Assuming ax^2 + bx + c = 0 is always a parabola.

WHY: If a = 0, it’s a straight line.

CORRECT: Always check the coefficient of the highest power.

MEMORY TIP: "No 'a', no curve."

8. Wrong period for tan(x)

WRONG: Using 2*pi as the period for tan(x).

WHY: Tangent repeats every pi.

CORRECT: Period of tan(x) and cot(x) is pi.

MEMORY TIP: "Sin/Cos are 2, Tan is 1."

Calculus (8 Mistakes)
9. Forgetting "+ C" in Indefinite Integrals

WRONG: Integral cos(x) dx = sin(x).

WHY: Losing the constant of integration loses marks in subjective steps or multi-correct options.

CORRECT: sin(x) + C.

MEMORY TIP: "Don't be a dunce, add C at once."

10. Using L'Hopital for non-0/0 forms

WRONG: Applying L'Hopital to lim_{x->0} (cos x / x).

WHY: This is 1/0 (Infinity), not 0/0.

CORRECT: Check the form first. If not 0/0 or inf/inf, use direct limits.

MEMORY TIP: "Check the form before you transform."

11. Forgetting the Chain Rule in Integration

WRONG: Integral e^{3x} dx = e^{3x}.

WHY: You must divide by the derivative of the exponent.

CORRECT: (e^{3x} / 3) + C.

MEMORY TIP: "Differentiate? Multiply. Integrate? Divide."

12. Ignoring Discontinuity in Definite Integrals

WRONG: Integrating 1/x^2 from -1 to 1 normally.

WHY: The function is undefined at x = 0.

CORRECT: Break the integral at the point of discontinuity or check for convergence.

MEMORY TIP: "Mind the Gap."

13. Misapplying the Power Rule to 1/x

WRONG: Integral x^{-1} dx = (x^0 / 0).

WHY: Power rule n+1 fails for n = -1.

CORRECT: Integral (1/x) dx = ln|x| + C.

MEMORY TIP: "Power is -1, Log is the fun."

14. Confusing dy/dx of a^x and x^a

WRONG: d/dx (2^x) = x * 2^{x-1}.

WHY: 2^x is exponential, not a power function.

CORRECT: d/dx (a^x) = a^x * ln(a).

MEMORY TIP: "Variable on top? Log will pop."

15. Range constraints in Inverse Trig

WRONG: sin^{-1}(sin(2pi/3)) = 2pi/3.

WHY: 2pi/3 is outside the principal range [-pi/2, pi/2].

CORRECT: Convert to sin^{-1}(sin(pi/3)) = pi/3.

MEMORY TIP: "Check the branch or lose the ranch."

16. Forgetting to differentiate the bounds in Leibniz Rule

WRONG: Just plugging the bound into the function.

WHY: You must multiply by the derivative of the upper/lower limit.

CORRECT: f(h(x)) * h'(x) - f(g(x)) * g'(x).

MEMORY TIP: "Plug and Prime."

Probability (7 Mistakes)
17. Treating "Independent" as "Mutually Exclusive"

WRONG: Setting P(A AND B) = 0 for independent events.

WHY: Independent means P(A AND B) = P(A) * P(B). Mutually exclusive means they can't happen together.

CORRECT: Distinguish between "no overlap" and "no influence."

MEMORY TIP: "Exclusive is Empty, Independent is Product."

18. Circular Permutation: Forgetting (n-1)!

WRONG: Arranging n people at a round table in n! ways.

WHY: Rotation makes many arrangements identical.

CORRECT: (n - 1)!.

MEMORY TIP: "Fix one seat, then complete."

19. Overcounting in "At Least" problems

WRONG: Calculating P(at least 1) by adding P(1) + P(2)... and double-counting overlaps.

WHY: Intersection cases get counted twice.

CORRECT: Use 1 - P(None).

MEMORY TIP: "At least? Go Reverse."

20. Neglecting the "Identical Items" rule

WRONG: Arranging BALL in 4! ways.

WHY: The two Ls are indistinguishable.

CORRECT: 4! / 2!.

MEMORY TIP: "Divide by the double."

21. Confusing p and q in Binomial

WRONG: Calculating P(X=k) using probability of failure as success.

WHY: JEE often asks for "failure" probability to trick you.

CORRECT: Clearly define p = success before starting.

MEMORY TIP: "P is what you want."

22. Sampling with vs. without Replacement

WRONG: Keeping the denominator constant in "without replacement" problems.

WHY: The total count decreases after each draw.

CORRECT: Reduce n by 1 for each successive draw.

MEMORY TIP: "Without? Subtract."

23. Misapplying Bayes' Denominator

WRONG: Using only one path for the total probability.

WHY: You must sum all possible paths that lead to the outcome.

CORRECT: Use the Theorem of Total Probability for the denominator.

MEMORY TIP: "Total is the sum of all paths."

Linear Algebra (7 Mistakes)
24. Assuming AB = BA

WRONG: Expanding (A+B)^2 as A^2 + 2AB + B^2.

WHY: Matrix multiplication is not commutative.

CORRECT: A^2 + AB + BA + B^2.

MEMORY TIP: "Order matters in Matrices."

25. Forgetting to Transpose in Adjoint

WRONG: Adj(A) = Matrix of Cofactors.

WHY: The Adjoint is the Transpose of the cofactor matrix.

CORRECT: Adj(A) = [C_ij]^T.

MEMORY TIP: "Cofactor then Flip."

26. Determinant Scalar Multiplication

WRONG: det(kA) = k * det(A).

WHY: Each row gets multiplied by k.

CORRECT: det(kA) = k^n * det(A) (where n is the order).

MEMORY TIP: "Scale by the power of Order."

27. Inverse of a Singular Matrix

WRONG: Trying to find A^-1 when det(A) = 0.

WHY: Division by zero is impossible.

CORRECT: Check det(A) first. If 0, inverse doesn't exist.

MEMORY TIP: "Zero Det, No Inverse set."

28. Trace of a Product

WRONG: Tr(AB) = Tr(A) * Tr(B).

WHY: Trace is additive, not multiplicative.

CORRECT: Tr(A + B) = Tr(A) + Tr(B), but Tr(AB) has no such simple rule.

MEMORY TIP: "Trace stays with the Sum."

29. Cramer's Rule: Infinite vs. No Solution

WRONG: Assuming D = 0 always means "No Solution."

WHY: If Dx = Dy = Dz = 0, it could be infinite solutions.

CORRECT: If D = 0, check all Di. If all 0, it’s consistent (infinite) or inconsistent.

MEMORY TIP: "All Zeros? Check the ratio."

30. Matrix Multiplication Dimensions

WRONG: Multiplying a 3x2 matrix by a 3x2 matrix.

WHY: Inner dimensions must match (m x n) * (n x p).

CORRECT: Only multiply if columns of first = rows of second.

MEMORY TIP: "Inside match, outside batch."