class Docente:
    def __init__(self):
        self.__id = None
        self.__nombres = None
        self.__apellidos = None
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def getNombres(self):
        return self.__nombres
    
    def setNombres(self, nombres):
        self.__nombres = nombres
    
    def getApellidos(self):
        return self.__apellidos
    
    def setApellidos(self, apellidos):
        self.__apellidos = apellidos