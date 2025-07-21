import subprocess

print("Script destinado a pegar a versão do banner de um host em uma porta especifica")
print("Insira os parâmetros necessários para que o programa funcione!!")

host = input("Insira o host que deseja realizar a verificação: ")
port = input("Insira a porta que deseja realizar a verificação: ")


nmap_command = ["nmap", "-p", port, "--script=banner", host]
banner_scan = subprocess.run(nmap_command, capture_output=True, text=True)


if banner_scan.returncode == 0:
    print("Banner encontrado:")
    for line in banner_scan.stdout.splitlines():
        if line.strip() and line.strip()[0].isdigit():
            print(line.strip())
else:
    print("Erro ao executar o comando Nmap:")
    print(banner_scan.stderr)

print("Programa encerrado!")
