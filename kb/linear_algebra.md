Determinant Properties

|A| = |A_transpose|

|AB| = |A| * |B|

|k * A| = (k^n) * |A|  [n = order of matrix]

|A^n| = |A|^n

|adj A| = |A|^(n-1)

|adj(adj A)| = |A|^((n-1)^2)

Matrix Operations

A * (adj A) = |A| * I

A^-1 = (1 / |A|) * adj A

(AB)^-1 = B^-1 * A^-1

(AB)^T = B^T * A^T

Symmetric: A = A^T

Skew-Symmetric: A = -(A^T)

Orthogonal: A * A^T = I

Idempotent: A^2 = A

Involutory: A^2 = I

Nilpotent: A^k = 0 (matrix)

System of Equations (AX = B)

Unique Sol: |A| != 0

Infinite Sol: |A| = 0 AND adj(A)*B = 0

No Solution: |A| = 0 AND adj(A)*B != 0

Cramer's Rule: x = Dx/D, y = Dy/D, z = Dz/D


## Determinants: Scalar Multiplication
- **Rule:** - LaTeX: $|kA| = k^n |A|$ where $n$ is the order of the matrix.
  - ASCII: det(k*A) = (k^n) * det(A)
  - **Common Mistakes:** Thinking $|kA| = k|A|$. This is a classic JEE trap for $3 \times 3$ matrices ($k^3$).

## Cramer's Rule (Systems)
- **Solution:** - LaTeX: $x = \frac{D_x}{D}, y = \frac{D_y}{D}$
  - ASCII: x = Dx / D, y = Dy / D
  - **Common Mistakes:** Assuming a unique solution exists when $D = 0$. (When $D=0$, the system is either inconsistent or has infinite solutions).

## Matrix Inversion
- **Formula:** - LaTeX: $A^{-1} = \frac{1}{|A|} \text{adj}(A)$
  - ASCII: A^-1 = (1/det(A)) * adj(A)
  - **Common Mistakes:** Trying to invert a "singular" matrix (where $|A| = 0$).

## Adjoint Properties
- **Determinant of Adjoint:**
  - LaTeX: $|\text{adj}(A)| = |A|^{n-1}$
  - ASCII: det(adj(A)) = det(A)^(n-1)
  - **Common Mistakes:** Using $|A|^n$ instead of $|A|^{n-1}$.
---
## Matrix (mathematics) (from Wikipedia)

In mathematics, a matrix (pl.: matrices) is a rectangular array of numbers or other mathematical objects with elements or entries arranged in rows and columns, usually satisfying certain properties of addition and multiplication.

denotes a matrix with two rows and three columns. This is often referred to as a "two-by-three matrix", a 2 × 3 matrix, or a matrix of dimension 2 × 3.

In linear algebra, matrices are used as linear maps. In geometry, matrices are used for geometric transformations (for example rotations) and coordinate changes. In numerical analysis, many computational problems are solved by reducing them to a matrix computation, and this often involves computing with matrices of huge dimensions. Matrices are used in most areas of mathematics and scientific fields, either directly, or through their use in geometry and numerical analysis.

### Definition

A matrix is a rectangular array of numbers (or other mathematical objects), called the "entries" of the matrix. Matrices are subject to standard operations such as addition and multiplication. Most commonly, a matrix over a field

is a rectangular array of elements of ⁠

⁠. A real matrix and a complex matrix are matrices whose entries are respectively real numbers or complex numbers. More general types of entries are discussed below. For instance, this is a real matrix:

The numbers (or other objects) in the matrix are called its entries or its elements. The horizontal and vertical lines of entries in a matrix are respectively called rows and columns.

### Basic operations

Several basic operations can be applied to matrices. Some, such as transposition and submatrix do not depend on the nature of the entries. Others, such as matrix addition, scalar multiplication, matrix multiplication, and row operations involve operations on matrix entries and therefore require that matrix entries are numbers or belong to a field or a ring.

In this section, it is supposed that matrix entries belong to a fixed ring, which is typically a field of numbers.

### Linear equations

Matrices can be used to compactly write and work with multiple linear equations, that is, systems of linear equations. For example, if A is an m × n matrix, x designates a column vector (that is, n × 1 matrix) of n variables x1, x2, ..., xn, and b is an m × 1 column vector, then the matrix equation

is equivalent to the system of linear equations

a_x_+a_x_+&\cdots +a_x_=b_\\&\ \ \vdots \x_+a_x_+&\cdots +a_x_=b_}}

Using matrices, this can be solved more compactly than would be possible by writing out all the equations separately. If n = m and the equations are independent, then this can be done by writing

where A−1 is the inverse matrix of A. If A has no inverse, solutions—if any—can be found using its generalized inverse.

### Linear transformations

Matrices and matrix multiplication reveal their essential features when related to linear transformations, also known as linear maps. A real m-by-n matrix A gives rise to a linear transformation

⁠ to the (matrix) product Ax, which is a vector in ⁠

⁠ Conversely, each linear transformation

arises from a unique m-by-n matrix A: explicitly, the (i, j)-entry of A is the ith coordinate of f (ej), where ej = (0, ..., 0, 1, 0, ..., 0) is the unit vector with 1 in the jth position and 0 elsewhere. The matrix A is said to represent the linear map f, and A is called the transformation matrix of f.

can be viewed as the transform of the unit square into a parallelogram with vertices at (0, 0), (a, b), (a + c, b + d), and (c, d). The parallelogram pictured at the right is obtained by multiplying A with each of the column vectors ⁠

⁠ in turn. These vectors define the vertices of the unit square. The following table shows several 2 × 2 real matrices with the associated linear maps of ⁠

⁠. The blue original is mapped to the green grid and shapes. The origin (0, 0) is marked with a black point.

Under the 1-to-1 correspondence between matrices and linear maps, matrix multiplication corresponds to composition of maps: if a k-by-m matrix B represents another linear map ⁠

⁠, then the composition g ∘ f is represented by BA since

The last equality follows from the above-mentioned associativity of matrix multiplication.

The rank of a matrix A is the maximum number of linearly independent row vectors of the matrix, which is the same as the maximum number of linearly independent column vectors. Equivalently it is the dimension of the image of the linear map represented by A. The rank–nullity theorem states that the dimension of the kernel of a matrix plus the rank equals the number of columns of the matrix.

### Square matrix

A square matrix is a matrix with the same number of rows and columns. An n-by-n matrix is known as a square matrix of order n. Any two square matrices of the same order can be added and multiplied.

The entries aii form the main diagonal of a square matrix. They lie on the imaginary line running from the top left corner to the bottom right corner of the matrix.

Square matrices of a given dimension form a noncommutative ring, which is one of the most common examples of a noncommutative ring.

### Computational aspects

Matrix calculations can be often performed with different techniques. Many problems can be solved by both direct algorithms and iterative approaches. For example, the eigenvectors of a square matrix can be obtained by finding a sequence of vectors xn converging to an eigenvector when n tends to infinity.

To choose the most appropriate algorithm for each specific problem, it is important to determine both the effectiveness and precision of all the available algorithms. The domain studying these matters is called numerical linear algebra. As with other numerical situations, two main aspects are the complexity of algorithms and their numerical stability.

Determining the complexity of an algorithm means finding upper bounds or estimates of how many elementary operations such as additions and multiplications of scalars are necessary to perform some algorithm, for example, multiplication of matrices. Calculating the matrix product of two n-by-n matrices using the definition given above needs n3 multiplications, since for any of the n2 entries of the product, n multiplications are necessary. The Strassen algorithm outperforms this "naive" algorithm; it needs only n2.807 multiplications.  Theoretically faster but impractical matrix multiplication algorithms have been developed, as have speedups to this problem using parallel algorithms or distributed computation systems such as MapReduce.

In many practical situations, additional information about the matrices involved is known. An important case concerns sparse matrices, that is, matrices whose entries are mostly zero. There are specifically adapted algorithms for, say, solving linear systems Ax = b for sparse matrices A, such as the conjugate gradient method.

An algorithm is, roughly speaking, numerically stable if little deviations in the input values do not lead to big deviations in the result. For example, one can calculate the inverse of a matrix by computing its adjugate matrix:

}^=\operatorname  (})/\det(}).}

H

### Decomposition

There are several methods to render matrices into a more easily accessible form. They are generally referred to as matrix decomposition or matrix factorization techniques. These techniques are of interest because they can make computations easier.

The LU decomposition factors matrices as a product of lower (L) and an upper triangular matrices (U). Once this decomposition is calculated, linear systems can be solved more efficiently by a simple technique called forward and back substitution. Likewise, inverses of triangular matrices are algorithmically easier to calculate. The Gaussian elimination is a similar algorithm; it transforms any matrix to row echelon form. Both methods proceed by multiplying the matrix by suitable elementary matrices, which correspond to permuting rows or columns and adding multiples of one row to another row. Singular value decomposition (SVD) expresses any matrix A as a product UDV∗, where U and V are unitary matrices and D is a diagonal matrix.

The eigendecomposition or diagonalization expresses A as a product VDV−1, where D is a diagonal matrix and V is a suitable invertible matrix. If A can be written in this form, it is called diagonalizable. More generally, and applicable to all matrices, the Jordan decomposition transforms a matrix into Jordan normal form, that is to say matrices whose only nonzero entries are the eigenvalues λ1 to λn of A, placed on the main diagonal and possibly entries equal to one directly above the main diagonal, as shown at the right. Given the eigendecomposition, the nth power of A (that is, n-fold iterated matrix multiplication) can be calculated via

and the power of a diagonal matrix can be calculated by taking the corresponding powers of the diagonal entries, which is much easier than doing the exponentiation for A instead. This can be used to compute the matrix exponential eA, a need frequently arising in solving linear differential equations, matrix logarithms and square roots of matrices. To avoid num

### Abstract algebraic aspects and generalizations

Matrices can be generalized in different ways. Abstract algebra uses matrices with entries in more general fields or even rings, while linear algebra codifies properties of matrices in the notion of linear maps. It is possible to consider matrices with infinitely many columns and rows. Another extension is tensors, which can be seen as higher-dimensional arrays of numbers, as opposed to vectors, which can often be realized as sequences of numbers, while matrices are rectangular or two-dimensional arrays of numbers. Matrices, subject to certain requirements tend to form groups known as matrix groups. Similarly under certain conditions matrices form rings known as matrix rings. Though the product of matrices is not in general commutative, certain matrices form fields sometimes called matrix fields. (However the term "matrix field" is ambiguous, also referring to certain forms of physical fields that continuously map points of some space to matrices.) In general, matrices over any ring and their multiplication can be represented as the arrows and composition of arrows in a category, the category of matrices over that ring. The objects of this category are natural numbers, representing the dimensions of the matrices.

### Applications

There are numerous applications of matrices, both in mathematics and other sciences. Some of them merely take advantage of the compact representation of a set of numbers in a matrix. For example, Text mining and automated thesaurus compilation makes use of document-term matrices such as tf-idf to track frequencies of certain words in several documents.

Complex numbers can be represented by particular real 2-by-2 matrices via

under which addition and multiplication of complex numbers and matrices correspond to each other. For example, 2-by-2 rotation matrices represent the multiplication with some complex number of absolute value 1, as above. A similar interpretation is possible for quaternions and Clifford algebras in general.

In game theory and economics, the payoff matrix encodes the payoff for two players, depending on which out of a given (finite) set of strategies the players choose. The expected outcome of the game, when both players play mixed strategies, is obtained by multiplying this matrix on both sides by vectors representing the strategies. The minimax theorem central to game theory is closely related to the duality theory of linear programs, which are often formulated in terms of matrix-vector products.

Early encryption techniques such as the Hill cipher also used matrices. However, due to the linear nature of matrices, these codes are comparatively easy to break. Computer graphics uses matrices to represent objects; to calculate transformations of objects using affine rotation matrices to accomplish tasks such as projecting a three-dimensional object onto a two-dimensional screen, corresponding to a theoretical camera observation; and to apply image convolutions such as sharpening, blurring, edge detection, and more. Matrices over a polynomial ring are important in the study of control theory.

Chemistry makes use of matrices in various ways, particularly since the use of quantum theory to discuss molecular bonding and spectroscopy. Examples are t



---
## Determinant (from Wikipedia)

In mathematics, the determinant is a scalar-valued function of the entries of a square matrix. The determinant of a matrix A is commonly denoted det(A), det A, or |A|. Its value characterizes some properties of the matrix and the linear map represented, on a given basis, by the matrix. In particular, the determinant is nonzero if and only if the matrix is invertible and the corresponding linear map is an isomorphism. However, if the determinant is zero, the matrix is referred to as singular, meaning it does not have an inverse.

The determinant is completely determined by the two following properties: the determinant of a product of matrices is the product of their determinants, and the determinant of a triangular matrix is the product of its diagonal entries.

The determinant of a 2 × 2 matrix is

and the determinant of a 3 × 3 matrix is

### Two by two matrices

The determinant of a 2 × 2 matrix

is denoted either by "det" or by vertical bars around the matrix, and is defined as

3&7\\1&-4}=}=(3\cdot (-4))-(7\cdot 1)=-19.}

### Geometric meaning

If the matrix entries are real numbers, the matrix A represents the linear map that maps the basis vectors to the columns of A.  The images of the basis vectors form a parallelogram that represents the image of the unit square under the mapping.  The parallelogram defined by the columns of the above matrix is the one with vertices at (0, 0), (a, c), (a + b, c + d), and (b, d), as shown in the accompanying diagram.

The absolute value of ad − bc is the area of the parallelogram, and thus represents the scale factor by which areas are transformed by A.

The absolute value of the determinant together with the sign becomes the signed area of the parallelogram. The signed area is the same as the usual area, except that it is negative when the angle from the first to the second vector defining the parallelogram turns in a clockwise direction (which is opposite to the direction one would get for the identity matrix).

To show that ad − bc is the signed area, one may consider a matrix containing two vectors u ≡ (a, c) and v ≡ (b, d) representing the parallelogram's sides. The signed area can be expressed as |u| |v| sin θ for the angle θ between the vectors, which is simply base times height, the length of one vector times the perpendicular component of the other. Due to the sine this already is the signed area, yet it may be expressed more conveniently using the cosine of the complementary angle to a perpendicular vector, e.g. u⊥ = (−c, a), so that |u⊥| |v| cos θ′ becomes the signed area in question, which can be determined by the pattern of the scalar product to be equal to ad − bc according to the following equations:

}=|}|\,|}|\,\sin \,\theta =\left|}^\right|\,\left|}\right|\,\cos \,\theta '=\cdot =ad-bc.}

Thus the determinant gives the area scale factor and the orientation induced by the mapping represented by A. When the determinant is equal to one, the linear mapping defined by the matrix preserves area and orientation.

If an n × n real matrix A is written in terms

### Definition

Let A be a square matrix with n rows and n columns, so that it can be written as

a_&a_&\cdots &a_\&a_&\cdots &a_\\\vdots &\vdots &\ddots &\vdots \&a_&\cdots &a_}.}

etc. are, for many purposes, real or complex numbers. As discussed below, the determinant is also defined for matrices whose entries are in a commutative ring.

The determinant of A is denoted by det(A), or it can be denoted directly in terms of the matrix entries by writing enclosing bars instead of brackets:

a_&a_&\cdots &a_\&a_&\cdots &a_\\\vdots &\vdots &\ddots &\vdots \&a_&\cdots &a_}.}

There are various equivalent ways to define the determinant of a square matrix A, i.e. one with the same number of rows and columns: the determinant can be defined via the Leibniz formula, an explicit formula involving sums of products of certain entries of the matrix. The determinant can also be characterized as the unique function depending on the entries of the matrix satisfying certain properties. This approach can also be used to compute determinants by simplifying the matrices in question.

### Berezin integral

The conventional definition of the determinant, as a sum over permutations over a product of matrix elements, can be written using the somewhat surprising notation of the Berezin integral. In this notation, the determinant can be written as

A\eta \right]\,d\theta \,d\eta =\det A}

-dimensional vectors of anti-commuting Grassmann numbers (aka "supernumbers"), taken from the Grassmann algebra. The

here is the exponential function. The integral sign is meant to be understood as the Berezin integral. Despite the use of the integral symbol, this expression is in fact an entirely finite sum.

This unusual-looking expression can be understood as a notational trick that rewrites the conventional expression for the determinant

}\operatorname (\sigma )a_\cdots a_.}

by using some novel notation. The anti-commuting property of the Grassmann numbers captures the sign (signature) of the permutation, while the integral combined with the

ensures that all permutations are explored. That is, the Taylor's series for

terms, because the square of a Grassmann number is zero, and there are exactly

distinct Grassmann variables. Meanwhile, the integral is defined to vanish, if the corresponding Grassmann number does not appear in the integrand. Thus, the integral selects out only those terms in the

distinct variables; all lower-order terms vanish. Thus, the somewhat magical combination of the integral sign, the use of anti-commuting variables, and the Taylor's series for

just encodes a finite sum, identical to the conventional summation.

This form is popular in physics, where it is often used as a stand-in for the Jacobian determinant. The appeal is that, notationally, the integral takes the form of a path integral, such as in the path integral formulation for quantized Hamiltonian mechanics. An example can be found in the theory of Fadeev–Popov ghosts; although this theory may seem rather abstruse, it's best to keep in mind that the use of the ghost fields is little more than a n

### Generalizations and related notions

Determinants as treated above admit several variants: the permanent of a matrix is defined as the determinant, except that the factors

occurring in Leibniz's rule are omitted. The immanant generalizes both by introducing a character of the symmetric group

### Calculation

Determinants are mainly used as a theoretical tool. They are rarely calculated explicitly in numerical linear algebra, where for applications such as checking invertibility and finding eigenvalues the determinant has largely been supplanted by other techniques. Computational geometry, however, does frequently use calculations related to determinants.

While the determinant can be computed directly using the Leibniz rule this approach is extremely inefficient for large matrices, since that formula requires calculating

matrix. Thus, the number of required operations grows very quickly: it is of order

. The Laplace expansion is similarly inefficient. Therefore, more involved techniques have been developed for calculating determinants.



---
## Eigenvalues and eigenvectors (from Wikipedia)

In linear algebra, an eigenvector ( EYE-gən-) or characteristic vector is a (nonzero) vector that has its direction unchanged (or reversed) by a given linear transformation. More precisely, an eigenvector

when the linear transformation is applied to it:

. The corresponding eigenvalue, characteristic value, or characteristic root is the multiplying factor

(possibly a negative or complex number).

Geometrically, vectors are multi-dimensional quantities with magnitude and direction, often pictured as arrows. A linear transformation rotates, stretches, or shears the vectors upon which it acts. A linear transformation's eigenvectors are those vectors that are only stretched or shrunk, with neither rotation nor shear. The corresponding eigenvalue is the factor by which an eigenvector is stretched or shrunk. If the eigenvalue is negative, the eigenvector's direction is reversed.

The eigenvectors and eigenvalues of a linear transformation serve to characterize

### Matrices

by a factor λ, where λ is a scalar, then

is called an eigenvector of A, and λ is the corresponding eigenvalue. This relationship can be expressed as:

Given an n-dimensional vector space and a choice of basis, there is a direct correspondence between linear transformations from the vector space into itself and n-by-n square matrices. Hence, in a finite-dimensional vector space, it is equivalent to define eigenvalues and eigenvectors using either the language of linear transformations, or the language of matrices.

### Overview

Eigenvalues and eigenvectors feature prominently in the analysis of linear transformations. The prefix eigen- is adopted from the German eigen (cognate with the English word own) for 'proper', 'characteristic', 'own'. Originally used to study principal axes of the rotational motion of rigid bodies, eigenvalues and eigenvectors have a wide range of applications, for example in stability analysis, vibration analysis, atomic orbitals, facial recognition, and matrix diagonalization.

In essence, an eigenvector v of a linear transformation T is a nonzero vector that, when T is applied to it, does not change direction. Applying T to the eigenvector only scales the eigenvector by the scalar value λ, called an eigenvalue. This condition can be written as the equation

referred to as the eigenvalue equation or eigenequation. In general, λ may be any scalar. For example, λ may be negative, in which case the eigenvector reverses direction as part of the scaling, or it may be zero or complex.

The example here, based on the Mona Lisa, provides a simple illustration. Each point on the painting can be represented as a vector pointing from the center of the painting to that point. The linear transformation in this example is called a shear mapping. Points in the top half are moved to the right, and points in the bottom half are moved to the left, proportional to how far they are from the horizontal axis that goes through the middle of the painting. The vectors pointing to each point in the original image are therefore tilted right or left, and made longer or shorter by the transformation. Points along the horizontal axis do not move at all when this transformation is applied. Therefore, any vector that points directly to the right or left with no vertical component is an eigenvector of this transformation, because the mapping does not change its direction. Moreover, these eigenvectors all have an eigenvalue equal to one, because the mapping does not change their length either.

Li

### Eigenvalues and eigenvectors of matrices

Eigenvalues and eigenvectors are often introduced to students in the context of linear algebra courses focused on matrices.

Furthermore, linear transformations over a finite-dimensional vector space can be represented using matrices, which is especially common in numerical and computational applications.

Consider n-dimensional vectors that are formed as a list of n scalars, such as the three-dimensional vectors

These vectors are said to be scalar multiples of each other, or parallel or collinear, if there is a scalar λ such that

Now consider the linear transformation of n-dimensional vectors defined by an n-by-n matrix A,

A_&A_&\cdots &A_\&A_&\cdots &A_\\\vdots &\vdots &\ddots &\vdots \&A_&\cdots &A_\\}\\\\vdots \}=\\\\vdots \}}

=A_v_+A_v_+\cdots +A_v_=\sum _^A_v_.}

If it occurs that v and w are scalar multiples, that is if

then v is an eigenvector of the linear transformation A and the scale factor λ is the eigenvalue corresponding to that eigenvector. Equation (1) is the eigenvalue equation for the matrix A.

Equation (1) can be stated equivalently as

where I is the n-by-n identity matrix and 0 is the zero vector.

### Eigenvalues and eigenfunctions of differential operators

The definitions of eigenvalue and eigenvectors of a linear transformation T remains valid even if the underlying vector space is an infinite-dimensional Hilbert or Banach space. A widely used class of linear transformations acting on infinite-dimensional spaces are the differential operators on function spaces. Let D be a linear differential operator on the space

of infinitely differentiable real functions of a real argument t. The eigenvalue equation for D is the differential equation

The functions that satisfy this equation are eigenvectors of D and are commonly called eigenfunctions.

### General definition

The concept of eigenvalues and eigenvectors extends naturally to arbitrary linear transformations on arbitrary vector spaces. Let V be any vector space over some field K of scalars, and let T be a linear transformation mapping V into V,

We say that a nonzero vector v ∈ V is an eigenvector of T if and only if there exists a scalar λ ∈ K such that

This equation is called the eigenvalue equation for T, and the scalar λ is the eigenvalue of T corresponding to the eigenvector v. T(v) is the result of applying the transformation T to the vector v, while λv is the product of the scalar λ with v.

### Dynamic equations

The simplest difference equations have the form

The solution of this equation for x in terms of t is found by using its characteristic equation

-a_\lambda ^-a_\lambda ^-\cdots -a_\lambda -a_=0,}

which can be found by stacking into matrix form a set of equations consisting of the above difference equation and the k – 1 equations xt–1 = xt–1, ..., xt–k+1 = xt–k+1, giving a k-dimensional system of the first order in the stacked variable vector [xt  ⋅⋅⋅   xt–k+1] in terms of its once-lagged value, and taking the characteristic equation of this system's matrix. This equation gives k characteristic roots λ1, ... , λk, for use in the solution equation

=c_\lambda _^+\cdots +c_\lambda _^.}

A similar procedure is used for solving a differential equation of the form

x}}}+a_x}}}+\cdots +a_}+a_x=0.}

### Calculation

The calculation of eigenvalues and eigenvectors is a topic where theory, as presented in elementary linear algebra textbooks, is often very far from practice.

