from random import choice, randint, randrange
from os import system
import pickle


##### Asignacion de una id digital para el sistema #####
id_lists = []
def assign_id():
    random_id = randint(1000, 9999)
    if random_id not in id_lists:
        id_lists.append(random_id)
        return random_id
    else:
        random_id = assign_id()


########### Clase main ###########
class identifier:
    def __init__(self, name, sex):
        self.id = assign_id()
        self.name = name
        self.sex = sex


class human(identifier):
    def __init__(self, dni, name, sex, address, email, phone):
        super().__init__(name, sex)
        #self.id
        self.dni = dni
        self.address = address
        self.email = email
        self.phone = phone
########### Clase empleado ###########
class employee(human):
    def __init__(self, dni, name, sex, address, email, phone, charge, since):
        super().__init__(dni, name, sex, address, email, phone)
        #self.id
        self.type = 'EMPLEADO'
        self.charge = charge
        self.since = since
########### Clase adoptador ###########
class adopter(human):
    def __init__(self, dni, name, sex, address, email, phone, able_to_adopt):
        super().__init__(dni, name, sex, address, email, phone)
        #self.id
        self.type = 'ADOPTANTE'
        self.able_to_adopt = able_to_adopt
########### Clase donante ###########
class donor(human):
    def __init__(self, dni, name, sex, address, email, phone):
        super().__init__(dni, name, sex, address, email, phone)
        #self.id
        self.type = 'DONANTE'


########### Clase animal ###########
class pet(identifier):
    def __init__(self, name, age, sex, breed, weight, available_for_adoption):
        super().__init__(name, sex)
        #self.id
        self.age = age
        self.breed = breed
        self.weight = weight
        self.available_for_adoption = available_for_adoption
        self.adopted = False
        self.history = {}
class dog(pet):
    def __init__(self, name, age, sex, breed, weight, available_for_adoption):
        super().__init__(name, age, sex, breed, weight, available_for_adoption)
        #self.id
        self.type = 'PERRO'
class hamster(pet):
    def __init__(self, name, age, sex, breed, weight, available_for_adoption):
        super().__init__(name, age, sex, breed, weight, available_for_adoption)
        #self.id
        self.type = 'HAMSTER'
class parrot(pet):
    def __init__(self, name, age, sex, breed, weight, available_for_adoption):
        super().__init__(name, age, sex, breed, weight, available_for_adoption)
        #self.id
        self.type = 'LORO'
class parakeet(pet):
    def __init__(self, name, age, sex, breed, weight, available_for_adoption):
        super().__init__(name, age, sex, breed, weight, available_for_adoption)
        #self.id
        self.type = 'PERICO'
class cat(pet):
    def __init__(self, name, age, sex, breed, weight, available_for_adoption):
        super().__init__(name, age, sex, breed, weight, available_for_adoption)
        #self.id
        self.type = 'GATO'


########### Leer base de datos ###########
def read_data(type):
    global id_lists
    try:
        with open('./.data', 'rb') as id_data:
            id_lists = pickle.load(id_data)
            id_data.close()
            del id_data
    except FileNotFoundError: open('./.data', 'wb')
    if type == 'users':
        try:
            with open('./.users_data', 'rb') as data:
                users = pickle.load(data)
                data.close()
                del data
                return users
        except FileNotFoundError: 
            open('./.users_data', 'wb')
            return []
    elif type == 'pets':
        try:
            with open('./.pets_data', 'rb') as data:
                pets = pickle.load(data)
                data.close()
                del data
                return pets
        except FileNotFoundError: 
            open('./.pets_data', 'wb')
            return []

########### Escribir base de datos ###########
def write_data(type, list):
    global id_lists
    with open('./.data', 'wb') as id_data:
        pickle.dump(list, id_data)
        id_data.close()
        del id_data
    if type == 'users':
        with open('./.users_data', 'wb') as data:
            pickle.dump(list, data)
            data.close()
            del data
    else:
        with open('./.pets_data', 'wb') as data:
            pickle.dump(list, data)
            data.close()
            del data


########### Logo de la fundacion ###########
def hlpf(): system('clear'), print("\n↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦ HAPPY LITTLE PAWS FUNDATION ↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤")


########### Comprobacion para registro de usuario o animal ###########
def confirmation(answer, id):
        if answer == 'si':
            input(f'\nRegistro exitoso con el ID {id}!\n\nPresiona enter para continuar')
            return True
        else: 
            input('\nRegistro cancelado.\n\nPresione enter para continuar')
            return False


########### Opcion 1 del menu principal, registrar usuario ###########
def register_user():
    hlpf()
    choice = int(input("""
↦↦↦↦↦↦ Registrar usuario ↤↤↤↤↤↤
    1. Adoptador
    2. Empleado
    3. Volver

Por favor, ingrese el tipo de usuario a registrar: """))-1
    if choice > -1 and choice < 2:
        users_data = read_data('users')
        list_of_users = ['adoptante','empleado']
        hlpf()
        print(f"""\n↦↦↦↦↦↦ Registro de {list_of_users[choice]} ↤↤↤↤↤↤""")
        dni = input('Cedula: ')
        name = input('Nombre: ')
        sex = input('Sexo: ')
        address = input('Direccion: ')
        email = input('Correo electronico: ')
        phone = input('Telefono: ')
        if choice == 0: 
            able_to_adopt = input('Posibilidad de adoptar: ')
            var = adopter(dni, name, sex, address, email, phone, able_to_adopt)
        elif choice == 1:
            charge = input('Cargo:')
            since = input('Desde: ')
            var = employee(dni, name, sex, address, email, phone, charge, since)
        question = input(f"""\nSeguro deseas registrar este {list_of_users[choice]}? (Si/No): """).lower()
        confir = confirmation(question, var.id)
        if confir == True: 
            users_data.append(var)
        write_data('users', users_data)
    else:
        main()


########### Opcion 2 del menu principal, registrar animal ###########
def register_pet():
    hlpf()
    choice = int(input('''
↦↦↦↦↦↦ Registrar animal ↤↤↤↤↤↤
    1. Gato
    2. Hamster
    3. Loro
    4. Perico
    5. Perro
    6. Volver

Por favor, ingrese el tipo de animal a registrar: '''))-1
    if choice > -1 and choice < 5:
        pets_data = read_data('pets') 
        list_of_pets = ['gatos','hamsters','loros','pericos','perros']
        hlpf()
        print(f'''\n↦↦↦↦↦↦ Registro para {list_of_pets[choice]} ↤↤↤↤↤↤\n''')
        name = input('Nombre: ')
        age = input('Edad(Puede ser aprox): ')
        sex = input('Sexo: ')
        breed = input('Raza: ')
        weight = input('Peso(Kg): ')
        available_for_adoption = input('Disponible para adopcion?: ')
        if choice == 0: var = cat(name, age, sex, breed, weight, available_for_adoption)
        elif choice == 1: var = hamster(name, age, sex, breed, weight, available_for_adoption)
        elif choice == 2: var = parrot(name, age, sex, breed, weight, available_for_adoption)
        elif choice == 3: var = parakeet(name, age, sex, breed, weight, available_for_adoption)
        elif choice == 4: var = dog(name, age, sex, breed, weight, available_for_adoption)
        question = input(f"""\nSeguro deseas registrar este {list_of_pets[choice]}? (Si/No): """).lower()
        confir = confirmation(question, var.id)
        if confir == True: 
            pets_data.append(var)
        write_data('pets', pets_data)
    else:
        main()


########################################## FALTA CORREGIR ##########################################
########################################## FALTA CORREGIR ##########################################
########### Opcion 1 del menu principal, modificar registro ###########
# def modify_registration():
#     hlpf()
#     choice = int(input('''
# ↦↦↦↦↦↦ Modificar registro ↤↤↤↤↤↤
#     1. Lista de usuarios
#     2. Lista de animales
#     3. Volver

# Por favor, ingrese una opcion: '''))-1
#     if choice > -1 and choice < 2:
#         names = ['usuarios', 'animales']
#         hlpf()
#         print(f'\n↦↦↦↦↦↦ Lista de {names[choice]} ↤↤↤↤↤↤\n')
#         if choice == 0:
#             for id, data in users.items():
#                 print(f'''{id} | {data.type} | {data.name}\n''')
#             idn = int(input('Ingrese el ID del registro a modificar: '))
#             if idn in users.keys():
#                 input('Ok')

#         else:
#             for id, data in pets.items():
#                 print(f'''{id} | {data.type} | {data.name}\n''')
#             enter = input('Ingrese el ID del registro a modificar: ')
#     else:
#         main()
########################################## FALTA CORREGIR ##########################################
########################################## FALTA CORREGIR ##########################################


########### Opcion 4 del menu principal, eliminar usuario ###########
def delete_user():
    hlpf()
    print(f'\n↦↦↦↦↦↦ Lista de usuarios ↤↤↤↤↤↤\n')
    users_data = read_data('users')
    for data in users_data:
        print(f'''{data.id} | {data.type} | {data.name}\n''')
    idn = input('Ingrese el ID del registro a eliminar (Para volver solo presione enter sin ingresar): ')
    if len(idn) > 0:
        for n, data in enumerate(users_data):
            for n, id in enumerate(id_lists):
                if id == data.id:
                    del id_lists[n]
            if int(idn) == data.id:
                del users_data[n]
                input('\nUsuario eliminado\n\nPresione enter para continuar')
                write_data('users', users_data)
    elif len(idn) == 0:
        main()
    else:
        input('\nUsuario no encontrado\n\nPresione enter para continuar')
        delete_user()


########### Opcion 5 del menu principal, lista de usuarios ###########
def users_list():
    hlpf()
    print(f'\n↦↦↦↦↦↦ Lista de usuarios ↤↤↤↤↤↤\n')
    users_data = read_data('users')
    for data in users_data:
        print(f'''{data.id} | {data.type} | {data.name}\n''')
    input('Presione enter para continuar')
    main()


########### Opcion 6 del menu principal, lista de animales ###########
def animals_list():
    hlpf()
    print(f'\n↦↦↦↦↦↦ Lista de animales ↤↤↤↤↤↤\n')
    pets_data = read_data('pets')
    for data in pets_data:
        print(f'''{data.id} | {data.type} | {data.name}\n''')
    input('Presione enter para continuar')
    main()


########### Opcion 7 del menu principal, registrar donacion ###########
def donation():
    hlpf()


############################## Menu principal ##############################
def main():
    hlpf()
    choice = int(input('''
Bienvenida(o)

↦↦↦↦↦↦ MENÚ DE OPCIONES ↤↤↤↤↤↤
    1. Registrar usuario
    2. Registrar animal
    3. Modificar registro
    4. Eliminar usuario
    5. Lista de usuarios
    6. Lista de animales
    7. Ingresar donacion
    8. Salir

Por favor, ingrese el numero correspondiente a la opción deseada: '''))
    while choice != 8:
        if choice == 1:
            register_user()
        elif choice == 2:
            register_pet()
        elif choice == 3:
            modify_registration()
        elif choice == 4:
            delete_user()
        elif choice == 5:
            users_list()
        elif choice == 6:
            animals_list()
        elif choice == 7:
            donation()
    exit()


if __name__ == '__main__':
    main()