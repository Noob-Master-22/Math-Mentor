Basics & Bayes

P(A U B) = P(A) + P(B) - P(A intersection B)

P(A/B) = P(A intersection B) / P(B)

Independent Events: P(A intersection B) = P(A) * P(B)

Total Probability: P(E) = Sum [ P(Ai) * P(E/Ai) ]

Bayes' Theorem: P(A1/E) = [ P(E/A1) * P(A1) ] / Sum [ P(E/Ai) * P(Ai) ]

Distributions

Expectation E(X) = Sum (xi * pi)

Variance Var(X) = E(X^2) - [E(X)]^2

Standard Deviation (SD) = sqrt(Variance)

Binomial Dist: P(X=r) = nCr * p^r * q^(n-r)

Binomial Mean = np

Binomial Var = npq

Statistics

Combined Mean = (n1m1 + n2m2) / (n1 + n2)

Variance of first n natural numbers = (n^2 - 1) / 12

Coefficient of Variation = (SD / Mean) * 100


## Addition Theorem
- **General Rule:** - LaTeX: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
  - ASCII: P(A or B) = P(A) + P(B) - P(A and B)
  - **Common Mistakes:** Forgetting to subtract the intersection $P(A \cap B)$, leading to probabilities $> 1$.

## Conditional Probability
- **Definition:** - LaTeX: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
  - ASCII: P(A given B) = P(A and B) / P(B)
  - **Common Mistakes:** Dividing by $P(A)$ instead of the condition $P(B)$.

## Bayes' Theorem
- **Formula:** - LaTeX: $P(A_i|B) = \frac{P(B|A_i)P(A_i)}{\sum P(B|A_j)P(A_j)}$
  - ASCII: P(Ai|B) = [P(B|Ai) * P(Ai)] / Sum[P(B|Aj) * P(Aj)]
  - **Common Mistakes:** Misidentifying the prior $P(A_i)$ vs the likelihood $P(B|A_i)$.

## Independent Events
- **Definition:** - LaTeX: $P(A \cap B) = P(A) \cdot P(B)$
  - ASCII: P(A and B) = P(A) * P(B)
  - **Common Mistakes:** Confusing "Independent" with "Mutually Exclusive" (where $P(A \cap B) = 0$).
  
---
## Bayes' theorem (from Wikipedia)

Bayes' theorem (alternatively Bayes' law or Bayes' rule), named after Thomas Bayes (), gives a mathematical rule for inverting conditional probabilities, allowing the probability of a cause to be found given its effect. For example, with Bayes' theorem, the probability that a patient has a disease given that they tested positive for that disease can be found using the probability that the test yields a positive result when the disease is present. The theorem was developed in the 18th century by Bayes and independently by Pierre-Simon Laplace.

One of Bayes' theorem's many applications is Bayesian inference, an approach to statistical inference, where it is used to invert the probability of observations given a model configuration (i.e., the likelihood function) to obtain the probability of the model configuration given the observations (i.e., the posterior probability).

### Statement of theorem

Bayes' theorem is stated mathematically as the following equation:

is a conditional probability: the probability of event

is true. It is also called the posterior probability of

is also a conditional probability: the probability of event

is true. It can also be interpreted as the likelihood of

are the probabilities of observing

respectively without any given conditions.

, the quantity of interest, is often called 'the prior probability' (prior to new evidence). Technically both

could be called prior, unconditioned, or marginal probabilities.

Bayes' theorem may be derived from the relation between joint and conditional probabilities. The joint probability of the events

, is equal to the conditional probability of

The two products must therefore be equal to each other:

### Interpretations

The interpretation of Bayes' rule depends on the interpretation of probability ascribed to the terms. The two predominant classes of interpretation are described below.



---
## Binomial distribution (from Wikipedia)

In probability theory and statistics, the binomial distribution with parameters n and p is the discrete probability distribution of the number of successes in a sequence of n independent experiments, each asking a yes–no question, and each with its own Boolean-valued outcome: success (with probability p) or failure (with probability q = 1 − p). A single success/failure experiment is also called a Bernoulli trial or Bernoulli experiment, and a sequence of outcomes is called a Bernoulli process. For a single trial, that is, when n = 1, the binomial distribution is a Bernoulli distribution. The binomial distribution is the basis for the binomial test of statistical significance.

The binomial distribution is frequently used to model the number of successes in a sample of size n drawn with replacement from a population of size N. If the sampling is carried out without replacement, the draws are not independent and so the resulting distribution is a hypergeometric distribution, not a binomial one.  However, for N much larger than n, the binomial distribution remains a good approximation, and is widely used.



---
## Probability theory (from Wikipedia)

Probability theory or probability calculus is the branch of mathematics concerned with probability. Although there are several different probability interpretations, probability theory treats the concept in a rigorous mathematical manner by expressing it through a set of axioms. Typically these axioms formalise probability in terms of a probability space, which assigns a measure taking values between 0 and 1, termed the probability measure, to a set of outcomes called the sample space. Any specified subset of the sample space is called an event.

Central subjects in probability theory include discrete and continuous random variables, probability distributions, and stochastic processes (which provide mathematical abstractions of non-deterministic or uncertain processes or measured quantities that may either be single occurrences or evolve over time in a random fashion).

Although it is not possible to perfectly predict random events, much can be said about their behavior. Two major results in probability theory describing such behaviour are the law of large numbers and the central limit theorem.

As a mathematical foundation for statistics, probability theory is essential to many human activities that involve quantitative analysis of data. Methods of probability theory also apply to descriptions of complex systems given only partial knowledge of their state, as in statistical mechanics or sequential estimation. A great discovery of twentieth-century physics was the probabilistic

### Treatment

Most introductions to probability theory treat discrete probability distributions and continuous probability distributions separately. The measure theory-based treatment of probability covers the discrete, continuous, a mix of the two, and more.

### Classical probability distributions

Certain random variables occur very often in probability theory because they well describe many natural or physical processes. Their distributions, therefore, have gained special importance in probability theory. Some fundamental discrete distributions are the discrete uniform, Bernoulli, binomial, negative binomial, Poisson and geometric distributions. Important continuous distributions include the continuous uniform, normal, exponential, gamma and beta distributions.

### Convergence of random variables

In probability theory, there are several notions of convergence for random variables. They are listed below in the order of strength, i.e., any subsequent notion of convergence in the list implies convergence according to all of the preceding notions.

converges weakly to the random variable

if their respective CDF converges

is continuous. Weak convergence is also called convergence in distribution.

Most common shorthand notation:

The sequence of random variables

is said to converge towards the random variable

\mathbb  \left(\left|X_-X\right|\geq \varepsilon \right)=0}

Most common shorthand notation:

The sequence of random variables

is said to converge towards the random variable

. Strong convergence is also known as almost sure convergence.

Most common shorthand notation:

As the names indicate, weak convergence is weaker than strong convergence. In fact, strong convergence implies convergence in probability, and convergence in probability implies weak convergence. The reverse statements are not always true.

