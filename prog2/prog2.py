import socket
import pickle
import numpy as np
import time

def main():
    HOST_PROG3 = 'prog3'

    # lê a porta escolhida por prog3 (escrita no arquivo)
    with open('/tmp/porta_prog3.txt') as f:
        PORT_PROG3 = int(f.read().strip())

    print(f"prog2 vai conectar ao prog3 em {HOST_PROG3}:{PORT_PROG3}")

    # abre socket para receber prog1
    HOST_PROG2 = '0.0.0.0'
    PORT_PROG2 = 6000  # fixa para prog1

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST_PROG2, PORT_PROG2))
        server_socket.listen()
        print(f"prog2 aguardando conexão de prog1 na porta {PORT_PROG2}...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                data = conn.recv(4096)
                if not data:
                    continue

                recebido = pickle.loads(data)
                matriz = recebido['matriz']
                start_time = recebido['start_time']

                print(f"Recebido de prog1:\n{matriz}")

                try:
                    matriz_invertida = np.linalg.inv(matriz)
                    determinante = np.linalg.det(matriz)
                except np.linalg.LinAlgError:
                    matriz_invertida = None
                    determinante = None
                    print("Matriz singular — não pode ser invertida.")

                pacote_resultado = {
                    'determinante': determinante,
                    'start_time': start_time
                }

                # conecta ao prog3 para enviar resultado
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_to_prog3:
                    client_to_prog3.connect((HOST_PROG3, PORT_PROG3))
                    client_to_prog3.sendall(pickle.dumps(pacote_resultado))

                print("Resultado enviado para prog3.\n")

if __name__ == "__main__":
    main()
