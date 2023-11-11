// npm install axios - NODEJS
const axios = require('axios');

const vetor = [14, 1, 15, 1, 1, 15, 15, 15, 0, 0, 0, 14, 14, 0, 0, 0];
const vetor_str = vetor.join(',');

const url = `https://josephus123.pythonanywhere.com/classificar?vetor=${vetor_str}`;

axios.get(url)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
