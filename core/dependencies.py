from database import SessionLocal

def get_db():              #closes db connection at each session
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
