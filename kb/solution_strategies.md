1. Quadratic Roots
10-Second ID: Look for ax^2 + bx + c = 0 or expressions involving (alpha)^n + (beta)^n.

First Reach: Sum of roots (-b/a) and Product of roots (c/a).

Common Trap: Forgetting to check if the discriminant D >= 0 for "real roots." JEE often gives a value for k that works for the sum/product but makes the roots imaginary.

How to Verify: Substitute your found roots back into the equation. If the roots are simple (like 1 or 2), just plug them in; if they are complex, check if their sum matches -b/a.

2. Logarithmic Equations
10-Second ID: Equations with log in the base or argument, often with different bases.

First Reach: Base Change Formula: log_b(a) = log(a) / log(b).

Common Trap: Solving the algebra but forgetting the Domain Constraints. The argument must be > 0, and the base must be > 0 and != 1.

How to Verify: Plug your answer into the original equation. If your answer makes any log argument negative or zero, it is an "extraneous solution" and must be rejected.

3. AP / GP Word Problems
10-Second ID: Mentions of "three numbers in...", "sum of n terms", or "common difference/ratio."

First Reach: * For AP: a, a+d, a+2d (or a-d, a, a+d for 3 terms).

For GP: a, ar, ar^2 (or a/r, a, ar for 3 terms).

Common Trap: Confusing the "sum of n terms" (S_n) with the "nth term" (T_n). Also, for infinite GP, forgetting the condition |r| < 1.

How to Verify: Use a small value for n (like n=1 or n=2). If your general formula for S_n doesn't match the sum of the first two terms you calculated manually, the formula is wrong.

4. Probability with Bayes' Theorem
10-Second ID: "An event has happened (e.g., a ball is red), find the probability it came from a specific source (e.g., Bag A)."

First Reach: Tree Diagram. Visualize the branches of the "Total Probability" first.

Common Trap: Only calculating the probability of the specific path and forgetting to divide by the Total Probability (the sum of all paths leading to that result).

How to Verify: The final probability must be between 0 and 1. Also, the sum of probabilities of all possible sources (e.g., P(Bag A|Red) + P(Bag B|Red)) must equal 1.

5. Integration by Parts (IBP)
10-Second ID: Integral of a product of two different types of functions (e.g., x * sin(x) or e^x * x^2).

First Reach: ILATE Rule (Inverse, Log, Algebraic, Trig, Exponential) to choose u.

Common Trap: Forgetting the minus sign in the formula Integral u dv = uv - Integral v du. Also, "Looping" integrals (like e^x * sin x) where you need to integrate twice to get the original integral back.

How to Verify: Differentiate your final answer. If the derivative equals the original integrand, your integration is correct.

6. Matrix Inverse (3x3)
10-Second ID: Question asks for A^-1 or involves an equation like AX = B.

First Reach: Check the Determinant |A|. If |A| = 0, the inverse doesn't exist.

Common Trap: Calculating the cofactor matrix but forgetting to Transpose it to get the Adjoint.

How to Verify: Multiply your result by the original matrix: A * A^-1. You should get the Identity Matrix I. Just checking one element (like the first row, first column) is usually enough to confirm.

7. Limits at Infinity
10-Second ID: lim_{x -> inf} with rational functions (fractions) or radical expressions.

First Reach: Divide every term by the highest power of x present in the denominator.

Common Trap: Forgetting that sqrt(x^2) is |x|. If x approaches -inf, sqrt(x^2) becomes -x, which flips the sign of your answer.

How to Verify: Use the "Degree Rule":

If Degree(Num) > Degree(Den), limit is inf.

If Degree(Num) < Degree(Den), limit is 0.

If Degree(Num) = Degree(Den), limit is the ratio of leading coefficients.