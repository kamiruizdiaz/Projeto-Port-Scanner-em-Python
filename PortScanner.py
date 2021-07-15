import nmap

scanner = nmap.PortScanner()


print(" Seja bem vindo ao PortScanner")
print("<---------------------------->")


ip = input("Digite um ip ou host a ser varrido: ")
print("O ip que voce digitou foi: ", ip)
type(ip)


menu = input("""\nEntre com o numero do tipo de Scan que voce deseja fazer:
                    1 -> Scan do tipo SYN
                    2 -> Scan do tipo UDP
                    3 -> Scan do tipo Intenso
                    Numero do Scan: """)
print("Voce escolheu o scan de numero: ", menu)


if menu == "1":
    print("Versao do NMAP: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())


elif menu == "2":
    print("Versao do NMAP: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['udp'].keys())


elif menu == "3":
    print("Versao do NMAP: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())
