from flask_restful import Resource
from aplication.models.monitoring_models.monitoring_system_models import so_name, uptime_so, cpu_usage, memory_usage, disk_usage, network_usage


class MonitoringResource(Resource):
    def get(self):
        name = so_name()
        uptime = uptime_so()
        cpu = cpu_usage()
        memoria = memory_usage()
        disco = disk_usage()
        bytes_sent = network_usage()

        return {"message": f'Nome do Host: {name} | UpTime: {uptime} | CPU: {cpu}% | Memória: {memoria}% | Disco: {disco}% | Bytes Enviados/Recbidos: {bytes_sent}'}