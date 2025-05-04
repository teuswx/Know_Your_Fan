# Know Your Fan

Know Your Fan é uma aplicação desenvolvida com o objetivo de identificar e validar a presença digital de fãs em plataformas sociais como X e Twitch, além de realizar uma validação por OCR (Reconhecimento Óptico de Caracteres) de documentos enviados.

---

## 📦 Bibliotecas Utilizadas

- **streamlit**: construção da interface web interativa.
- **urllib**: manipulação de URLs para extração de nomes de usuário.
- **requests**: envio de requisições HTTP para APIs externas.
- **dotenv**: carregamento de variáveis de ambiente para segurança de chaves.
- **os**: acesso a funcionalidades do sistema operacional.
- **re**: uso de expressões regulares.
- **unicodedata**: normalização de textos para comparação robusta.
- **difflib**: cálculo de similaridade textual.

---

## 🧠 Funcionalidade de Validação com IA

O projeto utiliza um serviço de OCR externo (https://api.ocr.space/) para transformar imagens de documentos em texto e, em seguida, verificar se os dados fornecidos pelo usuário (nome e CPF) estão presentes na imagem.

```python
# Exemplo de uso da função de OCR e validação
from Validacao_IA import extrairTexto, validarDocumento

texto = extrairTexto(imagem_bytes)
resultado = validarDocumento(texto, nome, cpf)
```

A função `validarDocumento` faz uso de heurísticas de similaridade textual para identificar se o nome e CPF do usuário constam na imagem enviada.

---

## 🌐 Validação de Redes Sociais

O arquivo `Scraping.py` contém uma simulação de verificação de perfis nas redes sociais **X** e **Twitch**, com base em nomes de usuário extraídos das URLs.

```python
# Exemplo de uso da verificação
verifica_interacao("https://x.com/mateushp4", "https://twitch.tv/lucas01")
```

Dependendo do status do usuário em cada rede, a função retorna mensagens informando se ele segue ou não a organização FURIA em cada plataforma.

---

## 🖥️ Interface do Projeto

A interface é construída com `streamlit`, oferecendo uma navegação simples com abas:

- **Home**
- **Formulário** (submissão de dados)
- **Resultado** (retorno da verificação)

A navegação é feita pela sidebar utilizando o componente `st_on_hover_tabs`.

---

## 🚀 Execução

1. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

2. Crie um arquivo `.env` com sua chave da API (crie sua chave em: https://ocr.space/ocrapi):
    ```
    API_KEY=sua_chave_ocr_space
    ```

3. Execute o app:
    ```bash
    streamlit run app.py
    ```

---

## 👥 Equipe

- Desenvolvido por: Mateus Henrique Pereira