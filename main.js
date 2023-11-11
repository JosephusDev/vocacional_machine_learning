// npm install axios - NODEJS
const axios = require('axios');

const vetor = [14, 1, 15, 1, 1, 15, 15, 15, 0, 0, 0, 14, 14, 0, 0, 0];
const vetor_str = vetor.join(',');

/* Vetor de entrada: Notas de cada disciplina:
###    "interesse_matematica", "interesse_biologia", "interesse_ciencias_sociais",
###    "interesse_quimica", "interesse_fisica", "interesse_economia",
###    "interesse_direito", "nota_matematica", "nota_biologia", "nota_quimica",
###    "nota_fisica", "nota_economia", "nota_direito", "nota_programacao",
###    "nota_enfermagem", "nota_contabilidade"*/

const url = `https://josephus123.pythonanywhere.com/classificar?vetor=${vetor_str}`;

axios.get(url)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
