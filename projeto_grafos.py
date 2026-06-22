from neo4j import GraphDatabase

# CONFIGURAÇÕES DE CONEXÃO

URI = "neo4j+s://8afc4485.databases.neo4j.io"
AUTH = ("neo4j", "mgfsMCRqZYTI9zOTxXP3lX3Er2cF0x-y6lsz5pltn1M")

# DADOS E RELACIONAMENTOS (CYPHER)

QUERIES = [
    # Constraints
    "CREATE CONSTRAINT user_id_unique IF NOT EXISTS FOR (u:User) REQUIRE u.id IS UNIQUE;",
    "CREATE CONSTRAINT movie_id_unique IF NOT EXISTS FOR (m:Movie) REQUIRE m.id IS UNIQUE;",
    "CREATE CONSTRAINT series_id_unique IF NOT EXISTS FOR (s:Series) REQUIRE s.id IS UNIQUE;",

    # Usuários
    """
    CREATE (u1:User {id: "U01", name: "Ana"}),
           (u2:User {id: "U02", name: "Paulo"}),
           (u3:User {id: "U03", name: "João"}),
           (u4:User {id: "U04", name: "Maya"}),
           (u5:User {id: "U05", name: "Lonan"}),
           (u6:User {id: "U06", name: "Pedro"}),
           (u7:User {id: "U07", name: "Eduarda"}),
           (u8:User {id: "U08", name: "Marcos"}),
           (u9:User {id: "U09", name: "Alan"}),
           (u10:User {id: "U10", name: "Alana"})
    """,

    # Filmes
    """
    CREATE (m1:Movie {id: "M01", title: "The Matrix", releaseYear: 1999}),
           (m2:Movie {id: "M02", title: "The Godfather", releaseYear: 1972}),
           (m3:Movie {id: "M03", title: "Star Wars", releaseYear: 1977}),
           (m4:Movie {id: "M04", title: "The Green Mile", releaseYear: 1999}),
           (m5:Movie {id: "M05", title: "The Dark Knight", releaseYear: 2008}),
           (m6:Movie {id: "M06", title: "Forrest Gump", releaseYear: 1994}),
           (m7:Movie {id: "M07", title: "Dead Poets Society", releaseYear: 1989}),
           (m8:Movie {id: "M08", title: "Pulp Fiction", releaseYear: 1994}),
           (m9:Movie {id: "M09", title: "Inception", releaseYear: 2010}),
           (m10:Movie {id: "M10", title: "Home Alone", releaseYear: 1990})
    """,

    # Séries
    """
    CREATE (s1:Series {id: "S01", title: "Breaking Bad", releaseYear: 2008}),
           (s2:Series {id: "S02", title: "The Walking Dead", releaseYear: 2010}),
           (s3:Series {id: "S03", title: "Stranger Things", releaseYear: 2016}),
           (s4:Series {id: "S04", title: "Game of Thrones", releaseYear: 2011}),
           (s5:Series {id: "S05", title: "Dark", releaseYear: 2017}),
           (s6:Series {id: "S06", title: "The Crown", releaseYear: 2016}),
           (s7:Series {id: "S07", title: "Friends", releaseYear: 1994}),
           (s8:Series {id: "S08", title: "The Office", releaseYear: 2005}),
           (s9:Series {id: "S09", title: "Black Mirror", releaseYear: 2011}),
           (s10:Series {id: "S10", title: "Chernobyl", releaseYear: 2019})
    """,

    # Gêneros
    """
    CREATE (g1:Genre {name: "Ficção Científica"}),
           (g2:Genre {name: "Drama"}),
           (g3:Genre {name: "Ação"}),
           (g4:Genre {name: "Comédia"}),
           (g5:Genre {name: "Terror"}),
           (g6:Genre {name: "Suspense"}),
           (g7:Genre {name: "Romance"})
    """,

    # Histórico de Assistidos (WATCHED)
    """
    MATCH (u1:User {id: "U01"}), (m1:Movie {id: "M01"}) CREATE (u1)-[:WATCHED {rating: 5.0}]->(m1) WITH 1 as dummy
    MATCH (u1:User {id: "U01"}), (s1:Series {id: "S01"}) CREATE (u1)-[:WATCHED {rating: 5.0}]->(s1) WITH 1 as dummy
    MATCH (u2:User {id: "U02"}), (m2:Movie {id: "M02"}) CREATE (u2)-[:WATCHED {rating: 4.8}]->(m2) WITH 1 as dummy
    MATCH (u2:User {id: "U02"}), (s3:Series {id: "S03"}) CREATE (u2)-[:WATCHED {rating: 4.0}]->(s3) WITH 1 as dummy
    MATCH (u3:User {id: "U03"}), (m3:Movie {id: "M03"}) CREATE (u3)-[:WATCHED {rating: 4.2}]->(m3) WITH 1 as dummy
    MATCH (u3:User {id: "U03"}), (s4:Series {id: "S04"}) CREATE (u3)-[:WATCHED {rating: 5.0}]->(s4) WITH 1 as dummy
    MATCH (u4:User {id: "U04"}), (m9:Movie {id: "M09"}) CREATE (u4)-[:WATCHED {rating: 4.7}]->(m9) WITH 1 as dummy
    MATCH (u4:User {id: "U04"}), (s5:Series {id: "S05"}) CREATE (u4)-[:WATCHED {rating: 4.9}]->(s5) WITH 1 as dummy
    MATCH (u5:User {id: "U05"}), (m5:Movie {id: "M05"}) CREATE (u5)-[:WATCHED {rating: 5.0}]->(m5) WITH 1 as dummy
    MATCH (u5:User {id: "U05"}), (s8:Series {id: "S08"}) CREATE (u5)-[:WATCHED {rating: 4.5}]->(s8) WITH 1 as dummy
    MATCH (u6:User {id: "U06"}), (m10:Movie {id: "M10"}) CREATE (u6)-[:WATCHED {rating: 3.8}]->(m10) WITH 1 as dummy
    MATCH (u6:User {id: "U06"}), (s7:Series {id: "S07"}) CREATE (u6)-[:WATCHED {rating: 4.0}]->(s7) WITH 1 as dummy
    MATCH (u7:User {id: "U07"}), (m6:Movie {id: "M06"}) CREATE (u7)-[:WATCHED {rating: 4.5}]->(m6) WITH 1 as dummy
    MATCH (u7:User {id: "U07"}), (s6:Series {id: "S06"}) CREATE (u7)-[:WATCHED {rating: 4.3}]->(s6) WITH 1 as dummy
    MATCH (u8:User {id: "U08"}), (m8:Movie {id: "M08"}) CREATE (u8)-[:WATCHED {rating: 4.6}]->(m8) WITH 1 as dummy
    MATCH (u8:User {id: "U08"}), (s9:Series {id: "S09"}) CREATE (u8)-[:WATCHED {rating: 4.2}]->(s9) WITH 1 as dummy
    MATCH (u9:User {id: "U09"}), (m4:Movie {id: "M04"}) CREATE (u9)-[:WATCHED {rating: 4.9}]->(m4) WITH 1 as dummy
    MATCH (u9:User {id: "U09"}), (s10:Series {id: "S10"}) CREATE (u9)-[:WATCHED {rating: 5.0}]->(s10) WITH 1 as dummy
    MATCH (u10:User {id: "U10"}), (m7:Movie {id: "M07"}) CREATE (u10)-[:WATCHED {rating: 4.4}]->(m7) WITH 1 as dummy
    MATCH (u10:User {id: "U10"}), (s2:Series {id: "S02"}) CREATE (u10)-[:WATCHED {rating: 3.5}]->(s2)
    """,

    # Conectando Filmes aos Gêneros
    """
    MATCH (m1:Movie {id: "M01"}), (g1:Genre {name: "Ficção Científica"}) CREATE (m1)-[:IN_GENRE]->(g1) WITH 1 as dummy
    MATCH (m2:Movie {id: "M02"}), (g2:Genre {name: "Drama"}) CREATE (m2)-[:IN_GENRE]->(g2) WITH 1 as dummy
    MATCH (m3:Movie {id: "M03"}), (g1:Genre {name: "Ficção Científica"}) CREATE (m3)-[:IN_GENRE]->(g1) WITH 1 as dummy
    MATCH (m4:Movie {id: "M04"}), (g2:Genre {name: "Drama"}) CREATE (m4)-[:IN_GENRE]->(g2) WITH 1 as dummy
    MATCH (m5:Movie {id: "M05"}), (g3:Genre {name: "Ação"}) CREATE (m5)-[:IN_GENRE]->(g3) WITH 1 as dummy
    MATCH (m6:Movie {id: "M06"}), (g7:Genre {name: "Romance"}) CREATE (m6)-[:IN_GENRE]->(g7) WITH 1 as dummy
    MATCH (m7:Movie {id: "M07"}), (g2:Genre {name: "Drama"}) CREATE (m7)-[:IN_GENRE]->(g2) WITH 1 as dummy
    MATCH (m8:Movie {id: "M08"}), (g3:Genre {name: "Ação"}) CREATE (m8)-[:IN_GENRE]->(g3) WITH 1 as dummy
    MATCH (m9:Movie {id: "M09"}), (g6:Genre {name: "Suspense"}) CREATE (m9)-[:IN_GENRE]->(g6) WITH 1 as dummy
    MATCH (m10:Movie {id: "M10"}), (g4:Genre {name: "Comédia"}) CREATE (m10)-[:IN_GENRE]->(g4)
    """,

    # Conectar Séries aos Gêneros
    """
    MATCH (s1:Series {id: "S01"}), (g2:Genre {name: "Drama"}) CREATE (s1)-[:IN_GENRE]->(g2) WITH 1 as dummy
    MATCH (s2:Series {id: "S02"}), (g5:Genre {name: "Terror"}) CREATE (s2)-[:IN_GENRE]->(g5) WITH 1 as dummy
    MATCH (s3:Series {id: "S03"}), (g1:Genre {name: "Ficção Científica"}) CREATE (s3)-[:IN_GENRE]->(g1) WITH 1 as dummy
    MATCH (s4:Series {id: "S04"}), (g2:Genre {name: "Drama"}) CREATE (s4)-[:IN_GENRE]->(g2) WITH 1 as dummy
    MATCH (s5:Series {id: "S05"}), (g6:Genre {name: "Suspense"}) CREATE (s5)-[:IN_GENRE]->(g6) WITH 1 as dummy
    MATCH (s6:Series {id: "S06"}), (g2:Genre {name: "Drama"}) CREATE (s6)-[:IN_GENRE]->(g2) WITH 1 as dummy
    MATCH (s7:Series {id: "S07"}), (g4:Genre {name: "Comédia"}) CREATE (s7)-[:IN_GENRE]->(g4) WITH 1 as dummy
    MATCH (s8:Series {id: "S08"}), (g4:Genre {name: "Comédia"}) CREATE (s8)-[:IN_GENRE]->(g4) WITH 1 as dummy
    MATCH (s9:Series {id: "S09"}), (g1:Genre {name: "Ficção Científica"}) CREATE (s9)-[:IN_GENRE]->(g1) WITH 1 as dummy
    MATCH (s10:Series {id: "S10"}), (g2:Genre {name: "Drama"}) CREATE (s10)-[:IN_GENRE]->(g2)
    """
]


# ==========================================
# 3. FUNÇÃO PARA RECOMENDAR CONTEÚDO
# ==========================================
def recomendar_conteudo(user_id):
    query = """
    MATCH (u:User {id: $user_id})-[:WATCHED]->(ja_visto)-[:IN_GENRE]->(g:Genre)
    MATCH (recomendacao)-[:IN_GENRE]->(g)
    WHERE NOT (u)-[:WATCHED]->(recomendacao)
    RETURN DISTINCT 
        recomendacao.title AS titulo, 
        labels(recomendacao) AS tipo, 
        recomendacao.releaseYear AS ano,
        g.name AS genero
    LIMIT 3
    """
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            resultado = session.run(query, user_id=user_id)
            return [dict(registro) for registro in resultado]


# ==========================================
# EXECUÇÃO PRINCIPAL DO PROGRAMA
# ==========================================
if __name__ == "__main__":
    print("🚀 Iniciando conexao e populando o banco Neo4j...")

#    with GraphDatabase.driver(URI, auth=AUTH) as driver:
#       with driver.session() as session:
#            for i, q in enumerate(QUERIES, 1):
#                session.run(q)

    print("🎉 Banco de dados populado com sucesso!")
    print("-" * 50)

    # Executando a recomendação dinâmica no terminal
    id_usuario = input("Digite o ID de um usuario para ver recomendacoes (Ex: U01, U02): ").strip().upper()
    print(f"\n🤖 Buscando recomendacoes para o usuario {id_usuario}...\n")

    recomenda_lista = recomendar_conteudo(id_usuario)

    if recomenda_lista:
        print(f"🍿 Sugestoes de Assistencia:")
        for idx, item in enumerate(recomenda_lista, 1):
            tipo = "Filme" if "Movie" in item['tipo'] else "Série"
            print(f"{idx}. [{tipo}] {item['titulo']} ({item['ano']}) - Genero: {item['genero']}")
    else:
        print("❌ Nenhuma recomendacao encontrada para este ID.")
