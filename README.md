## Prerequirements
- [Install Python](https://www.python.org/downloads/)

- [Install Docker](https://docs.docker.com/engine/install/)

- [Install Docker Compose](https://docs.docker.com/compose/install/)

## How to run
- Launch Elasticsearch with Docker compose:
```shell
docker compose up
```
- Create an Elasticsearch index:
```shell
python create_index.py
```
- Index a rectangle:
```shell
python index_data.py
```
- Search for a polygon the point belongs to:
```shell
python query_data.py
```