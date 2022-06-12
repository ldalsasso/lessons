from common.exceptions import BaseException


class InexistentUserException(BaseException):
    pass


class SameUserException(BaseException):
    pass
