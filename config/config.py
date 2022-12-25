import configparser


class Config:
    """ 
    project configuration 
    """

    @staticmethod
    def get(section, key):
        """ 
        class-method for parsing config.ini key-values 
        """
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        return config.get(section, key)