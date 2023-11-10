class Persona:
    contador_personas= 0

    def _init_(self, nombre:str, apellido:str, cedula:str, correo:str):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._correo = correo

    def _str_(self):
        return f'Persona {self._dict.str_()}'

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
    def cedula(self):
        return self.cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def correo(self):
        return self.correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

if "_name_" == '_main_':
    objPersona1 = Persona(nombre='carlos', apellido='asencio', cedula='0952695732', correo='carlosmadesco12@mail.com')
    print(objPersona1._str_())

from persona import Persona


class Empleado(Persona):
    contador_empleados= 0

    def _init_(self, id_empleado, sueldo, nombre, apellido, cedula):
        self._id_empleado = id_empleado
        self._sueldo = sueldo
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula

    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def _str_(self):
        return f'Empleado {self._dict.str_()}'


if "_name_" == '_main_':
    e1 = Empleado(nombre='carlos', apellido='asencio', sueldo='1000', cedula='0952695732', id_empleado=1)
    print(e1)


class Cliente:
    contador_cliente = 0

    def _init_(self, nombre, apellido, fecha_registro, vip):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_registro = fecha_registro
        self._vip = vip
        Cliente.contador_cliente += 1
        self._id_cliente = Cliente.contador_cliente

    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    def _str_(self):
        return f'Cliente: {self._dict.str_()}'

if "_name_" == '_main_':
    cli1 = Cliente(nombre='carlos', apellido='asencio', fecha_registro='10-11-2023', vip= True)
    print(cli1)
    cli2 = Cliente(nombre='carlos', apellido='asencio', fecha_registro='20-12-2023', vip= False)
    print(cli2)