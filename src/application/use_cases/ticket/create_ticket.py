from datetime import UTC, datetime

from src.domain.entities.message import Message
from src.domain.entities.ticket import Ticket
from src.domain.entities.user import User
from src.domain.repositories.message_repository import IMessageRepository
from src.domain.repositories.ticket_repository import ITicketRepository
from src.domain.repositories.user_repository import IUserRepository
from src.domain.value_objects.ticket_category import TicketCategory
from src.domain.value_objects.ticket_id import TicketID
from src.domain.value_objects.ticket_status import TicketStatus


class UserCreateTicketUseCase:
    def __init__(
        self,
        user_repo: IUserRepository,
        ticket_repo: ITicketRepository,
        message_repo: IMessageRepository,
    ) -> None:
        self.user_repo = user_repo
        self.ticket_repo = ticket_repo
        self.message_repo = message_repo

    def __call__(
        self, user: User, title: str, category_name: TicketCategory, text: str
    ) -> Ticket:
        status = TicketStatus.open_status()
        category = TicketCategory(category_name)
        ticket_id = TicketID.new()

        messages = []
        msg = Message.create(ticket_id=ticket_id, user_id=user.id, text=text)
        self.message_repo.save(msg)
        messages.append(msg)

        created_at = datetime.now(tz=UTC)
        ticket = Ticket(
            id=ticket_id,
            title=title,
            user_id=user.id,
            status=status,
            category=category,
            created_at=created_at,
            updated_at=created_at,
            resolution=None,
            closed_at=None,
            messages=messages,
            status_history=[],
        )
        self.ticket_repo.save(ticket=ticket)

        return ticket
