
#algoritmo04

faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

def calcular_percentuais(faturamento):
    total_faturamento = sum(faturamento.values())
    
    percentuais = {}
    for estado, valor in faturamento.items():
        percentuais[estado] = (valor / total_faturamento) * 100
    
    return percentuais, total_faturamento

if __name__ == "__main__":
    percentuais, total = calcular_percentuais(faturamento_por_estado)
    
    print(f"Total de faturamento: R${total:.2f}")
    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")
