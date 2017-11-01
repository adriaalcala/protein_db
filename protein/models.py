from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, ForeignKey, MetaData
from sqlalchemy.dialects.mysql import JSON, TEXT


_base_metadata = MetaData(
    naming_convention={
        "pk": "%(table_name)s_pk",
        "fk": "%(table_name)s_%(column_0_name)s_foreign",
        "ck": "%(table_name)s_%(constraint_name)s",
        "ix": '%(table_name)s_%(column_0_name)s_index',
        "uq": "%(table_name)s_%(column_0_name)s_unique",
    }
)
Base = declarative_base(metadata=_base_metadata)

class Protein(Base):
    __tablename__ = "proteins"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sequence= Column(TEXT, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    specie_id = Column(Integer, ForeignKey("species.id"), nullable=False)

class Specie(Base):
    __tablename__ = "species"
    id = Column(Integer, primary_key=True, autoincrement=True)
    short_label = Column(TEXT, nullable=True)
    tax_id = Column(Integer, nullable=True)
    full_name = Column(TEXT, nullable=True)

class Interactions(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    protein_id_1 = Column(ForeignKey("proteins.id"), nullable=False)
    protein_id_2 = Column(ForeignKey("proteins.id"), nullable=False)
    extra_data = Column(JSON, nullable=True)

