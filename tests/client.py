from flask import json, Response
from werkzeug.utils import cached_property


class ApiTestingResponse(Response):

    @cached_property
    def json(self):
        assert self.mimetype == 'application/json'
        return json.loads(self.data)
