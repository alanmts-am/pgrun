# PGrun

Projeto voltado para rodar queries SQL com Postgres, tanto de UPDATE quanto de SELECT, em diversos bancos

## Arquivo de configurações YAML

Para funcionar devidamente, primeiramente, insera a conexão do banco principal que contem todas as demais conexões
```yml
connection:
  host: localhost
  port: 5432
  database: test
  username: test
  password: qwerty1234
```

Posteriormente, insera as queries nos devidos lugares
```yml
sql:
  # Query para listar a conexão com os bancos. Deve ser na sequência host, port, database_name, username, password
  database:
```

Por fim, indique no arquivo, qual o tipo de query a ser executada, verdadeiro para o SELECT e falso para o UPDATE
```yml
options:
  select: False
```

A query em si deve ser inserida dentro do arquivo query.sql, na raiz do projeto

## Como rodar

Para baixar as dependências, será necessário instalar o Poetry.

[Instalação](https://python-poetry.org/docs/#installation)

Assim que baixado, basta instalar as dependências
```bash
poetry install
```

Assim que estiver com tudo configurado, rode o comando Poetry ou Python
```Bash
poetry run python pgrun/query.py
```