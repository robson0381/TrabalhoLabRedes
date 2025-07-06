import socket
import pickle
import time

def main():
    HOST = '0.0.0.0'
    PORT = 0  # 0 → sistema escolhe porta livre automaticamente

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        PORT = s.getsockname()[1]  # lê a porta escolhida pelo sistema

        # escreve a porta escolhida num arquivo para que prog2 saiba
        with open('/tmp/porta_prog3.txt', 'w') as f:
            f.write(str(PORT))

        print(f"prog3 escutando na porta {PORT}...")

        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(4096)
                if not data:
                    continue

                # Deserializa pacote
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
