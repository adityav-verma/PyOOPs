def singleton(_class):
    _instances = {}

    def wrapper(*args, **kwargs):
        if _class not in _instances:
            _instances[_class] = _class(*args, **kwargs)
        return _instances[_class]
    return wrapper
