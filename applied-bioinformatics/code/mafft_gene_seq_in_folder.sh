#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo ""
  echo "Error: <sequence_dir> required"
  echo ""
  echo "Usage: $0 <sequence_dir>"
  echo ""
  exit 1
fi

SEQUENCE_DIR="$1"
MAFFT_MSA_DIR="mafft_msa_$(date +%Y-%m-%d-%H.%M.%S)"

cd "$SEQUENCE_DIR" || exit
mkdir -p "$MAFFT_MSA_DIR"

# run MAFFT on each fasta file in <sequence_dir>
for fasta_file in ./*.fasta
do
    output_file_name="mafft_msa_${fasta_file/.\//}"
    echo "Running MAFFT for gene sequences in $fasta_file"
    mafft --auto --quiet "$fasta_file" > "$MAFFT_MSA_DIR/$output_file_name"
done

echo "Check MAFFT MSA result at directory $SEQUENCE_DIR/$MAFFT_MSA_DIR"
