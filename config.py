# import os


class Config:
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://dellavia_api:powerapp@10.200.186.27/PowerApp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
