import streamlit as st
from datetime import date
from st_on_hover_tabs import on_hover_tabs
from components.formulario import formulario
# Configurações da página
st.set_page_config(layout="wide")
st.header("Know Your Fan")

# Estilo personalizado
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

# Barra lateral com navegação
with st.sidebar:
   tabs = on_hover_tabs(
    tabName=['Formulário', 'Resultado'],
    iconName=['assignment', 'Check'],
    styles={
        'navtab': {
            'background-color': 'transparent',
            'color': '#818181',
            'font-size': '18px',
            'transition': '.3s',
            'white-space': 'nowrap',
            'text-transform': 'uppercase',
            'list-style-type': 'none',
            'margin-bottom': '30px',
            'padding-left': '30px',
        },
        'tabStyle': {
            ':hover': {
                'background-color': '#222',
                'color': 'red',
                'cursor': 'pointer'
            }
        },
        'iconStyle': {
            'position': 'fixed',
            'left': '7.5px',
            'text-align': 'left'
        },
    },
    key="1"
)


# Conteúdo das abas
if tabs == 'Formulário':        
    formulario()

elif tabs == 'Resultado':
    st.title("Página de Economia")
    st.write(f'Nome da aba: {tabs}')
