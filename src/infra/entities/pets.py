import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from src.infra.configs import Base


class AnimalTypes(enum.Enum):
    """Define animal types."""

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    """Pets entity."""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        """Repr."""
        return f"""Pet: [name={self.name}, specie={self.specie},
        user_id={self.user_id}]"""

    def __eq__(self, other):
        """Eq."""
        if (
            (self.id == other.id)
            and (self.name == other.name)
            and (self.specie == other.specie)
            and (self.age == other.age)
            and (self.user_id == other.user_id)
        ):
            return True
        return False
