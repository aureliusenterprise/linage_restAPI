import asyncio
import logging
from flask import request
from flask_restx import Resource
from m4i_atlas_core import create_entities, get_entities_by_type_name

from .ingress_controller_process_model import IngressControllerProcess
from .ingress_controller_process_serializers import \
    m4i_ingress_controller_process_model as ingress_controller_process_serializer
from ... import output_filter_functions, m4i_output_model, m4i_output_get_model, api

"""
Defining ingress_controller_process, (Kafka to Elastic) NameSpace
"""
log = logging.getLogger(__name__)
ns = api.namespace('process/ingress_controller_process', description='Ingress Controller Process')


@ns.route("/")
class ingress_controller_process_Class(Resource):

    @api.response(200, 'Ingress Controller Process Entities in Atlas')
    @api.response(400, 'Ingress Controller Process is not Defined in Atlas')
    @api.doc(id='get_ingress_controller_process_entities')
    @api.marshal_with(m4i_output_get_model)
    def get(self):
        """
        Returns list of Ingress Controller Entities
        """
        search_result = asyncio.run(get_entities_by_type_name("m4i_ingress_controller_process"))
        transformed_response = output_filter_functions.transform_get_response(search_result)
        return transformed_response, 200

    @api.response(200, 'Ingress Controller Process Entity successfully created.')
    @api.response(500, "ValueError")
    @api.expect(ingress_controller_process_serializer, validate=True)
    @api.doc(id='post_ingress_controller_process_entities')
    @api.marshal_with(m4i_output_model)
    def post(self):
        """
        Creates a new Ingress Controller Process Entity.
        """
        obj = IngressControllerProcess.from_dict(request.json)
        entity = obj.convert_to_atlas()
        data_read_response = asyncio.run(create_entities(entity))
        transformed_response = output_filter_functions.transform_post_response(data_read_response)
        return transformed_response, 200
