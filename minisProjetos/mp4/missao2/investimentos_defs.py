# Propósito do arquivo:
# Define a classe `Investimento`, que é o modelo para cada aplicação financeira
# que o usuário cadastra. Contém os dados e a lógica de progressão mensal.

from constantes_base import constants # CORRIGIDO: Aponta para a pasta correta

class Investimento:
    """
    Representa um investimento individual, guardando suas características
    (percentual CDI, aporte, recorrência) e estado (total investido, resgate).
    """
    def __init__(self, percentual_cdi_usuario, valor_aporte, eh_recorrente_str):
        """
        Cria (inicializa) um novo objeto de investimento.
        Args:
            percentual_cdi_usuario (float): O percentual do CDI que este investimento rende.
            valor_aporte (float): O valor do aporte inicial (e dos aportes mensais, se recorrente).
            eh_recorrente_str (str): A string "sim" ou "não" vinda do usuário.
        """
        self.percentual = float(percentual_cdi_usuario)
        self.aporte_inicial = float(valor_aporte)
        # Assegura que 's' seja tratado como 'sim' para a lógica booleana
        if eh_recorrente_str.lower() == 's':
            self.recorrente = True
        else:
            self.recorrente = eh_recorrente_str.lower() == 'sim'
        
        self.total_investido = self.aporte_inicial
        self.resgate = self.aporte_inicial
        self.primeiro_mes_concluido = False

    def avancar_mes(self):
        """
        Simula a passagem de um mês para este investimento.
        """
        if self.recorrente and self.primeiro_mes_concluido:
            self.total_investido += self.aporte_inicial
            self.resgate += self.aporte_inicial

        taxa_efetiva_mensal = (self.percentual / 100.0) * constants.TAXA_CDI_BASE_MENSAL_SIMULACAO
        
        rendimento_no_mes = self.resgate * taxa_efetiva_mensal
        self.resgate += rendimento_no_mes
        
        if not self.primeiro_mes_concluido:
            self.primeiro_mes_concluido = True

    def get_tipo_str(self):
        """Retorna "[R]" para recorrente ou "[U]" para único (para exibição)."""
        return "[R]" if self.recorrente else "[U]"