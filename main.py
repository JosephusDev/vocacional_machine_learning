import pandas as pd

titulos = [
    "interesse_matematica", "interesse_biologia", "interesse_ciencias_sociais",
    "interesse_quimica", "interesse_fisica", "interesse_economia",
    "interesse_direito", "nota_matematica", "nota_biologia", "nota_quimica",
    "nota_fisica", "nota_economia", "nota_direito", "nota_programacao",
    "nota_enfermagem", "nota_contabilidade", "target", "cursos"
]

dados = pd.read_csv("inscricao.csv", names = titulos, skiprows = 1, delimiter = ";")

dados_array = dados[["interesse_matematica", "interesse_biologia", "interesse_ciencias_sociais",
    "interesse_quimica", "interesse_fisica", "interesse_economia",
    "interesse_direito", "nota_matematica", "nota_biologia", "nota_quimica",
    "nota_fisica", "nota_economia", "nota_direito", "nota_programacao",
    "nota_enfermagem", "nota_contabilidade"]].to_numpy()

X = dados_array

y = dados['target'].to_numpy()

cursos = list([['Informatica'], ['Hidraulica'], ['Agronomia'], ['Enfermagem'], ['Contabilidade'], ['Economia'], ['Direito'], ['Informatica', 'Hidraulica'], ['Hidraulica', 'Agronomia'], ['Enfermagem', 'Agronomia'], ['Economia', 'Direito'], ['Economia', 'Contabilidade']])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.45, random_state = 43)

def classificar(a):
    res = classificador.predict([a])
    for v in res:
        return " - ".join(cursos[v])

from sklearn import svm

classificador = svm.SVC(C = 1.0)

classificador.fit(X_train, y_train)

y_pred = classificador.predict(X_test)

print(classificar([16,8,8,8,16,2,4,15,5,5,13,0,0,0,0,0]))