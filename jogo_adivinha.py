#Criando um programa de adivinha
import random as ran
import time
import streamlit as st

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


#Site do jogo 
#https://share.streamlit.io/
