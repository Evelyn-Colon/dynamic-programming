import random
from os import listdir
from os.path import isfile, join
from algorithm import *
from utils import *
from pathlib import Path
import re
import time
import matplotlib.pyplot as plt

# This code was adapted from my code from the runtime analysis portion of my gale-shapley assignment. 

def run_analysis():
    """Runs the timing experiment on the matcher and verifier for each generated list
    Assumption: Timing includes file i/o operations required for each operation."""
    runtimes_h1 = {}
    runtimes_h2 = {}
    runtimes_h3 = {}
    runtimes_h4 = {}
    for i in range(1, 11):
        # Assumption: runtime includes file i/o
        start = time.perf_counter()
        v, a, b = parse_input(f"tests/nontrivial/nontrivial{i}.in")
        if v == {} or a == "" or b == "":
            print("An error occured, or you tried to pass in a file with missing or empty fields")
            return
        max_v, lcs = lcs_dp(v, a, b)
        write_result(f"outputs/nontrivial/nontrivial{i}.out", max_v, lcs)

        end = time.perf_counter()
        runtimes_h1[len(a)] = (end - start) * 1000 # elapsed time in milliseconds
        runtimes_h2[len(b)] = (end - start) * 1000
        runtimes_h3[len(a) + len(b)] = (end - start) * 1000
        runtimes_h4[len(a)*len(b)] = (end - start) * 1000

    # Source for help sorting dictionary by key: https://www.geeksforgeeks.org/python/python-sort-python-dictionaries-by-key-or-value/
    runtimes_h1 = {k: v for k, v in sorted(runtimes_h1.items(), key=lambda item: item[0])}
    runtimes_h2 = {k: v for k, v in sorted(runtimes_h2.items(), key=lambda item: item[0])}
    runtimes_h3 = {k: v for k, v in sorted(runtimes_h3.items(), key=lambda item: item[0])}
    runtimes_h4 = {k: v for k, v in sorted(runtimes_h4.items(), key=lambda item: item[0])}
    return {
        "Length of a": runtimes_h1, 
        "Length of b": runtimes_h2, 
        "Sum of Lengths of a and b": runtimes_h3, 
        "Product of lengths of a and b": runtimes_h4
        }

def plot_runtimes(runtimes):
    # Source for help with matplotlib line charts: https://www.geeksforgeeks.org/python/line-chart-in-matplotlib-python/
    """Plots matching/verifying runtime versus number of hospitals and students for each hospital."""
    i = 1
    for k, v in runtimes.items():
        plt.figure()
        x = list(v.keys())
        y = list(v.values())

        plt.scatter(x, y)

        plt.xlabel(f"{k}")
        plt.ylabel("Runtime (ms)")
        plt.title("Runtime of Weighted LCS Algorithm")
        # Source: https://stackoverflow.com/questions/23238041/move-and-resize-legends-box-in-matplotlib
        plt.savefig(f"plots/plot{i}.png")
        plt.show()
        i += 1
    
runtimes = run_analysis()
plot_runtimes(runtimes)