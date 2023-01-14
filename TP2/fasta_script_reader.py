import sys

# function to open a fasta file and
def adn_read(fastafile):
    # create a list with the letters that we consider as nucleotid
    NTP_LIST = ["A", "C", "G", "T"]
    # create an empty dictonary to store the sequence and their headers
    sequence_dict = {}
    # open the fasta file
    with open(fastafile, "r") as fasta_file:
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
                line = line.strip()
                line = line.upper()
                column_counter = 0
                for char in line:
                    column_counter += 1
                    if char not in NTP_LIST:
                        print("The sequence has ",len(line), " nucleotides")
                        print(char + " is not a nucl in line " + str(line_counter) +
                              " and column " + str(column_counter) + " for sequence " + header[1:] )

#print(sys.argv)
#for arg in sys.argv[1:]:
#    adn_read(arg)


print(adn_read("exemple.fasta"))