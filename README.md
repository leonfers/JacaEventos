# JacaEventos
Aplicativo de eventos criado para avaliação da matéria de programação corporativa.

#### Diagrama de classes
![](http://gdurl.com//clKR "Diagrama de Classes")
#### Diagrama entidade relacionamento
![](http://gdurl.com/NmY2 "DER")
#### Diagrama de caso de uso
![](http://gdurl.com/eiR6 "Diagrama de caso de uso")
#### Arquitetura da solução
![](http://gdurl.com/UUGM "Arquitetura de solução")

#### Tecnologias usadas
* Python/Django - linguagem e framework
* PostgreSQL - Banco de Dados
* Heroku - Deploy e Hospedagem
* Django Rest - Api
* Padrao PEP 8 para python/django

#### Observações

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
