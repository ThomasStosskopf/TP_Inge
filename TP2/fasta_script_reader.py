"""
This script will go in every line of a
fasta file and find if a letter is a nucleotide or not
it will also give the length of every sequence
"""

def adn_read(fastafile):
    """function to open a fasta file and find if a
    letter is or not a nucleotide"""
    # create a list with the letters that we consider as nucleotid
    nucl_list = ["A", "C", "G", "T"]
    # create an empty dictonary to store the sequence and their headers
    sequence_dict = {}
    # open the fasta file
    with open(fastafile, "r", encoding="utf-8") as fasta_file:
        # Initialize a line counter... to count lines !
        line_counter = 0
        # initialize variable to keep track of the header we encounter
        header = ""
        current_sequence = ""
        # Iterate through each line in the files
        for line in fasta_file:
            # for each line, add +1 to the line_counter variable
            line_counter += 1
            # if the line start with ">" we start this 'if' statement
            # it means it's a header
            if line.startswith(">"):
                # Add the line in our dictionary as a key
                header = line.strip()
                sequence_dict[line.strip()] = ""
                # if the current_sequence is not empty, it means we already did at least one loop
                if current_sequence:
                    sequence_dict[line.strip()] = current_sequence
                    current_sequence = ""
        # return sequence_dict
            else:
                # remove '\n' at the end of the line
                line = line.strip()
                # make all the letter in caps in the line
                line = line.upper()
                # counter to count the column where there is no nucleotide
                column_counter = 0
                for char in line:
                    # add +1 to the counter for every char encounter in the line
                    column_counter += 1
                    if char not in nucl_list:
                        # print the number of nucleotide in the sequence
                        print("The sequence ", header[1:],"has ",len(line), " nucleotides")
                        # print a message to indicate in which position
                        # the letter is not a nucleotide
                        print(char + " is not a nucleotide in line " + str(line_counter) +
                              " and column " + str(column_counter) + " for sequence " + header[1:] )



print(adn_read("exemple.fasta"))