import subprocess
import re
import sys
import threading
import time
from colorama import Fore, Style, init

init(autoreset=True)

def print_positive(message):
    print(f"\n {Fore.GREEN}[+] {message} [+]{Style.RESET_ALL}\n")

def print_negative(message):
    print(f"\n {Fore.RED}[-] {message} [-]{Style.RESET_ALL}\n")

def animate_loading():
    while not event.is_set():
        for cursor in '|/-\\':
            sys.stdout.write(cursor)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')

def perform_ping(host):
    global event
    event = threading.Event()
    animate_thread = threading.Thread(target=animate_loading)
    animate_thread.start()

    try:
        ping_process = subprocess.Popen(["ping", "-c", "4", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = ping_process.communicate()
        event.set()
    except Exception as e:
        event.set()
        raise e

    return output, error

def perform_port_scan(host, params):
    global event
    event = threading.Event()
    animate_thread = threading.Thread(target=animate_loading)
    animate_thread.start()

    try:
        result = subprocess.run(["nmap"] + params + [host], capture_output=True, text=True)
        event.set()  # Sinaliza para a thread de animação parar
    except Exception as e:
        event.set()  # Certifique-se de parar a thread de animação em caso de exceção
        raise e

    return result.stdout

print("Programa destinado a reconhecer se o HOST está ativo ou não!")
print("Mude os parametros para que as exigências sejam atendidas.")
print("É necessário a digitação de um HOST.")

h = input("Digite o HOST que deseja fazer a identificação: ")

print(f"O host que o usuário inseriu foi: {h}")
print("Verificando se o HOST está ativo...", end='', flush=True)

lines = []
print("")
try:
    output, error = perform_ping(h)
    lines = output.splitlines()
except Exception as e:
    print_negative(f"Erro durante a verificação do HOST: {e}")

if len(lines) >= 2 and re.search(r'ttl=(\d+)', lines[1]):
    ttl_match = re.search(r'ttl=(\d+)', lines[1])
    ttl_value = int(ttl_match.group(1))

    if ttl_value > 0:
        print_positive("Ativo!")
        print(f"O TTL detectado é: {ttl_value}")

        # Identificação do sistema operacional
        if 0 < ttl_value <= 64:
            print("Possível sistema operacional: ** Linux **")
        elif 64 < ttl_value <= 128:
            print("Possível sistema operacional: ** Windows **")
        elif ttl_value == 255:
            print("Possível sistema operacional: ** Solaris **")
        else:
            print("Não é possível inferir o sistema operacional com base no TTL.")
        print("O HOST está ativo e disponível para identificação de portas.")
        print("")
        
        opc = input("Deseja começar uma varredura de portas no HOST? S ou N: ")

        if opc.upper() == "S":
            print("Os parametros que já estão presentes na varredura são: -sS -sV -Pn")
            parametros = ["-sS", "-sV", "-Pn"]
            print("Executando varredura... ", end='', flush=True)
            try:
                result = perform_port_scan(h, parametros)
                lines = result.splitlines()
                if any("open" in line for line in lines):
                    print("Portas abertas:")
                    for line in lines:
                        if "open" in line:
                            print(line)
            except Exception as e:
                print_negative(f"\nErro durante a varredura de portas: {e}")
    else:
        print_negative("Não ativo.")
else:
    print_negative("Não ativo ou não está respondendo ao ping.")
    print("Lembrando que para alguns HOST's é necessário a conexão em VPN para a identificação.")

print("\nPrograma Finalizado!")
