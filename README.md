# Template para projetos Django Rest

Você precisa criar uma API escalável em um curto prazo, e se preocupa profundamente com a qualidade do seu trabalho.
O `template-django-rest` cuida dos detalhes para que você possa se concentrar em tornar sua API incrível.
O Scaffolding de um projeto leva segundos. Basta adicionar seus próprios recursos à API e começar a entregar.

## Highlights
- Desenvolvimento moderno de Python com Python 3.10
- Django 4.1
- Desenvolvimento local totalmente dockerizado através do docker-compose.
- PostgreSQL 12
- Comece com cobertura de teste completa e implantação contínua.
- [Celery](http://www.celeryproject.org/) configurado e pronto para usar.
- Integração com [Django Rest Framework](http://www.django-rest-framework.org/).
- Autenticação com [JWT](https://jwt.io/).
- Documentação da api gerada automaticamente via [drf-yasg](https://github.com/axnsan12/drf-yasg).
- Uma base pequena porem robusta - apenas o suficiente para maximizar sua produtividade e nada mais.

## Começo rápido

Instale o [cookiecutter](https://github.com/audreyr/cookiecutter):

```bash
sudo apt install cookiecutter
```

Scaffold o seu projeto:
```
cookiecutter gh:rafaelgontijo/template-django-rest
```

Tente criar um usuário!

```bash
curl -d '{"username":"'"$RANDOM"'", "password":"test", "email":"test@test.com", "first_name":"test", "last_name":"user"}' \
     -H "Content-Type: application/json" \
     -X POST http://localhost:8000/api/v1/users/
```

## Base desse projeto

Esse projeto foi baseado no projeto [cookiecutter-django-rest](https://github.com/agconti/cookiecutter-django-rest) de [Andrew Conti](https://github.com/agconti)
