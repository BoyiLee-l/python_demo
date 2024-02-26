from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

dbPath = "datafile.db"
engine = create_engine("sqlite:///%s" %dbPath)
metadata = MetaData(engine)
people = Table("people", metadata, Column("id", Integer, primary_key=True), Column("name", String), Column("count", Integer))
Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

# todo:insert
insert_statement = people.insert()
# session.execute(insert_statement, [
#     {"name": "Naleo", "count": 50},
#     {"name": "Abigail", "count": 40}
# ])
# session.commit()
# todo:update
session.execute(people.update().values(count=105).where(people.c.name == "duncan"))

# todo:search
result = session.execute(select([people]).where(people.c.name == "duncan"))
for row in result:
    print(row)