from flask_restful import Resource
from aplication.models.hostname_models import get_hostname

class HostnameResorce(Resource):
    def get(self):
        hostname = get_hostname()
        return {"message": f"A API está executando no host: {hostname}"}
