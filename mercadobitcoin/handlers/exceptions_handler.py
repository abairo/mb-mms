from rest_framework.views import exception_handler
from mercadobitcoin.handlers.exception_base import ExceptionBase
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, ExceptionBase):
        return Response({"error": exc.error_message}, status=exc.status_code)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response
