class InvalidPosition(Exception):
    def __init__(self, *args, **kwargs):
        super(InvalidPosition, self).__init__(*args, **kwargs)