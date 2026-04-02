# dynamic-programming
Preconditions:
- File is not empty
- The alphabet cannot be the empty set, and strings a and b may not be empty. 

# Sources for help generating random test cases
https://randomwordgenerator.com/ (generate random words for small/trivial cases)
https://word.tips/unscramble-word-finder/ (find anagrams for the second string in small/trivial cases)
https://randomwordgenerator.com/sentence.php (random sentences for nontrivial cases)
https://www.calculatorsoup.com/calculators/statistics/random-number-generator.php (randomly assigned weights for alphabet characters)

# Question 2: Recurrence Relation

\[
    OPT(i, j) = \begin{cases}
    0 & \text{if } i = 0 \\
    0 & \text{if } j = 0 \\
    \max(OPT(i-1, j-1) + v_{c}, OPT(i-1, j), OPT(i, j-1)) & \text{if } a_{i} = b_{j} = c \\
    \max(OPT(i-1, j), OPT(i, j-1)) & \text{otherwise}
    \end{cases}

\]