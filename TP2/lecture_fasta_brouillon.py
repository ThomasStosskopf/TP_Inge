# function to read a fasta file and find the 'N' character

def fasta_find_N(file):
    headers = []
    sequence = []
    list_ADN = ['A','C','G','T']
    count_not_nucl = 0
    count_line = 0
    with open(file, 'r') as file_opened:
        for line in file_opened:
            if line.startswith('>'):
                headers.append(line)
            else:
                line = line.strip()
                line = line.upper()
                
                sequence.append(line)
        all_seq = "".join(sequence)
        for char in all_seq:
            if char in list_ADN:
                continue
            else:
                print("This is not a nucleotide")
                count_not_nucl += 1
    return count_not_nucl




print(fasta_find_N("mitochondrie_humaine.fasta"))

