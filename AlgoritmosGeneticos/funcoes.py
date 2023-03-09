# irei utilizar uma lista para representar meu indivíduo
# a quantidade de elementos de uma lista é a quantidade de genes.
# cada gene varia apenas de 0 ou 1.

def função_objetivo_cb(indivíduo):
    """Computa a função objetivo para um indivíduo
    Args:
        Indivíduo: lista contendo todos os genes das caixas binarias.
    Return:
        Um valor representando a soma dos genes do indivíduo."""
    return sum(indivíduo)