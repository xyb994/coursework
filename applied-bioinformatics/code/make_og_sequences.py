#!/usr/bin/env python

import os
import sys
import subprocess
import time

import numpy as np
import pandas as pd


def find_and_append_sequence(sequences_dir, species_id, sequence_id, file_out):
    # this function runs find_and_append_sequence.sh with provided arguments
    # to append matching header and its sequences to file_out
    subprocess.check_call("./find_and_append_sequence.sh "
                          f"{sequences_dir} {species_id} "
                          f"{sequence_id} {file_out}",
                          shell=True)


if len(sys.argv) < 3:
    print("Usage:   ./make_og_sequences.py <FILE_IN> <SEQUENCES_DIR>")
    print("Example: ./make_og_sequences.py "
          "Orthogroups.csv.1.0.csv ../../Bryobacterales")
    sys.exit()

FILE_IN = sys.argv[1]
SEQUENCES_DIR = sys.argv[2]

# verify species sequence dir exist, otherwise exit
if not os.path.isdir(SEQUENCES_DIR):
    print(f"No such directory: {SEQUENCES_DIR}")
    sys.exit()

# create directory for orthologs sequence file
date_time_str = time.strftime('%Y%m%d-%H.%M.%S', time.localtime())
og_seq_dir = f"{SEQUENCES_DIR}/Orthogroup_sequences_{date_time_str}"
os.mkdir(og_seq_dir)

# read CSV data into a Pandas DataFrame
df = pd.read_csv(FILE_IN, delimiter=",")
orthogroups_count = len(df)
species_count = len(df.columns) - 3

print("\nFinished reading csv data,\n"
      f"df.shape={df.shape}\n"
      f"orthogroups_count={orthogroups_count}\n"
      f"species_count={species_count}\n")

# iterate through orthogroup rows
for row in range(orthogroups_count):
    # first column of each row contains OG number
    # we use it as output ortholog's filename
    orthogroup_number = df.iat[row, 0]
    file_out = f"{og_seq_dir}/{orthogroup_number}.fasta"

    print("Appending sequence file for orthogroup "
          f"{orthogroup_number} to {file_out}")

    # iterate through each column with sequence ID
    for column in range(1, species_count + 1):
        species_id = df.columns[column].split("_ASM", 1)[0]
        sequence_id = df.iat[row, column]
        # calling function to invoke find_and_append_sequence.sh for each cell
        find_and_append_sequence(SEQUENCES_DIR, species_id, sequence_id,
                                 file_out)
