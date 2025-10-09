#!/usr/bin/env bash

echo -e "\n\n\n##### QUIZ COMPLETE #####\n"

if [ ! -f "./fingerprint.txt" ]; then
    echo "Error: fingerprint.txt not found. Please run init_quiz.sh first."
    echo "Delete your answers file and try again."
    exit 1
fi

name=$(cat ./fingerprint.txt | xxd -r -p)
line2=$(head -n 2 ~/Desktop/*_answers.txt)
name2=$(echo "$line2" | xxd -r -p)
echo "       Detected user: $name"
echo "Name in answers file: $name2"

cat ~/Desktop/*_answers.txt
