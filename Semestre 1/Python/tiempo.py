import time

class rendimiento():
    __start=None
    __end=None

    def __init__(self) -> None:
        pass

    def __iniciar(self):
        self.__start = time.time()
    
    def __terminar(self):
        self.__end = time.time()

    def medir_tiempo(self,func):
        self.__iniciar()
        func()
        self.__terminar()
        return(self.__end - self.__start)