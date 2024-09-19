
#algoritmo05

def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

if __name__ == "__main__":
    string_a_inverter = input("Digite uma string para inverter: ")
    
    resultado = inverter_string(string_a_inverter)
    
    print(f"String invertida: {resultado}")
