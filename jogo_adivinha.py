#Criando um programa de adivinha
#Para rodar precisamos colocar "Streamlit run jogo_adivinha"

import random as ran
import time
import streamlit as st

st.title("🎮 Tenta vencer a máquina HAHA")
st.subheader("Vamos ver se você é bom de adivinhação")

# Número aleatório do PC
pc = ran.randint(0, 20)

# Entrada do usuário
palpite = st.number_input("Escolha um número entre 0 e 20:", min_value=0, max_value=20, step=1)

# Botão para confirmar
if st.button("Chutar número"):
    st.write("Carregando...")
    time.sleep(3)  # só para dar suspense
    
    if palpite == pc:
        st.success(f"Filha da mâe, acertoou! kkkk, eu pensei exatamente no {pc}")
    else:
        st.error(f"Se ferrou, eu escolhi {pc} e não {palpite}")


#Site do jogo 
#https://share.streamlit.io/
