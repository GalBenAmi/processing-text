# Function to process data
import sys
import string
def process_data(file_path):
    # Open the file in read mode with the specified encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read lines from the file and store them in an array
        lines = file.readlines()

    # Given array of allowed characters
    allowed_chars =set([' ',',',':','-','.','\n','"'])
    allowed_chars.update(set(string.ascii_letters))

    a="פםןוטארקףךלחיעכגדשץתצמנהבסז"
    allowed_chars.update(set(a))

    def filter_chars(word):
        return ''.join(char for char in word if char in allowed_chars)

    # Initialize an empty array to store  filtered lines
    filtered_lines = []

    # Iterate through each line
    for line in lines:
        # Split the line into an array of words
        words = line.split()

        # filter word based on allowed characters
        filtered_words = [filter_chars(word) for word in words]
        for word in filtered_words:
            #removes empty words 
            if len(word)==0:
                filtered_words.remove(word)
                
        

        # remove empty lines
        if len(filtered_words)==1:
            if len(filtered_words[0])==0:
                continue

        # Join the  filtered words back into a line and append to the main array
        filtered_lines.append(' '.join(filtered_words)+'\n')

    # Return the filtered lines
    return filtered_lines



file_path = sys.argv[1]
output_file_path = sys.argv[1]
output_file_path=output_file_path[:-4] +' filterd.txt'


# Process data and write to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(process_data(file_path))