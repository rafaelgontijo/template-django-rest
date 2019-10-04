# {{cookiecutter.repository_name}}

{{cookiecutter.description}}

## Pré-requisitos

- [Docker](https://docs.docker.com/install/)  
- [Docker Compose](https://docs.docker.com/compose/install/)  

## Desenvolvimento

Iniciar o ambiente de desenvolvimento, após terminar de rodar o script de iniciação, você terá a api disponível na url: http://localhost:8000/api/v1/ e também um ambiente de simulação de caixa de email na url: http://localhost:8025
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

## Produção

Para o ambiente de produção esse projeto esta preparado para usar o [Docker Swarm](https://docs.docker.com/engine/swarm/)

Para montar o ambiente use a documentação do [Docker Swarm Rocks
](https://dockerswarm.rocks/)