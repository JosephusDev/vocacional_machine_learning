from flask import Flask, request, jsonify
import pandas as pd
from sklearn import svm

app = Flask(__name__)

titulos = [
    "interesse_matematica", "interesse_biologia", "interesse_ciencias_sociais",
    "interesse_quimica", "interesse_fisica", "interesse_economia",
    "interesse_direito", "nota_matematica", "nota_biologia", "nota_quimica",
    "nota_fisica", "nota_economia", "nota_direito", "nota_programacao",
    "nota_enfermagem", "nota_contabilidade", "target", "cursos"
]

dados = pd.read_csv("inscricao.csv", names=titulos, skiprows=1, delimiter=";")

dados_array = dados[
    [
        "interesse_matematica", "interesse_biologia", "interesse_ciencias_sociais",
        "interesse_quimica", "interesse_fisica", "interesse_economia",
        "interesse_direito", "nota_matematica", "nota_biologia", "nota_quimica",
        "nota_fisica", "nota_economia", "nota_direito", "nota_programacao",
        "nota_enfermagem", "nota_contabilidade"
    ]
].to_numpy()

X = dados_array
y = dados['target'].to_numpy()

cursos = list([['Informatica'], ['Hidraulica'], ['Agronomia'], ['Enfermagem'], ['Contabilidade'], ['Economia'], ['Direito'], ['Informatica', 'Hidraulica'], ['Hidraulica', 'Agronomia'], ['Enfermagem', 'Agronomia'], ['Economia', 'Direito'], ['Economia', 'Contabilidade']])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.45, random_state=43)

classificador = svm.SVC(C=1.0)
classificador.fit(X_train, y_train)

def classificar(a):
    res = classificador.predict([a])
    for v in res:
        return " - ".join(cursos[v])

@app.route('/classificar', methods=['GET'])
def classificar_api():
    vetor = [
        int(request.args.get('interesse_matematica')),
        int(request.args.get('interesse_biologia')),
        int(request.args.get('interesse_ciencias_sociais')),
        int(request.args.get('interesse_quimica')),
        int(request.args.get('interesse_fisica')),
        int(request.args.get('interesse_economia')),
        int(request.args.get('interesse_direito')),
        int(request.args.get('nota_matematica')),
        int(request.args.get('nota_biologia')),
        int(request.args.get('nota_quimica')),
        int(request.args.get('nota_fisica')),
        int(request.args.get('nota_economia')),
        int(request.args.get('nota_direito')),
        int(request.args.get('nota_programacao')),
        int(request.args.get('nota_enfermagem')),
        int(request.args.get('nota_contabilidade'))
    ]

    resultado = classificar(vetor)
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run()
