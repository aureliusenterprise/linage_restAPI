import asyncio
import logging
from flask import request
from flask_restx import Resource
from m4i_atlas_core import create_entities, get_entities_by_type_name

from .kubernetes_service_process_model import KubernetesServiceProcess
from .kubernetes_service_process_serializers import \
    m4i_kubernetes_service_process_model as kubernetes_service_process_serializer
from ... import output_filter_functions, m4i_output_model, m4i_output_get_model, api

"""
Defining kubernetes_service_process, (Kafka to Elastic) NameSpace
"""
log = logging.getLogger(__name__)
ns = api.namespace('process/kubernetes_service_process', description='Kubernetes Service Process')


@ns.route("/")
class kubernetes_service_process_Class(Resource):

    @api.response(200, 'Kubernetes Service Process Entities in Atlas')
    @api.response(400, 'Kubernetes Service Process is not Defined in Atlas')
    @api.doc(id='get_kubernetes_service_process_entities')
    @api.marshal_with(m4i_output_get_model)
    def get(self):
        """
        Returns list of Kubernetes Service Entities
        """
        search_result = asyncio.run(get_entities_by_type_name("m4i_kubernetes_service_process"))
        transformed_response = output_filter_functions.transform_get_response(search_result)
        return transformed_response, 200

    @api.response(200, 'Kubernetes Service Process Entity successfully created.')
    @api.response(500, "ValueError")
    @api.expect(kubernetes_service_process_serializer, validate=True)
    @api.doc(id='post_kubernetes_service_process_entities')
    @api.marshal_with(m4i_output_model)
    def post(self):
        """
        Creates a new Kubernetes Service Process Entity.
        """
        obj = KubernetesServiceProcess.from_dict(request.json)
        entity = obj.convert_to_atlas()
        data_read_response = asyncio.run(create_entities(entity))
        transformed_response = output_filter_functions.transform_post_response(data_read_response)
        return transformed_response, 200
