from abc import ABC
import re
import logging
from rest_framework.views import exception_handler
from .messages import Messages
from .documents import ErrorDocument


logger = logging.getLogger(__name__)


def base_exception_handler(exc, context):
    logger.error("Exception occurred", exc_info=True)
    try:
        error_class = eval(exc.__class__.__name__)(exc, context)

        # saving error logs to mongoengine
        error = str(exc, context)
        ErrorDocument(error_detail=error).save()

    except NameError:
        error_class = Error(exc, context)
    return error_class.result()

class Error(ABC):

    def __init__(self, exc, context):
        self.translate = Messages.translate.value
        self.exc = exc
        self.context = context
        self.response = exception_handler(exc, context)

    def result(self):
        return self.response


class ValidationError(Error):
    pass


class IntegrityError(Error):
    pass


class PermissionDenied(Error):
    pass


class InvalidToken(Error):
    pass


class Http404(Error):
    pass


class Throttled(Error):
    
    def result(self):
        code = self.exc.get_codes()
        detail = self.response.data.pop('detail')
        time = re.findall(r'\d+', detail)[0]
        self.response.data['error'] = self.translate.get(
            code, detail).format(eval(time))
        return self.response


class MethodNotAllowed(Error):
    
    def result(self):
        code = self.exc.get_codes()
        detail = self.response.data.pop('detail')
        method = re.findall(r'\".+\"', detail)[0]
        self.response.data['error'] = self.translate.get(
            code, detail).format(eval(method))
        return self.response


class DoesNotExist(Error):
    pass


class TokenError(Error):
    pass
        
class NotAuthenticated(Error):
    pass

class ParseError(Error):
    pass

class AuthenticationFailed(Error):
    pass

class NotAuthenticated(Error):
    pass

class NotAcceptable(Error):
    pass

class UnsupportedMediaType(Error):
    pass


