1. Finding Matrix Inverse
Problem 1: 2x2 Inverse with Variables

Question: If A = [[1, 2], [3, 4]], find A^-1.

Approach: For a 2x2 matrix [[a, b], [c, d]], the inverse is (1/det) * [[d, -b], [-c, a]].

Working:

Calculate Determinant |A|:
|A| = (1 * 4) - (2 * 3) = 4 - 6 = -2

Since |A| != 0, the inverse exists.

Swap diagonal elements (1 and 4) and change signs of off-diagonal elements (2 and 3):
Adj(A) = [[4, -2], [-3, 1]]

A^-1 = (1/|A|) * Adj(A)
A^-1 = (-1/2) * [[4, -2], [-3, 1]]

Multiply the scalar:
A^-1 = [[-2, 1], [1.5, -0.5]]

Final Answer: [[-2, 1], [1.5, -0.5]]

Problem 3: Property-Based Inverse

Question: If A is a 3x3 matrix such that A^2 - 5A + 7I = 0, express A^-1 in terms of A and I.

Approach: Multiply the entire matrix equation by A^-1.

Working:

A^-1 * (A^2 - 5A + 7I) = A^-1 * 0

(A^-1 * A * A) - 5(A^-1 * A) + 7(A^-1 * I) = 0

I * A - 5I + 7A^-1 = 0

A - 5I + 7A^-1 = 0

Isolate A^-1:
7A^-1 = 5I - A
A^-1 = (1/7)(5I - A)

Final Answer: (1/7)(5I - A)

2. Cramer's Rule
Problem 3: Solving a 2-Variable System

Question: Solve using Cramer's Rule:
3x + 2y = 8
2x - y = 3

Approach: Find D, Dx, and Dy. Solutions are x = Dx/D and y = Dy/D.

Working:

D = |3, 2; 2, -1| = (3 * -1) - (2 * 2) = -3 - 4 = -7

Dx = |8, 2; 3, -1| = (8 * -1) - (2 * 3) = -8 - 6 = -14

Dy = |3, 8; 2, 3| = (3 * 3) - (8 * 2) = 9 - 16 = -7

x = Dx / D = -14 / -7 = 2

y = Dy / D = -7 / -7 = 1

Final Answer: x = 2, y = 1

Problem 4: Consistency Check (3-Variable)

Question: For what value of k does the system have no solution?
x + y + z = 2
x + 2y + 3z = 5
x + 3y + kz = 8

Approach: A system has no solution if D = 0 but at least one of Dx, Dy, Dz != 0.

Working:

Calculate D:
D = |1, 1, 1; 1, 2, 3; 1, 3, k|
D = 1(2k - 9) - 1(k - 3) + 1(3 - 2)
D = 2k - 9 - k + 3 + 1 = k - 5

For no solution, set D = 0 => k = 5.

Check Dx at k = 5:
Dx = |2, 1, 1; 5, 2, 3; 8, 3, 5|
Dx = 2(10 - 9) - 1(25 - 24) + 1(15 - 16)
Dx = 2(1) - 1(1) + 1(-1) = 2 - 1 - 1 = 0

Check Dy at k = 5:
Dy = |1, 2, 1; 1, 5, 3; 1, 8, 5|
Dy = 1(25 - 24) - 2(5 - 3) + 1(8 - 5)
Dy = 1 - 4 + 3 = 0

Check Dz at k = 5:
Dz = |1, 1, 2; 1, 2, 5; 1, 3, 8|
Dz = 1(16 - 15) - 1(8 - 5) + 2(3 - 2) = 1 - 3 + 2 = 0
Wait, if D=Dx=Dy=Dz=0, the system has infinite solutions, not "no solution".

Final Answer: There is no value of k for which this specific system has "no solution"; at k=5, it has infinite solutions.

3. Finding Eigenvalues
Problem 5: 2x2 Eigenvalues

Question: Find the eigenvalues of A = [[4, 1], [2, 3]].

Approach: Solve the characteristic equation det(A - lambda*I) = 0.

Working:

A - lambda*I = [[4-L, 1], [2, 3-L]] (where L = lambda)

det = (4-L)(3-L) - (1*2) = 0

12 - 4L - 3L + L^2 - 2 = 0

L^2 - 7L + 10 = 0

Factorize: (L - 5)(L - 2) = 0

L1 = 5, L2 = 2

Final Answer: 2, 5

Problem 6: Eigenvalues of a Triangular Matrix

Question: Find the eigenvalues of:
A = [[1, 7, 9], [0, 8, 6], [0, 0, 3]]

Approach: For any upper or lower triangular matrix, the eigenvalues are simply the diagonal elements.

Working:

The characteristic equation is (1-L)(8-L)(3-L) = 0.

This is because the determinant of a triangular matrix is the product of its diagonal elements.

The roots are clearly 1, 8, and 3.

Final Answer: 1, 8, 3