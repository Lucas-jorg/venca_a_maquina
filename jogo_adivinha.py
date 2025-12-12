#Criando um programa de adivinha
import random as ran
import time
import streamlit as st
from supabase import create_client, Client

# --- Supabase: ler secrets e criar cliente (cacheado) ---
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_ANON_KEY = st.secrets["SUPABASE_ANON_KEY"]

@st.cache_resource
def get_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

supabase = get_client()

def salvar_resultado(nome: str, resultado: str):
    # validações simples
    if not nome or not nome.strip():
        return
    if resultado not in ("ganhou", "perdeu"):
        return
    supabase.table("resultados").insert({
        "nome": nome.strip(),
        "resultado": resultado
    }).execute()

def contar_por_resultado(valor: str) -> int:
    # retorna apenas a contagem sem trazer linhas
    resp = supabase.table("resultados").select("id", count="exact").eq("resultado", valor).execute()
    # SDK v2 fornece count na resposta
    return getattr(resp, "count", 0)


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

    try:
        salvar_resultado(nome, resultado)
        st.info("Resultado salvo no banco online ✅")
    except Exception:
        st.warning("Não foi possível salvar agora. Tente novamente mais tarde.")


#Site do jogo 
#https://share.streamlit.io/
