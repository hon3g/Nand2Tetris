from symbol_table import (
    comp,
    dest,
    jump,
)


def a_to_bi(a):
    """translate a instruction to its binary repr"""
    n = int(a[1:])
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


def asm_to_bi(ls):
    """translate every assembly line to its binary repr"""
    for i in range(len(ls)):
        if ls[i].startswith('@'):
            ls[i] = a_to_bi(ls[i])
        else:
            ls[i] = c_to_bi(ls[i])

    return ls
