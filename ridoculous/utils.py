import os
import sys
import importlib.util

from typing import Any, Callable, Union

def defaultattr(obj: object, attribute: str, default: Any= None):
    if not hasattr(obj, attribute):
        setattr(obj, attribute, default)
    return getattr(obj, attribute)

def import_from_filepath(filepath: str) -> Union[Callable, None]:
    """Import module and return instance of given function name

    Arguments:
        dotpath {str} -- the dotpath for the import
        name {str} -- the method name to import

    Returns:
        Callable -- method attribute of import
    """
    '''
    base, name = '.'.join(filepath.split('.')[:-1]), filepath.split('.')[-1]
    print(f'base: {base!r}, name: {name!r}')
    if name:
        module = __import__(base, fromlist=[name])
    else:
        module = __import__(base)
    if module:
        return module
    return None
    '''
    spec = importlib.util.find_spec(filepath)
    if spec:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return None


def load_modules_from_directory(directory: str):
    module_paths = [
        ''.join(
            os.path.join(
                root, f).replace(directory, '').replace('.py', '').replace('__init__', '').replace('/', '.')[1:])
        for root, dirs, files in os.walk(directory)
        if '__init__.py' in files
        for f in files
        if f.endswith('.py')
    ]
    sys.path.append(directory)
    modules = [import_from_filepath(fp) for fp in reversed(sorted(module_paths, key=len))]
    return [m for m in modules if m]
