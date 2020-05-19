from abc import ABC, abstractmethod

import simplejson


class BaseHttpCall(ABC):

    @abstractmethod
    def make_call(self):
        pass

    def run(self):
        try:
            r = self.make_call()
        except Exception as exc:
            return self.process_request_exception(exc)
        return self.process_response(r)

    def process_response(self, response):
        success = response.status_code >= 200 and response.status_code < 300
        try:
            return success, response.json()
        except (AttributeError, simplejson.JSONDecodeError):
            return success, {}

    def process_request_exception(self, exc):
        return False, {}
