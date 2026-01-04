from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from project_manager.core.database import Base

"""
Caracteristicas del usuario y consideraciones a futuro
Este por ahora solamente contara con username para identificar los projectos relacionados al usuario

A futuro se espera lograr implementar contraseña la cual cifre los proyectos, eso para mayor privacidad

"""

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)

    projects = relationship(
        "Project", 
        back_populates='user', 
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'<User id={self.id} username="{self.username}">'  