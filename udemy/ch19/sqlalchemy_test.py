from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect

dbPath = "datafile.db"
engine = create_engine("sqlite:///%s" %dbPath)
metadata = MetaData(engine)
people = Table("people", metadata, Column("id", Integer, primary_key=True), Column("name", String), Column("count", Integer))

# todo:insert
# insert_statement = people.insert()
# session.execute(insert_statement, [
#     {"name": "Naleo", "count": 50},
#     {"name": "Abigail", "count": 40}
# ])
# session.commit()
# todo:update
# session.execute(people.update().values(count=105).where(people.c.name == "duncan"))
# todo:search
# result = session.execute(select([people]).where(people.c.name == "duncan"))
# for row in result:
#     print(row)

# todo:declarative_base
Base = declarative_base()

class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    count = Column("count", Integer)

Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

# new1 = People(name= "Jane", count=5)
# new2 = People(name= "Jared", count=51)
# new3 = People(name= "Keith", count=25)
# new4 = People(name= "Mark", count=55)
# session.add(new1)
# session.add(new2)
# session.add(new3)
# session.add(new4)

# jane = session.query(People).filter_by(name="Jane").first()
# session.delete(jane)
session.commit()

for r in session.query(People).all():
    print(r.id, r.name, r.count)

inspector = inspect(engine)
print(inspector.get_table_names())