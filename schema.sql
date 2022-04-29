CREATE TABLE usuarios (
	user_id INTEGER PRIMARY KEY,
	user_name varchar(50) not NULL,
	user_senha varchar(64) NOT NULL
);

CREATE TABLE vagas (
	vaga_id INTEGER PRIMARY KEY,
	vaga_categoria VARCHAR(30) NOT NULL,
	vaga_titulo VARCHAR(40) NOT NULL,
	vaga_empresa VARCHAR(50) NOT NULL,
	vaga_salario VARCHAR(15) NOT NULL,
	vaga_localizacao VARCHAR(30) NOT NULL,
	vaga_descricao TEXT NOT NULL,
	vaga_beneficios VARCHAR(200),
	vaga_descricao_empresa TEXT
);

CREATE TABLE inscricoes (
	inscri_ID INTEGER PRIMARY KEY,
	user_id INTEGER,
	vaga_id INTEGER,
	FOREIGN KEY (user_id) REFERENCES usuarios (user_id),
	FOREIGN KEY (vaga_id) REFERENCES vagas (vaga_id)
)