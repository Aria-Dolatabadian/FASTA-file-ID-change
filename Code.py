# Open the input and output files
input_file = "T5paired, trimmed pairs contig list.fa"
output_file = "T5paired, trimmed pairs contig list_updated.fa"

# Initialize a counter for the new IDs
id_counter = 1

# Open the input file for reading and the output file for writing
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # Check if the line starts with '>'
        if line.startswith(">"):
            # Create the new ID using the counter
            new_id = f">T5_22GHGVLT31_contig_{id_counter}"
            id_counter += 1
            # Write the new ID to the output file
            outfile.write(new_id + "\n")
        else:
            # Write the sequence line as is to the output file
            outfile.write(line)

print("ID names updated and saved to", output_file)
