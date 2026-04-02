import sys
from utils import parse_input, write_result
from algorithm import lcs_dp
def main():
    try:
        in_filepath = sys.argv[1]
        out_filepath = sys.argv[2]
        v, a, b = parse_input(in_filepath)
        print(v)
        print(a)
        print(b)
        # max_v, lcs = lcs_dp(v, a, b)
        # write_result(out_filepath, max_v, lcs)
    except IndexError:
        print("Usage: python3 src/main.py <input_filepath> <output_filepath>")   

if __name__ == "__main__":
    main()