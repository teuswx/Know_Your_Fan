import streamlit as st
from datetime import date
from utils.Validacao_IA import extrairTexto, validarDocumento
from utils.Scraping import verifica_interacao
def formulario():
    
    st.title("Formulário: Conheça seu Fã 🎮")

    with st.form("form_dados_fan"):
        st.subheader("Dados Pessoais")

        nome = st.text_input("Nome completo")
                    
        cpf = st.text_input("CPF (somente números)")
        endereco = st.text_area("Endereço completo")

        st.subheader("Interesses e Atividades")

        interesses = st.multiselect(
            "Quais são seus interesses em e-sports?",
            ["FPS", "MOBA", "Battle Royale", "Card Games", "Fighting Games", "Simulação", "Outro"]
        )

        eventos = st.text_area("Eventos de e-sports que você participou no último ano")
        atividades = st.text_area("Atividades realizadas como fã (streaming, cosplay, produção de conteúdo, etc.)")

        st.subheader("Compras Relacionadas")

        compras = st.text_area("Produtos de e-sports que você comprou no último ano (ex: camisetas, ingressos, periféricos)")

        x = st.text_input("Link do seu X")
        twitch = st.text_input("Link da sua Twitch")

        st.title("Importe seu documento (Carteira de identidade)")
        arquivo = st.file_uploader("Escolha um arquivo", type=["png", "jpg"])

        data_envio = st.form_submit_button("Enviar")

    if data_envio:
        
        if not nome:
            st.error("Por favor, insira seu nome completo")
            return
        if cpf:
            if not any(char.isdigit() for char in cpf):
                st.error("O CPF deve conter apenas números")
                return
            elif len(cpf) != 11:
                st.error("O CPF deve conter 11 números")
                return
    
       
        if not endereco:
            print((endereco))
            st.error("Por favor, insira seu endereço completo.")
            return
        if not interesses:
            st.error("Por favor, selecione pelo menos um interesse em e-sports.")
            return
        
        if not eventos:
            st.error("Por favor, descreva os eventos de e-sports que você participou no último ano.")
            return

        if not atividades:
            st.error("Por favor, descreva as atividades realizadas como fã (streaming, cosplay, etc.).")
            return

        if not compras:
            st.error("Por favor, descreva os produtos de e-sports que você comprou no último ano.")
            return
        if not x:
            st.error("Por favor, escreva o link do seu Twitter")
            return
        if not twitch:
            st.error("Por favor, Por favor, escreva o link do seu Twitter")
            return

        if arquivo is None:
  
            st.error("Faça o upload de algum arquivo de Identidade")
            return
    
        texto = extrairTexto(arquivo)  
        validacao_do_documento = validarDocumento(texto, nome, cpf)

        teste = verifica_interacao(x,twitch)
        print(teste)
        if validacao_do_documento['valido']:

            st.success("Dados validados com sucesso!")
            st.write("🔎 Resumo dos dados coletados:")
            st.write(f"**Nome:** {nome}")
            st.write(f"**CPF:** {cpf}")
            st.write(f"**Endereço:** {endereco}")
            st.write(f"**Interesses:** {', '.join(interesses)}")
            st.write(f"**Eventos:** {eventos}")
            st.write(f"**Atividades:** {atividades}")
            st.write(f"**Compras:** {compras}")
            st.write(f"**Data do envio:** {date.today()}")
            st.write(f"Você carregou: {arquivo.name}")
        else:
            st.error("O seu documento não parece válido!\n"
            "- Verifique se a imagem tem uma qualidade boa\n"
            "- Verifique se preencheu o campo nome e CPF corretamente")

