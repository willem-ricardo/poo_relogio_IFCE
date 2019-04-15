class Hora:
    ### Construtor
    def __init__(self, h = 0, m = 0, s = 0):
        if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
            self.__hora = h
            self.__minuto = m
            self.__segundo = s
        else:
            self.__hora = 0
            self.__minuto = 0
            self.__segundo = 0
        
    ### Métodos de atribuição
    def set_hora(self, hora):
        if 0 <= hora <= 24:
            self.__hora = hora
            
    def set_minuto(self, minuto):
        if 0 <= minuto <= 59:
            self.__minuto = minuto
            
    def set_segundo(self, segundo):
        if 0 <= segundo <= 59:
            self.__segundo = segundo
            
    ### Métodos de exibição
    def get_hora(self):
        return self.__hora
    
    def get_minuto(self):
        return self.__minuto
    
    def get_segundo(self):
        return self.__segundo
    
    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(
            self.__hora,
            self.__minuto,
            self.__segundo)
    
    def str_12(self):
        return "{:02d}:{:02d}:{:02d} {:s}".format(
            12 if self.__hora == 0 or self.__hora == 12 else self.__hora % 12,
            self.__minuto,
            self.__segundo,
            "AM" if self.__hora < 12 else "PM")
    
    ### Métodos utilitários
    def mais_um_segundo(self):
        self.__segundo += 1
        
        if self.__segundo == 60:
            self.__segundo = 0
            self.__minuto += 1
            if self.__minuto == 60:
                self.__minuto = 0
                self.__hora += 1
                if self.__hora == 24:
                    self.__hora = 0     
            