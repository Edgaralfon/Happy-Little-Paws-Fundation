from random import choice, randint, randrange
from os import system
import pickle

########### base de datos ###########
id_lists = []
users_data = []
pets_data = []
donations = 0
empty_dict = {}
empty_list = []


##### Asignacion de una id digital para el sistema #####
def assign_id():
    global id_lists
    random_id = randint(1000, 9999)
    if random_id not in id_lists:
        return random_id
    else:
        random_id = assign_id()


########### Clase main ###########
class identifier:
    def __init__(self, name, age, sex):
        self.id = assign_id()
        self.name = name
        self.age = age
        self.sex = sex


class human(identifier):
    def __init__ (self, dni, name, age, sex, address, email, phone):
        super().__init__(name, age, sex)
        #self.id
        self.dni = dni
        self.address = address
        self.email = email
        self.phone = phone
########### Clase empleado ###########
class employee(human):
    def __init__(self, dni, name, age, sex, address, email, phone, charge, since):
        super().__init__(dni, name, age, sex, address, email, phone)
        #self.id
        self.type = 'EMPLEADO'
        self.charge = charge
        self.since = since
########### Clase adoptador ###########
class adopter(human):
    def __init__(self, dni, name, age, sex, address, email, phone):
        super().__init__(dni, name, age, sex, address, email, phone)
        #self.id
        self.type = 'ADOPTANTE'
########### Clase donante ###########
class donor(human):
    def __init__(self, dni, name, age, sex, address, email, phone):
        super().__init__(dni, name, age, sex, address, email, phone)
        #self.id
        self.type = 'DONANTE'
        self.__donated = 0

    @property
    def donated(self):
        return self.__donated
    @donated.setter
    def donated(self, amount):
        self.__donated += amount


########### Clase animal ###########
class pet(identifier):
    def __init__(self, name, age, sex, breed, weight):
        super().__init__(name, age, sex)
        #self.id
        self.breed = breed
        self.weight = weight
        self.__available_for_adoption = False
        self.__history = {}
        self.adopted_by = ''
    
    @property
    def available_for_adoption(self):
        if self.__available_for_adoption == True:
            return 'Si'
        else: return 'No'
    @available_for_adoption.setter
    def available_for_adoption(self, new_input):
        if new_input == 'si':
            self.__available_for_adoption = True
        else: self.__available_for_adoption = False
    
    @property
    def history(self):
        return self.__history
    @history.setter
    def history(self, new_history, comments):
        self.__history[new_history] = comments

class dog(pet):
    def __init__(self, name, age, sex, breed, weight):
        super().__init__(name, age, sex, breed, weight)
        #self.id
        self.type = 'PERRO'
class hamster(pet):
    def __init__(self, name, age, sex, breed, weight):
        super().__init__(name, age, sex, breed, weight)
        #self.id
        self.type = 'HAMSTER'
class parrot(pet):
    def __init__(self, name, age, sex, breed, weight):
        super().__init__(name, age, sex, breed, weight)
        #self.id
        self.type = 'LORO'
class parakeet(pet):
    def __init__(self, name, age, sex, breed, weight):
        super().__init__(name, age, sex, breed, weight)
        #self.id
        self.type = 'PERICO'
class cat(pet):
    def __init__(self, name, age, sex, breed, weight):
        super().__init__(name, age, sex, breed, weight)
        #self.id
        self.type = 'GATO'


########### Leer base de datos ###########
def read_data():
    global id_lists, users_data, pets_data, donations
    try:
        with open('./.data', 'rb') as file:
            id_lists = pickle.load(file)
            users_data = pickle.load(file)
            pets_data = pickle.load(file)
            donations = pickle.load(file)
    except FileNotFoundError: open('./.data', 'wb')
    except EOFError: pass


########### Escribir base de datos ###########
def write_data():
    with open('./.data', 'wb') as file:
        pickle.dump(id_lists, file)
        pickle.dump(users_data, file)
        pickle.dump(pets_data, file)
        pickle.dump(donations, file)


########### Funcion a prueba de errores para los integers ###########
def numbers_funtion(type):
    try:
        if type == 'age':
            age = int(input('    Edad: '))
            return age
        else:
            weight = float(input('    Peso(Kg): '))
            return weight
    except ValueError: print('  Por favor, ingrese la informacion en números'), numbers_funtion(type)


########### Logo de la fundacion ###########
def hlpf() -> str: system('clear'), print("\n↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦↦ HAPPY LITTLE PAWS FUNDATION ↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤↤")


########### Comprobacion para registro de usuario o animal ###########
def confirmation(answer, id) -> bool:
        if answer == 'si':
            input(f'\n Registro exitoso con el ID {id}!\n\n Presiona enter para continuar')
            return True
        else: 
            input('\n Registro cancelado.\n\n Presione enter para continuar')
            return False


########### Opcion 1 del menu principal, realizar adopcion ###########
def adoption():
    read_data()
    hlpf()
    print("\n↦↦↦↦↦↦ Lista de animales disponibles para adoptar ↤↤↤↤↤↤\n")
    adoptable = list(filter(lambda pet: pet.available_for_adoption == 'Si', pets_data))
    for pet in adoptable:
        print(f'''    {pet.id} | {pet.type} | {pet.name}\n''')
    try:
        id = int(input(' Ingrese el ID del registro para ver mas informacion\n (Para volver solo presione enter sin ingresar algun ID): '))
    except ValueError: main()
    if len(str(id)) > 3:
        found = False
        for pet in pets_data:
            if id == pet.id:
                found = True
                hlpf()
                print(f'\n↦↦↦↦↦↦ Informacion de animal número {pet.id} ({pet.type}) ↤↤↤↤↤↤\n')
                print(f"    Nombre: {pet.name}\n    Edad: {pet.age}\n    Sexo: {pet.sex}\n    Raza: {pet.breed}\n    Peso: {pet.weight}Kg\n    Historial medico: ")
                try:
                    assert pet.history != empty_dict
                    for historyName, historyComment  in pet.history.items():
                        print(f'      + {historyName}: {historyComment}')
                except AssertionError: print('      + Ninguna hasta el momento')
        if found == True:
            try:
                choice = int(input('\n (1) Adoptar         (Enter) Volver\n Por favor, ingrese una opcion: '))
            except ValueError: adoption()
            if choice == 1:
                hlpf()
                print(f'\n↦↦↦↦↦↦ Lista de usuarios ↤↤↤↤↤↤\n')
                adopters = list(filter(lambda adopter: adopter.type == 'ADOPTANTE', users_data))
                for user in adopters:
                    print(f'''    {user.id} | {user.type} | {user.name}\n''')
                try:
                    idn = int(input(' Ingrese el ID del adoptante\n (Para volver solo presione enter sin ingresar algun ID): '))
                except ValueError: adoption()
                found = False
                for user in adopters:
                    if idn == user.id:
                        found = True
                        hlpf()
                        print(f'\n↦↦↦↦↦↦ Informacion de usuario número {user.id} ({user.type}) ↤↤↤↤↤↤\n')
                        print(f"    Cedula: {user.dni}\n    Nombre: {user.name}\n    Edad: {user.age}\n    Sexo: {user.sex}\n    Direccion: {user.address}\n    Email: {user.email}\n    Telefono: {user.phone}")
                        break
                if found == True:
                    question = input(f'\n Desea dar a {pet.name} en adopcion a este usuario? (Si/No): ').lower()
                    if question == 'si':
                        pet.available_for_adoption = 'No'
                        pet.adopted_by = user
                        write_data()
                        input('\n ADOPCION COMPLETADA EXITOSAMENTE! FELICIDADES!\n\n Presione enter para continuar')
                    else: input('\n Adopcion cancelada!\n\n Presione enter para continuar')
                else: input(f'\n Numero ID invalido\n\n Presione enter para continuar')


########### Opcion 2 del menu principal, registrar usuario ###########
def register_user():
    hlpf()
    try:
        choice = int(input("""
↦↦↦↦↦↦ Registrar usuario ↤↤↤↤↤↤\n
    (1) Adoptador
    (2) Empleado
    (3) Volver

Por favor, ingrese el tipo de usuario a registrar: """))-1
    except ValueError: register_user()
    if choice > -1 and choice < 2:
        list_of_users = ['adoptante','empleado']
        read_data()
        hlpf()
        print(f"""\n↦↦↦↦↦↦ Registro de {list_of_users[choice]} ↤↤↤↤↤↤\n""")
        dni = input('    Cedula: ').title()
        name = input('    Nombre completo: ').title()
        age = numbers_funtion('age')
        sex = input('    Sexo: ').title()
        address = input('    Direccion: ').title()
        email = input('    Correo electronico: ').title()
        phone = input('    Telefono: ')
        if choice == 0: 
            var = adopter(dni, name, age, sex, address, email, phone)
        elif choice == 1:
            charge = input('    Cargo: ').title()
            since = input('    Desde: ').title()
            var = employee(dni, name, age, sex, address, email, phone, charge, since)
        question = input(f"""\n Seguro deseas registrar este {list_of_users[choice]}? (Si/No): """).lower()
        confir = confirmation(question, var.id)
        if confir == True: 
            users_data.append(var)
            id_lists.append(str(var.id))
        write_data()
    else:
        main()


########### Opcion 3 del menu principal, registrar animal ###########
def register_pet():
    hlpf()
    try:
        choice = int(input('''
↦↦↦↦↦↦ Registrar animal ↤↤↤↤↤↤\n
    (1) Gato
    (2) Hamster
    (3) Loro
    (4) Perico
    (5) Perro
    (6) Volver

Por favor, ingrese el tipo de animal a registrar: '''))-1
    except ValueError: register_pet()
    if choice > -1 and choice < 5:
        list_of_pets = ['gato','hamster','loro','perico','perro']
        read_data() 
        hlpf()
        print(f'''\n↦↦↦↦↦↦ Registro para {list_of_pets[choice]} ↤↤↤↤↤↤\n''')
        name = input('    Nombre: ').title()
        age = numbers_funtion('age')
        sex = input('    Sexo: ').title()
        breed = input('    Raza: ').title()
        weight = numbers_funtion('weight')
        available_for_adoption = input('    Disponible para adopcion? (Si/No): ').lower()
        if choice == 0: var = cat(name, age, sex, breed, weight)
        elif choice == 1: var = hamster(name, age, sex, breed, weight)
        elif choice == 2: var = parrot(name, age, sex, breed, weight)
        elif choice == 3: var = parakeet(name, age, sex, breed, weight)
        elif choice == 4: var = dog(name, age, sex, breed, weight)
        var.available_for_adoption = available_for_adoption
        question = input(f"""\n Seguro deseas registrar este {list_of_pets[choice]}? (Si/No): """).lower()
        confir = confirmation(question, var.id)
        if confir == True: 
            pets_data.append(var)
            id_lists.append(str(var.id))
        write_data()
    else:
        main()


########### Opcion 4 del menu principal, lista de usuarios ###########
def users_list():
    read_data()
    hlpf()
    print(f'\n↦↦↦↦↦↦ Lista de usuarios ↤↤↤↤↤↤\n')
    for user in users_data:
        print(f'''    {user.id} | {user.type} | {user.name}\n''')
    try:
        idn = int(input(' Ingrese el ID del registro para ver mas informacion\n (Para volver solo presione enter sin ingresar algun ID): '))
    except ValueError: main()
    if len(str(idn)) > 3:
        found = False
        for user in users_data:
            if idn == user.id:
                found = True
                hlpf()
                print(f'\n↦↦↦↦↦↦ Informacion de usuario número {user.id} ({user.type}) ↤↤↤↤↤↤\n')
                print(f"    Cedula: {user.dni}\n    Nombre: {user.name}\n    Edad: {user.age}\n    Sexo: {user.sex}\n    Direccion: {user.address}\n    Email: {user.email}\n    Telefono: {user.phone}")
                if user.type == 'EMPLEADO':
                    print(f'    Cargo: {user.charge}\n    Desde: {user.since}')
                elif user.type == 'DONANTE':
                    print(f'    Dinero donado: {user.donated}$')
                break
        if found == True: 
            choice = int(input('\n (1) Eliminar usuario     (2) Volver\n Por favor, ingrese una opcion: '))
            if choice == 1:
                sure = input('\n Esta segura(o) de eliminar este usuario? (Si/No): ').lower()
                if sure == 'si':
                    found = False
                    for n, id in enumerate(id_lists):
                        if idn == int(id):
                            del id_lists[n]
                            break
                    for n, user in enumerate(users_data):
                        if idn == user.id:
                            found = True
                            del users_data[n]
                            input('\n Usuario eliminado\n\n Presione enter para continuar')
                            write_data()
                            break
        else: input(f'\n Numero ID invalido\n\n Presione enter para continuar')


########### Opcion 5 del menu principal, lista de animales ###########
def animals_list():
    read_data()
    hlpf()
    print(f'\n↦↦↦↦↦↦ Lista de animales ↤↤↤↤↤↤\n')
    for pet in pets_data:
        print(f'''    {pet.id} | {pet.type} | {pet.name}\n''')
    try:
        id = int(input(' Ingrese el ID del registro para ver mas informacion\n (Para volver solo presione enter sin ingresar algun ID): '))
    except ValueError: main() 
    if len(str(id)) > 0:
        found = False
        for pet in pets_data:
            if id == pet.id:
                found = True
                hlpf()
                print(f'\n↦↦↦↦↦↦ Informacion de animal número {pet.id} ({pet.type}) ↤↤↤↤↤↤\n')
                print(f"    Nombre: {pet.name}\n    Edad: {pet.age}\n    Sexo: {pet.sex}\n    Raza: {pet.breed}\n    Peso: {pet.weight}Kg\n    Historial medico: ")
                try:
                    assert pet.history != empty_dict
                    for historyName, historyComment  in pet.history.items():
                        print(f'      + {historyName}: {historyComment}')
                except AssertionError: print('      + Ninguna hasta el momento')
                try:
                    assert pet.adopted_by != ''
                    print(f'    Adoptado por: {pet.adopted_by.name}')
                except AssertionError: print(f"    Disponible para adoptar?: {pet.available_for_adoption}")
                break
        if found == True:
            try:
                choice = int(input('\n (1) Cambiar disponibilidad para adoptar\n (2) Agregar entrada al historial medico\n (Enter) Volver\n Por favor, ingrese una opcion: '))
            except ValueError: animals_list()
            if choice == 1:
                hlpf()
                print(f'\n↦↦↦↦↦↦ Disponibilidad para adopcion para {pet.id} ({pet.type}) ↤↤↤↤↤↤\n')
                available_for_adoption = input('    Disponible para adoptar? (Si/No): ').lower()
                pet.available_for_adoption = available_for_adoption
                write_data()
                input('\n Cambio realizado satifastoriamente\n Presione enter para continuar')
            elif choice == 2:
                hlpf()
                print(f'\n↦↦↦↦↦↦ Agregar entrada medica para {pet.id} ({pet.type}) ↤↤↤↤↤↤\n')
                history_name = input('    Ingresar el nombre de la entrada: ')
                history_comment = input('    Ingresar datos complementarios para la entrada: ')
                question = input(f"""\n Seguro deseas agregar esta entrada medica? (Si/No): """).lower()
                if question == 'si': 
                    pet.history[history_name] = history_comment
                    write_data()
                    input('\n Entrada al historial medico agregada sastifactoriamente\n Presione enter para continuar')
                else: input('\n Entrada al historial medico cancelada\n Presione enter para continuar')
        else: input(f'\nNumero ID invalido (Presione enter para continuar)')
    elif len(str(id)) == 0:
        main()


########### Opcion 6 del menu principal, registrar donacion ###########
def donation():
    global donations
    read_data()
    hlpf()
    print(f'\n↦↦↦↦↦↦ Agregar donacion ↤↤↤↤↤↤                   Total de donaciones: {donations:5d}$\n')
    question = input(f""" Desea agregar una donacion? (Si/No): """).lower()
    if question == 'si':
        hlpf()
        print(f'\n↦↦↦↦↦↦ Agregar donacion ↤↤↤↤↤↤                   Total de donaciones: {donations:5d}$\n')
        dni = input('    Cedula: ')
        name = input('    Nombre completo: ')
        age = numbers_funtion('age')
        sex = input('    Sexo: ')
        address = input('    Direccion: ')
        email = input('    Correo electronico: ')
        phone = input('    Telefono: ')
        var = donor(dni, name, age, sex, address, email, phone)
        question = input(f"""\n Confirme para proceder (Si/No): """).lower()
        if question == 'si':
            hlpf()
            donation = int(input(f'\n↦↦↦↦↦↦ Agregar donacion ↤↤↤↤↤↤                   Total de donaciones: {donations:5d}$\n\n    Por favor, ingrese el monto a donar: '))
            question = input(f"""\n Confirme si el monto es correcto, (Si/No): """).lower()
            confir = confirmation(question, var.id)
            if confir == True: 
                users_data.append(var)
                id_lists.append(str(var.id))
                var.donated = donation
                donations += donation
            write_data()
    else:
        main()


############################## Menu principal ##############################
def main():
    hlpf()
    try:
        choice = int(input(''' 
 Bienvenida(o)

↦↦↦↦↦↦ MENÚ DE OPCIONES ↤↤↤↤↤↤\n
    (1) Realizar adopcion
    (2) Registrar usuario
    (3) Registrar animal
    (4) Lista de usuarios
    (5) Lista de animales
    (6) Ingresar donacion
    (7) Salir

 Por favor, ingrese el numero correspondiente a la opción deseada: '''))
        if choice > 7: raise ValueError
    except ValueError: main()
    while choice < 7:
        if choice == 1:
            adoption()
        elif choice == 2:
            register_user()
        elif choice == 3:
            register_pet()
        elif choice == 4:
            users_list()
        elif choice == 5:
            animals_list()
        elif choice == 6:
            donation()
    exit()


if __name__ == '__main__':
    main()