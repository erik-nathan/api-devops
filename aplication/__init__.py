import os
from flask import Flask
from flask_restful import Api
from aplication.resources.healthcheck_resource import HealthcheckResource
from aplication.resources.hostname_resource import HostnameResorce


def create_app():
    app = Flask(__name__)
    api = Api(app)

    if 'FLASK_CONFIG' in os.environ.keys():
        app.config.from_object('aplication.settings.' + os.environ['FLASK_CONFIG'])
    else:
        app.config.from_object('aplication.settings.Development')

    api.add_resource(HealthcheckResource, '/healthcheck')
    api.add_resource(HostnameResorce, '/hostname')

    return app
