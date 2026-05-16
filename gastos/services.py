import requests

AWESOMEAPI_URL = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"

def buscar_cotacoes():
    """Busca da cotação atual do Dólar e do Euro em relação ao Real."""
    try:
        response = requests.get(AWESOMEAPI_URL, timeout=5)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        data = response.json()
        return {
            "dolar": float(data["USDBRL"]["bid"]),
            "euro": float(data["EURBRL"]["bid"])
        }
    
    except Exception:
        return None