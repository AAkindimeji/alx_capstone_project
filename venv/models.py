from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'  # Specify the table name

    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    surname = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    message = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Contact {self.first_name} {self.surname}>"
