import os

class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # RenderのPostgres URLは "postgres://" で始まるがSQLAlchemyは "postgresql://" が必要
    _db_url = os.environ.get("DATABASE_URL", "sqlite:///memodb.sqlite")
    if _db_url.startswith("postgres://"):
        _db_url = _db_url.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = _db_url
