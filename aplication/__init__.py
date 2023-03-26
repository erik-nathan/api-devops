import os
from flask import Flask
from flask_restful import Api
from aplication.resources.healthcheck_resource import HealthcheckResource
from aplication.resources.monitoring_resources.monitoring_system_resource import MonitoringResource
from aplication.resources.monitoring_resources.monitoring_service_resource import MonitoringServiceResource
from aplication.resources.docker.list_containers_resources import ListContainerResource


def create_app():
    app = Flask(__name__)
    api = Api(app)

    if 'FLASK_CONFIG' in os.environ.keys():
        app.config.from_object('aplication.settings.' + os.environ['FLASK_CONFIG'])
    else:
        app.config.from_object('aplication.settings.Development')

    api.add_resource(HealthcheckResource, '/healthcheck')
    api.add_resource(MonitoringResource, '/monitoring/os')
    api.add_resource(MonitoringServiceResource, '/monitoring/services')
    api.add_resource(ListContainerResource, '/docker/lista')

    return app
