import os

class IBM:
    @staticmethod
    def getToken(var_name: str = 'apikey', default=None):
        """
        Retorna o valor de uma variável de ambiente.
        """
        value = os.getenv(var_name) 
        return value if value else os.environ.get(var_name, default)
        
    