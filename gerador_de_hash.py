import streamlit as st  # Importa a biblioteca Streamlit para criar a interface do aplicativo
import hashlib  # Importa a biblioteca hashlib para calcular os hashes

# Define o título do aplicativo
st.title("Gerador de Hash")

# Solicita que o usuário insira o texto para gerar o hash
string = st.text_input("Digite o texto a ser gerado o hash:")

# Cria um menu suspenso para escolher o tipo de hash
menu = st.selectbox("Escolha o tipo de hash:", ["MD5", "SHA1", "SHA256", "SHA512"])

# Quando o botão é pressionado, gera o hash e exibe o resultado
if st.button("Gerar Hash"):
    # Utiliza o tipo de hash selecionado para gerar o hash
    # e converte o resultado para hexadecimal para torná-lo legível
    match menu:  # Inicia uma estrutura de controle de fluxo match (Python 3.10+)
        case "MD5":  # Caso o tipo de hash seja MD5
            resultado = hashlib.md5(string.encode('utf-8')).hexdigest()  # Calcula o hash MD5
            st.write(f"O hash MD5 da string '{string}' é: {resultado}")  # Exibe o resultado
        case "SHA1":  # Caso o tipo de hash seja SHA1
            resultado = hashlib.sha1(string.encode('utf-8')).hexdigest()  # Calcula o hash SHA1
            st.write(f"O hash SHA1 da string '{string}' é: {resultado}")  # Exibe o resultado
        case "SHA256":  # Caso o tipo de hash seja SHA256
            resultado = hashlib.sha256(string.encode('utf-8')).hexdigest()  # Calcula o hash SHA256
            st.write(f"O hash SHA256 da string '{string}' é: {resultado}")  # Exibe o resultado
        case "SHA512":  # Caso o tipo de hash seja SHA512
            resultado = hashlib.sha512(string.encode('utf-8')).hexdigest()  # Calcula o hash SHA512
            st.write(f"O hash SHA512 da string '{string}' é: {resultado}")  # Exibe o resultado







