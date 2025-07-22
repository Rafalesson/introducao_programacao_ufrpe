# Simulador de Mercado Socioeconômico

![Status](https://img.shields.io/badge/status-concluído-green)

Um simulador de mercado baseado em agentes (Agent-Based Model) escrito em Python. O projeto modela as interações entre consumidores (agentes `Pessoa`) e produtores (agentes `Empresa`) em uma microeconomia, observando o desenvolvimento de cenários socioeconômicos ao longo do tempo.

## 🚀 Sobre o Projeto

O objetivo deste simulador é criar um ambiente virtual para estudar como variáveis macroeconômicas, como inflação e salário mínimo, e decisões individuais de consumo e precificação afetam a distribuição de riqueza, o padrão de vida (conforto) e a saúde do mercado (falências de empresas).

A simulação é projetada para ser modular e configurável, permitindo a análise de diferentes cenários econômicos.

## ✨ Funcionalidades

- **Modelagem Baseada em Agentes:** Simulação do comportamento de agentes `Pessoa` (consumidores) e `Empresa` (produtores).
- **Classes Socioeconômicas:** A população é estratificada em 7 classes (A, B1, B2, C1, C2, D, E), com parâmetros realistas de salário e patrimônio baseados no cenário brasileiro.
- **Mercado Dinâmico:** Empresas ajustam seus preços, margens de lucro e estoques mensalmente com base nas vendas e na concorrência.
- **Variáveis Macroeconômicas:** A simulação opera com base em uma taxa de **inflação** e um **salário mínimo** que são atualizados anualmente, influenciando toda a economia.
- **Mecanismos de Falência:**
    - **Pessoas:** Indivíduos sem salário e com patrimônio negativo são removidos da simulação.
    - **Empresas:** Empresas com prejuízo consecutivo por 18 meses declaram falência e são desativadas do mercado.
- **Interface de Console Dinâmica:** As tabelas de resultados se ajustam dinamicamente ao tamanho dos números, mantendo o alinhamento e a legibilidade.
- **População Configurável:** Um script auxiliar (`gerar_populacao.py`) permite gerar populações de qualquer tamanho com base nos parâmetros definidos.

## 📁 Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
simulador_economico/
|
|-- data/                 # Arquivos de dados de entrada
|    |-- categorias.json
|    |-- empresas.csv
|    +-- pessoas.txt
|
|-- scripts/              # Ferramentas auxiliares
|    +-- gerar_populacao.py
|
|-- simulador/            # Pacote com o código fonte da simulação
|    |-- __init__.py
|    |-- agents.py         # Define as classes Pessoa e Empresa
|    |-- config.py         # Parâmetros globais (inflação, salário mínimo)
|    |-- io_handler.py     # Lógica para ler os arquivos de dados
|    +-- presentation.py   # Lógica para exibir as tabelas no console
|
+-- main.py               # Ponto de entrada para executar a simulação
+-- README.md             # Este arquivo
```

## ⚙️ Como Executar

Siga os passos abaixo para rodar a simulação.

### Pré-requisitos
- Python 3.x

### 1. Preparação dos Dados

Antes de iniciar a simulação, é necessário gerar o arquivo com a população de agentes.

1.  Verifique se os arquivos `data/categorias.json` e `data/empresas.csv` estão preenchidos.
2.  **Execute o gerador de população** para criar o arquivo `data/pessoas.txt`. Abra o terminal na pasta raiz do projeto e rode:
    ```bash
    python scripts/gerar_populacao.py
    ```
    Isso criará uma população de 1000 pessoas com base nos parâmetros definidos.

### 2. Iniciando a Simulação

Com os dados prontos, execute o arquivo principal:
```bash
python main.py
```

### 3. Interagindo com a Simulação

- Pressione **Enter** para avançar **1 mês**.
- Digite um **número** (ex: `120`) e pressione Enter para avançar múltiplos meses.
- Digite **`sair`** para encerrar a simulação.

## 🔧 Configuração

Você pode facilmente alterar os cenários econômicos modificando as variáveis no arquivo `simulador/config.py`:

- `INFLACAO_ANUAL`: Define a taxa de inflação inicial para o primeiro ano da simulação.
- `SALARIO_MINIMO`: Define o salário mínimo inicial.

Ambas as variáveis são atualizadas dinamicamente a cada ano que passa na simulação.

---

*Desenvolvido por Rafael Alesson e Ana Beatriz*