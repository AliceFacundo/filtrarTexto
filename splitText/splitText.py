import re

arquivo = '0205236227140.txt'
def extrair_texto(arquivo): # Função que vai extrair as mensagens de texto
    with open(arquivo, 'r') as file: # Abre o arquivo em formato de leitura
        texto = file.read() # Guarda na variável texto o que há no arquivo 

    padrao = (r':\s*([A-Za-z0-9\s.,!?\'"’“”“”´`?.,!çÇéÉíÍóÓúÚâÂêÊôÔûÛàáÀãÃõÕ]+(?<!\W))') # Cria um padrão que vai filtrar do texto: caracteres alfanuméricos, 
    # com ou sem acento e pontuações, que apareçam depois de ":" e que estejam apenas entre caracteres alfanuméricos.
    # TODO: descobrir por que as pontuações no final das frases não estão entrando nas strings.
    texto_filtrar = re.findall(padrao, texto) # Encontra todas as correspondências do padrão

    return texto_filtrar # Retorna a lista de strings

def imprimir_lista_strings(lista): # Imprime a lista de strings 
    for item in lista:
        print(item)

# Chama as funções
texto_filtrado = extrair_texto(arquivo)
imprimir_lista_strings(texto_filtrado)

