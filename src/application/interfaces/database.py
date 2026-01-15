from abc import abstractmethod
from typing import Protocol


class DBSession(Protocol):
    @abstractmethod
    def commit(self) -> None: ...

    @abstractmethod
    def flush(self) -> None: ...

    @abstractmethod
    def rollback(self) -> None: ...
