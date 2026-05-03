import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings  # Impor settings dari config.py

# Mengambil URL dari config
DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    # WAJIB: Aiven MySQL memerlukan SSL agar koneksi tidak ditolak
    connect_args={"ssl": {"ssl_mode": "REQUIRED"}}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()