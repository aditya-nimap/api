from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func


from core.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)

    full_name = Column(String(150), nullable=False)

    email = Column(String(225), unique=True, nullable=False, index=True)

    mobile_number = Column(String(20), unique=True, nullable=False, index=True)

    password_hash = Column(String, nullable=False)

    status = Column(String(20), default="active")

    profile_image = Column(String, nullable=True)

    last_login = Column(DateTime, nullable=True)

    created_at = Column(DateTime, server_default=func.now())

    updated_date = Column(DateTime, server_default=func.now(), onupdate=func.now())
