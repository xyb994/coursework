#!/bin/bash

# https://github.com/ChrisCreevey/catsequences
# concatenating multiple fasta alignments for input of raxml consensus tree
wget https://raw.githubusercontent.com/ChrisCreevey/catsequences/master/catsequences.c
cc catsequences.c -o catsequences -lm

# create a list containing names of fasta files and run catsequences
ls -- *.fasta > fasta_file_list
catsequences fasta_file_list

# modify allseqs.parition.txt
# to specify AA substitution models and meet RAxml -q file syntax
sed 's/^/WAG, /' allseqs.partitions.txt > allseqs.partitions.WAG.txt
sed -i 's/;//' allseqs.partitions.WAG.txt
