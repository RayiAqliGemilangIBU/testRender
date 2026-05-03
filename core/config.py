from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Nilai default adalah database lokal (untuk development)
    # Jika di Environment Variable (Render) ada DATABASE_URL, maka nilai ini akan diganti otomatis
    DATABASE_URL: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()