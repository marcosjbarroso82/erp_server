from rest_framework.serializers import ModelSerializer


class BaseModelSerializer(ModelSerializer):

    def __init__(self, *args, **kwargs):
        if kwargs.get('context'):
            action = kwargs['context']['view'].action

            fields_config = getattr(self.Meta, 'fields_config')

            if fields_config and fields_config.get(action):
                custom_fields_by_action = fields_config.get(action)

                if custom_fields_by_action.get('fields'):
                    self.Meta.fields = custom_fields_by_action.get('fields')

                if custom_fields_by_action.get('read_only_fields'):
                    self.Meta.read_only_fields = custom_fields_by_action.get('read_only_fields')

                if custom_fields_by_action.get('exclude'):
                    self.Meta.exclude = custom_fields_by_action.get('exclude')

                if custom_fields_by_action.get('write_only_fields'):
                    self.Meta.write_only_fields = custom_fields_by_action.get('write_only_fields')
        super(BaseModelSerializer, self).__init__(*args, **kwargs)



    class Meta:
        abstract = True
