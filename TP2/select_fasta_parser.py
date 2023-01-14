"""script to create parser"""
import argparse
import sys

def create_parser():
    """ Declares new parser and adds parser arguments """
    program_description=''' reading fasta file and checking sequence format '''
    parser =  argparse.ArgumentParser(add_help=True,description=program_description)
    parser.add_argument('-i','--inputfile',default=sys.stdin,
    help="required input file in fasta format",type=argparse.FileType("r"),required=True)
    return parser

def main():
    """ Main function for reading fasta file and checking sequence format """
    parser = create_parser()
    args = parser.parse_args()
    args = args.__dict__
    print(args["inputfile"])
    fasta_sequence = args["inputfile"].read()
    print(fasta_sequence)


if __name__ == "__main__":
    main()
