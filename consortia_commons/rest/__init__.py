from enum import IntEnum, Enum
from flask import request, abort, make_response, Response
from typing import Union


class StatusCodes(IntEnum):
    OK = 200
    OK_PARTIAL = 207
    BAD_REQUEST = 400
    NOT_FOUND = 404
    UNACCEPTABLE = 406
    SERVER_ERR = 500
    FORBIDDEN = 403
    UNAUTHORIZED = 401


class StatusMsgs(str, Enum):
    OK = 'OK'
    OK_PARTIAL = 'Partial Success'
    BAD_REQUEST = 'Bad Request'
    NOT_FOUND = 'Not Found'
    UNACCEPTABLE = 'Unacceptable Request'
    SERVER_ERR = 'Internal Server Error'
    FORBIDDEN = 'Forbidden'
    UNAUTHORIZED = 'Unauthorized'


def is_json_request():
    return request.content_type == 'application/json'


def rest_server_err(e, dict_only: bool = False) -> Union[dict, Response]:
    response = rest_response(StatusCodes.SERVER_ERR, StatusMsgs.SERVER_ERR, f"{e}", True)
    return _rest_return(response, dict_only)


def rest_ok(desc, dict_only: bool = False) -> Union[dict, Response]:
    response = rest_response(StatusCodes.OK, StatusMsgs.OK, desc, True)
    return _rest_return(response, dict_only)


def rest_bad_req(desc, dict_only: bool = False) -> Union[dict, Response]:
    response = rest_response(StatusCodes.BAD_REQUEST, StatusMsgs.BAD_REQUEST, desc, True)
    return _rest_return(response, dict_only)


def rest_not_found(desc, dict_only: bool = False) -> Union[dict, Response]:
    response = rest_response(StatusCodes.NOT_FOUND, StatusMsgs.NOT_FOUND, desc, True)
    return _rest_return(response, dict_only)


def rest_forbidden(desc, dict_only: bool = False) -> Union[dict, Response]:
    response = rest_response(StatusCodes.FORBIDDEN, StatusMsgs.FORBIDDEN, desc, True)
    return _rest_return(response, dict_only)


def rest_unauthorized(desc, dict_only: bool = False) -> Union[dict, Response]:
    response = rest_response(StatusCodes.UNAUTHORIZED, StatusMsgs.UNAUTHORIZED, desc, True)
    return _rest_return(response, dict_only)


def _rest_return(response, dict_only: bool = False) -> Union[dict, Response]:
    return response if dict_only is True else full_response(response)


def rest_response(code: StatusCodes, name: str, desc, dict_only: bool = False) -> Union[dict, Response]:
    response = {
        'code': code,
        'name': name,
        'description': desc
    }
    return response if dict_only is True else full_response(response)


def full_response(response: dict) -> Response:
    return make_response(response, int(response.get('code')), get_json_header())


def get_json_header(headers: dict = None) -> dict:
    if headers is None:
        headers = {}
    headers["Content-Type"] = "application/json"
    return headers


def abort_bad_req(desc):
    abort(StatusCodes.BAD_REQUEST, description=desc)


def abort_internal_err(desc):
    abort(StatusCodes.SERVER_ERR, description=desc)


def abort_not_found(desc):
    abort(StatusCodes.NOT_FOUND, description=desc)


def abort_forbidden(desc):
    abort(StatusCodes.FORBIDDEN, description=desc)


def abort_unauthorized(desc):
    abort(StatusCodes.UNAUTHORIZED, description=desc)

