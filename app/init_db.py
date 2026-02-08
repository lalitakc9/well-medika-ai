from app.db import engine, Base

def init():
    Base.metadata.create_all(bind=engine)
    print("DB initialized successfully")

if __name__ == "__main__":
    init()