1. Bayes' Theorem
Problem 1: The Manufacturing Defect

Question: A factory has two machines, A and B. Machine A produces 60% of items and Machine B produces 40%. 2% of items from A are defective, while 1% from B are defective. If an item is picked at random and found to be defective, what is the probability it was produced by Machine A?

Approach: Use Bayes' Theorem: P(A|D) = [P(D|A) * P(A)] / P(D), where D is the event of being defective.

Working:

P(A) = 0.60, P(B) = 0.40

P(D|A) = 0.02, P(D|B) = 0.01

Total probability of defective P(D):
P(D) = [P(D|A)*P(A)] + [P(D|B)*P(B)]
P(D) = (0.02 * 0.60) + (0.01 * 0.40)
P(D) = 0.012 + 0.004 = 0.016

Apply Bayes' Formula:
P(A|D) = (0.02 * 0.60) / 0.016
P(A|D) = 0.012 / 0.016 = 12 / 16 = 3/4

Final Answer: 0.75 or 3/4

Problem 2: The Truth Teller

Question: A speaks truth in 75% of cases and B in 80% of cases. In what percentage of cases are they likely to contradict each other in stating the same fact?

Approach: Contradiction happens when (A speaks truth AND B lies) OR (A lies AND B speaks truth).

Working:

P(A_truth) = 0.75, P(A_lie) = 0.25

P(B_truth) = 0.80, P(B_lie) = 0.20

P(Contradict) = [P(A_truth) * P(B_lie)] + [P(A_lie) * P(B_truth)]

P(Contradict) = (0.75 * 0.20) + (0.25 * 0.80)

P(Contradict) = 0.15 + 0.20 = 0.35

Percentage = 0.35 * 100 = 35%

Final Answer: 35%

2. Binomial Distribution
Problem 3: Hitting the Target

Question: The probability of a man hitting a target is 1/4. If he fires 7 times, what is the probability of hitting the target at least twice?

Approach: P(At least 2) = 1 - [P(X=0) + P(X=1)]. Use P(X=r) = nCr * p^r * q^(n-r).

Working:

n = 7, p = 1/4, q = 3/4

P(X=0) = 7C0 * (1/4)^0 * (3/4)^7 = 1 * 1 * (2187 / 16384)

P(X=1) = 7C1 * (1/4)^1 * (3/4)^6 = 7 * (1/4) * (729 / 4096) = 5103 / 16384

P(X < 2) = (2187 + 5103) / 16384 = 7290 / 16384

P(X >= 2) = 1 - 7290 / 16384 = 9094 / 16384

Simplify: 4547 / 8192

Final Answer: 4547 / 8192

Problem 4: Multiple Choice Guessing

Question: In a test of 5 questions, each with 4 options, what is the probability that a student gets at least 4 correct answers by guessing?

Approach: Binomial distribution with n=5, p=1/4, and X >= 4.

Working:

P(X=4) = 5C4 * (1/4)^4 * (3/4)^1 = 5 * (1/256) * (3/4) = 15 / 1024

P(X=5) = 5C5 * (1/4)^5 * (3/4)^0 = 1 * (1/1024) * 1 = 1 / 1024

P(X >= 4) = 15/1024 + 1/1024 = 16 / 1024

Simplify: 1 / 64

Final Answer: 1/64

3. Conditional Probability
Problem 5: Family Composition

Question: A family has two children. Given that at least one of them is a boy, what is the probability that both are boys?

Approach: P(A|B) = P(A AND B) / P(B). Let A = both are boys, B = at least one is a boy.

Working:

Sample Space S = {BB, BG, GB, GG}

Event B (At least one boy) = {BB, BG, GB}, so P(B) = 3/4

Event A AND B (Both boys) = {BB}, so P(A AND B) = 1/4

P(A|B) = (1/4) / (3/4) = 1/3

Final Answer: 1/3

Problem 6: Two Dice Sum

Question: Two dice are thrown. If the sum of the numbers is 7, what is the probability that at least one die shows a 3?

Approach: Reduce the sample space to only outcomes where the sum is 7.

Working:

Event S_7 (Sum is 7) = {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}. Total = 6 outcomes.

Event T (At least one 3) within S_7: {(3,4), (4,3)}. Total = 2 outcomes.

P(T|S_7) = 2 / 6 = 1/3

Final Answer: 1/3

4. Combinations & Permutations
Problem 7: Committee Selection

Question: A committee of 5 is to be formed from 6 gentlemen and 4 ladies. What is the probability that the committee contains at least 3 ladies?

Approach: Total ways = 10C5. Favorable cases = (3L, 2G) + (4L, 1G).

Working:

Total Ways = 10C5 = (10*9*8*7*6) / (5*4*3*2*1) = 252

Case 1 (3 Ladies, 2 Gents) = 4C3 * 6C2 = 4 * 15 = 60

Case 2 (4 Ladies, 1 Gent) = 4C4 * 6C1 = 1 * 6 = 6

Total Favorable = 60 + 6 = 66

Probability = 66 / 252

Simplify: 11 / 42

Final Answer: 11/42

Problem 8: Word Arrangement

Question: The letters of the word 'ARTICLE' are arranged at random. Find the probability that the vowels occupy even places.

Approach: Identify vowel positions and use permutations. Word: A, R, T, I, C, L, E (7 letters). Vowels: A, I, E (3). Consonants: R, T, C, L (4).

Working:

Total arrangements = 7! = 5040

Even places in a 7-letter word are 2nd, 4th, and 6th. (3 places).

Number of ways to place 3 vowels in 3 even places = 3! = 6

Number of ways to place 4 consonants in remaining 4 places = 4! = 24

Total Favorable = 6 * 24 = 144

Probability = 144 / 5040

Simplify: 1 / 35

Final Answer: 1/35