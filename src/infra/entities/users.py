from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.configs import Base


class Users(Base):
    """Users entity."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id_pet = relationship("Pets")

    def __repr__(self):
        """Repr."""
        return f"User [name={self.name}]"

    def __eq__(self, other):
        """Eq."""
        if (
            (self.id == other.id)
            and (self.name == other.name)
            and (self.password == other.password)
        ):
            return True
        return False
