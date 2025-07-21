import subprocess

print("Script destinado a identificação de firewall em sites web")
print("Insira os parâmetros necessários para que o programa funcione!!")

host = input("Insira o host que deseja realizar a verificação: ")
print(f"O site inserido foi: {host}")

resposta = input("O site que você inseriu está correto? S ou N: ")
resposta = resposta.upper()

if resposta == "S":
    print("O comando irá mostrar os dados abaixo!")

    try:
        result = subprocess.run(["wafw00f", host], capture_output=True, text=True, check=True)
        
        # Itera sobre as linhas da saída e imprime a linha inteira se contiver "is behind"
        for line in result.stdout.split('\n'):
            if "is behind" in line:
                print("Firewall encontrado:")
                print(line)
                print("************************************************")
        
        print(result.stdout)
        print("Programa finalizado!")
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando:", e)
    except Exception as e:
        print("Erro inesperado:", e)
else:
    print("Programa finalizado, caso queira realizar uma nova verificação, reinicie o script.")
