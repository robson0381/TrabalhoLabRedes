import socket
import pickle
import threading
import time

def main():
    HOST = '0.0.0.0'
    PORT_INFO = 7000  # porta fixa para registrar

    # cria socket dinâmico
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_socket.bind((HOST, 0))
    DATA_PORT = data_socket.getsockname()[1]
    print(f"prog3 escutando para dados na porta {DATA_PORT}...")

    data_socket.listen()

    # thread para informar a porta
    def info_server():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as info_socket:
            info_socket.bind((HOST, PORT_INFO))
            info_socket.listen()
            while True:
                conn, _ = info_socket.accept()
                with conn:
                    conn.sendall(str(DATA_PORT).encode())

    threading.Thread(target=info_server, daemon=True).start()

    # aguarda conexões para dados
    while True:
        conn, addr = data_socket.accept()
        with conn:
            data = conn.recv(4096)
            if not data:
                continue

            resultado = pickle.loads(data)
            determinante = resultado['determinante']
            start_time = resultado['start_time']
            tempo_total = time.time() - start_time

            print("=== Resultado recebido ===")
            if determinante is None:
                print("Matriz singular — não foi possível calcular o determinante.")
            else:
                print(f"Determinante: {determinante:.4f}")
            print(f"Tempo total: {tempo_total:.4f} segundos\n")

if __name__ == "__main__":
    main()
