import socket

hostname = "google.com"
porta = [21, 22, 23, 25, 80, 110, 119, 143, 443, 445, 3389, 8080]
file = open("Exportscan.txt", '+w')

try:

    for p in porta:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.3)
        scan = cliente.connect_ex((hostname, p))
        if scan == 0:
            print(f"Porta aberta: {p} {socket.getservbyport(p)}")

except:
    print("Alvo não existe")
