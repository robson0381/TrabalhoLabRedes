import socket
import pickle
import numpy as np
import time
import os

def main():
    # Entrada do usuário
    ordem = int(input("Digite a ordem das matrizes (ex: 3 para 3x3): "))
    quantidade = int(input("Digite o número de matrizes a serem geradas: "))

    # Configurações do destino (prog2)
    HOST_PROG2 = 'prog2'
    PORT_PROG2 = int(os.environ.get('PROG2_PORT', 6000))

    for i in range(quantidade):
        # Geração da matriz
        matriz = np.random.randint(1, 10, (ordem, ordem))
        start_time = time.time()

        # Pacote a ser enviado
        pacote = {
            'matriz': matriz,
            'start_time': start_time
        }

        # Envio via socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST_PROG2, PORT_PROG2))
            s.sendall(pickle.dumps(pacote))

        print(f"[{i+1}/{quantidade}] Matriz enviada com sucesso.")
        time.sleep(0.5)  # Pequeno intervalo para evitar sobrecarga

if __name__ == "__main__":
    main()
