class APIError(Exception):
    """Base para errores de negocio."""
    status_code = 400
    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)
        if status_code:
            self.status_code = status_code
        self.message = message

class NotFound(APIError):
    status_code = 404

class Unauthorized(APIError):
    status_code = 401