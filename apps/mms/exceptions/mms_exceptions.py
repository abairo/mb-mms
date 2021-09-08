from mercadobitcoin.handlers.exception_base import ExceptionBase


class RangeOutOfLimit(ExceptionBase):
    error_message = 'Range fora do limite'
    status_code = 400
