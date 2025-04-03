agenda = {
     "Luis": {"telefono": "555-1234", "email": "luis@email.com"},
     "Ana": {"telefono": "555-5678", "email": "ana@email.com"},
     "Roni": {"telefono": "555-879", "email": "roni@email.com"},
     "Carlos": {"telefono": "555-099", "email": "carlos@email.com"},
     "lucas": {"telefono": "555-623", "email": "lucas@email.com"},
     "Donovan": {"telefono": "555-001", "email": "donovan@email.com"},
     "Issac": {"telefono": "555-712", "email": "issac@email.com"},
     "Santiago": {"telefono": "555-1230", "email": "santiago@email.com"},
     "Lian": {"telefono": "556-9622", "email": "lian@email.com"},
     "Valeria": {"telefono": "774-8892", "email": "valeria@email.com"},
     "Evelin": {"telefono": "889-6723", "email": "evelin@email.com"},
     "Daniela": {"telefono": "888-2321", "email": "daniela@email.com"},
     "christian": {"telefono": "882-9923", "email": "christian@email.com"},
     "Ian": {"telefono": "992-8734", "email": "ian@email.com"},
     "Dilan": {"telefono": "992-7672", "email": "dilan@email.com"},
 }
 
def mostrar_menu():
    print("\n📱 AGENDA DE CONTACTOS")
    print("1. Ver contactos")
    print("2. Agregar cpntacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
 
def ver_contactos():
    if not agenda:
        print("\n📭 La bandeja esta vasia.")
    else:
        print("\n📖 Lista de contactos:")
        for nombre, info in  agenda.items():
            print(f"📌 {nombre} - 📞 {info['telefono']} - ✉{info['email']}")
 
def agredar_contacto():
    nombre = input("\n Ingresa el nombre: ")
    telefono = input("📞 Ingresa el numero: ")
    email = input("✉ Ingresa el email: ")
     
    if nombre in agenda:
        print("⚠ El contacto ya existe.")
    else:
        agenda[nombre] = {"telefono": telefono, "email": email}
        print(f"✅ contacto {nombre} agregado con exito")
         
def buscar_contacto():
    nombre = input("\n🔎 Ingresa el nombre del contacto a buscar: ")
    if nombre in agenda:
        info = agenda[nombre]
        print(f"📌 {nombre} - 📞 {info['telefono']} - ✉ {info['email']}")
    else:
        print("✖ Contacto no encontrado.")
 
def eliminar_contacto():
    nombre = input("\n🗑 Ingresa el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"✅ Contacto {nombre} eliminado.")
         
    else:
        print("✖ Contacto no encontrado.")
 
while True:
    mostrar_menu()
    opcion = input("Ingresa el numero de agrado: ")
     
    if opcion == "1":
        ver_contactos()
    elif opcion == "2":
        agredar_contacto()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Esperamos ayudarle otro momento👋")
        break
    else:
        print("Error ⚠, ingrese un numero valido")
