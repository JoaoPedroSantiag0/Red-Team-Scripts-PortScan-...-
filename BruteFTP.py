import subprocess

print("Programa destinado a brute force no serviço ssh (porta 21) de um host")
print("Insira os parametros necessarios para que o programa funcione!!")

host = input("Insira o ip que deseja realizar o teste de brute force: ")

print("O host inserido foi: ", host)

process = subprocess.Popen(["hydra", "-L", "teste.txt", "-P", "teste.txt", host, "ftp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

for line in process.stdout:
    print(line.strip())
    if "[21][ftp]" in line:
        print("Combinação encontrada:", line.strip())


process.wait()

print("Programa encerrado!")