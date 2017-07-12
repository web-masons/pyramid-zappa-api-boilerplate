import datetime
from marshmallow import Schema
from pyramid.renderers import JSON


class RenderSchema(Schema):
    """
    Schema to prevent marshmallow from using its default type mappings.

    We use this schema for rendering output: For those cases we don't want
    marshmallow's default type mappings. We want Pyramid's JSON-rendering
    functionality instead, where we already have some json-adapers.
    """
    TYPE_MAPPING = {}


def custom_json_renderer():
    """
    Return a custom json renderer that can deal with some datetime objects.
    """
    def datetime_adapter(obj, request):
        return obj.isoformat()

    def time_adapter(obj, request):
        return str(obj)

    json_renderer = JSON()
    json_renderer.add_adapter(datetime.datetime, datetime_adapter)
    json_renderer.add_adapter(datetime.time, time_adapter)
    return json_renderer
