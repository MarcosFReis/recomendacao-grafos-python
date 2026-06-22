#  Sistema de Recomendação de Streaming com Inteligência de Grafos

Este projeto implementa a modelagem e a arquitetura de um banco de dados orientado a grafos utilizando **Python** e **Neo4j**. O objetivo principal é simular o motor de recomendações de uma plataforma de streaming de vídeo (como Netflix ou Prime Video), sugerindo novos conteúdos aos usuários de forma personalizada com base em seus históricos de visualização e preferências de gênero.

##  Desafio de Negócio
Em plataformas tradicionais baseadas em bancos de dados relacionais (SQL), realizar cruzamentos complexos de tabelas gigantescas (como `Usuarios` -> `Historico` -> `Filmes` -> `Generos`) exige múltiplos comandos `JOIN`, o que degrada a performance do sistema em larga escala. 

A abordagem por **Teoria dos Grafos** elimina a necessidade de JOINS complexos através da **Adjacência Livre de Índices (Index-free Adjacency)**, onde o sistema simplesmente caminha pelos ponteiros físicos que interconectam os nós em tempo real.

##  Modelagem do Grafo (Arquitetura)
O banco de dados na nuvem foi estruturado utilizando quatro tipos de **Nós (Vértices)** e duas principais **Arestas (Relacionamentos Direcionados)**:

* **Nós:**
  * `:User` (Guarda o ID único e o Nome do cliente)
  * `:Movie` (Guarda o ID, Título e Ano de lançamento)
  * `:Series` (Guarda o ID, Título e Ano de lançamento)
  * `:Genre` (Guarda o Nome do gênero cinematográfico)
* **Relacionamentos:**
  * `(:User)-[:WATCHED {rating: float}]->(:Movie/:Series)`
  * `(:Movie/:Series)-[:IN_GENRE]->(:Genre)`

##  Lógica do Algoritmo de Recomendação
A consulta desenvolvida em linguagem **Cypher** dentro do script Python realiza o seguinte caminhamento na rede:
1. Identifica o usuário alvo através do parâmetro `user_id`.
2. Mapeia todos os conteúdos que ele já assistiu (`-[:WATCHED]->`) e extrai seus respectivos gêneros (`-[:IN_GENRE]->`).
3. Busca no ecossistema global outros filmes e séries que pertencem a esses mesmos gêneros.
4. Aplica uma cláusula de negação (`WHERE NOT`) para expurgar títulos que o usuário já assistiu, garantindo recomendações 100% inéditas.

##  Tecnologias Utilizadas
* **Python 3.12+**: Linguagem base para execução do script, tratamento de entradas e manipulação de estruturas.
* **Neo4j AuraDB (Cloud)**: Banco de dados em grafos nativo hospedado na nuvem.
* **Driver Oficial do Neo4j para Python**: Gerenciamento de sessões, execução de queries assíncronas e parsing de objetos de rede para dicionários Python nativos.

##  Como Executar o Projeto

Para rodar o script e conectar no banco, o caminho é bem direto:

1. Cria um ambiente virtual (.venv) no seu editor e instala o driver oficial do Neo4j rodando o comando clássico no terminal:
   pip install neo4j

2. Abre o arquivo `projeto_grafos.py` e joga as tuas credenciais do AuraDB lá no topo:
   URI = "neo4j+s://seu-id.databases.neo4j.io"
   AUTH = ("neo4j", "SUA_SENHA_AURA_DB")

3. Coloca o arquivo para rodar. O próprio script cuida de verificar se os dados já existem no banco usando a lógica do `MERGE` para não duplicar nada. Depois disso, o terminal vai abrir o input pedindo o ID do usuário (pode testar com U01 ou o usuário que quiser seguindo essa linha) para cuspir as recomendações personalizadas na hora.
