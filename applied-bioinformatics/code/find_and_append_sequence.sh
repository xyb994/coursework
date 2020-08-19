#!/bin/bash

main() {
  check_and_store_arguments "$@"
  find_header_and_sequence_to_append
  check_there_are_match
  append_header_and_sequence
}

check_and_store_arguments() {
  if [ "$#" -ne 4 ]; then
    echo "4 arguments required."
    echo ""
    echo "Usage: $0 <sequences_dir> <species_id> <sequence_id> <file_out>"
    echo "Example: $0 ~/dir-to/species-faa GCA_9085 CAL34838.1 og001_seq.fasta"
    echo ""
    exit 1
  fi

  SEQUENCES_DIR="$1"
  SPECIES_ID="$2"
  SEQUENCE_ID="$3"
  FILE_OUT="$4"
}

find_header_and_sequence_to_append() {
  # look for SEQUENCE_ID in a species' FAA file to get sequence header
  header_to_append=$(cat "$SEQUENCES_DIR"/"$SPECIES_ID"*.faa \
                       | grep "$SEQUENCE_ID")

  # store sequences content
  # starting below matching SEQUENCE_ID header to next ">" character
  # sed regex adopted from https://stackoverflow.com/a/38978201/3250423
  sequence_to_append=$(cat "$SEQUENCES_DIR"/"$SPECIES_ID"*.faa \
                         | sed -n "/$SEQUENCE_ID/,/>/{/$SEQUENCE_ID/!{/>/!p}}")
}

check_there_are_match() {
  # if header_to_append or sequence_to_append is empty, exit
  if [[ -z "$header_to_append" || -z "$sequence_to_append" ]]; then
    echo "Could not find matching sequence $SEQUENCE_ID"
    exit 1
  fi
}

append_header_and_sequence() {
  echo "${header_to_append//"$SEQUENCE_ID"/"$SPECIES_ID $SEQUENCE_ID"}" \
          >> "$FILE_OUT"
  echo "$sequence_to_append" >> "$FILE_OUT"
}

main "$@"
