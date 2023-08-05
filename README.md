# extratoclube-challenge
Sistema web full-stack

## [Requisitos]
* Docker
* Python 3.11+
* Node 14.18

## [Sobre o Projeto]
Sistema desenvolvido para extração de dados de beneficio no portal extrato clube.

## [Backend]
* FastAPI 
* Celery 
* RabbitMQ 
* Redis 
* Elasticsearch 
* Playwright 

## [Front End]
* ReactJS
* Tailwind CSS 
* Axios 
* react-icons
* react-toastify

## [Execução do Projeto]
Obrigatório o uso do Docker

Rodar o comando ```docker compose up --build -d``` no mesmo diretório onde está o arquivo docker-compose.yml

## [API]
A API estará disponivel em http://localhost:8000

URL da documentação: http://localhost:8000/docs

[Rotas]
  *  POST - http://localhost:8000/v1/solicitacao-matricula - Irá gerar uma solicitação para extração das matriculas
  *  GET - http://localhost:8000/v1/status-solicitacao/{id_solicitacao} - Verifica como está o andamento da solicitação
  *  GET - http://localhost:8000/v1/consultar-matricula/{cpf} - Consulta as matriculas do cpf especificado

A Consulta das matriculas também poderá ser feita pelo frontend, disponível em: http://localhost:3000/

## [Autor]
Gustavo Henrique Oliveira dos Santos

https://www.linkedin.com/in/guhenriq/






