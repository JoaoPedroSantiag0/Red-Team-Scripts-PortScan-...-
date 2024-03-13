import subprocess

print("Programa destinado a reconhecer portas abertas em um HOST.")
print("Mude os parâmetros para que as exigências sejam atendidas.")
print("É necessário a digitação de um HOST válido.")

h = input("\nDigite o HOST que deseja fazer a varredura: ")
print("Os parametros que já estão presentes na varredura são: -sS -sV -Pn")

# Lista de parâmetros padrão
parametros = ["-sS", "-sV", "-Pn"]

print("Executando varredura...")
result = subprocess.run(["nmap"] + parametros + [h], capture_output=True, text=True)

if result.returncode == 0:
    lines = result.stdout.splitlines()
    if any("open" in line for line in lines):
        print("Portas abertas:")
        for line in lines:
            if "open" in line:
                print(line)
else:
    print(f"Erro ao executar o nmap. Mensagem de erro: {result.stderr}")
