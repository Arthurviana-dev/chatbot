import streamlit as st
from openai import OpenAI

# Título do chatbot
st.write("# Chatbot do Arthur")

# Inicializa o cliente OpenAI (api rest para se conectar aos dois programas)
client = OpenAI(api_key="minha_chave_api)

# Inicializa o histórico de mensagens se não existir
if "lista_mensagens" not in st.session_state:
    st.session_state.lista_mensagens = []

# Campo de entrada de texto do usuário 
texto_usuario = st.chat_input("Digite sua mensagem")

# 1. mostrar o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

# 2. processar nova mensagem: Se o usuário digitou algo
if texto_usuario:
    # Guarda e exibe a mensagem do usuário imediatamente
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    
    with st.chat_message("user"):
        st.write(texto_usuario)

    # Exibe um "spinner" enquanto a IA gera a resposta
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            # Envia todo o histórico para a API da OpenAI
            resposta_ia = client.chat.completions.create(
                messages=st.session_state["lista_mensagens"],
                model="gpt-4o" 
            )
            
            # Extrai o texto da resposta da IA
            texto_resposta_ia = resposta_ia.choices[0].message.content
            st.write(texto_resposta_ia)

    # Guarda a resposta da IA no histórico da sessão
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
