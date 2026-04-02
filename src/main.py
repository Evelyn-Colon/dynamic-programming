import sys
from utils import parse_input, write_result
from algorithm import lcs_dp
def main():
    try:
        in_filepath = sys.argv[1]
        out_filepath = sys.argv[2]
    except IndexError:
        print("Usage: python3 src/main.py <input_filepath> <output_filepath>")   
        return    
    v, a, b = parse_input(in_filepath)
    print(v)
    print(a)
    print(b)
    if v == {} or a == "" or b == "":
        print("An error occured, or you tried to pass in a file with missing or empty fields")
        return
    max_v, lcs = lcs_dp(v, a, b)
    print(max_v)
    print(lcs)
    write_result(out_filepath, max_v, lcs)
    

if __name__ == "__main__":
    main()