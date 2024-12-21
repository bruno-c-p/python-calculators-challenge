from typing import Dict
from .http_unprocesable_entity import HttpUnprocessableEntityError
from .http_bad_request import HttpBadRequestError

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, HttpUnprocessableEntityError):
        return {"message": str(error)}, 422
    if isinstance(error, HttpBadRequestError):
        return {"message": str(error)}, 400
    return {"message": str(error)}, 500