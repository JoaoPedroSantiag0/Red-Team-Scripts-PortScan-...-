import subprocess

print("Programa destinado a realização de WpScan")
print("Verifique se o host tem conexão HTTP ou HTTPS")

verificação = input("O host que deseja realizar o brute force de diretórios é HTTPS ou HTTP?: ")
if verificação.upper() == "HTTPS":
    print("Adicione somente a parte dos número ou domínios do host que deseja realizar o brute force de diretórios")
    print("Exemplos: 10.10.11.239 ou exemplo.com")
    print("Para que fique assim quando o código for rodar no terminal: https://10.10.11.239")
    host = input("Insira o host que você deseja realizar o brute force de diretórios: ")
    WpScan = subprocess.run(["wpscan", "https://"+host] + ["--enumerate", "p"])
elif verificação.upper() == "HTTP":
    print("Adicione somente a parte dos número ou domínios do host que deseja realizar o brute force de diretórios")
    print("Exemplos: 10.10.11.239 ou exemplo.com")
    print("Para que fique assim quando o código for rodar no terminal: http://10.10.11.239")
    host = input("Insira o host que você deseja realizar o brute force de diretórios: ")
    WpScan = subprocess.run(["wpscan", "http://"+host] + ["--enumerate", "p"])


print("Programa finalizado!!!")