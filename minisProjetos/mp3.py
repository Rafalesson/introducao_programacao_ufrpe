def simulador_investimentos():
    """Executa o simulador de investimentos."""

    print("SIMULADOR DE INVESTIMENTOS")
    print("\x1B[3mOlá, vou te ajudar a simular as possibilidades de investimentos\x1B[0m")

    ipca = 5.53
    cdi = 14.65
    poupanca_anual = 6.00

    print("\nPra começar, quero te dizer que as \033[34mtaxas anuais\033[0m que estou utilizando são:")
    print(f"\033[34mIPCA\033[0m (inflação): \033[35m{ipca:.2f}%\033[0m")
    print(f"\033[34mCDI\033[0m (juros):.... \033[35m{cdi:.2f}%\033[0m")
    print(f"\033[34mPoupança\033[0m:....... \033[35m{poupanca_anual:.2f}%\033[0m")
    
    valor_valido = False
    while not valor_valido:
        try:
            valor = float(input("\nAgora me informa o valor em reais que você vai investir:\033[32m R$ \033[0m"))
            print("\x1B[3mOk, registrei o valor do seu investimento.\x1B[0m")
            valor_valido = True
        except ValueError:
            print("\033[31mEntrada inválida. Por favor, digite um número.\033[0m")

    print("\nEssas são as opções de investimento que tenho disponíveis para você:")
    print("[A] \033[34mCDB\033[0m valendo 100% do CDI, taxa final de \033[35m14.65%\033[0m")
    print("[B] \033[34mCDB\033[0m valendo 110% do CDI, taxa final de \033[35m16.12%\033[0m")
    print("[C] \033[34mCDB\033[0m valendo 120% do CDI, taxa final de \033[35m17.58%\033[0m")
    print("[D] \033[34mLCA\033[0m valendo  95% do CDI, taxa final de \033[35m13.92%\033[0m")
    print("\x1B[3mObs.: Lembre que o CDB retém IR na fonte, enquanto a LCA não.\x1B[0m")

    opcao = input("\nQual o investimento que você quer fazer (A, B, C ou D)? ").strip().upper()
    while opcao not in ["A", "B", "C", "D"]:
        opcao = input("\033[31mOpção inválida. Escolha entre A, B, C ou D: \033[0m").strip().upper()

    print("\x1B[3mOk, registrei a sua opção de investimento.\x1B[0m")

    if opcao == "A":
        taxa_ano = cdi * 1.00
        nome_investimento = "CDB 100% CDI"
    elif opcao == "B":
        taxa_ano = cdi * 1.10
        nome_investimento = "CDB 110% CDI"
    elif opcao == "C":
        taxa_ano = cdi * 1.20
        nome_investimento = "CDB 120% CDI"
    else:
        taxa_ano = cdi * 0.95
        nome_investimento = "LCA 95% CDI"

    if opcao in ["A", "B", "C"]:
        print("\x1B[3m")
        print("Como você escolheu um CDB, vou te lembrar das taxas regressivas de Imposto de Renda:")
        print("Até 6 meses:...... \033[35m22.5%\033[0m")
        print("Até 12 meses:..... \033[35m20.0%\033[0m")
        print("Até 24 meses:..... \033[35m17.5%\033[0m")
        print("Acima de 24 meses: \033[35m15.0%\033[0m")
        print("\x1B[0m")

    while True:
        try:
            tempo_meses = int(input("\nQuanto tempo você gostaria de esperar para resgatar esse investimento (em meses)? "))
            if tempo_meses <= 0:
                print("\033[31mO tempo deve ser um número positivo de meses.\033[0m")
            else:
                print("\x1B[3mOk, registrei o tempo para o resgate.\x1B[0m")
                break
        except ValueError:
            print("\033[31mEntrada inválida. Por favor, digite um número inteiro de meses.\033[0m")

    # --- Define a alíquota de IR com base no tempo de aplicação (apenas para CDB) ---
    aliquota_ir = 0
    if opcao in ["A", "B", "C"]:
        if tempo_meses <= 6:
            aliquota_ir = 22.5
        elif tempo_meses <= 12:
            aliquota_ir = 20.0
        elif tempo_meses <= 24:
            aliquota_ir = 17.5
        else:
            aliquota_ir = 15.0

    taxa_mes = (1 + taxa_ano / 100)**(1 / 12) - 1
    valor_bruto = valor * (1 + taxa_mes)**tempo_meses
    lucro_bruto = valor_bruto - valor
    imposto = lucro_bruto * (aliquota_ir / 100) if opcao in ["A", "B", "C"] else 0
    valor_liquido = valor_bruto - imposto

    taxa_poupanca_mes = (1 + poupanca_anual / 100)**(1 / 12) - 1
    valor_poupanca = valor * (1 + taxa_poupanca_mes)**tempo_meses

    taxa_ipca_mes = (1 + ipca / 100)**(1 / 12) - 1
    valor_corrigido_ipca = valor * (1 + taxa_ipca_mes)**tempo_meses
    ganho_real = valor_liquido - valor_corrigido_ipca

    print("\n--- RESUMO DA SIMULAÇÃO ---")
    print("\nTAXAS UTILIZADAS")
    if opcao in ["A", "B", "C"]:
        print(f"{'Taxa de IR aplicada........:':<35} \033[35m{aliquota_ir:.2f}%\033[0m")
    else:
        print(f"{'Imposto de Renda...........:':<35} Isento (LCA)")
    print(f"{'Taxa de rendimento anual...:':<35} \033[35m{taxa_ano:.2f}%\033[0m")
    print(f"{'Taxa de rendimento mensal..:':<35} \033[35m{taxa_mes * 100:.2f}%\033[0m")

    print("\nRESULTADO")
    print(f"{'Valor investido............:':<35} \033[32mR$ {valor:.2f}\033[0m")
    print(f"{'Tempo de aplicação.........:':<35} \033[34m{tempo_meses} meses\033[0m")
    if opcao in ["A", "B", "C"]:
        print(f"{'Dedução do IR..............:':<35} \033[35m{aliquota_ir:.2f}%\033[0m")
        print(f"{'Valor deduzido de IR.......:':<35} \033[32mR$ {imposto:.2f}\033[0m")
    print(f"{'Valor final estimado.......:':<35} \033[32mR$ {valor_liquido:.2f}\033[0m")
    print(f"{'Lucro total................:':<35} \033[32mR$ {valor_liquido - valor:.2f}\033[0m")

    # --- Pergunta se o usuário quer análises adicionais ---
    analise = input("\nVocê gostaria de ver algumas análises adicionais? (\033[32msim\033[0m/\033[31mnão\033[0m): ").strip().lower()
    
    if analise == "sim":
        print("\nANÁLISES POUPANÇA")
        lucro_poupanca = valor_poupanca - valor
        diferenca_lucro = valor_liquido - valor_poupanca
        print(f"Se você tivesse investido \033[32mR$ {valor:.2f}\033[0m na poupança, ao final dos \033[34m{tempo_meses} meses\033[0m:")
        print(f"O valor resgatado seria....................................: \033[32mR$ {valor_poupanca:.2f}\033[0m")
        print(f"Lucro total................................................: \033[32mR$ {lucro_poupanca:.2f}\033[0m")
        print(f"A diferença de lucro em relação ao {nome_investimento} é de: \033[32mR$ {diferenca_lucro:.2f}\033[0m")

        print("\nANÁLISES INFLAÇÃO")
        inflacao_acumulada = ((valor_corrigido_ipca / valor) - 1) * 100  
        desvalorizacao = ((valor / valor_corrigido_ipca) - 1) * 100
        exemplo_preco = valor
        preco_corrigido = exemplo_preco * ((1 + taxa_ipca_mes) ** tempo_meses)
        valor_resgate_corrigido = valor_liquido * (valor / valor_corrigido_ipca)
        valor_poupanca_corrigida = valor_poupanca * (valor / valor_corrigido_ipca)

        print(f"{'A inflação acumulada foi de..................:':<50} \033[35m{inflacao_acumulada:.2f}%\033[0m")
        print(f"{'Resultando em uma desvalorização de..........:':<50} \033[35m{desvalorizacao:.2f}%\033[0m")
        print(f"{'Se você comprava algo por....................:':<50} \033[32mR$ {exemplo_preco:.2f}\033[0m")
        print(f"{'O mesmo item custaria corrigido pela inflação:':<50} \033[32mR$ {preco_corrigido:.2f}\033[0m")
        print(f"{'O resgate ajustado ao valor real é...........:':<50} \033[32mR$ {valor_resgate_corrigido:.2f}\033[0m")
        print(f"{'A poupança ajustada ao valor real é..........:':<50} \033[32mR$ {valor_poupanca_corrigida:.2f}\033[0m")

    print("\nRESUMO FINAL")
    print(f"{'Valor investido...............:':<35} \033[32mR$ {valor:.2f}\033[0m")
    print(f"{'Valor resgatado (investimento):':<35} \033[32mR$ {valor_liquido:.2f}\033[0m")
    print(f"{'Se fosse na poupança..........:':<35} \033[32mR$ {valor_poupanca:.2f}\033[0m")
    print(f"{'Correção da inflação..........:':<35} \033[32mR$ {valor_corrigido_ipca:.2f}\033[0m")
    print(f"{'Ganho real acima da inflação..:':<35} \033[32mR$ {ganho_real:.2f}\033[0m")

    print("\n\x1B[3mEspero ter ajudado!\x1B[0m")

simulador_investimentos()
