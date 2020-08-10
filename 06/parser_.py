import re
from symbol_table import pre_defined_sb


def read_asm_file_to_code(file_path):
    """fetch path to assembly file from command line"""
    with open(file_path, 'r') as file:
        asm_code = []
        for line in file:
            asm_code.append(line)

    return asm_code


def write_bi_code_to_file(bi_code, file_path):
    """write hack file with binary code"""
    with open(file_path, 'w') as file:
        for i in bi_code:
            file.write(f'{i}\n')


def remove_white_space(ls):
    """remove any white space"""
    for i in range(len(ls)):
        ls[i] = re.sub(r'\s+', '', ls[i])

    return ls


def remove_comments(ls):
    """remove everything after and including '//'"""
    for i in range(len(ls)):
        ls[i] = re.sub(r'//.*', '', ls[i])

    return ls


def remove_empty_lines(ls):
    """filter out ''s"""
    return list(filter(lambda x: x != '', ls))


def clean_code(ls):
    """remove white space, comments, and empty lines"""
    ls = remove_white_space(ls)
    ls = remove_comments(ls)
    ls = remove_empty_lines(ls)

    return ls


def handle_labels(ls):
    """replace @XXX with number
    remove pseudo command (XXX)"""

    # assign each line a number
    line_num = {}
    counter = 0
    for i in ls:
        if not i.startswith('('):
            line_num[i] = counter
            counter += 1
        else:
            sb = i[1:-1]
            line_num[sb] = counter

    # replace @XXX with number
    var_address = 16
    for i in range(len(ls)):
        if ls[i].startswith('@'):

            # replace with pre-defined symbols if found
            if pre_defined_sb.get(ls[i][1:]) is not None:
                ls[i] = '@' + pre_defined_sb[ls[i][1:]]

            # replace by (XXX) line number if search failed
            elif line_num.get(ls[i][1:]) is not None:
                ls[i] = '@' + str(line_num[ls[i][1:]])

            else:
                ls[i] = '@' + str(var_address)
                var_address += 1

    # remove (XXX)'s
    ls = list(filter(lambda x: not x.startswith('('), ls))

    return ls
