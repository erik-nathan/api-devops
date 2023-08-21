from flask_restful import Resource
from aplication.models.monitoring_models.monitoring_services_models import check_website

class MonitoringServiceResource(Resource):
    def get(self):
        urls = [
            "facebook.com",
            "google.com",
            "github.com"
        ]
        results = []
        for url in urls:
            results.append(check_website(url))
        return results
