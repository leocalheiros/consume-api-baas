from ..views.http_types.http_response import HttpResponse
from .types.http_not_found import HttpNotFoundError
from .types.http_unprocessable_entity import HttpUnprocessableEntityError
from .types.http_bad_request import HttpBadRequest
from .types.http_unauthorized import HttpUnauthorizedError
from .types.http_invalid_action import HttpInvalidActionError
from .types.http_invalid_type import HttpInvalidTypeError


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpUnprocessableEntityError, HttpBadRequest, HttpUnauthorizedError,
                          HttpInvalidActionError, HttpInvalidTypeError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
