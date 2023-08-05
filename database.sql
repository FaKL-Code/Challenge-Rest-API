CREATE TABLE product (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL,
    barcode VARCHAR NOT NULL
);

CREATE TABLE customer (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY(id)
);

-- api_user eh uma pessoa da empresa de desenvolvimento de sistemas
-- que faz login no painel de controle para gerar uma nova chave da API
CREATE TABLE api_user (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    PRIMARY KEY(id)
);

-- essa tabela armazena as chaves da API
-- cada chave eh vinculada a um usuario da api (api_user)
CREATE TABLE api_token (
    id VARCHAR(50) UNIQUE NOT NULL,
    token VARCHAR(50) UNIQUE NOT NULL,
    api_user_id INTEGER UNIQUE NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_api_token_user_api_id
      FOREIGN KEY (api_user_id)
      REFERENCES api_user(id)
      ON DELETE CASCADE
);

CREATE TABLE supplier (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY(id)
);

-- tabela para many-to-many entre fornecedor (supplier)
-- e produtos, para armazenar quais produtos cada fornecedor oferece
-- a quantidade que cada fornecedor tem do produto e qual preco esta vendendo
CREATE TABLE supplier_product (
    supplier_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity NUMERIC(10, 2) NOT NULL DEFAULT 1,
    price NUMERIC(10, 2) NOT NULL);

-- armazena cada transacao feita entre uma loja e um fornecedor
CREATE TABLE purchase (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    supplier_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    total_amount NUMERIC(10,2) NOT NULL,

    PRIMARY KEY(id),
    CONSTRAINT fk_purchase_supplier_id
      FOREIGN KEY (supplier_id)
      REFERENCES supplier(id),

    CONSTRAINT fk_purchase_customer_id
      FOREIGN KEY (customer_id)
      REFERENCES customer(id)
);

-- tabela para relacao many-to-many
CREATE TABLE purchase_product (
    product_id INTEGER NOT NULL,
    purchar_id INTEGER NOT NULL,
    quantity NUMERIC(10, 2) NOT NULL DEFAULT 1,
    price NUMERIC(10, 2) NOT NULL);
