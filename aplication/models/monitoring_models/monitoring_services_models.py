import requests
import ssl
import socket
import datetime
import time


def check_website(url):
    try:
        time_inicial = time.time()
        response = requests.get(f'https://{url}', verify=True)
        time_final = time.time()
    except requests.exceptions.RequestException as e:
        # Se ocorrer um erro de solicitação, o site está inacessível
        return {
            "url": url,
            "status": "down",
            "error": str(e)
        }

    response_time = (time_final - time_inicial) * 1000
    response_time_ms = f"{round(response_time):.0f}ms"

    try:
        if response.status_code == 200:
            status = f"up - {response.status_code}"
        else:
            status = f"status_code {response.status_code}"
    except requests.exceptions.RequestException as e:
        status = "down"

    expiration_date = get_certificate_expiration_date(url)
    date = datetime.datetime.strptime(expiration_date, '%b %d %H:%M:%S %Y %Z')

    formatted = datetime.datetime.strftime(date, '%d/%m/%Y')

    # DATA ATUAL
    date_now = datetime.datetime.now()

    # DIFERENÇA DE DATAS
    difference_between_dates = date - date_now
    difference = difference_between_dates.days

    return {
        "Aplicação": url,
        "Status": status,
        "Tempo de resposta": response_time_ms,
        "Data de validade do certificado": formatted,
        "Expira em": difference
    }


def get_certificate_expiration_date(hostname, port=443):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(), server_hostname=hostname)
    conn.connect((hostname, port))
    ssl_info = conn.getpeercert()
    expiration = ssl_info['notAfter']
    return expiration
