import socket

def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.error as e:
        print(f"Erro ao obter o endereço IP de {hostname}: {e}")
        return None

def get_hostname(ip_address):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.error as e:
        print(f"Erro ao obter o nome do host para o endereço IP {ip_address}: {e}")
        return None

# Exemplo de uso:
host = input("Insira o nome de um host: ")
print(f"O host que você inseriu foi: {host}\n")
ip = get_ip_address(host)
print(f"O endereço IP de {host} é: {ip}")

if ip:
    hostname = get_hostname(ip)
    if hostname:
        print(f"O nome do host para o endereço IP {ip} é: {hostname}")