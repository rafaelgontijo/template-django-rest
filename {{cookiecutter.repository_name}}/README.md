# {{cookiecutter.repository_name}}

{{cookiecutter.description}}

## Prerequisites

- [Docker](https://docs.docker.com/install/)  
- [Docker Compose](https://docs.docker.com/compose/install/)  

## Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
