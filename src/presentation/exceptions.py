class PresentationError(Exception):
    """Base class for presentation exceptions"""


class NotAllFieldsAreFilledInError(PresentationError): ...
