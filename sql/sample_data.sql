-- este arquivo contém vários inserts de dados para amostra


INSERT INTO product (name, barcode) VALUES ('RIVOTRIL 2MG 30 COMPRIMIDOS ROCHE', '10993412');
INSERT INTO product (name, barcode) VALUES ('RITALINA 1MG 30 COMPRIMIDOS ROCHE', '34534534');

INSERT INTO product (name, barcode) VALUES ('FRANGO CONGELADO SADIA 1KG', '49239532');
INSERT INTO product (name, barcode) VALUES ('LINGUICA CALABRESA SEARA 500G', '523952314');
INSERT INTO product (name, barcode) VALUES ('PAO FRANCES CONGELADO 2KG', '4230402304');

INSERT INTO product (name, barcode) VALUES ('OLEO 15W40 TOP TURBO 1L LUBRAX PETROBRAS', '3902035');
INSERT INTO product (name, barcode) VALUES ('OLEO 10W40 TOYOTA 1L', '3902031');

INSERT INTO product (name, barcode) VALUES ('PARAFUSO FRANCES 1/4X50 INOX', '90524959');
INSERT INTO product (name, barcode) VALUES ('PARAFUSO FRANCES 3/8X60', '952934592');

INSERT INTO supplier (name, email) VALUES ('LABORATORIOS ROCHE DO BRASIL', 'vendas@roche.com.br');
INSERT INTO supplier (name, email) VALUES ('PAIF ATACADISTA SA', 'comercial@paifatacadista.com.br');
INSERT INTO supplier (name, email) VALUES ('XYZ ALIMENTOS LTDA', 'contato@xyzalimentos.com.br');
INSERT INTO supplier (name, email) VALUES ('METALLICA METALURGIA SA', 'nothingelsematters@metallica.com.br');

INSERT INTO customer (name) VALUES ('DROGARIA ZANAO EPP');
INSERT INTO customer (name) VALUES ('GRAN TURISMO AUTOPECAS EPP');
INSERT INTO customer (name) VALUES ('MERCADINHO DO JULIO ME');


INSERT INTO supplier_product (supplier_id, product_id, quantity, price) VALUES (1, 1, 174, 40.3);
INSERT INTO supplier_product (supplier_id, product_id, quantity, price) VALUES (1, 2, 523, 39.9);

INSERT INTO supplier_product (supplier_id, product_id, quantity, price) VALUES (2, 3, 523, 17.2);
INSERT INTO supplier_product (supplier_id, product_id, quantity, price) VALUES (2, 4, 200, 19.9);
INSERT INTO supplier_product (supplier_id, product_id, quantity, price) VALUES (2, 5, 980, 15.7);
INSERT INTO supplier_product (supplier_id, product_id, quantity, price) VALUES (3, 3, 200, 19.45);
INSERT INTO supplier_product (supplier_id, product_id, quantity, price) VALUES (3, 4, 200, 18.90);

INSERT INTO supplier_product (supplier_id, product_id, quantity, price) VALUES (4, 6, 190, 62.9);
INSERT INTO supplier_product (supplier_id, product_id, quantity, price) VALUES (4, 7, 190, 58.8);
INSERT INTO supplier_product (supplier_id, product_id, quantity, price) VALUES (4, 8, 1583, 1.10);
INSERT INTO supplier_product (supplier_id, product_id, quantity, price) VALUES (4, 9, 1293, 0.9);
