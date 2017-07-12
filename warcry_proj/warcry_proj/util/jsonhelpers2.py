"""
Duplicated from jsonhelpers so you can see the integration of
SchemaJsonRenderer separately.
"""

import datetime
from marshmallow import Schema
from pyramid.httpexceptions import HTTPInternalServerError
from pyramid.renderers import JSON


class SchemaJsonRenderer(JSON):
    """
    Extends Pyramid's JSON renderer with marshmallow-serialization.

    When a view-method defines a marshmallow Schema as request.render_schema,
    that schema will be used for serializing the return value.
    """

    def __call__(self, info):
        """
        If a schema is present, replace value with output from schema.dump(..).
        """
        original_render = super().__call__(info)

        def schema_render(value, system):
            request = system.get('request')
            if (request is not None and isinstance(getattr(request, 'render_schema', None), Schema)):
                try:
                    value, errors = request.render_schema.dump(value)
                except Exception:
                    errors = True

                if errors:
                    raise HTTPInternalServerError(body="Serialization failed.")

            return original_render(value, system)

        return schema_render


def custom_json_renderer2():
    """
    Return a custom json renderer that can deal with some datetime objects.
    """
    def datetime_adapter(obj, request):
        return obj.isoformat()

    def time_adapter(obj, request):
        return str(obj)

    json_renderer = SchemaJsonRenderer()
    json_renderer.add_adapter(datetime.datetime, datetime_adapter)
    json_renderer.add_adapter(datetime.time, time_adapter)
    return json_renderer
