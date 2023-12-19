# Dicionário de tradução "Plus2" para português
traducao_plus2_para_portugues = {
    "Jqlg": "Hoje",
    "xqw": "vou",
    "rtqitcoct": "programar"
}

# Função para traduzir uma string "Plus2" para português
def traduzir_plus2_para_portugues(texto_plus2):
    palavras_plus2 = texto_plus2.split()  # Divide o texto em palavras
    traducao_portugues = [traducao_plus2_para_portugues.get(palavra, palavra) for palavra in palavras_plus2]
    return " ".join(traducao_portugues)

# String "Plus2" fornecida
texto_plus2 = "rtkpv(\"jvvru://ujqtvwtn.cv/eDIPX\")"

# Extraindo a URL da string "Plus2" e traduzindo para o português
url_plus2 = texto_plus2.split("\"")[1]
url_traduzida = traduzir_plus2_para_portugues(url_plus2)

# Imprimindo a URL traduzida
print(f"A URL traduzida para o português é: {url_traduzida}")

# Prof, fiquei muiiito tempo nessa, e não saiu nada, então tive que apelar para fontes esternas. Sorry 😓