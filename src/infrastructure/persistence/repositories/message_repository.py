from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.message import Message
from src.domain.repositories.message_repository import IMessageRepository
from src.domain.value_objects.ticket_id import TicketID
from src.infrastructure.persistence.models import MessageORM


class SqlAlchemyMessageRepository(IMessageRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, message: Message) -> None:
        model = MessageORM()
        model.ticket_id = message.ticket_id.value
        model.text_ = message.text
        model.created_at = datetime.now(UTC)
        model.user_id = message.user_id.value

        self.session.add(model)
        self.session.commit()

    def get_by_ticket_id(self, ticket_id: TicketID) -> list[Message]:
        stmt = (
            select(MessageORM)
            .where(MessageORM.ticket_id == ticket_id.value)
            .order_by(MessageORM.created_at.asc())
        )
        res = self.session.scalars(stmt)

        return list(res)
