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
                letter_val = line.split()
                letter = letter_val[0]
                if (len(letter) != 1):
                    raise ValueError(f"Character should only have length 1: {letter}")
                val = int(letter_val[1])
                v[letter] = val
            a = file.readline().strip()
            if not a:
                raise ValueError("Missing or empty a!")
            b = file.readline().strip()
            if not b:
                raise ValueError("Missing or empty b")
            return v, a, b

    except FileNotFoundError as e:
        print(e)
        return {}, "", ""  
    except ValueError as e:
        print(e)
        return {}, "", "" 
    except IndexError as e:
        print(e)
        return {}, "", ""  

def write_result(out_filepath, max_v, lcs):
    pass

