# JacaEventos
Aplicativo de eventos criado para avaliacao da materia de programacao corporativa.

#### Diagrama de classes
![Alt text](http://gdurl.com/K7mq "Diagrama de Classes")
#### Diagrama entidade relacionamento
![Alt text]("DER")
#### Diagrama de caso de uso
![Alt text](http://gdurl.com/eiR6 "Diagrama de caso de uso")

#### Tecnologias usadas
* Python/Django - linguagem e framework
* PostgreSQL - Bonco de Dados
* Heroku - Deploy e Hospedagem
* Django Rest - Api
* Padrao PEP 8 para python/django

#### Observacoes

** Para baixar e rodar o JacaEventos localmente:**

```bash
$ git init 
$ git remote add origin master https://github.com/leonfers/JacaEventos
$ git pull orgin master
$ pip install -r requirements.txt
$ python manage.py runserver
```

** Povoando o banco de dados para testes **
```bash
$ python manage.py shell
$ exec(open('povoar.py').read())
```
