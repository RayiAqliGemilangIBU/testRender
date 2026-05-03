from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Nilai default adalah database lokal (untuk development)
    # Jika di Environment Variable (Render) ada DATABASE_URL, maka nilai ini akan diganti otomatis
    DATABASE_URL: str = "mysql://avnadmin:AVNS_GjhyxjVJeUW0aR1l5gj@mysql-3067baad-kaibcc25-3c13.h.aivencloud.com:14745/defaultdb?ssl-mode=REQUIRED"
    
    class Config:
        env_file = ".env"

settings = Settings()