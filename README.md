<a>
    <img src="assets\quote_genius_logo.png" alt="Quote Genius logo" title="Quote Genius" align="right" height="60" />
</a>

# Quote Genius

![GitHub all releases](https://img.shields.io/github/downloads/FaKL-Code/Challenge-Rest-API/total)
<img src="https://komarev.com/ghpvc/?username=FaKL-Code&color=brightgreen" alt="watching_count" />
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)


<a href="https://www.fiap.com.br">
    <img src="assets\fiap.png" alt="FIAP logo" title="FIAP" align="right" height="60" />
</a>

## Enterprise Challenge 2023

### Desafio

No dia a dia dos comércios, uma das tarefas que mais consome tempo é a de fazer compras para reposição. É comum ter que preparar uma listagem dos produtos, consultar vários fornecedores, comparar preços, tudo manualmente. Além disso, muitos vendedores não fornecem uma lista de todos os produtos disponíveis. Some isso ao desencontro entre as informações dos produtos entre as base de dados dos comerciantes, o que mostra o tamanho do problema.

### Sistema Atual

Nosso sistema atualmente consiste em um backend e uma base de dados que concentra as informações mais pertinentes para o funcionamento do protótipo. Dessa forma, ele faz a criação de novas chaves da API, autenticaçao, e CRUD dos dados.

### Possíveis Melhorias

Estudamos aumentar a escalabidade do projeto por meio de arquitetura de micro serviços. Também podemos melhorar a segurança por meio de autenticação em dois fatores e permissões granulares para as chaves da API.
Outra funcionalidade também interessante é a integração com sistema de pagamentos, para facilitar as transações, e mais adiante, integração com sistema de transportes.

## Escopo do Projeto

O projeto atua como uma plataforma que visa unificar e padronizar as transações comerciais entre fornecedores e comércios menores, por meio de uma API REST, com a qual os desenvolvedores de sistemas de ERP iriam integrar seus softwares, provendo uma funcionalidade útil, lucrativa e produtiva para todos os envolvidos.

## Especificação do Projeto

Desenvolvemos uma API utilizando o Django Rest Framework do Python, essa API será hospedada em uma t2.micro (Máquina virtual AWS EC2) e tem alguns recursos de segurança, como os tokens de autenticação JWT.

No Código Fonte temos um diagrama de arquitetura, uma página inicial do projeto e, caso seja necessário usar uma base de dados apartada, os scripts para criação e carga da base.

Optamos por utilizar o próprio front-end do framework.

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

7. Crie um super usuário preenchendo os campos necessários ao usar o comando:
```bash
python manage.py createsuperuser
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

Para Validar o funcionamento da API basta acessar cada um dos endpoits e tentar realizar requisições, lembrando que para acessar os dados, será necessário a autenticação a partir do token gerado no momento do login
