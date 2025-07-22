# simulador/agents.py

import statistics
import random
import datetime
from simulador import config

# --- Agente Empresa ---
class Empresa:
    """Representa uma empresa no mercado, com seus produtos, custos e estratégias."""
    def __init__(self, categoria: str, nome: str, produto: str, custo: float, qualidade: int):
        # Atributos fixos da empresa
        self.nome = nome
        self.categoria = categoria
        self.produto = produto
        self.qualidade = qualidade
        
        # Atributos financeiros dinâmicos
        self.custo = custo  # Custo de produção de uma unidade
        self.custo_operacional = self.custo * 0.10  # Custo mensal para a empresa existir
        self.margem = 0.05  # Margem de lucro inicial de 5%
        self.lucro_total = 0.0  # Lucro acumulado ao longo da simulação
        self.preco_atual = self.custo * (1 + self.margem)  # Preço de venda para o consumidor

        # Atributos de estoque e vendas
        self.oferta = 0  # Quantidade de produtos disponíveis no início do mês
        self.reposicao = 10  # Quantidade de produtos a serem repostos no próximo mês
        self.vendas = 0  # Quantidade de produtos vendidos no mês

        # Atributos de controle de falência
        self.meses_consecutivos_prejuizo = 0
        self.falida = False  # Flag que indica se a empresa quebrou
        self.data_falencia = None  # Data em que a falência ocorreu

    def ajustar_para_proximo_mes(self, todas_empresas: list, data_atual: datetime.date):
        """Executa a lógica mensal da empresa: custos, prejuízo e estratégia de mercado."""
        # Se a empresa já faliu, ela não participa mais das atividades do mercado.
        if self.falida:
            return

        # 1. CUSTOS MENSAIS: A empresa tem despesas fixas e variáveis.
        self.lucro_total -= self.custo_operacional  # Paga o custo de existir (aluguel, etc.)
        
        # O custo de produção varia com a inflação e a volatilidade do mercado.
        inflacao_mensal = (1 + config.INFLACAO_ANUAL)**(1/12) - 1
        fator_volatilidade = random.uniform(-0.005, 0.005)
        self.custo *= (1 + inflacao_mensal + fator_volatilidade)
        self.custo_operacional = self.custo * 0.10  # O custo operacional também é atualizado.

        # 2. VERIFICAÇÃO DE FALÊNCIA: Com base no resultado do mês.
        lucro_bruto_vendas = (self.preco_atual - self.custo) * self.vendas
        lucro_liquido_mes = lucro_bruto_vendas - self.custo_operacional

        if lucro_liquido_mes < 0:
            self.meses_consecutivos_prejuizo += 1  # Incrementa o contador de prejuízos.
        else:
            self.meses_consecutivos_prejuizo = 0  # Zera o contador se houve lucro.
        
        # Se atingir 18 meses seguidos de prejuízo, a empresa quebra.
        if self.meses_consecutivos_prejuizo >= 18:
            self.falida = True
            self.data_falencia = data_atual
            self.oferta = 0
            self.vendas = 0
            return

        # 3. ESTRATÉGIA DE MERCADO: Ajusta estoque e preço com base no desempenho.
        concorrentes = [e for e in todas_empresas if e.categoria == self.categoria and e.nome != self.nome and e.oferta > 0]
        preco_medio_concorrencia = statistics.mean([c.preco_atual for c in concorrentes]) if concorrentes else self