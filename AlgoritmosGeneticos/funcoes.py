from random import choice, choices, randint, sample


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
    gene = randint(0, n)
    return gene


def indivíduo_cnb(valor_maximo, n):
    """Gera um indivíduo para o problema das caixas não binarias.

    Args:
        n: número de genes do indivíduo.
        valor_maximo: Valor maximo para a caixa binaria
    Return:
        Uma lista com n genes. Cada gene é um valor zero a valor_maximo.
    """
    indivíduo = [gene_cnb(valor_maximo) for i in range(n)]
    return indivíduo


def população_caixas_n_binarias(valor_maximo, tamanho, n):
    """Cria uma populção de caixas não binarias.

    arg:
        tamanho: quantos da população irá ter na caixa binarias.
        n: Quantidade de genes nas caixas binarias
    return:
        população: lista de individuos"""
    população = [
        indivíduo_cnb(valor_maximo, n) for _ in range(tamanho)
    ]  # sendo n o numero de individuos.
    return população


def mutação_cnb(valor_maximo, indivíduo):
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


################################
# SENHA
################################################


def gene_letra(letras):
    """Sorteia uma letra.

    Args:
      letras: letras possíveis de serem sorteadas.

    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = choice(letras)
    return letra


def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha

    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.

    Return:
      Lista com n letras
    """

    candidato = [gene_letra(letras) for _ in range(tamanho_senha)]

    return candidato


def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha

    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.

    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = [individuo_senha(tamanho_senha, letras) for _ in range(tamanho)]
    return populacao


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: população do problema
      fitness: fitness de todos os individuos da população.
      tamanho_torneio: quantidade de invidiuos que batalham entre si

    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados


def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.

    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.

    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo


def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha

    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca += abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = [
        funcao_objetivo_senha(individuo, senha_verdadeira) for individuo in populacao
    ]

    return resultado


##########################################################################################
# Senha sem tamanho
###########################################


def mutacao_tamanho_senha(individuo, letras, maximo):
    """Realiza a mutação de um gene no problema da senha.

    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
      maximo: maximo de genes que podem ser retirados ou adicionados.

    Return:
      Um individuo (senha) com um gene retirado ou adicionado.
    """

    n_mudar_tamanho = randint(1, maximo)
    soma_ou_subtração = randint(0, 1)

    if soma_ou_subtração:
        somar = [gene_letra(letras) for _ in range(n_mudar_tamanho)]
        individuo = individuo + somar
    else:
        if n_mudar_tamanho > len(individuo) - 1:
            n_mudar_tamanho = len(individuo) - 1
        subtrair = sample(individuo, n_mudar_tamanho)
        for gene in subtrair:
            individuo.remove(gene)
    return individuo


def funcao_objetivo_senha_sem_tamanho(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha

    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância. E pela distancia do tamanho da senha para o tamanho correto.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca += abs(ord(letra_candidato) - ord(letra_oficial))

    delta_tamanho = abs(len(senha_verdadeira) - len(individuo)) * 10
    diferenca += delta_tamanho

    return diferenca


def funcao_objetivo_pop_senha_sem_tamanho(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = [
        funcao_objetivo_senha_sem_tamanho(individuo, senha_verdadeira)
        for individuo in populacao
    ]

    return resultado
