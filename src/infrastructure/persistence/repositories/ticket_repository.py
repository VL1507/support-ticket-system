from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.ticket import Ticket
from src.domain.repositories.ticket_repository import ITicketRepository
from src.domain.value_objects.ticket_id import TicketID
from src.domain.value_objects.ticket_status import TicketStatus
from src.domain.value_objects.user_id import UserID
from src.infrastructure.persistence.models import TicketORM, TicketStatusORM


class SqlAlchemyTicketRepository(ITicketRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(self, ticket_id: TicketID) -> Ticket | None:
        stmt = select(TicketORM).where(TicketORM.id == ticket_id.value)
        return self.session.scalar(stmt)

    def save(self, ticket: Ticket) -> None:
        ticket_status_id = self.session.scalar(
            select(TicketStatusORM).where(
                TicketStatusORM.name == ticket.status.name
            )
        )
        if ticket_status_id is None:
            raise Exception("ticket_status_id is None")

        model = TicketORM()
        model.id = ticket.id.value
        model.title = ticket.title
        model.user_id = ticket.user_id.value
        model.ticket_status_id = ticket_status_id
        model.resolution_text = ticket.resolution
        model.closed_at = ticket.closed_at

        self.session.add(model)
        self.session.commit()

    def find_by_user(self, user_id: UserID) -> list[Ticket]:
        stmt = select(TicketORM).where(TicketORM.user_id == user_id.value)
        return list(self.session.scalars(stmt))

    def find_all_open(self) -> list[Ticket]:
        stmt = (
            select(TicketORM)
            .join(TicketStatusORM)
            .where(TicketStatusORM.is_closed.is_(False))
        )
        return list(self.session.scalars(stmt))

    def change_status(
        self,
        ticket_id: TicketID,
        new_status: TicketStatus,
        changed_by: UserID,
        comment: str | None = None,
    ) -> bool: ...
