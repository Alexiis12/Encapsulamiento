from persona import Persona


class Empleado(Persona):

    def _int_(self, id_empleado, sueldo, nombre, apellido, cedula):
        super()._init_(nombre=nombre, apellido=apellido, cedula=cedula)
        self._ide_empleado= id_empleado
        self._sueldo= sueldo
        self._nombre = nombre
        self._apellido = apellido
        self._cedula  = cedula


    @property
    def id_empleado(self):
        return self ._ide_empleado

    @id_empleado.setter
    def id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo (self, sueldo):
        self._sueldo = sueldo

    def _str_(self):
        return f'Empleado {self._dict.str_()}'

    e1 = id_empleado(nombre='carlos', apellido='asencio', sueldo='1000', cedula= '0952695732', id_empleado='1')
    print(e1)
