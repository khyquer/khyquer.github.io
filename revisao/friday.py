# Lista com os dias da semana, começando por Sunday
dias_da_semana = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Lista com frases da música, mesma ordem dos dias
frases = [
    "Sunday always comes too late",
    "Monday you can fall apart",
    "Tuesday I stay in bed",
    "Wednesday I watch the walls instead",
    "Thursday doesn't even start",
    "It's Friday I'm in love",
    "Saturday wait"
]

# Instruções para o usuário
print("Digite o número do dia da semana:")
print("0 - Sunday")
print("1 - Monday")
print("2 - Tuesday")
print("3 - Wednesday")
print("4 - Thursday")
print("5 - Friday")
print("6 - Saturday")

# Entrada do usuário (como texto)
numero = input()

# Vários ifs separados
if numero == "0":
    print(frases[0])
if numero == "1":
    print(frases[1])
if numero == "2":
    print(frases[2])
if numero == "3":
    print(frases[3])
if numero == "4":
    print(frases[4])
if numero == "5":
    print(frases[5])
if numero == "6":
    print(frases[6])
if numero not in ["0", "1", "2", "3", "4", "5", "6"]:
    print("Número inválido")
