from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship 
from project_manager.core.database import Base
from project_manager.models.enums import PriorityEnum

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    description = Column(Text)

    priority = Column(
       Enum(PriorityEnum), 
       default=PriorityEnum.MEDIA,
       nullable=False 
    )

    finished = Column(Boolean, default=False, nullable=False)

    user_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )

    user = relationship(
        'User', 
        back_populates='projects'
    )

    task = relationship(
        'Task', 
        back_populates='project', 
        cascade='all, delete-orphan'
    )

    