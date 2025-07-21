import subprocess

print("Programa destinado a quebra de senhas de WiFi's")
print("Para o bom funcionamento do script deve-se ter o programa 'aircrack-ng' instalado")
print("Insira os parâmetros necessários para que o programa funcione!!")
print("É necessário que o usuário tenha um arquivo de analise de rede (.pcap) COM PADRÃO 802.11 WIRELESS para realizar a quebra de senha do WiFi")
print("\nA Wordlist padrão do script é a ROCKYOU.txt! Caso deseje alterar a mesma entre nos códigos do programa e modifique o path da lista")
arquivo = input("\nInsira o nome do arquivo pcap: ")

resultado = subprocess.run(["aircrack-ng", arquivo, "-w" , "/usr/share/wordlists/rockyou.txt"], capture_output=True, text=True)

if resultado.returncode != 0:
    print("Ocorreu um erro ao executar aircrack-ng. Verifique se os parâmetros estão corretos e se o arquivo pcap é válido.")
    print("Erro:", resultado.stderr)
else:

    redes_wifi = [linha.strip() for linha in resultado.stdout.splitlines() if linha.strip().isdigit()]

    print("\nRedes WiFi encontradas:")
    for i, rede in enumerate(redes_wifi, 1):
        print(f"{i}: {rede}")

    escolha = input("\nEscolha o número da rede WiFi que deseja testar: ")

    if escolha.isdigit() and 1 <= int(escolha) <= len(redes_wifi):
        rede_escolhida = redes_wifi[int(escolha) - 1]
        print(f"\nVocê escolheu testar a rede WiFi: {rede_escolhida}")
    else:
        print("Escolha inválida. Por favor, insira um número correspondente a uma das redes WiFi listadas.")