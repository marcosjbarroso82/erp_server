from rest_framework.serializers import ModelSerializer

AVAILABLE_CONFIGS_FIELD = ('fields', 'read_only_fields', 'exclude', 'write_only_fields')


class BaseModelSerializer(ModelSerializer):

    def __init__(self, *args, **kwargs):
        if kwargs.get('context'):
            action = kwargs['context']['view'].action

            fields_config = getattr(self.Meta, 'fields_config')

            if fields_config and fields_config.get(action):
                custom_fields_by_action = fields_config.get(action)

                for key, value in custom_fields_by_action.items():
                    assert key in AVAILABLE_CONFIGS_FIELD, "The %s can't support" % key
                    setattr(self.Meta, key, value)

        super(BaseModelSerializer, self).__init__(*args, **kwargs)

    class Meta:
        abstract = True
