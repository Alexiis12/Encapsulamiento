class Cliente:

    def _init_(self,  nombre:str, apellido:str, cedula:str, correo:str, edad:int = None, vip:bool = False, fecha_nacimiento= None):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._cedula = cedula
        self._correo = correo
        self._vip = vip
        self._fecha_nacimiento = fecha_nacimiento

    #def _str_(self):
    #    return (f'Persona [nombre: {self._nombre}, epellido: {self._apellido}'
    #            f'cedula: {self._cedula}, correo= {self._cedula}, vip?:{self._vip}]')

    def _str_(self):
        return f'Cliente {self._dict.str_()}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo= correo

    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, vip):
        self._vip = vip

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

'''
if _name_ == '_main_':
    objectPersona1 = Persona(nombre='carlos', apellido='asencio', edad='23',cedula='0952695732', correo='carlosmadesco12@gmail.com')
    print(objectPersona1)
    print(objectPersona1._nombre)
    print(objectPerson
    a1._apellido)
    print(objectPersona1._edad)

    p2 = Persona (nombre='carlos', cedula='0952695732', apellido='asencio', edad='23', correo='carlosmadesco12@gmail.com')
    print(p2)
    print(p2._nombre)
    print(p2._apellido)
    print(p2._edad)

    p3 = Persona ('carlos', 'asencio','0952695732', 'carlosmadesco12@gmail.com')
'''

if _name_ == '_main_':
    objCliente1 = Cliente(nombre='carlos', apellido='asencio', edad=23, cedula='0952695732', correo='carlosmadesco12@mail.com')
    print(objCliente1._str_())

    print(objCliente1.nombre)
    objCliente1.nombre = 'carlos'
    print(objCliente1.nombre)