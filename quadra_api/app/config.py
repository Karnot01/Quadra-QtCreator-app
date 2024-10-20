class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:kemakosuli01946@172.30.128.1:5432/quadra'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '3d5cc4c36ee75febd8c3dd06ed515c56' # Falta sacar la secret key para quadra esta es secret key de la otra app
    JWT_ALGORITHM = 'HS256'