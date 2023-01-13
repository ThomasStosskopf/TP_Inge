import sys

# function to open a fasta file and
def adn_read(fastafile):
    # create a list with the letters that we consider as nucleotid
    NTP_LIST = ["A", "C", "G", "T"]
    # creat an empty dictonnary to store the sequence and their headers
    sequence_dict = {}
    # open the fasta file
    with open(fastafile, "r") as fasta_file:
        # Initialize a line counter... to count lines !
        line_counter = 0
        # initialize variable to keep track of the header we encounter
        header = ""
        # Iterate through each line in the files (we didn't open the entire file in one variable this time)
        for line in fasta_file:
            # for each line, add +1 to the line_counter variable
            line_counter += 1
            # if the line start with "with" we start this if statement, and it means that it's a header
            if line.startswith(">"):
                header = line.strip()
            else:
                line = line.strip()
                line = line.upper()
                column_counter = 0
                for char in line:
                    column_counter += 1
                    if char not in NTP_LIST:
                        print(char + " It's not a nucl in line " + str(counter) +
                              " and column " + str(column_counter) + " for sequence " + header[1:])


#print(sys.argv)
#for arg in sys.argv[1:]:
#    adn_read(arg)


