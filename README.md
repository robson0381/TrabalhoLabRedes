Trabalho de Redes — Matrizes com Docker
Este projeto implementa um sistema distribuído para geração, processamento e cálculo de determinantes de matrizes via sockets TCP, utilizando 3 programas em Python, orquestrados com Docker e Docker Compose.

📁 Estrutura do projeto
Copiar
Editar
TrabalhoLabRedes/
├── prog1/
│   ├── Dockerfile
│   └── prog1.py
├── prog2/
│   ├── Dockerfile
│   └── prog2.py
├── prog3/
│   ├── Dockerfile
│   └── prog3.py
├── docker-compose.yml
└── README.md
🚀 Requisitos
Docker instalado.

Docker Compose instalado.

Git (opcional, para clonar o repositório).

🔧 Como executar
1️⃣ Clone o repositório
bash
Copiar
Editar
git clone https://github.com/robson0381/TrabalhoLabRedes.git
cd TrabalhoLabRedes
2️⃣ Suba os containers
bash
Copiar
Editar
docker compose up --build
Isso criará a rede e iniciará os 3 containers (prog1, prog2, prog3).

Você verá que prog3 imprimirá a porta em que está escutando e prog2 ficará aguardando a criação do arquivo da porta.

🖥️ Execução dos programas
Programa 3 — já iniciado
No log do docker compose up, você verá algo como:

nginx
Copiar
Editar
prog3 | prog3 escutando na porta 32000...
Programa 2 — já iniciado
No log do docker compose up, você verá prog2 aguardando conexão do prog1.

Programa 1 — rodar manualmente
Abra um novo terminal e execute:

bash
Copiar
Editar
docker exec -it prog1 bash
Dentro do container:

bash
Copiar
Editar
python prog1.py
Siga as instruções para informar a ordem e a quantidade de matrizes. Ele enviará as matrizes para prog2 que processará e enviará o resultado para prog3.

🧹 Finalizar containers
Quando quiser parar:

bash
Copiar
Editar
docker compose down
📖 Observações
O programa só funciona corretamente com os 3 containers rodando.

É necessário esperar prog3 criar o arquivo de porta antes de prog2 continuar.