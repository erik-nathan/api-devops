import docker

def list_containers():
    HOST_DOCKER = 'unix://var/run/docker.sock'
    client = docker.DockerClient(base_url=HOST_DOCKER)
    container_list = client.containers.list()
    container_info_list = []
    for container in container_list:
        container_short_id = container.short_id
        container_name = container.name
        container_attrs = container.attrs
        container_status = container_attrs['State']['Status']

        container_info_list.append({
            "ID do Container": container_short_id,
            "Nome do Container": container_name,
            "Status do Container": container_status
        })
    return container_info_list


# Chamar a função para listar e imprimir informações sobre os containers do Docker
# list_containers()
