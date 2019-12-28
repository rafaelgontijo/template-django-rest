# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Pré-requisitos

- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [AWS CLI](https://snapcraft.io/aws-cli)
- [EB CLI](https://docs.aws.amazon.com/pt_br/elasticbeanstalk/latest/dg/eb-cli3-install-advanced.html)

## Desenvolvimento

Antes de rodar o ambiente pela primeira vez, execute o comando abaixo, para criar o db:
```bash
make migrate
```

Iniciar o ambiente de desenvolvimento:
:
```bash
make up
```

Rodar os testes
```bash
make test
```

Rodar um comando dentro do container docker:

```bash
docker-compose run --rm django [comando]
```
Ex:
```bash
docker-compose run --rm django python manage.py makemessages -l en -l pt_BR
```

Rode o comando, para ver as outras opções do comando "make":
```bash
make help
```

### Ambiente de desenvolvimento

Ao rodar o comando para iniciar o ambiente de desenvolvimento, você terá a api disponível na url: http://localhost:8000/api/v1/ e também um ambiente de simulação de caixa de email na url: http://localhost:8025.
Juntamente com isso você tem um ambiente de debug remoto rodando na porta "5678", podendo ser usado no Vscode.

### Git Flow

Esse projeto segue os preceitos do [git flow](https://danielkummer.github.io/git-flow-cheatsheet/index.pt_BR.html).

### Linter

Configure o seu Editor/IDE para utilizar o flake8 como linter.
{% if cookiecutter.use_celery == 'y' %}

## Celery

O projeto está configurado para rodar fila de tarefas assíncronas com base em mensagens distribuída, para isso ele utiliza [Celery](http://www.celeryproject.org/) e [Rabbitmq](https://www.rabbitmq.com/).
Para as tarrefas agendadas é utilizado para auxiliar o projeto [django-celery-beat](https://django-celery-beat.readthedocs.io/en/latest/).
{% endif %}

## Produção

Para o ambiente de produção esse projeto esta preparado para usar o [AWS Elastic Beanstalk](https://aws.amazon.com/pt/elasticbeanstalk/) com ambiente [Multi-Container](https://docs.aws.amazon.com/pt_br/elasticbeanstalk/latest/dg/create_deploy_docker_ecs.html) e as imagens armazenadas no [AWS ECR](https://aws.amazon.com/pt/ecr/).