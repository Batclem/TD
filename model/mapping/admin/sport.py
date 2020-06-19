from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint


class Sport(Base):
    __tablename__ = 'sports'
    __table_args__ = (UniqueConstraint('name'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    name = Column(String(50), nullable=False)
    id_coach = Column(String(36), nullable=True)


    def __repr__(self):
        return "<Sport(%s)>" % (self.name)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "id_coach": self.id_coach
        }
