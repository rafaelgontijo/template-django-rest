# Template para projetos Django Rest

Você precisa criar uma API escalável em um curto prazo, e se preocupa profundamente com a qualidade do seu trabalho.
O `template-django-rest` cuida dos detalhes para que você possa se concentrar em tornar sua API incrível.
O Scaffolding de um projeto leva segundos. Basta adicionar seus próprios recursos à API e começar a entregar.

## Highlights
- Desenvolvimento moderno de Python com Python 3.6+
- Django 2.2+
- Desenvolvimento local totalmente dockerizado através do docker-compose.
- PostgreSQL 11.3+
- Comece com cobertura de teste completa e implantação contínua.
- Integração com [Django Rest Framework](http://www.django-rest-framework.org/) completa
- Uma base pequena porem robusta - apenas o suficiente para maximizar sua produtividade e nada mais.

## Começo rápido

Instale o [cookiecutter](https://github.com/audreyr/cookiecutter):

```bash
sudo apt install cookiecutter
```

Scaffold o seu projeto:
```
cookiecutter gh:ivoryit/template-django-rest
```

Tente criar um usuário!

```bash
curl -d '{"username":"'"$RANDOM"'", "password":"test", "email":"test@test.com", "first_name":"test", "last_name":"user"}' \
     -H "Content-Type: application/json" \
     -X POST http://localhost:8000/api/v1/users/
```

## Base desse projeto

Esse projeto foi baseado no projeto [cookiecutter-django-rest](https://github.com/agconti/cookiecutter-django-rest) de [Andrew Conti](https://github.com/agconti)
