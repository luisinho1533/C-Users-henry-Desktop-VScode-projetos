import socket

hostname = "google.com"
porta = range(1, 65535)

try:

    for p in porta:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.1)
        scan = cliente.connect_ex((hostname, p))
        if scan == 0:
            print(f"Porta aberta: {p} {socket.getservbyport(p)}")

except:
    print("Alvo não existe")
