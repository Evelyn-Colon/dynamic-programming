import re

def parse_input(filename):
    """This function was adapted from a similar function, read_requests, in my greedy-algorithms assignment.
    This function takes a filename as input and returns a dictionary of an alphabet and matching values, a 
    string sequence a, and a string sequence b which will be used in the DP algorithm."""
    try:
        with open(filename, "r") as file:
            line_1 = file.readline()
            if not line_1 or line_1.strip() == "":
                raise ValueError("First line is empty!")
            k = int(line_1)
            v = {}
            for i in range(k):
                line = file.readline()
                if (not line or line.strip() == ""):
                    raise ValueError("Missing alphabet letter")
                letter_val = line.lower().split()
                letter = letter_val[0]
                if (len(letter) != 1):
                    raise ValueError(f"Character should only have length 1: {letter}")
                if letter in v:
                    raise KeyError("Character is already listed once in the alphabet! No duplicates.")
                val = int(letter_val[1])
                v[letter] = val    
            a = file.readline().strip().lower()
            if not a:
                raise ValueError("Missing or empty a!")
            b = file.readline().strip().lower()
            a_clean = re.sub(r'[^a-z0-9]', '', a)
            b_clean = re.sub(r'[^a-z0-9]', '', b)
            # Source for help removing extra nonalphanumeric characters from strings: https://www.geeksforgeeks.org/python/python-remove-all-characters-except-letters-and-numbers/
            if not b_clean:
                raise ValueError("Missing or empty b")
            # Source for help with subsets
            if not set(b_clean).issubset(v.keys()) or not set(a_clean).issubset(v.keys()):
                raise KeyError("alphabet does not contain all of the characters in a and b!")
            return v, a_clean, b_clean

    except FileNotFoundError as e:
        print(e)
        return {}, "", ""  
    except ValueError as e:
        print(e)
        return {}, "", "" 
    except IndexError as e:
        print(e)
        return {}, "", ""  
    except KeyError as e:
        print(e)
        return {}, "", ""

def write_result(out_filepath, max_v, lcs):
    """This function takes in an output filepath, the maximum value, and the least common subsequence itself
    and writes the data to the file"""
    with open(out_filepath, "w") as file:
        file.write(f"{max_v}\n{lcs}")

