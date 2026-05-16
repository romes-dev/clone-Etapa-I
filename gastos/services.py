"""Serviços externos do app de gastos."""

import requests

AWESOMEAPI_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"


def buscar_cotacoes():
    """Busca cotação atual do dólar e euro em reais via AwesomeAPI."""
    try:
        response = requests.get(AWESOMEAPI_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "dolar": float(data["USDBRL"]["bid"]),
            "euro": float(data["EURBRL"]["bid"]),
        }
    except Exception:
        return None
