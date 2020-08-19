# Geoderms

A group project for \_\_\_ at \_\_\_ in Spring 2020 by \_\_\_, \_\_\_, \_\_\_, \_\_\_ and Yibo \_\_.

This folder currently only contains code written by myself.

## Prerequisites

* Anaconda virtual environment with Python 3.7
* Orthofinder
* MAFFT
* RaxML

## Example Usage

1. Acquire FAA proteome files for selected prokaryote species: `pro_____ote query.txt`

2. Run orthofinder to get Orthogroups.csv: `orthofinder2 -S diamond -f /home/___/share/___/geoderms/data/proqueryote-faa-79-2020-04-24-1242.20/`

3. Generate 2 CSV files, one with max of 128 USCO orthogroup row, another with the rest of OG rows with cell content replaced as gene count and less than 75% 0 gene count row eliminated: `./process_ogs_csv.py -t 1.0 /home/___/share/___/geoderms/data/prok-prot-faa-79-20200416/Results_Apr21_1/Orthogroups.csv`

5. Make orthologs sequences file: `./make_og_sequences.py /home/___/share/___/geoderms/data/prok-prot-faa-79-20200416/Results_Apr21_1/Orthogroups.csv.1.0.csv /home/___/share/___/geoderms/data/prok-prot-faa-79-20200416/`

6. Run MAFFT on all ortholog sequences: `./mafft_gene_seq_in_folder.sh "/home/___/share/___/geoderms/data/prok-prot-faa-79-20200416/Orthogroup_sequences_20200422-13.49.12/"`

7. Prepare data for RAxML:
```
cd /home/___/share/___/geoderms/data/prok-prot-faa-79-20200416/Orthogroup_sequences_20200422-13.49.12/mafft_msa_2020-04-28-20.12.53/128/
./concatenate_sequences.sh
```

8. Run raxmlHPC: `raxmlHPC-PTHREADS -M -f a -m PROTGAMMAAUTO -s allseqs.fas -q allseqs.partitions.WAG.txt -p 3523953 -x 3523953 -# 3 -n allin1_0506_1`

9. Check consensus tree file at `/home/___/share/___/geoderms/data/prok-prot-faa-79-20200416/Orthogroup_sequences_20200422-13.49.12/mafft_msa_2020-04-28-20.12.53/128/RAxML_bestTree.allin1_0506_1`