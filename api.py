from flask import request
from flask.ext.restful import Resource, Api
from werkzeug.exceptions import HTTPException

from database import Document


class NotFound(HTTPException):
    code = 404
    data = {}


class DocumentsApi(Api):
    
    def init_app(self, app):
        super(DocumentsApi, self).init_app(app)
        app.after_request(self.add_cors_headers)

    def add_cors_headers(self, response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response


class DocumentsResource(Resource):
    default_length = 100

    def get(self, document_id=None):
        if document_id:
            return self.get_one(document_id)
        return self.get_list()

    def get_one(self, document_id):
        document = Document.query.get(document_id)
        return document.as_dict()

    def get_list(self):
        query = self.paginate(Document.query)
        documents = [row.as_dict() for row in query]
        return documents

    def paginate(self, query):
        offset = int(request.args.get('start', 0))
        limit = int(request.args.get('length', self.default_length))
        if offset < 0 or limit < 0:
            raise NotFound()
        entries = query.limit(limit).offset(offset).all()
        if not entries:
            raise NotFound()

        return entries


api = DocumentsApi()
api.add_resource(DocumentsResource, '/documents/<int:document_id>', '/documents')
