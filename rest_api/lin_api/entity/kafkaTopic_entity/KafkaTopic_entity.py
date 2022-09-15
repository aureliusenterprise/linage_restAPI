import asyncio
import logging
from flask import request
from flask_restx import Resource
from m4i_atlas_core import (create_entities, get_entities_by_type_name)

from .m4i_kafkaTopic_entity_serializers import m4i_kafkaTopic_entity_model as kafkaTopic_entity_serializer
from .model.KafkaTopicApiModel import KafkaTopicApiModel
from ... import output_filter_functions, m4i_output_model, m4i_output_get_model, api

""" 
Defining kafkaTopic  Entity
"""
log = logging.getLogger(__name__)
ns = api.namespace('entity/kafkaTopic_entity', description='Operations related to the Kafka Topic Entity')


@ns.route("/")
class kafkaTopic_Class(Resource):
    @api.response(200, 'kafkaTopic Entities in Atlas')
    @api.response(400, 'kafkaTopic is not Defined in Atlas')
    @api.doc(id='get_kafkaTopic_entities')
    @api.marshal_with(m4i_output_get_model)
    def get(self):
        """
        Returns list of kafkaTopic Entities
        """
        search_result = asyncio.run(get_entities_by_type_name("m4i_kafka_topic"))
        transformed_response = output_filter_functions.transform_get_response(search_result)
        return transformed_response, 200

    @api.response(200, 'kafkaTopic Entity successfully created.')
    @api.response(500, "ValueError")
    @api.response(204, "Kafka Topic already Exists")
    @api.expect(kafkaTopic_entity_serializer)
    @api.doc(id='post_kafkaTopic_entities')
    @api.marshal_with(m4i_output_model)
    def post(self):
        """
        Creates a new kafkaTopic Entity.
        """
        obj = KafkaTopicApiModel.from_dict(request.json)
        entity, ref = obj.convert_to_atlas()
        data_read_response = asyncio.run(create_entities(*entity, referred_entities=ref))
        transformed_response = output_filter_functions.transform_post_response(data_read_response)
        return transformed_response, 200
