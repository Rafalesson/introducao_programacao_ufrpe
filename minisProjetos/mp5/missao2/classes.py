class Empresa:
    def __init__(self, categoria: str, nome: str, produto: str, custo: float, qualidade: int):
        self.nome = nome
        self.categoria = categoria
        self.produto = produto
        self.custo = custo
        self.qualidade = qualidade
        self.margem = 0.05
        self.oferta = 0
        self.reposicao = 10
        self.vendas = 0
        self.lucro_total = 0.0
        self.preco_atual = 0.0

    def ajustar_para_proximo_mes(self):
        """Aplica as regras de negócio da empresa para o próximo ciclo."""
        if self.oferta == 0 and self.vendas > 0:
            self.reposicao += 1
            self.margem += 0.01
        elif self.oferta >= 10:
            if self.reposicao > 1: self.reposicao -= 1
            if self.margem > 0.01: self.margem -= 0.01
        self.vendas = 0
        self.oferta = self.reposicao
        self.preco_atual = self.custo * (1 + self.margem)

class Pessoa:
    def __init__(self, patrimonio: float, salario: float, grupo: str):
        self.patrimonio = patrimonio
        self.salario = salario
        self.grupo = grupo
        self.conforto = 0.0

    def _realizar_compra(self, empresa: Empresa):
        """Função auxiliar para centralizar a lógica de uma transação."""
        self.patrimonio -= empresa.preco_atual
        empresa.oferta -= 1
        empresa.vendas += 1
        empresa.lucro_total += (empresa.preco_atual - empresa.custo)
        self.conforto += empresa.qualidade

    def _tentar_compra_orcamento(self, empresas_categoria: list[Empresa], orcamento_categoria: float) -> bool:
        """Tenta comprar o produto de maior qualidade/menor preço dentro do orçamento."""
        produtos_acessiveis = sorted(
            [e for e in empresas_categoria if e.preco_atual <= orcamento_categoria and e.oferta > 0],
            key=lambda x: (-x.qualidade, x.preco_atual)
        )
        if produtos_acessiveis:
            self._realizar_compra(produtos_acessiveis[0])
            return True
        return False

    def _tentar_compra_patrimonio(self, empresas_categoria: list[Empresa]) -> bool:
        """Como fallback, tenta comprar o produto mais barato possível com o patrimônio."""
        produtos_disponiveis = sorted([e for e in empresas_categoria if e.oferta > 0], key=lambda x: x.preco_atual)
        if produtos_disponiveis and self.patrimonio >= produtos_disponiveis[0].preco_atual:
            self._realizar_compra(produtos_disponiveis[0])
            return True
        return False

    def simular_compras_do_mes(self, empresas: list[Empresa], categorias: list[str], percentuais: list[float]):
        """Simula as decisões de compra de uma pessoa para o mês."""
        rendimento_mensal = self.salario + (self.patrimonio * 0.006)
        self.conforto = 0
        for i, categoria in enumerate(categorias):
            orcamento_categoria = rendimento_mensal * percentuais[i]
            empresas_da_categoria = [e for e in empresas if e.categoria == categoria]
            compra_realizada = self._tentar_compra_orcamento(empresas_da_categoria, orcamento_categoria)
            if not compra_realizada:
                self._tentar_compra_patrimonio(empresas_da_categoria)
        self.patrimonio += rendimento_mensal