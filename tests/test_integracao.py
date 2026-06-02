"""Teste de integração: valida comunicação com a AwesomeAPI de cotações."""

from unittest.mock import Mock, patch

from gastos.services import buscar_cotacoes


def test_buscar_cotacoes_retorna_dolar_e_euro():
    """Verifica que a função processa corretamente a resposta da API."""
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "USDBRL": {"bid": "5.20"},
        "EURBRL": {"bid": "5.80"},
    }

    with patch("gastos.services.requests.get", return_value=mock_response):
        resultado = buscar_cotacoes()

    assert resultado is not None
    assert resultado["dolar"] == 5.20
    assert resultado["euro"] == 5.80


def test_buscar_cotacoes_retorna_none_em_falha():
    """Verifica que a função retorna None quando a API está indisponível."""
    with patch("gastos.services.requests.get", side_effect=Exception("Erro de rede")):
        resultado = buscar_cotacoes()

    assert resultado is None
