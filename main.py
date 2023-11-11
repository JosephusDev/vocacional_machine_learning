import requests

url = "https://josephus123.pythonanywhere.com/classificar"

# Vetor de entrada: Notas de cada disciplina:
###    "interesse_matematica", "interesse_biologia", "interesse_ciencias_sociais",
###    "interesse_quimica", "interesse_fisica", "interesse_economia",
###    "interesse_direito", "nota_matematica", "nota_biologia", "nota_quimica",
###    "nota_fisica", "nota_economia", "nota_direito", "nota_programacao",
###    "nota_enfermagem", "nota_contabilidade"

vetor = [14, 1, 15, 1, 1, 15, 15, 15, 0, 0, 0, 14, 14, 0, 0, 0]

# Transformar o vetor em uma string separada por vírgulas
vetor_str = ",".join(map(str, vetor))

# Adicionar o vetor à URL
full_url = f"{url}?vetor={vetor_str}"

# Fazer a solicitação GET
response = requests.get(full_url)

# Exibir a resposta
print(response.json())
