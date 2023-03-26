import psutil
import datetime
import socket


def so_name():
    try:
        name_so = socket.gethostname()
    except Exception as e:
        name_so = ''
        print(f'Error: Nome do S.O | {e}')
    return name_so


def uptime_so():
    try:
        date_now = datetime.datetime.now()
        start_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        uptime = date_now - start_time
        uptime_str = str(datetime.timedelta(seconds=uptime.seconds))
    except Exception as e:
        uptime_str = 'ERROR UPTIME'
        print(f'Error: UpTime | {e}')
    return uptime_str


def cpu_usage():
    try:
        porcentagem_cpu = psutil.cpu_percent(interval=1)
    except Exception as e:
        porcentagem_cpu = 0
        print(f'Error: Porcentagem CPU | {e}')
    return porcentagem_cpu


def memory_usage():
    try:
        memoria = psutil.virtual_memory()
        porcentagem_memoria = memoria.percent
    except Exception as e:
        porcentagem_memoria = 'ERROR MEMÓRIA'
        print(f'Error: Porcentagem Memória | {e}')
    return porcentagem_memoria


def disk_usage():
    try:
        disco = psutil.disk_usage('/')
        porcentagem_disco = disco.percent
    except Exception as e:
        porcentagem_disco = 'ERROR DISCO'
        print(f'Error: Porcentagem Disco | {e}')
    return porcentagem_disco


def network_usage():
    try:
        net_io_counters = psutil.net_io_counters()
        bytes_sent = net_io_counters.bytes_sent
        bytes_recv = net_io_counters.bytes_recv
    except Exception as e:
        bytes_recv, bytes_sent = 'ERROR REDE'
        print(f'Error: Informações de Rede | {e}')
    return bytes_sent, bytes_recv