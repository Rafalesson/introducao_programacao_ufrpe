import statistics
import random
import datetime
from simulador import config

class Empresa:
    """Representa uma empresa no mercado, com seus produtos, custos e estratégias."""
    def __init__(self, categoria: str, nome: str, produto: str, custo: float, qualidade: int):
        self.nome = nome
        self.categoria = categoria
        self.produto = produto
        self.qualidade = qualidade
        self.custo = custo
        self.custo_operacional = self.custo * 0.10
        self.margem = 0.05
        self.oferta = 0
        self.reposicao = 10
        self.vendas = 0
        self.lucro_total = 0.0
        self.preco_atual = self.custo * (1 + self.margem)
        self.meses_consecutivos_prejuizo = 0
        self.falida = False
        self.data_falencia = None

    def ajustar_para_proximo_mes(self, todas_empresas: list, data_atual: datetime.date):
        """Executa a lógica mensal da empresa: custos, prejuízo e estratégia de mercado."""
        if self.falida:
            return

        self.lucro_total -= self.custo_operacional
        inflacao_mensal = (1 + config.INFLACAO_ANUAL)**(1/12) - 1
        fator_volatilidade = random.uniform(-0.005, 0.005)
        fator_variacao_custo = inflacao_mensal + fator_volatilidade
        self.custo *= (1 + fator_variacao_custo)
        self.custo_operacional = self.custo * 0.10

        lucro_bruto_vendas = (self.preco_atual - self.custo) * self.vendas
        lucro_liquido_mes = lucro_bruto_vendas - self.custo_operacional
        if lucro_liquido_mes < 0:
            self.meses_consecutivos_prejuizo += 1
        else:
            self.meses_consecutivos_prejuizo = 0
        
        if self.meses_consecutivos_prejuizo >= 18:
            self.falida = True
            self.data_falencia = data_atual
            self.oferta = 0
            self.vendas = 0
            return

        concorrentes = [e for e in todas_empresas if e.categoria == self.categoria and e.nome != self.nome and e.oferta > 0]
        preco_medio_concorrencia = statistics.mean([c.preco_atual for c in concorrentes]) if concorrentes else self.preco_atual
        vendeu_muito = self.oferta < self.reposicao * 0.1
        vendeu_pouco = self.oferta > self.reposicao * 0.5
        if vendeu_muito and self.vendas > 0:
            self.reposicao += max(1, round(self.vendas * 0.2))
        elif vendeu_pouco and self.reposicao > 5:
            self.reposicao = round(self.reposicao * 0.9)
        if vendeu_muito:
            self.margem *= 1.10 if self.preco_atual < preco_medio_concorrencia else 1.05
        elif vendeu_pouco:
            if self.margem > 0.02:
                self.margem *= 0.90 if self.preco_atual > preco_medio_concorrencia else 0.95
        
        self.vendas = 0
        self.oferta = self.reposicao
        self.preco_atual = self.custo * (1 + self.margem)

class Pessoa:
    """Representa um consumidor na simulação, com seu patrimônio, salário e decisões de compra."""
    def __init__(self, nome: str, patrimonio: float, salario: float):
        self.nome = nome
        self.patrimonio = patrimonio
        self.salario = salario
        self.conforto = 0.0

    def _realizar_compra(self, empresa: Empresa):
        self.patrimonio -= empresa.preco_atual
        empresa.oferta -= 1
        empresa.vendas += 1
        empresa.lucro_total += (empresa.preco_atual - empresa.custo)
        self.conforto += empresa.qualidade

    def _tentar_compra_orcamento(self, empresas_categoria: list, orcamento_categoria: float) -> bool:
        produtos_acessiveis = sorted(
            [e for e in empresas_categoria if e.preco_atual <= orcamento_categoria and e.oferta > 0],
            key=lambda x: (-x.qualidade, x.preco_atual)
        )
        if produtos_acessiveis:
            self._realizar_compra(produtos_acessiveis[0])
            return True
        return False

    def _tentar_compra_patrimonio(self, empresas_categoria: list) -> bool:
        produtos_disponiveis = sorted([e for e in empresas_categoria if e.oferta > 0], key=lambda x: x.preco_atual)
        if produtos_disponiveis and self.patrimonio >= produtos_disponiveis[0].preco_atual:
            self._realizar_compra(produtos_disponiveis[0])
            return True
        return False

    def simular_compras_do_mes(self, empresas: list, categorias_dict: dict):
        rendimento_mensal = self.salario + (self.patrimonio * 0.005)
        self.conforto = 0
        for categoria, percentual in categorias_dict.items():
            orcamento_categoria = rendimento_mensal * percentual
            empresas_da_categoria = [e for e in empresas if e.categoria == categoria]
            compra_realizada = self._tentar_compra_orcamento(empresas_da_categoria, orcamento_categoria)
            if not compra_realizada:
                self._tentar_compra_patrimonio(empresas_da_categoria)
        
        self.patrimonio += rendimento_mensal