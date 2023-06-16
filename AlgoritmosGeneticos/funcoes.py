from random import choice, choices, randint, sample, random, shuffle, uniform
import numpy as np


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


def gene_cnb(n, i=0, inteiro=True):
    """Gera um gene valido para um indivíduo da caixa não binaria.
    Args:
        n: numero maximo da caixa.
        i: numero minimo da caixa.
        iteiro: Se for False a caixa irá ter numeros float.
    Return:
        Um valor entre 0 e n."""
    if inteiro:
        gene = randint(i, n)
    else:
        gene = uniform(i, n)
    return gene


def indivíduo_cnb(valor_maximo, n, valor_minimo=0, inteiro=True):
    """Gera um indivíduo para o problema das caixas não binarias.

    Args:
        n: número de genes do indivíduo.
        valor_maximo: Valor maximo para a caixa binaria.
        valor_minimo: Valor minimo para a caixa binaria.
        iteiro: Se for False a caixa irá ter numeros float.
    Return:
        Uma lista com n genes. Cada gene é um valor zero a valor_maximo.
    """
    indivíduo = [gene_cnb(valor_maximo, valor_minimo, inteiro) for _ in range(n)]
    return indivíduo


def população_caixas_n_binarias(valor_maximo, tamanho, n, valor_minimo=0, inteiro=True):
    """Cria uma populção de caixas não binarias.

    arg:
        tamanho: quantos da população irá ter na caixa binarias.
        n: Quantidade de genes nas caixas binarias
        valor_maximo: Valor maximo para a caixa binaria
        valor_minimo: Valor minimo para a caixa binaria
        iteiro: Se for False a caixa irá ter numeros float.

    return:
        população: lista de individuos"""
    população = [
        indivíduo_cnb(valor_maximo, n, valor_minimo, inteiro) for _ in range(tamanho)
    ]  # sendo n o numero de individuos.
    return população


def mutacao_cnb(valor_maximo, indivíduo, valor_minimo=0, inteiro=True):
    """Realiza a mutação de um gene no problema das caixas não binárias

    Args:
        indivíduo: uma lista representando um individuo no problema das caixas binárias.

    Return:
        Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = randint(0, len(indivíduo) - 1)
    indivíduo[gene_a_ser_mutado] = gene_cnb(valor_maximo, valor_minimo, inteiro)
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


# NOVIDADE
def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2

    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.

    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


# NOVIDADE
def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).

    Args:
      n: inteiro positivo, Número de cidades que serão visitadas pelo caixeiro.

    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random(), random())

    return cidades


# NOVIDADE
def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante

    Args:
      cidades: Dicionário onde as chaves são os nomes das cidades e os valores são as coordenadas das cidades.

    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    shuffle(nomes)
    return nomes


# NOVIDADE
def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.

    Args
      tamanho: Tamanho da população.
      cidades: Dicionário onde as chaves são os nomes das cidades e os valores são as coordenadas das cidades.

    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao


# NOVIDADE
def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.

    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.

    Ver pág. 37 do livro do Wirsansky.

    Args:
      pai: uma lista representando um individuo
      mae: uma lista representando um individuo

    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    corte1 = randint(0, len(pai) - 2)
    corte2 = randint(corte1 + 1, len(pai) - 1)
    filho1 = pai[corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)

    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)

    return filho1, filho2


# NOVIDADE
def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.

    Args:
      individuo: uma lista representado um individuo.

    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    index1, index2 = sample(range(len(individuo)), k=2)
    individuo[index1], individuo[index2] = individuo[index2], individuo[index1]
    return individuo


# NOVIDADE
def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.

    Args:
      individuo: Lista contendo a ordem das cidades que serão visitadas
      cidades: Dicionário onde as chaves são os nomes das cidades e os valores são as coordenadas das cidades.

    Returns:
      distancia : A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0

    for posicao in range(len(individuo) - 1):
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao + 1]]
        distancia += distancia_entre_dois_pontos(partida, chegada)

    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]
    distancia += distancia_entre_dois_pontos(partida, chegada)

    return distancia


# NOVIDADE
def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.

    Args:
      populacao: Lista com todos os inviduos da população
      cidades: Dicionário onde as chaves são os nomes das cidades e os valores são as coordenadas das cidades.

    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = [funcao_objetivo_cv(individuo, cidades) for individuo in populacao]

    return resultado


######################################################################## Mochila  ####################################


def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila

    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.

    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """

    valor_total = 0
    peso_total = 0

    for pegou_item, nome_item in zip(individuo, ordem_dos_nomes):
        if pegou_item:
            valor_total += objetos[nome_item]["valor"]
            peso_total += objetos[nome_item]["peso"]

    return valor_total, peso_total


def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.

    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.

    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """

    valor_individuo, peso_individuo = computa_mochila(
        individuo, objetos, ordem_dos_nomes
    )

    if peso_individuo > limite:
        valor_individuo = 0.01

    return valor_individuo


def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila

    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.

    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes)
        )

    return resultado


def função_objetivo_Himmelblau(indivíduo):
    """Computa a função objetivo para um indivíduo

    Args:
        Indivíduo: uma lista com cordenadas x,y.
    Return:
        Um valor representando a soma dos genes do indivíduo."""
    x = indivíduo[0]
    y = indivíduo[1]

    return (x**2 + y - 11) ** 2 + (x + y**2 - 7) ** 2


def função_objetivo_Himmelblau_pop(lista_individuos):
    """Computa a funcao objetivo de uma populaçao no problema de Himmelblau.

    Args:
      lista_individuos: lista com a população de individuos.

    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = [
        função_objetivo_Himmelblau(individuo) for individuo in lista_individuos
    ]

    return resultado


def função_objetivo_Rastrigin(indivíduo):
    """Computa a função objetivo para um indivíduo

    Args:
        Indivíduo: uma lista com cordenadas x,y.
    Return:
        Um valor representando a soma dos genes do indivíduo."""
    x = indivíduo[0]
    y = indivíduo[1]

    return (
        20
        + (x**2 - 10 * np.cos(2 * np.pi * x))
        + (y**2 - 10 * np.cos(2 * np.pi * y))
    )


def função_objetivo_Rastrigin_pop(lista_individuos):
    """Computa a funcao objetivo de uma populaçao no problema de Rastrigin.

    Args:
      lista_individuos: lista com a população de individuos.

    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = [função_objetivo_Rastrigin(individuo) for individuo in lista_individuos]

    return resultado


def mutação_grossa(individuo):
    # Mutação por passos peguenos
    gene_a_ser_mutado = randint(0, len(individuo) - 1)
    taxa = uniform(-1, 1)
    individuo[gene_a_ser_mutado] = individuo[gene_a_ser_mutado] * (1 + taxa)
    return individuo


def mutação_media(individuo):
    # Mutação por passos peguenos
    gene_a_ser_mutado = randint(0, len(individuo) - 1)
    taxa = uniform(-1, 1) / 10
    individuo[gene_a_ser_mutado] = individuo[gene_a_ser_mutado] * (1 + taxa)
    return individuo


def mutação_fina(individuo):
    # Mutação por passos peguenos
    gene_a_ser_mutado = randint(0, len(individuo) - 1)
    taxa = uniform(-1, 1) / 1000
    individuo[gene_a_ser_mutado] = individuo[gene_a_ser_mutado] * (1 + taxa)
    return individuo


def mutação_Função(individuo, maximo, minimo):
    # Mutação por passos peguenos
    mutação = random()
    variavel_min = 0.3
    variavel_medio = 0.9
    variavel_max = 0.98

    if variavel_min < mutação < variavel_medio:
        mutação_fina(individuo)
        

    elif variavel_medio < mutação < variavel_max:
        mutação_grossa(individuo)
        

    elif mutação < variavel_min:
        mutação_media(individuo)
        
    elif mutação > variavel_max:
        mutacao_cnb(maximo, individuo, minimo, False)
        
        

    return individuo
    # Passos pequenos do gradiente.
    # gene_a_ser_mutado = randint(0, len(individuo) - 1)
    # taxa = random()/100
    # x = individuo[0]
    # y = individuo[1]
    # if gene_a_ser_mutado == 0:
    #     grad_x = 4 * x**3 + 4 * x * y - 42 * x + 2 * y**2 - 14
    #     individuo[gene_a_ser_mutado] = individuo[gene_a_ser_mutado] - (grad_x * taxa)
    # elif gene_a_ser_mutado == 1:
    #     grad_y = 4 * y**3 + 4 * x * y - 26 * y + 2 * x**2 - 22
    #     individuo[gene_a_ser_mutado] = individuo[gene_a_ser_mutado] - (grad_y * taxa)
