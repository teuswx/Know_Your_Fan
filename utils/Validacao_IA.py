import requests
from dotenv import load_dotenv
import os
import re
import unicodedata
from difflib import SequenceMatcher

def extrairTexto(imagem_bytes):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = 'https://api.ocr.space/parse/image'
    
    files = {
        'file': ('imagem.png', imagem_bytes)
    }
    
    data = {
        'apikey': api_key,
        'language': 'por'
    }
    
    try:
        response = requests.post(url, files=files, data=data, timeout=30)

        if response.status_code == 200:
            resultado = response.json()
            
            if resultado.get('OCRExitCode') == 1:
                texto = resultado['ParsedResults'][0]['ParsedText']
                return texto
            else:
                erro = resultado.get('ErrorMessage', 'Erro desconhecido.')
                print(f"Erro ao processar a imagem: {erro}")
        else:
            print(f"Erro HTTP: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")


def validarDocumento(texto, nome, cpf):
    def normalizar(texto):
        texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode()
        return texto.lower().strip()
    
    def similaridade(a, b):
        return SequenceMatcher(None, a, b).ratio()

    def cpf_no_texto(cpf, texto):
        cpf = re.sub(r'\D', '', cpf)
        texto = texto.split('\n')
        limiar = 0.8
        for linha in texto:
            linha_limpa = re.sub(r'\D', '', linha)
            if len(linha_limpa) >= 8: 
                sim = SequenceMatcher(None, cpf, linha_limpa).ratio()
                if sim >= limiar:
                    return True
        return False

   
    def nome_no_texto(nome, texto, limiar=0.8):
        nome_norm = normalizar(nome)
        texto_norm = normalizar(texto)
        linhas = texto_norm.split('\n') 
        for linha in linhas:
            if similaridade(nome_norm, linha.strip()) >= limiar:
                return True
        return False

    cpf_encontrado = cpf_no_texto(cpf, texto)
    nome_encontrado = nome_no_texto(nome, texto)

    return {
        "cpf_encontrado": cpf_encontrado,
        "nome_encontrado": nome_encontrado,
        "valido": cpf_encontrado and nome_encontrado
    }

