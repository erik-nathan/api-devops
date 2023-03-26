from flask_restful import Resource
from aplication.models.docker_models.list_containers_models import list_containers


class ListContainerResource(Resource):
    def get(self):
        lista = list_containers()
        return lista
