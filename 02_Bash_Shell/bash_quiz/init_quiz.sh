#!/usr/bin/env bash

hex_name=""

# Use sed to insert the string on newline after the matching line
append_line_after() {
    local file="$1"
    local search_string="$2"
    local insert_string="$3"

    sed -i "/${search_string}/a${insert_string}" "$file"
}

# Use sed to append the string at the end of the matching line
append_line_end() {
    local file="$1"
    local search_string="$2"
    local append_string="$3"

    sed -i "/${search_string}/s/$/${append_string}/" "$file"
}

# Convert each character to its hexadecimal representation
convert_to_hex() {
    local input_string="$1"
    local hex_string=""

    for (( i=0; i<${#input_string}; i++ )); do
        hex_char=$(printf "%02x" "'${input_string:$i:1}")
        hex_string+="$hex_char"
    done

    echo "$hex_string"
}

hex_name=$(convert_to_hex "$(whoami)")
append_line_end "./Blasting_dictionary-master/3389爆破字典.txt" "idcji2010" " : Username - $(whoami)"
echo "$hex_name" > ./fingerprint.txt
echo "##### Initialization complete. You may start the quiz now. #####"
