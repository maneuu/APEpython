import lib_vogais as lv

menu = """
🔠 MENU - MANIPULAÇÃO DE VOGAIS 🔠

1️⃣ - Verificar se o texto contém apenas vogais.
2️⃣ - Contar a quantidade de vogais no texto.
3️⃣ - Exibir o texto sem vogais.
4️⃣ - Substituir vogais por '*'.
5️⃣ - Mostrar as vogais presentes no texto.
6️⃣ - Exibir a frequência de cada vogal.
7️⃣ - Mostrar a vogal mais frequente.
8️⃣ - 🚪 Sair.
"""

while True:
    print(menu)
    while True:
        try:
            opcao = int(input("📝 Escolha uma opção (1-8): "))
            if 1 <= opcao <= 8:
                break
            else:
                print("❌ Opção inválida! Escolha um número entre 1 e 8.")
        except ValueError:
            print("⚠️ Digite um número válido!")

    if opcao == 8:
        print("👋 Programa finalizado! Até a próxima!")
        break

    texto = input("✍️ Digite um texto: ")

    if opcao == 1:
        resultado = lv.eh_texto_vogal(texto)
        if resultado:
            print("😍 Uau! Seu texto é composto apenas por vogais!")
        else:
            print("😕 Hmm... Seu texto contém outros caracteres além das vogais.")
    elif opcao == 2:
        quantidade = lv.quantidade_vogais(texto)
        print(f"🔢 O seu texto possui {quantidade} vogais. Incrível, não é?")
    elif opcao == 3:
        texto_sem_vogais = lv.remove_vogais(texto)
        print("📝 Confira como ficou seu texto sem as vogais:")
        print(texto_sem_vogais)
    elif opcao == 4:
        texto_substituido = lv.substitui_vogais(texto)
        print("✨ Olha só! As vogais foram substituídas por '*':")
        print(texto_substituido)
    elif opcao == 5:
        vogais_encontradas = lv.identifica_vogais(texto)
        if vogais_encontradas:
            vogais_formatado = ", ".join(vogais_encontradas)
            print("🔍 Você usou as seguintes vogais no seu texto:")
            print(vogais_formatado)
        else:
            print("❌ Não encontramos nenhuma vogal no seu texto!")
    elif opcao == 6:
        frequencias = lv.frequencia_vogais(texto)
        vogais = ['a', 'e', 'i', 'o', 'u']
        print("📊 Frequência das vogais no seu texto:")
        for i in range(len(vogais)):
            vogal = vogais[i]
            freq = frequencias[i]
            print(f"   {vogal.upper()}: {freq}")
    elif opcao == 7:
        mais_freq = lv.vogal_mais_frequente(texto)
        print("🏆 A estrela do seu texto é a vogal:")
        print(mais_freq)

    print("\n🔄 Voltando ao menu...\n")
