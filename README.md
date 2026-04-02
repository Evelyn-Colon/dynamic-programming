# dynamic-programming
Preconditions:
- File is not empty
- The alphabet cannot be the empty set, and strings a and b may not be empty. 

# Question 1: Empirical Comparison

The input files used for analysis are located in the directory `tests/nontrivial`, and the corresponding outputs are located in `outputs/nontrivial`. I used a few different comparisons:
- the relationship between the length of a and the runtime, 
- the relationship between the length of b and the runtime, 
- the relationship between the combined length of a and b and the runtime, and 
- the relationship between the product of the lengths of a and b and the runtime.

The graphs are below:

![Runtime vs. Length of A](plots/1.png)
![Runtime vs. Length of B](plots/2.png)
![Runtime vs. Length of A + Length of B](plots/3.png)
![Runtime vs. Length of A * Length of B](plots/4.png)

There appears to be no clear relationship between the length of `A` and the runtime or the length of `B` and the runtime. There appears to be a slightly stronger relationship between the length of `A` + the length of `B` and the runtime, indicating that the runtime is dependent on the size of both input strings. The relationship between the product of the lengths of `A` and `B` and the runtime seems to be a strong linear relationship, which seems to suggest the runtime is in `O(m * n)`, where `m` is the length of `A` and `n` is the length of `B`.

I referred to the following resources to help me formulate test cases for the runtime analysis:
- https://randomwordgenerator.com/ (generate random words for small/trivial cases)
- https://word.tips/unscramble-word-finder/ (find anagrams for the second string in small/trivial cases)
- https://randomwordgenerator.com/sentence.php (random sentences for nontrivial cases)
- https://www.calculatorsoup.com/calculators/statistics/random-number-generator.php (randomly assigned weights for alphabet characters)

# Question 2: Recurrence Relation

![Recurrence Relation](recurrence_relation.png)

Where $$OPT(i,j) = $$ the value of the common subsequence with maximum value when considering $$a_{1}...a{i}$$ and $$b_{1}...b{j}$$.

I referred to this Reddit post for help formatting the recurrence relation correctly in LaTeX: https://www.reddit.com/r/LaTeX/comments/15wwidi/multiple_lines_in_curly_bracket_i_want_make_the/#:~:text=Comments%20Section,%5C%5D

## Explanation of the Recurrence Relation

There are two base cases in this recurrence relation:
- If the set of characters in `a` being considered is empty, then the maximum value must be zero; this is trivial.
- Likewise, if the set of characters in `b` being considered is empty, then the maximum value must be zero.

Additionally, there are two recursive cases in this recurrence relation:
- If the characters $$a_{i}$$ and $$b_{j}$$ are equal, this means that we can consider adding a new character to the LCS.
- This means there are three possible solutions we can consider to this subproblem:
    - If we add the shared character to the LCS, that means that neither $$a_{i}$$ and $$b_{j}$$ could have been considered before this point; if one of them had, then we would not have a one-to-one pairing if we added the shared character again. Either $$a_{i}$$ would be matched to more than one position in b, or vice versa. Therefore, we add the value of the shared character to the maximum value of a common subsequence in which $$a_{1}...a_{i-1}$$ and $$b_{1}...b_{j-1}$$ are considered. This gives us the first term in the `max` expression on the third line of the recurrence relation.
    - If we choose not to add the shared character, then we have two possibilities which signify that $$OPT(i,j)$$ is basically the same as if we **could not** add the character; essentially, we treat either $$a_{i}$$ or $$b_{j}$$ as though it does not exist in the characters to be considered:
        - $$OPT(i,j)$$ is the maximum value of a common subsequence obtained when considering the first `i-1` characters in `a` and the first `j` characters in `b` (treating $$a_{i}$$ as though it is not available for matching). This gives us the second term in the `max` expression on the third line of the recurrence relation. 
        - $$OPT(i,j)$$ is the maximum value of a common subsequence obtained when considering the first `i` characters in `a` and the first `j-1` characters in `b` (treating $$b_{j}$$ as though it is not available for matching.) This gives us the third term in the `max` expression on the third line of the recurrence equation.
- If $$a_{i}$$ and $$b_{j}$$ are **not** equal, the logic is similar, except now we cannot consider the first possibility described above because we cannot add a new value. The second and third cases remain the same, and those are now the only cases being considered because $$a_{i}$$ and $$b_{j}$$ cannot be matched.

# Question 3: Big-Oh
## Pseudocode
```plaintext
input: a, b, v (values corresponding to characters in alphabet)
M: solution array
for i in 0...m
    M[i, 0] = 0
for j in 0...n
    M[0, j] = 0

for i in 1...m
    for j in 1...n
        if a[i] = b[j]
            M[i, j] = max(M[i - 1, j - 1] + v[a[i]], M[i - 1, j], M[i, j - 1])
        else
            M[i, j] = max(M[i - 1, j], M[i, j - 1])
return M[m, n]
```

The above pseudocode retrieves the value of the HVLCS, but we need to use backtracking to retrieve the actual value of the HVLCS:

```plaintext
lcs = empty string we will use to build the solution
Find-Solution(i, j)
    if i = 0 or j = 0
        return
    if a[i] = b[i] and M[i, j] = M[i - 1, j - 1] + v[a[i]]
        lcs += Find-Solution(i - 1, j - 1) + a[i]
    else if M[i, j] = M[i - 1, j]
        lcs += Find-Solution(i - 1, j)
    else
        lcs += Find-Solution(i, j - 1)
```

The above pseudocode constructs the HVLCS from the solution array `M`.
