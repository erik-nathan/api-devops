class Config(object):
    DEBUG = True
    TESTING = True

class Production(Config):
    DEBUG = False

class Testing(Config):
    TESTING = True

class Development(Config):
    DEBUG = True