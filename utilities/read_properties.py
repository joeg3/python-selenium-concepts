import configparser

config = configparser.RawConfigParser()
config.read("./configuration/config.ini")

class ReadConfig():
    
    @staticmethod
    def getApplicationURL():
        url = config.get("common data", "base_url")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common data", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common data", "password")
        return password