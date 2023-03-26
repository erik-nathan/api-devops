from flask_restful import Resource
from aplication.models.monitoring_models.monitoring_services_models import check_website

class MonitoringServiceResource(Resource):
    def get(self):
        urls = [
            "jira-isi.pe.senai.br",
            "jenkins.isitics.com",
            "api.dev.mouralock.isitics.com"
        ]
        results = []
        for url in urls:
            results.append(check_website(url))
        return results
