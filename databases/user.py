from sqlalchemy import create_engine,String
from sqlalchemy.orm import Mapped, mapped_column,DeclarativeBase,sessionmaker
from databases.session import engine
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100),unique=True)

Base.metadata.create_all(engine)

# user = User(
#     name="sundar",
#     email="sundar.rajan@bc.in"
# )

# insert
# db.add(user)
# db.commit()
# db.refresh(user)

# getAll
# users = db.query(User).all()
# for user in users:
#     print(user.id,user.name,user.email)

# getByID
# user = db.query(User).filter(User.id==1).first()
# print(user.name)

# updateById
# user.name = "max"
# db.commit()
# db.refresh(user)
# print(user.name)

# DeleteById
# db.delete(user)
# db.commit()
# print(user.name)

