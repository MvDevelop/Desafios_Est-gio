
#algoritmo03

#JSON
{
    "faturamento": [
        {"dia": 1, "valor": 200.0},
        {"dia": 2, "valor": 0.0},
        {"dia": 3, "valor": 300.0},
        {"dia": 4, "valor": 400.0},
        {"dia": 5, "valor": 0.0},
        {"dia": 6, "valor": 500.0},
        {"dia": 7, "valor": 600.0}
    ]
}

#Solução

import json

def carregar_faturamento(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)["faturamento"]

def calcular_faturamento(faturamento):
    valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]
    
    if not valores:
        return None, None, 0  

    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    
    dias_acima_media = sum(1 for valor in valores if valor > media)

    return menor, maior, dias_acima_media

if __name__ == "__main__":
    faturamento = carregar_faturamento('faturamento.json')
    menor, maior, dias_acima_media = calcular_faturamento(faturamento)
    
    print(f"Menor valor de faturamento: R${menor:.2f}")
    print(f"Maior valor de faturamento: R${maior:.2f}")
    print(f"Número de dias acima da média: {dias_acima_media}")
