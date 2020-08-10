import re
from symbol_table import comp, dest, jump


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


def a_to_bi(n):
    """translate a instruction to its binary repr"""
    bi = ''
    for _ in range(15):
        bi = str(n % 2) + bi
        n //= 2

    return '0' + bi


def c_to_bi(c):
    """translate c instruction to its binary repr"""
    if '=' in c:
        index = c.index('=')
        comp_bi = get_comp_bi(c[index + 1:])
        dest_bi = dest[c[:index]]

        return '111' + comp_bi + dest_bi + '000'

    elif ';' in c:
        index = c.index(';')
        comp_bi = get_comp_bi(c[:index])
        jump_bi = jump[c[index + 1:]]

        return '111' + comp_bi + '000' + jump_bi


def get_comp_bi(sb):
    """get binary repr of comp symbol"""
    if comp[0].get(sb) is not None:
        comp_bi = '0' + comp[0].get(sb)

    else:
        comp_bi = '1' + comp[1][sb]

    return comp_bi


print(c_to_bi('0;JMP'))
