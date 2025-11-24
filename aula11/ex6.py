def celsius_para_fahrenheit():
    try:
        c = float(input("Digite a temperatura em Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C equivalem a {f}°F")
    except ValueError:
        print("Erro: digite um número válido para temperatura.")

celsius_para_fahrenheit()