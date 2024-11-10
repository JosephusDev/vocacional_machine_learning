# API de Predição vocacional

Esta API permite que você envie um vetor de 13 ou 16 posições para obter a classificação correspondente e predizer para seus usuários os cursos adequados pra fazerem no ensino médio ou superior, pode usá-la no seu website escolar ou acadêmico, antes do usuário se inscrever pode passar por um Quiz e o Modelo de Machine Learning predizer os cursos que seriam melhor para ele. Integração em PHP, Python, NodeJS.

## Base URL para Ensino Médio:

https://josephus123.pythonanywhere.com/classificar

## Base URL para Ensino Superior:

https://josephus123.pythonanywhere.com/classificar_sup


## Métodos Suportados:
- **GET**

## Parâmetros:

- **vetor**: Um vetor de 13 ou 16 posições separado por vírgulas. Correspondente as notas obtidas no seu QUIZ e as disciplinas cursadas no ensino médio, respectivamente:
- Interesse_* são as notas obtidas pelo quiz e nota_* são as notas do seu curso no médio.
### Médio
- "interesse_matematica", "interesse_biologia", "interesse_quimica", "interesse_fisica", "interesse_informatica", "interesse_desenho", "interesse_lingua", "interesse_cultura", "nota_matematica", "nota_biologia", "nota_quimica", "nota_fisica", "nota_lingua", "target", "cursos"

### Superior
- "interesse_matematica", "interesse_biologia", "interesse_ciencias_sociais", "interesse_quimica", "interesse_fisica", "interesse_economia", "interesse_direito", "nota_matematica", "nota_biologia", "nota_quimica", "nota_fisica", "nota_economia", "nota_direito", "nota_programacao", "nota_enfermagem", "nota_contabilidade"

## Exemplos de Integração

- **A Integração será feita após efetuar sua própria página de QUIZ com base ao vetor ou parâmetro da API**

### Python

```python
import requests

vetor = [14, 1, 15, 1, 1, 15, 15, 15, 0, 0, 0, 14, 14, 0, 0, 0]
vetor_str = ','.join(map(str, vetor))

url = f'https://josephus123.pythonanywhere.com/classificar_sup?vetor={vetor_str}'

response = requests.get(url)
data = response.json()

print(data)

```

### PHP

```php

<?php
$vetor = [14, 1, 15, 1, 1, 15, 15, 15, 0, 0, 0, 14, 14, 0, 0, 0];
$vetor_str = implode(',', $vetor);

$url = "https://josephus123.pythonanywhere.com/classificar_sup?vetor=$vetor_str";

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

const url = `https://josephus123.pythonanywhere.com/classificar_sup?vetor=${vetor_str}`;

axios.get(url)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```
## Considerações Finais:
- Esta API faz recurso a um Modelo de machine learning pré-definido, caso queira adaptar para sua necessidade, quer para outras ou novas disciplinas quanto para predições de outros fatores, entre em contacto:
- Email: condepinto2@gmail.com
