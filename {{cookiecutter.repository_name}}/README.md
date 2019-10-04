# {{cookiecutter.repository_name}}

{{cookiecutter.description}}

## Pré-requisitos

- [Docker](https://docs.docker.com/install/)  
- [Docker Compose](https://docs.docker.com/compose/install/)  

## Desenvolvimento

Iniciar o ambiente de desenvolvimento:
```bash
docker-compose up
```

Rodar um comando dentro do container docker:

```bash
docker-compose run --rm django [command]
```
## Produção

Para o ambiente de produção esse projeto esta preparado para usar o [Docker Swarm](https://docs.docker.com/engine/swarm/)

Para montar o ambiente use a documentação do [Docker Swarm Rocks
](https://dockerswarm.rocks/)