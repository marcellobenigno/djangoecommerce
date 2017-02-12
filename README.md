# Django E-Commerce

### Projeto do curso:

https://www.udemy.com/construa-um-e-commerce-com-python-3-e-django/

### Site da aplicação no Heroku:

https://ecommerce-marcellobenigno.herokuapp.com/

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.0
3. Ative o virtualenv.
4. Instale as dependências.
5. Crie um Banco de Dados PostgreSQL (djangoecommerce) e defina o usuário e senha (ex: user=postgres, password=postgres)
6. Configure a instância com o .env
7. Execute os testes.

```console
git clone git@github.com:marcellobenigno/djangoecommerce.git djangoecommerce_src
cd djangoecommerce_src
python -m venv .venv
createdb djangoecommerce
source .venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie um instância no heroku.
2. Envie as configuraçōes para o heroku.
3. Define una SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure o email
git push heroku master --force