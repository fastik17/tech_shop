

class ListSerializerMixin:
    """Use this mixin to be able to define list_serializer_class that
    will be used only for list action"""
    list_serializer_class = None
    serializer_class = None

    def get_serializer_class(self):
        if not self.list_serializer_class:
            raise AttributeError("You must set 'list_serializer_class' in order to use ListSerializerMixin")
        if self.action == 'list':
            return self.list_serializer_class
        else:
            return super().get_serializer_class()
