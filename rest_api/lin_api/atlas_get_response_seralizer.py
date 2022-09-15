from flask_restx import fields

from rest_api.lin_api.restplus import api

m4i_output_get_model = api.model('model_output', {
    'entities': fields.Integer(required=True),
    'qualifiedNames': fields.List(fields.String(), required=True)
})
