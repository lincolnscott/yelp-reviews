import json
import os

# Define input file path
input_file = 'reviews.json'

# Define output file directory
output_dir = 'reviews'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define chunk size (in lines)
chunk_size = 100000

# Define number of entries to write in each chunk
num_entries = 50000

# Define number of files to create
num_files = 10000

# Open input file
with open(input_file, 'r') as infile:

    # Read the file in chunks
    num_written = 0
    file_num = 0
    while num_written < num_files:
        lines = infile.readlines(chunk_size)
        if not lines:
            break

        # Process each line
        for line in lines:
            data = json.loads(line)
            text = data['text']
            stars = data['stars']

            # Write the desired fields to a new file
            file_num_str = str(file_num).zfill(6)
            filename = os.path.join(output_dir, file_num_str+'.txt')
            with open(filename, 'w') as outfile:
                outfile.write(f"{stars}\n{text}\n")

            num_written += 1
            file_num += 1

            # Check if we've reached the desired number of files
            if num_written >= num_files:
                break

print(f"Created {num_files} files")

print('Done!')
