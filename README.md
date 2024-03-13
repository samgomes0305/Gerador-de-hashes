# Gerador de Hash

Este é um simples aplicativo web desenvolvido em Python usando o Streamlit que permite aos usuários gerar diferentes tipos de hash para uma string de entrada.

## Funcionalidades

- **Entrada de Texto:** Os usuários podem inserir uma string de texto na caixa de entrada fornecida.
- **Seleção do Tipo de Hash:** Um menu suspenso permite aos usuários escolher entre os seguintes tipos de hash: MD5, SHA1, SHA256 e SHA512.
- **Geração de Hash:** Quando o botão "Gerar Hash" é pressionado, o aplicativo calcula o hash da string de entrada com base no tipo selecionado e exibe o resultado.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python (preferencialmente Python 3.x)
- Streamlit
- hashlib

Você pode instalar o Streamlit e o hashlib utilizando pip:

```bash
pip install streamlit hashlib
```

## Como Executar

Para executar o aplicativo, basta executar o seguinte comando no terminal:

```bash
streamlit run gerador_de_hash.py
```

Isso iniciará o servidor do Streamlit e abrirá o aplicativo em seu navegador padrão.

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, novos recursos ou encontrar problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request neste repositório.
