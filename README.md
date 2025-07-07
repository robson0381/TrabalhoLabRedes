# Trabalho de Redes — Matrizes com Docker

Este projeto implementa três programas (`prog1`, `prog2`, `prog3`) que se comunicam por sockets TCP para calcular determinantes de matrizes. Os programas rodam em containers Docker conectados por uma rede bridge. O código está versionado no GitHub.

Pré-requisitos: Docker, Docker Compose, Git instalados. No Windows recomenda-se rodar os comandos no terminal Git Bash.

Para executar:

1. Clone o repositório:
git clone https://github.com/robson0381/TrabalhoLabRedes.git
cd TrabalhoLabRedes

2. Construa e suba os containers:
docker compose up --build

Os containers `prog1`, `prog2` e `prog3` serão criados e conectados à rede. No terminal você verá `prog3` escutando em uma porta e `prog2` aguardando conexão de `prog1`.

3. Em um terminal separado, execute o prog2:
docker exec -it prog2 bash
python prog2.py

O `prog2` ficará aguardando conexão de `prog1`.

4. Em outro terminal separado, execute o prog1:
docker exec -it prog1 bash
python prog1.py

Digite a ordem das matrizes e a quantidade quando solicitado. O `prog1` enviará os dados para `prog2`, que calculará e enviará os resultados para `prog3`.

Os resultados aparecerão no terminal onde `prog3` está rodando.

Para parar os containers após o teste:
docker compose down
