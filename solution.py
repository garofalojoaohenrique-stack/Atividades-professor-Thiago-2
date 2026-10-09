from datetime import datetime, timedelta
import requests


def cotar():
    cotacoes = []
    hoje = datetime.today()
    url = (
        "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
        "CotacaoDolarDia(dataCotacao=@dataCotacao)"
    )

    for i in range(365):
        data = (hoje - timedelta(days=i)).strftime("%m-%d-%Y")
        resposta = requests.get(
            url,
            params={"@dataCotacao": "'" + data + "'", "$format": "json"},
            timeout=15,
        )
        resposta.raise_for_status()
        registros = resposta.json()["value"]
        cotacoes.append(registros[0]["cotacaoCompra"] if registros else None)

    return cotacoes
