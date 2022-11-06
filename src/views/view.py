import importlib

def load_view(path, result={}):
    actual_path = 'src.views.' + '.'.join(path.split('/'))
    module = importlib.import_module(actual_path)
    return module.load(result)