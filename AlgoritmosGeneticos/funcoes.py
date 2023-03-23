from random import choice, choices, randint


def gene_cb():
    """Gera um gene valido para um indivíduo
    
    Return:
        Um valor entre 0 ou 1."""
    genes = [0, 1]
    gene = choice(genes)
    return gene


def indivíduo_cb(n):
    """Gera um indivíduo para o problema das caixas binarias.

    Args:
        n: número de genes do indivíduo.
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    indivíduo = [gene_cb() for i in range(n)]
    return indivíduo


def população_caixas_binarias(tamanho, n):
    """Cria uma populção de caicas binarias.

    arg:
        tamanho: quantos da população irá ter na caixa binarias.
        n: Quantidade de genes nas caixas binarias
    return:
        população: lista de individuos"""
    população = [
        indivíduo_cb(n) for _ in range(tamanho)
    ]  # sendo n o numero de individuos.
    return população


def mutação_cb(indivíduo):
    """Realiza a mutação de um gene no problema das caixas binárias

    Args:
        indivíduo: uma lista representando um individuo no problema das caixas binárias.

    Return:
        Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = randint(0, len(indivíduo) - 1)
    indivíduo[gene_a_ser_mutado] = gene_cb()
    return indivíduo


def função_objetivo_cb(indivíduo):
    """Computa a função objetivo para um indivíduo

    Args:
        Indivíduo: lista contendo todos os genes das caixas binarias.
    Return:
        Um valor representando a soma dos genes do indivíduo."""
    return sum(indivíduo)


def selecao_roleta_max(população, fitness):
    """
    Seleciona indivíduo de uma população usando o método da roleta.
    Nota: apenas funciona para problemas de maximização

    Args:
        população: lista com todos os individuos da população.
        fitness: lista dos valores da função objetivo dos individuos da população.

    Returns:
        População: lista com os individuos selecionados.
    """
    população_selecionada = choices(população, weights=fitness, k=len(população))
    return população_selecionada


def cruzamento_ponto_simples(pai, mãe):
    """Operador de cruzamento de ponto simples.

    Args:
        pai: uma lista representando um individuo.
        mãe: uma lista representando um individuo.

    Returns:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    """

    ponto_de_corte = randint(1, len(pai) - 1)
    filho1 = pai[:ponto_de_corte] + mãe[ponto_de_corte:]
    filho2 = mãe[:ponto_de_corte] + pai[ponto_de_corte:]

    return filho1, filho2


def func_objetivo_população(população):
    """Calcula a função objetivo para todos os membros de uma população.

    Arg:
    '   população: lista com os individuos selecionados.

    Returns:
    Lista de valores representando os fitness dos individuos."""
    fitnnes = [função_objetivo_cb(individuo) for individuo in população]
    return fitnnes

def gene_cnb(n):
    """Gera um gene valido para um indivíduo da caixa não binaria.
    Args:
        n: numero maximo da caixa.
    Return:
        Um valor entre 0 e n."""
    gene = randint(0,n)
    return gene

def indivíduo_cnb(valor_maximo,n):
    """Gera um indivíduo para o problema das caixas não binarias.

    Args:
        n: número de genes do indivíduo.
        valor_maximo: Valor maximo para a caixa binaria
    Return:
        Uma lista com n genes. Cada gene é um valor zero a valor_maximo.
    """
    indivíduo = [gene_cnb(valor_maximo) for i in range(n)]
    return indivíduo


def população_caixas_n_binarias(valor_maximo,tamanho, n):
    """Cria uma populção de caixas não binarias.

    arg:
        tamanho: quantos da população irá ter na caixa binarias.
        n: Quantidade de genes nas caixas binarias
    return:
        população: lista de individuos"""
    população = [
        indivíduo_cnb(valor_maximo,n) for _ in range(tamanho)
    ]  # sendo n o numero de individuos.
    return população

def mutação_cnb(valor_maximo,indivíduo):
    """Realiza a mutação de um gene no problema das caixas não binárias

    Args:
        indivíduo: uma lista representando um individuo no problema das caixas binárias.

    Return:
        Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = randint(0, len(indivíduo) - 1)
    indivíduo[gene_a_ser_mutado] = gene_cnb(valor_maximo)
    return indivíduo

def função_objetivo_cnb(indivíduo):
    """Computa a função objetivo para um indivíduo

    Args:
        Indivíduo: lista contendo todos os genes das caixas binarias.
    Return:
        Um valor representando a soma dos genes do indivíduo."""
    return sum(indivíduo)

def func_objetivo_população_n_b(população):
    """Calcula a função objetivo para todos os membros de uma população.

    Arg:
    '   população: lista com os individuos selecionados.

    Returns:
    Lista de valores representando os fitness dos individuos."""
    fitnnes = [função_objetivo_cnb(individuo) for individuo in população]
    return fitnnes