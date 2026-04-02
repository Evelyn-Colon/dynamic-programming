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

![Recurrence Relation](recurrence_relation.png)

Where $$OPT(i,j) = $$ the value of the common subsequence with maximum value when considering $$a_{1}...a{i}$$ and $$b_{1}...b{j}$$.

## Explanation of the Recurrence Relation

There are two base cases in this recurrence relation:
- If the set of characters in `a` being considered is empty, then the maximum value must be zero; this is trivial.
- Likewise, if the set of characters in `b` being considered is empty, then the maximum value must be zero.

Additionally, there are two recursive cases in this recurrence relation:
- If the characters $$a_{i}$$ and $$b_{j}$$ are equal, this means that we can consider adding a new character to the LCS.
- This means there are three possible solutions we can consider to this subproblem:
    - If we add the shared character to the LCS, that means that neither $$a_{i}$$ and $$b_{j}$$ could have been considered before this point; if one of them had, then we would not have a one-to-one pairing if we added the shared character again. Either $$a_{i}$$ would be matched to more than one position in b, or vice versa. Therefore, we add the value of the shared character to the maximum value of a common subsequence in which $$a_{1}...a{i-1}$$ and $$b_{1}...b{j-1}$$ are considered. This gives us the first term in the `max` expression on the third line of the recurrence relation.
    - If we choose not to add the shared character, then we have two possibilities which signify that $$OPT(i,j)$$ is basically the same as if we **could not** add the character; essentially, we treat either $$a_{i}$$ or $$b_{j}$$ as though it does not exist in the characters to be considered:
        - $$OPT(i,j)$$ is the maximum value of a common subsequence obtained when considering the first `i-1` characters in `a` and the first `j` characters in `b` (treating $$a_{i}$$ as though it is not available for matching). This gives us the second term in the `max` expression on the third line of the recurrence relation. 
        - $$OPT(i,j)$$ is the maximum value of a common subsequence obtained when considering the first `i` characters in `a` and the first `j-1` characters in `b` (treating $$b_{j}$$ as though it is not available for matching.) This gives us the third term in the `max` expression on the third line of the recurrence equation.
- If $$a_{i}$$ and $$b_{j}$$ are **not** equal, the logic is similar, except now we cannot consider the first possibility described above because we cannot add a new value. The second and third cases remain the same, and those are now the only cases being considered because $$a_{i}$$ and $$b_{j}$$ cannot be matched.        