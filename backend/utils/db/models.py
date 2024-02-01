import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Time, Date


class BaseModel(DeclarativeBase):
    pass

class Department(BaseModel):
    __tablename__ = "Department"

    id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    title: Mapped[str]
    employers: Mapped[list["User"]] = relationship(back_populates="department")


class User(BaseModel):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    username: Mapped[str] = mapped_column(String(60), unique=False)
    job_title: Mapped[str]
    department_id: Mapped[int] = mapped_column(ForeignKey("Department.id"))
    department: Mapped["Department"] = relationship(back_populates="employers")
    worklog: Mapped[list["Worklog"]] = relationship(back_populates='user')


class Worklog(BaseModel):
    __tablename__ = "Worklog"

    id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    start_time: Mapped[datetime.datetime] = mapped_column(Time)
    end_time: Mapped[datetime.datetime] = mapped_column(Time, nullable=True, default=None)
    date: Mapped[datetime.datetime] = mapped_column(Date)
    user_id: Mapped[int] =  mapped_column(ForeignKey("User.id"))
    comment: Mapped[str] = mapped_column(String(256), nullable=True)
    user: Mapped["User"] = relationship(back_populates='worklog')


class Admin(BaseModel):
    __tablename__ = 'User'

    id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    username: Mapped[str] = mapped_column(String(30), default='Admin')
    password: Mapped[str] = mapped_column(String(256), default='')