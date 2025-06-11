from missao1.dados import Pessoa, Empresa

def _realizar_compra(pessoa: Pessoa, empresa: Empresa):
    """Função auxiliar para centralizar a lógica de uma transação."""
    pessoa.patrimonio -= empresa.preco_atual
    empresa.oferta -= 1
    empresa.vendas += 1
    empresa.lucro_total += (empresa.preco_atual - empresa.custo)
    pessoa.conforto += empresa.qualidade

def _tentar_compra_orcamento(pessoa: Pessoa, empresas_categoria: list[Empresa], orcamento_categoria: float) -> bool:
    """
    Tenta comprar o produto de maior qualidade dentro do orçamento mensal.
    Em caso de empate na qualidade, escolhe o de menor preço.
    """
    # A lista é ordenada primeiro pela qualidade (decrescente) e depois pelo preço (crescente).
    produtos_acessiveis = sorted(
        [e for e in empresas_categoria if e.preco_atual <= orcamento_categoria and e.oferta > 0],
        key=lambda x: (-x.qualidade, x.preco_atual)
    )

    if produtos_acessiveis:
        # A escolha do primeiro item da lista é garantidamente a melhor opção (qualidade/preço).
        _realizar_compra(pessoa, produtos_acessiveis[0])
        return True
    return False

def _tentar_compra_patrimonio(pessoa: Pessoa, empresas_categoria: list[Empresa]) -> bool:
    """Como fallback, tenta comprar o produto mais barato possível com o patrimônio."""
    produtos_disponiveis = sorted([e for e in empresas_categoria if e.oferta > 0], key=lambda x: x.preco_atual)
    if produtos_disponiveis and pessoa.patrimonio >= produtos_disponiveis[0].preco_atual:
        _realizar_compra(pessoa, produtos_disponiveis[0])
        return True
    return False

def simular_pessoa(pessoa: Pessoa, empresas: list[Empresa], categorias: list[str], percentuais: list[float]):
    """Simula as decisões de compra de uma pessoa para o mês."""
    rendimento_mensal = pessoa.salario + (pessoa.patrimonio * 0.006)
    pessoa.conforto = 0

    for i, categoria in enumerate(categorias):
        orcamento_categoria = rendimento_mensal * percentuais[i]
        empresas_da_categoria = [e for e in empresas if e.categoria == categoria]
        for e in empresas_da_categoria:
            e.preco_atual = e.custo * (1 + e.margem)

        compra_realizada = _tentar_compra_orcamento(pessoa, empresas_da_categoria, orcamento_categoria)
        if not compra_realizada:
            _tentar_compra_patrimonio(pessoa, empresas_da_categoria)

    pessoa.patrimonio += rendimento_mensal

def simular_empresa(empresa: Empresa):
    """Simula as decisões de uma empresa para o próximo mês."""
    if empresa.oferta == 0 and empresa.vendas > 0:
        empresa.reposicao += 1
        empresa.margem += 0.01
    elif empresa.oferta >= 10:
        if empresa.reposicao > 1:
            empresa.reposicao -= 1
        if empresa.margem > 0.01:
            empresa.margem -= 0.01
    empresa.vendas = 0
    empresa.oferta = empresa.reposicao

def simular_mercado(pessoas: list[Pessoa], empresas: list[Empresa], categorias: list[str], percentuais: list[float]):
    """Executa um ciclo de simulação de um mês."""
    for empresa in empresas:
        simular_empresa(empresa)
    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias, percentuais)