# API de Classificação

Esta API permite que você envie um vetor de 16 posições para obter a classificação correspondente e predizer cursos adequados pra usuários no seu website escolar ou acadêmico. Integração em PHP, Python, NodeJS.

## Base URL:

https://josephus123.pythonanywhere.com/classificar


## Métodos Suportados:
- **GET**

## Parâmetros:

- **vetor**: Um vetor de 16 posições separado por vírgulas.

## Exemplos de Integração

### Python

```python
import requests

vetor = [14, 1, 15, 1, 1, 15, 15, 15, 0, 0, 0, 14, 14, 0, 0, 0]
vetor_str = ','.join(map(str, vetor))

url = f'https://josephus123.pythonanywhere.com/classificar?vetor={vetor_str}'

response = requests.get(url)
data = response.json()

print(data)

```

### PHP

<?php
$vetor = [14, 1, 15, 1, 1, 15, 15, 15, 0, 0, 0, 14, 14, 0, 0, 0];
$vetor_str = implode(',', $vetor);

$url = "https://josephus123.pythonanywhere.com/classificar?vetor=$vetor_str";

$response = file_get_contents($url);
$data = json_decode($response, true);

print_r($data);
?>


### NODE JS

Certifique-se de instalar o módulo axios antes de executar este código: npm install axios

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
