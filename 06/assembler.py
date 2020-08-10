from code_ import asm_to_bi
from parser_ import (
    read_asm_file_to_code,
    clean_code,
    handle_labels,
    write_bi_code_to_file,
)
import sys


def main():

    # fetch path to assembly file from command line
    path_to_asm_file = sys.argv[1]

    # read file and append each line to a list
    asm_code = read_asm_file_to_code(path_to_asm_file)

    # remove whitespace, comments, and empty lines
    asm_code = clean_code(asm_code)

    # replace @XXX with number
    # remove pseudo command (XXX)
    asm_code = handle_labels(asm_code)

    # translate every assembly line to its binary repr
    bi_code = asm_to_bi(asm_code)

    # write hack file with binary code in same directory
    path_to_hack_file = path_to_asm_file.replace('asm', 'hack')
    write_bi_code_to_file(bi_code, path_to_hack_file)


if __name__ == '__main__':
    main()
