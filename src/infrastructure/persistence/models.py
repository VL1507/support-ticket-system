import datetime
import uuid

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKeyConstraint,
    Index,
    Integer,
    PrimaryKeyConstraint,
    String,
    Text,
    UniqueConstraint,
    Uuid,
    text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class RoleORM(Base):
    __tablename__ = "Role"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="Role_pkey"),
        UniqueConstraint("name", name="Role_name_key"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    User: Mapped[list["UserORM"]] = relationship(
        "UserORM", back_populates="role"
    )


class TicketCategoryORM(Base):
    __tablename__ = "TicketCategory"
    __table_args__ = (PrimaryKeyConstraint("id", name="TicketCategory_pkey"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    Ticket: Mapped[list["TicketORM"]] = relationship(
        "TicketORM", back_populates="ticket_category"
    )


class TicketStatusORM(Base):
    __tablename__ = "TicketStatus"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="TicketStatus_pkey"),
        UniqueConstraint("name", name="TicketStatus_name_key"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_closed: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("false")
    )

    Ticket: Mapped[list["TicketORM"]] = relationship(
        "TicketORM", back_populates="ticket_status"
    )
    TicketStatusHistory: Mapped[list["TicketStatusHistoryORM"]] = relationship(
        "TicketStatusHistoryORM",
        foreign_keys="[TicketStatusHistoryORM.from_status_id]",
        back_populates="from_status",
    )
    TicketStatusHistory_: Mapped[list["TicketStatusHistoryORM"]] = (
        relationship(
            "TicketStatusHistoryORM",
            foreign_keys="[TicketStatusHistoryORM.to_status_id]",
            back_populates="to_status",
        )
    )


class UserORM(Base):
    __tablename__ = "User"
    __table_args__ = (
        ForeignKeyConstraint(
            ["role_id"], ["Role.id"], name="User_role_id_fkey"
        ),
        PrimaryKeyConstraint("id", name="User_pkey"),
        UniqueConstraint("login", name="User_login_key"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    login: Mapped[str] = mapped_column(String(255), nullable=False)
    hash_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role_id: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )

    role: Mapped["RoleORM"] = relationship("RoleORM", back_populates="User")
    Ticket: Mapped[list["TicketORM"]] = relationship(
        "TicketORM", back_populates="user"
    )
    Message: Mapped[list["MessageORM"]] = relationship(
        "MessageORM", back_populates="user"
    )
    TicketStatusHistory: Mapped[list["TicketStatusHistoryORM"]] = relationship(
        "TicketStatusHistoryORM", back_populates="changed_by_user"
    )


class TicketORM(Base):
    __tablename__ = "Ticket"
    __table_args__ = (
        ForeignKeyConstraint(
            ["ticket_category_id"],
            ["TicketCategory.id"],
            name="Ticket_ticket_category_id_fkey",
        ),
        ForeignKeyConstraint(
            ["ticket_status_id"],
            ["TicketStatus.id"],
            name="Ticket_ticket_status_id_fkey",
        ),
        ForeignKeyConstraint(
            ["user_id"], ["User.id"], name="Ticket_user_id_fkey"
        ),
        PrimaryKeyConstraint("id", name="Ticket_pkey"),
        Index("Ticket_index_0", "user_id"),
        Index("Ticket_index_1", "created_at"),
        Index("Ticket_index_2", "updated_at"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    ticket_status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    ticket_category_id: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )
    resolution_text: Mapped[str | None] = mapped_column(Text)
    closed_at: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True)
    )

    ticket_category: Mapped["TicketCategoryORM"] = relationship(
        "TicketCategoryORM", back_populates="Ticket"
    )
    ticket_status: Mapped["TicketStatusORM"] = relationship(
        "TicketStatusORM", back_populates="Ticket"
    )
    user: Mapped["UserORM"] = relationship("UserORM", back_populates="Ticket")
    Message: Mapped[list["MessageORM"]] = relationship(
        "MessageORM", back_populates="ticket"
    )
    TicketStatusHistory: Mapped[list["TicketStatusHistoryORM"]] = relationship(
        "TicketStatusHistoryORM", back_populates="ticket"
    )


class MessageORM(Base):
    __tablename__ = "Message"
    __table_args__ = (
        ForeignKeyConstraint(
            ["ticket_id"], ["Ticket.id"], name="Message_ticket_id_fkey"
        ),
        ForeignKeyConstraint(
            ["user_id"], ["User.id"], name="Message_user_id_fkey"
        ),
        PrimaryKeyConstraint("id", name="Message_pkey"),
        Index("Message_index_0", "ticket_id"),
        Index("Message_index_1", "created_at"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticket_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    text_: Mapped[str] = mapped_column("text", Text, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)

    ticket: Mapped["TicketORM"] = relationship(
        "TicketORM", back_populates="Message"
    )
    user: Mapped["UserORM"] = relationship("UserORM", back_populates="Message")


class TicketStatusHistoryORM(Base):
    __tablename__ = "TicketStatusHistory"
    __table_args__ = (
        ForeignKeyConstraint(
            ["changed_by_user_id"],
            ["User.id"],
            name="TicketStatusHistory_changed_by_user_id_fkey",
        ),
        ForeignKeyConstraint(
            ["from_status_id"],
            ["TicketStatus.id"],
            name="TicketStatusHistory_from_status_id_fkey",
        ),
        ForeignKeyConstraint(
            ["ticket_id"],
            ["Ticket.id"],
            name="TicketStatusHistory_ticket_id_fkey",
        ),
        ForeignKeyConstraint(
            ["to_status_id"],
            ["TicketStatus.id"],
            name="TicketStatusHistory_to_status_id_fkey",
        ),
        PrimaryKeyConstraint("id", name="TicketStatusHistory_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticket_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    from_status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    to_status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    changed_by_user_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    changed_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=text("now()")
    )
    comment: Mapped[str | None] = mapped_column(Text)

    changed_by_user: Mapped["UserORM"] = relationship(
        "UserORM", back_populates="TicketStatusHistory"
    )
    from_status: Mapped["TicketStatusORM"] = relationship(
        "TicketStatusORM",
        foreign_keys=[from_status_id],
        back_populates="TicketStatusHistory",
    )
    ticket: Mapped["TicketORM"] = relationship(
        "TicketORM", back_populates="TicketStatusHistory"
    )
    to_status: Mapped["TicketStatusORM"] = relationship(
        "TicketStatusORM",
        foreign_keys=[to_status_id],
        back_populates="TicketStatusHistory_",
    )
