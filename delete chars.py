# Function to process data
import sys
def process_data(file_path):
    # Open the file in read mode with the specified encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read lines from the file and store them in an array
        lines = file.readlines()

    # Given array of allowed characters
    allowed_chars =[' ',',',':','-','.','\n','"']
    
    for i in range(65,91):
        allowed_chars.append(chr(i))
    for i in range(97,123):
        allowed_chars.append(chr(i))
    a="פםןוטארקףךלחיעכגדשץתצמנהבסז"
    for i in a:
        allowed_chars.append(i)
    # Function to filter characters based on the given array
    def filter_chars(word):
        return ''.join(char for char in word if char in allowed_chars)

    # Initialize an empty array to store reversed and filtered lines
    reversed_and_filtered_lines = []

    # Iterate through each line
    for line in lines:
        # Split the line into an array of words and reverse the order of words
        reversed_words = line.split()

        # Reverse the order of characters in each word and filter based on allowed characters
        reversed_and_filtered_words = [filter_chars(word) for word in reversed_words]
        for word in reversed_and_filtered_words:
            if len(word)==0:
                reversed_and_filtered_words.remove(word)
                
        

        # Join the reversed and filtered words back into a line and append to the main array
        if len(reversed_and_filtered_words)==1:
            if len(reversed_and_filtered_words[0])==0:
                continue

        # Join the reversed and filtered words back into a line and append to the main array
        reversed_and_filtered_lines.append(' '.join(reversed_and_filtered_words)+'\n')

    # Return the processed lines
    return reversed_and_filtered_lines



file_path = sys.argv[1]
#result = process_data(file_path)
output_file_path = sys.argv[1]
output_file_path=output_file_path[:-4] +' filterd.txt'


# Process data and write to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(process_data(file_path))