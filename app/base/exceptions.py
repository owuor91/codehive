class HttpError(Exception):
    error_code = "BAD_REQUEST"
    status_code = 400


class DatabaseError(Exception):
    error_code = "DATABASE_ERROR"
    status_code = 500
