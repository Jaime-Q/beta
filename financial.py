import random  

Tit = "=== Simulating a financial report with Python ==="
Sep = "-" * 40
Client_Count = 5

Clients = []

for i in range(Client_Count):
    print(f"Entering data for Client {i+1}")
    name = input("Full name: ")
    id = input("ID number: ")
    Age = int(input("Age: "))
    gastos = float(input("Monthly expenses: "))
    Cell = input("Mobile phone: ")
    Address = input("Address: ")
    Status = True  

    ingreso = random.randint(1000000, 8000000)  
    saldo = ingreso - gastos  

    client_info = {
        "Name": name,
        "ID": id,
        "Age": Age,
        "Monthly expenses": gastos,
        "Mobile phone": Cell,
        "Address": Address,
        "Activo": Status,
        "Ingreso": ingreso,
        "Saldo": saldo
    }
    Clients.append(client_info)

print(f"{Tit}")
for idx, client in enumerate(Clients, start=1):
    print(f"Cliente {idx}")
    print(Sep)
    print(f"Name: {client['Name']}")
    print(f"ID: {client['ID']}")
    print(f"Age: {client['Age']}")
    print(f"Monthly Expenses: ${client['Expenses']:,.2f}")
    print(f"Monthly Income:   ${client['Income']:,.2f}")
    print(f"Estimated Balance: ${client['Balance']:,.2f}")
    print(f"Phone: {client['Phone']}")
    print(f"Address: {client['Address']}")
    print(f"Active Client: {client['Status']}")
    print(Sep)