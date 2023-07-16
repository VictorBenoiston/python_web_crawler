# Fask-RESTful API web
 ## About the project:
This project defines itself as the development of an API able to retrieve data, from first and second instance (if there is), relying on different databases from different courts in Brazil. Crurently, we accept process numbers from TJAL and TJCE. The data retrieved is defined in:
* Class (Classe);
* Area (Área)
* Subject (Assunto)
* Distribuiton date (Data de Distribuição)
* Judge (Juíz)
* Parties of the process (Partes envolvidas)
* Legal moviments (Movimentação do processo)


Project structure:
```
.
├── README.md
├── app.py
├── crawler_main.py
├── requirements.txt
├── test_crawler.py
├── website_scraper.py
└── settings.py
```

* app.py - holds all endpoints and flask application initialization.
* crawler_main.py - encompasses all the crawlers used.
* requirements.txt - all the libraries necessary in order to run the applicaiton.
* test_crawler.py - holds the tests regarding the crawler.
* website_scraper.py - the algorithm responsible for extracting the data.

## Running 


### 1. Clone repository.
```bash
git clone repo
```

### 2. Install requirements.txt
```bash
pip3 isntall -r requirements.txt
```

### 3. Run following commands
```bash
python3 app.py
```

## Usage
### search endpoint
GET http://127.0.0.1:5000/search

REQUEST
```json
{
	"nuProcesso": "0710802-55.2018.8.02.0001"
}
```

RESPONSE
```json
{
	"Primary_data_1st_instance": {
		"Classe": "Procedimento Comum Cível",
		"Area": "Cível",
		"Assunto": "Dano Material",
		"Data de distribuicao": "02/05/2018 às 19:01 - Sorteio",
		"Juiz": "José Cícero Alves da Silva",
		"Valor da acao": "R$281.178,42"
	},
	"Parties_involved_1st_instance": {
		"Autor": "José Carlos Cerqueira Souza Filho Advogado: Vinicius Faria de Cerqueira",
		"Ré": "Cony Engenharia Ltda. Advogado: Carlos Henrique de Mendonça Brandão Advogado: Guilherme Freire Furtado Advogada: Maria Eugênia Barreiros de Mello Advogado: Vítor Reis de Araujo Carvalho",
		"Autora": "Livia Nascimento da Rocha Advogado: Vinicius Faria de Cerqueira",
		"Réu": "Banco do Brasil S A Advogado: Nelson Wilians Fratoni Rodrigues"
	},
	"legal_moviments_data_1st_instance": [
		{
			"05/05/2023": "Execução de Sentença Iniciada Seq.: 01 - Cumprimento de sentença"
		},
		{
			"05/05/2023": "Ato Publicado Relação: 0282/2023 Data da Publicação: 08/05/2023 Número do Diário: 3296"
		},
        ...
    ]

    "primary_data_2nd_instance": {
		"Classe": "Apelação Cível",
		"Area": "Cível",
		"Assunto": "Obrigações",
		"Relator": "VICE PRESIDENTE DO TRIBUNAL DE JUSTIÇA DE ALAGOAS",
		"Valor da acao": "281.178,42"
	},
	"parties_involved_2nd_instance": {
		"Apelante": "Banco do Brasil S A Advogado: Nelson Wilians Fratoni Rodrigues",
		"Apelado": "José Carlos Cerqueira Souza Filho Advogado: Vinicius Faria de Cerqueira",
		"Apelada": "Livia Nascimento da Rocha Advogado: Vinicius Faria de Cerqueira"
	},
	"legal_moviments_data_2nd_instance": [
		{
			"26/04/2023": "Certidão de Envio ao 1º Grau Faço remessa dos presentes autos à Origem."
		},
		{
			"26/04/2023": "Baixa Definitiva"
		},
        ...
    ]
}
```

## Unit Test with Pytest
```bash
pytest -v
```

### Test Output
```
test_crawler.py::test_primary_data_crawler_1st_instance PASSED                                                                                                                                                                                                                                                   [ 16%]
test_crawler.py::test_primary_data_crawler_2nd_instance PASSED                                                                                                                                                                                                                                                   [ 33%]
test_crawler.py::test_extract_parties_involved_1st_instance PASSED                                                                                                                                                                                                                                               [ 50%]
test_crawler.py::test_extract_parties_involved_2nd_instance PASSED                                                                                                                                                                                                                                               [ 66%]
test_crawler.py::test_extract_legal_moviments_1st_instance PASSED                                                                                                                                                                                                                                                [ 83%]
test_crawler.py::test_extract_legal_moviments_2nd_instance PASSED    

------------------------------------------------------------------------------------
6 passed in 0.20s
```
