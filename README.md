# API de Classificação

Esta API permite que você envie um vetor de 16 posições para obter a classificação correspondente e predizer para seus usuários os cursos adequados pra fazerem no superior pode usá-la no seu website escolar ou acadêmico. Integração em PHP, Python, NodeJS.

## Base URL:

https://josephus123.pythonanywhere.com/classificar


## Métodos Suportados:
- **GET**

## Parâmetros:

- **vetor**: Um vetor de 16 posições separado por vírgulas. Correspondente as notas obtidas no seu QUIZ e as disciplinas cursadas no ensino médio, respectivamente:
- "interesse_matematica", "interesse_biologia", "interesse_ciencias_sociais", "interesse_quimica", "interesse_fisica", "interesse_economia", "interesse_direito", "nota_matematica", "nota_biologia", "nota_quimica", "nota_fisica", "nota_economia", "nota_direito", "nota_programacao", "nota_enfermagem", "nota_contabilidade"

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

```php

<?php
$vetor = [14, 1, 15, 1, 1, 15, 15, 15, 0, 0, 0, 14, 14, 0, 0, 0];
$vetor_str = implode(',', $vetor);

$url = "https://josephus123.pythonanywhere.com/classificar?vetor=$vetor_str";

$response = file_get_contents($url);
$data = json_decode($response, true);

print_r($data);
?>
```

### NODE JS

Certifique-se de instalar o módulo axios antes de executar este código: npm install axios

```javascript

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
```
