#type: ignore
import re
### Buscando um padrão com re.search()
texto = "Olá, meu número de telefone é 1234-5634378."

resultado = re.search(r'\d{4}-\d{4}', texto)
if resultado:
    print("Telefone encontrado:", resultado.group())
else:
    print("Telefone não encontrado.")

###### Extraindo todas as correspondências com re.findall()

texto = "Os preços são R$ 10, R$ 20 e R$ 30, R$300, R$4394,  "

padrao = r'R\$\s*\d+'
resultados = re.findall(padrao, texto)

print("Valores encontrados:", resultados)

######Substituindo texto com re.sub()

texto = "O gato preto cruzou a rua."
padrao = r'gato'  # Procura pela palavra "gato"

novo_texto = re.sub(padrao, 'cachorro', texto)
print("Texto modificado:", novo_texto)

#### Dividindo uma string com re.split()

texto = "Maçã,Banana;Laranja Pera"
padrao = r'[;\s,]+'
resultado = re.split(padrao, texto)
print("Itens separados:", resultado)

#### Usando grupos de captura com ()

texto = "Data: 25/12/2023"
padrao1 = r'(\d{2})/(\d{2})/(\d{4})'
padrao2 = r'\d{2}/\d{2}/\d{4}'
resultado1 = re.search(padrao1, texto)
resultado2 = re.search(padrao2, texto)
if resultado1:
    dia, mes, ano = resultado1.groups()
    print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")
if resultado2:
    print(resultado2.group())

#### Compilando padrões com re.compile()

padrao = re.compile(r'\d{3}-\d{2}-\d{4}')  # Padrão de um número de seguro social (SSN)
texto = "Meu SSN é 123-45-6789."

resultado = padrao.search(texto)
if resultado:
    print("SSN encontrado:", resultado.group())


def validate(string: str) -> bool:
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'
    return re.match(padrao, string) is not None

# Exemplos de uso
emails = [
    "teste@example.com.br.ar.cre",
    "usuario@dominio.co",
    "teste@example....com",
    "email_invalido@com",
    "@semusuario.com",
    "usuario@.com"
]


# for e in emails:
#     print(f"{e}: {'Válido' if validar_email(e) else 'Inválido'}")