import requests

## Inicio

print("\n *********** Bem-vindos ***********")
print("\nObrigado por escolher o Mapa do Tempo Markin\n")
print("______________________________")

## Comunicação usuario

cidade = input("\nQual cidade você deseja?\nCidade: ")

## Api

api_ = "ca061480330ca14b6adc15cdfbe2d4d3"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_}&lang=pt_br"

## Comunicação api

requisicao    = requests.get(link)
requisicao_d  = requisicao.json()
descricao     = requisicao_d["weather"] [0] ["description"]
temperatura_a = requisicao_d["main"]["temp"]     - 273.15
temperatura_m = requisicao_d["main"]["temp_min"] - 273.15
temperatura_M = requisicao_d["main"]["temp_max"] - 273.15

## Resposta para o usuario

print("\n______________________________")
print(f"\nO clima está: {descricao}\n\nTemperatura Atual:  {temperatura_a:.0f}°C\nTemperatura Mínima: {temperatura_m:.0f}°C\nTemperatura Máxima: {temperatura_M:.0f}°C\n")
print("______________________________\n")
