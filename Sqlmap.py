import subprocess

def extrair_nomes_bancos(output):
    linhas = output.splitlines()
    nomes_bancos = []
    for linha in linhas:
        if "[*]" in linha:
            nomes_bancos.append(linha.strip("[*] ").strip())
    return nomes_bancos

print("Scripts para treino de sqlmap")

print("Script destinado a realizar uma tentativa de acesso a banco de dados!")
print("Passe os parâmetros para que as exigências sejam atendidas.")

url = input("Insira aqui a URL que deseja realizar a tentativa de acesso: ")
print(f"A URL que você inseriu foi: {url}")

print("\n\n!!!     IMPORTANTE    !!!")
print("\n\nO script irá executar inicialmente o parâmetro --crawl=2")
print("O script irá selecionar threads nível 5, alocando mais potência da sua máquina. Tenha ciência disso.")
print("O script tem o parâmetro automático --batch dando 'Yes' em todos os questionários.")

resp1 = input("A URL está correta? S ou N: ")
resp1 = resp1.upper()
if resp1 == "S":
    try:
        print("\n\nScript rodando...")
        sqlmap = subprocess.run(["sqlmap", "-u", url, "--batch", "--crawl=2", "--dbs", "--threads=5"], capture_output=True, text=True, check=True)
        if sqlmap.returncode == 0:
            nomes_bancos = extrair_nomes_bancos(sqlmap.stdout)
            
            if nomes_bancos:
                print("\n\nTabelas identificadas:")
                print("\n***********************")
                for nome_banco in nomes_bancos:
                    print(f"[*] {nome_banco}")
                print("***********************")
                print("\nPara ler as tabelas identificadas, você pode adicionar os seguintes parâmetros:")
                print("--D <tabela>")
                print("********************************************************************************************")
                print("\n\nDessa forma -> sqlmap -u <URL> --batch --crawl=2 --dbs --threads=5 --D <tabela> --tables")
                print("\n\n********************************************************************************************")
                print("\nPROGRAMA FINALIZADO!!")
            else:
                print("Nenhuma tabela identificada.")
        else:
            print("Ocorreu um erro durante a execução do script.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script: {e}")
else:
    print("Opção inválida, programa encerrado.")