from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine("sqlite:///database.db", echo=True)

SQLModel.metadata.create_all(engine)

hero1 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")

with Session(engine) as session:
    # Insere o herói no banco
    session.add(hero1)
    session.commit()

    # Consulta
    statement = select(Hero)
    results = session.exec(statement)
    for hero in results:
        print(hero)