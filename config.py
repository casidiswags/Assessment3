class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///gym.db'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_gym.db'  # Used as a separate database for testing

class ProductionConfig(Config):
    pass
