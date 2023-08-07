<a>
    <img src="quote_genius_logo.png" alt="Quote Genius logo" title="Quote Genius" align="right" height="60" />
</a>

# Quote Genius

![GitHub all releases](https://img.shields.io/github/downloads/FaKL-Code/Challenge-Rest-API/total)
<img src="https://komarev.com/ghpvc/?username=FaKL-Code&color=brightgreen" alt="watching_count" />
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)


<a href="https://www.fiap.com.br">
    <img src="fiap.png" alt="FIAP logo" title="FIAP" align="right" height="60" />
</a>

## Enterprise Challenge 2023

Para a atividade do Enterprise Challenge 2023, foi apresentado um desafio que consiste em ...

### Desafio

...

### Sistema Atual

...

### Possíveis Melhorias
...

## Escopo do Projeto

...

## Especificação do Projeto

...

# Componentes do Grupo:

## 4 SI
Julio Facal - RM84125 \
[![Julio github](https://img.shields.io/badge/GitHub-FaKL--Code-181717.svg?style=flat&logo=github)](https://github.com/FaKL-Code) \
Guilherme Mauser - RM82890 \
[![Guilherme github](https://img.shields.io/badge/GitHub-Guimauser05-181717.svg?style=flat&logo=github)](https://github.com/Guimauser05) \
Nicolas Morais - RM84393 \
[![Nicolas github](https://img.shields.io/badge/GitHub-nicmorais-181717.svg?style=flat&logo=github)](https://github.com/nicmorais) \
Rafael Zanão - RM82923 \
[![Rafael github](https://img.shields.io/badge/GitHub-Rafael--Zanao-181717.svg?style=flat&logo=github)](https://github.com/Rafael-Zanao) 

# Sumário

- [Instalação](#instalação)
    - [Requisitos](#requisitos)
    - [Setup](#setup)
- [Iniciar](#iniciar)
- [Links](#links)
- [Testes](#testes)

# Instalação

## Requisitos

- [Python 3.9](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [Git](https://git-scm.com/downloads) - (opcional, mas recomendado para clonar o projeto e atualizar as versões)

## Setup
1. Faça o download da última versão ou clone o projeto na sua máquina local usando:
```bash
git clone https://github.com/FaKL-Code/Challenge-Rest-API.git
```

2. Crie um ambiente virtual:

- No Windows usando:

```bash
python -m venv venv
``` 
- No Linux usando:

```bash
virtualenv --python python3 venv
```
3. Ative o ambiente virtual:

- No Windows usando:

```bash
venv\Scripts\activate.bat
```
- No Linux usando:

```bash
source venv/bin/activate
```

4. Instale as dependências usando:
```bash
pip install -r requirements.txt
```

5. Navegue ate o diretório "./challenge"

6. Faça as migrações dos modelos do projeto usando:
```bash
python manage.py makemigrations
python manage.py migrate
```

# Iniciar

1. Inicie o servidor usando:
```bash
python manage.py runserver
```

2. Acesse o servidor em http://127.0.0.1:8000/auth/register e crie seu usuário

3. Acesse o servidor em http://127.0.0.1:8000/auth/login e entre com o usuário que você criou

4. Copie o token "Access" gerado para futuras autenticações

# Links

Nossa API tem os seguintes endpoints:

1. Para ler toda a Documentação da API:
    - http://127.0.0.1:8000/readoc
    - http://127.0.0.1:8000/swagger
    - http://127.0.0.1:8000/swagger.json
------
2. Para cadastro de usuário e obtenção do Token:
    - http://127.0.0.1:8000/auth/register
    - http://127.0.0.1:8000/auth/login
    - http://127.0.0.1:8000/auth/login/refresh
-----
3. Para acessar o console administrativo:
    - http://127.0.0.1:8000/admin
------
4. Para acessar os dados:
    - http://127.0.0.1:8000/api/v1/customers
    - http://127.0.0.1:8000/api/v1/products
    - http://127.0.0.1:8000/api/v1/purchases
    - http://127.0.0.1:8000/api/v1/purchaseproducts
    - http://127.0.0.1:8000/api/v1/suppliers
    - http://127.0.0.1:8000/api/v1/supplierproducts

# Testes

Para Validar o funcionamento da API basta acessar cada um dos endpoits e tentar realizar requisições, lembrando que para acessar os dados, será necessário a authenticação a partir do token gerado no momento do login
