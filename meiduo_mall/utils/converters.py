from django.urls import converters


class UsernameConverter:

    regex = r'^[a-zA-Z0-9_-]{5,20}_-'

    def to_python(self, value):
        return value