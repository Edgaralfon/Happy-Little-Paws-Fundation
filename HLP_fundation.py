from random import choice, randint, randrange
from os import system

id_lists = []
users = {}
pets = {}


##### Asignacion de una id digital para el sistema #####
def assign_id():
    random_id = randint(1000, 9999)
    if random_id not in id_lists:
        return random_id
    else:
        random_id = assign_id()
    id_lists.append(random_id)


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
########### Clase perro ###########
class dog(pet):
    def __init__(self, name, age, sex, breed, weight, available_for_adoption):
        super().__init__(name, age, sex, breed, weight, available_for_adoption)
        #self.id
        self.type = 'PERRO'
########### Clase hamster ###########
class hamster(pet):
    def __init__(self, name, age, sex, breed, weight, available_for_adoption):
        super().__init__(name, age, sex, breed, weight, available_for_adoption)
        #self.id
        self.type = 'HAMSTER'
########### Clase loro ###########
class parrot(pet):
    def __init__(self, name, age, sex, breed, weight, available_for_adoption):
        super().__init__(name, age, sex, breed, weight, available_for_adoption)
        #self.id
        self.type = 'LORO'
########### Clase perico ###########
class parakeet(pet):
    def __init__(self, name, age, sex, breed, weight, available_for_adoption):
        super().__init__(name, age, sex, breed, weight, available_for_adoption)
        #self.id
        self.type = 'PERICO'
########### Clase gato ###########
class cat(pet):
    def __init__(self, name, age, sex, breed, weight, available_for_adoption):
        super().__init__(name, age, sex, breed, weight, available_for_adoption)
        #self.id
        self.type = 'GATO'


########### Funcion para registrar usuario ###########
def register_user():
    system('clear')
    choice = int(input("""
↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦ HAPPY LITTLE PAWS FUNDATION ↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤

↦↦↦↦↦↦ Registrar usuario ↤↤↤↤↤↤
    1. Adoptador
    2. Empleado
    3. Volver

Por favor, ingrese el tipo de usuario a registrar: """))
    if choice == 1:
        system('clear')
        ########### Funcion para registrar adoptante ###########
        print("""
↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦ HAPPY LITTLE PAWS FUNDATION ↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤

↦↦↦↦↦↦ Registro de adoptador ↤↤↤↤↤↤""")
        dni = input('Cedula: ')
        name = input('Nombre: ')
        sex = input('Sexo: ')
        address = input('Direccion: ')
        email = input('Correo electronico: ')
        phone = input('Telefono: ')
        able_to_adopt = input('Posibilidad de adoptar: ')
        var = adopter(dni, name, sex, address, email, phone, able_to_adopt)
        users[var.id] = var
    elif choice == 2:
        system('clear')
        ########### Funcion para registrar empleado ###########
        print("""
↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦ HAPPY LITTLE PAWS FUNDATION ↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤

↦↦↦↦↦↦ Registro de empleado ↤↤↤↤↤↤""")
        dni = input('Cedula: ')
        name = input('Nombre: ')
        sex = input('Sexo: ')
        address = input('Direccion: ')
        email = input('Correo electronico: ')
        phone = input('Telefono: ')
        charge = input('Cargo: ')
        since = input('Desde: ')
        var = employee(dni, name, sex, address, email, phone, charge, since)
        users[var.id] = var
    else:
        main()


def menu_pets(n):
    system('clear')
    list_of_pets = ['gatos','hamsters','loros','pericos','perros']
    print(f'''
↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦ HAPPY LITTLE PAWS FUNDATION ↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤

↦↦↦↦↦↦ Registro para {list_of_pets[n]} ↤↤↤↤↤↤''')
    name = input('Nombre: ')
    age = int(input('Edad(Puede ser aprox): '))
    sex = input('Sexo: ')
    breed = input('Raza: ')
    weight = float(input('Peso(Kg): '))
    available_for_adoption = input('Disponible para adopcion?: ')
    var = cat(name, age, sex, breed, weight, available_for_adoption)
    pets[var.id] = var

########### Funcion para registrar animal ###########
def register_pet():
    system('clear')
    choice = int(input('''
↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦ HAPPY LITTLE PAWS FUNDATION ↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤

↦↦↦↦↦↦ Registrar animal ↤↤↤↤↤↤
    1. Gato
    2. Hamster
    3. Loro
    4. Perico
    5. Perro
    6. Volver

Por favor, ingrese el tipo de animal a registrar: '''))
    if choice == 1:
        menu_pets(choice-1)
        
    elif choice == 2:
        menu_pets(choice-1)

    elif choice == 3:
        menu_pets(choice-1)

    elif choice == 4:
        menu_pets(choice-1)

    elif choice == 5:
        menu_pets(choice-1)

    else:
        main()

def modify_registration():
    system('clear')
    choice = int(input('''
↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦ HAPPY LITTLE PAWS FUNDATION ↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤

↦↦↦↦↦↦ Modificar registro ↤↤↤↤↤↤
    1. Lista de usuarios
    2. Lista de animales

Por favor, ingrese una opcion: '''))
    if choice == 1:
        system('clear')
        print('''
↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦ HAPPY LITTLE PAWS FUNDATION ↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤

↦↦↦↦↦↦ Lista de usuarios ↤↤↤↤↤↤
''')
        for id, data in users.items():
            print(f'''{id} | {data.type} | {data.name}\n''')
        enter = input('Ingrese el ID del registro a modificar: ')
    elif choice == 2:
        pass
    else:
        main()


def delete_user():
    system('clear')
    pass

def users_list():
    system('clear')
    pass

def animals_list():
    system('clear')
    pass

def donation():
    system('clear')
    pass


def main():
    system('clear')
    choice = int(input('''
↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦ HAPPY LITTLE PAWS FUNDATION ↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤
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