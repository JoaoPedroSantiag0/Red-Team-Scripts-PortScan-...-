import subprocess

print("Programa destinado a brute force de uma lista de diretórios")
print("Verifique se o host tem conexão HTTP ou HTTPS")

verificacao = input("O host que deseja realizar o brute force de diretórios é HTTPS ou HTTP?: ")

if verificacao.upper() in ["HTTP", "HTTPS"]:
    print("Adicione somente a parte dos números ou domínios do host que deseja realizar o brute force de diretórios")
    print("Exemplos: 10.10.11.239 ou exemplo.com")
    print("Para que fique assim quando o código for rodar no terminal: https://10.10.11.239")
    host = input("Insira o host que você deseja realizar o brute force de diretórios: ")

    try:
        subprocess.run(["gobuster", "dir", "-u", f"{verificacao.lower()}://{host}", "-w", "/usr/share/wordlists/dirb/extensions_common.txt"], check=True)
        print("GoBuster executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar GoBuster: {e}")
else:
    print("Opção inválida. Escolha entre HTTP ou HTTPS.")

print("Programa finalizado!!!")


