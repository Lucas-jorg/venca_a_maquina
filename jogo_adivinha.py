#Criando um programa de adivinha
import random as ran
import time
import streamlit as st
import mysql.connector

# 🔌 Conexão com MySQL
def conectar_db():
    return mysql.connector.connect(
        host="SEU_HOST",       # ex: "mysql-1234.railway.app"
        user="SEU_USUARIO",    # ex: "root"
        password="SUA_SENHA",
        database="jogo_web"
    )

st.title("🎮 Tenta vencer a máquina HAHA")
st.subheader("Vamos ver se você é bom de adivinhação")

# Nome do jogador
nome = st.text_input("Digite seu nome:")

# Número aleatório do PC
pc = ran.randint(0, 20)

# Entrada do usuário
palpite = st.number_input("Escolha um número entre 0 e 20:", min_value=0, max_value=20, step=1)

# Botão para confirmar
if st.button("Chutar número"):
    st.write("Carregando...")
    time.sleep(4)
    
    # Verifica resultado
    resultado = "ganhou" if palpite == pc else "perdeu"

    # Mensagem do jogo
    if resultado == "ganhou":
        st.success(f"Filha da mãe, Acertooou kkkk! Eu pensei no {pc}")
    else:
        st.error(f"Se ferrou kkkk, você errou! Eu escolhi {pc} e não {palpite}")

    # -------------------------------
    #  🔥 SALVAR NO BANCO DE DADOS
    # -------------------------------
    try:
        db = conectar_db()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO partidas (nome_jogador, resultado)
            VALUES (%s, %s)
        """, (nome, resultado))

        db.commit()
        cursor.close()
        db.close()

        st.info("Resultado registrado! (Você não vê, mas eu vejo 😈)")
    
    except Exception as e:
        st.error(f"Erro ao conectar ao banco: {e}")


#Site do jogo 
#https://share.streamlit.io/
