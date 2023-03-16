from random import choice

def função_objetivo_cb(indivíduo):
    """Computa a função objetivo para um indivíduo
    Args:
        Indivíduo: lista contendo todos os genes das caixas binarias.
    Return:
        Um valor representando a soma dos genes do indivíduo."""
    return sum(indivíduo)

def gene_cb():
    """Gera um gene valido para um indivíduo
    Return: 
        Um valor entre 0 ou 1."""
    genes = [0,1]
    gene = choice(genes)
    return(gene)
    
def indivíduo_cb(n):
    """Gera um indivíduo para o problema das caixas binarias.
    
    Args:
        n: número de genes do indivíduo.
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um.
        """
    indivíduo = [gene_cb() for i in range(n)]
    return indivíduo