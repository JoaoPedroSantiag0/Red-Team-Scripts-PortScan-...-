import subprocess

print("Programa destinado ao reconhecimento de hosts up na rede!")
print("O comando que será executado para a identificação dos hosts up é: arp-scan -l --ignoredups")
print("Ressaltando que caso o usuário deseje adicionar algum parâmetro, você pode adicionar na linha de comando.\n")


resultado = subprocess.run(["arp-scan", "-l", "--ignoredups"], capture_output=True, text=True)


if resultado.returncode == 0:
    
    linhas = resultado.stdout.split('\n')
    
    for linha in linhas:
        partes = linha.split()
        
        if len(partes) > 1 and any(caractere.isdigit() for caractere in partes[1]):
            print(f"HOST UP: {linha} <<- Informação adicional.")
else:

    print("Ocorreu um erro ao executar o comando arp-scan.")
    print("Código de retorno:", resultado.returncode)
    print("Saída de erro:", resultado.stderr)