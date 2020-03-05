import inspect
import re

from typing import List, NamedTuple

class BaseFunctionRDoc(object):
    name: str
    sig: str
    doc: str
    link: str
    toc_str: str
    markdown: str

    def __init__(self, obj: object= None):
        if not inspect.isfunction(obj):
            raise TypeError(f'{obj!r} is not a function')

        name = re.findall("function (.*) at", str(obj))
        self.name = name[0] if len(name) > 0 else None
        self.sig = str(inspect.signature(obj))
        self.doc = obj.__doc__
        self.link = f'{self.name}_{str(self.name.__hash__()).replace("-","")}'
        self.toc_str = f'- [ {self.name} ](#{self.link})\n'
        self.markdown = f'<a name="{self.link}"></a>\n#### `{self.name}{self.sig}`\n\n{self.doc}\n\n'

    @classmethod
    def get_functions_from_object(cls, obj: object= None):
        functions = []
        if obj:
            for a in dir(obj):
                attr = getattr(obj, a)
                if inspect.isfunction(attr) and obj.__name__ in str(attr):
                    functions.append(cls(attr))
        return functions

    def __repr__(self):
        return str(self.markdown)

    def __str__(self):
        return str(self.markdown)


class BaseClassRDoc(object):
    name: str
    sig: str
    doc: str
    toc_str: str
    link: str
    functions: List[BaseFunctionRDoc]
    markdown: str

    def __init__(self, obj: object = None):
        if not inspect.isclass(obj):
            raise TypeError(f'{obj!r} is not a class')

        name = re.findall("\'(.*)\'", str(obj))
        self.name = name[0] if len(name) > 0 else None
        self.sig = str(inspect.signature(getattr(obj, '__init__')))
        self.doc = obj.__doc__
        self.link = f'{self.name}_{str(self.name.__hash__()).replace("-", "")}'
        self.toc_str = f'- [ {self.name} ](#{self.link})\n'
        self.markdown = f'<a name="{self.link}"></a>\n### {self.name}{self.sig}\n\n{self.doc}\n\n'
        self.functions = BaseFunctionRDoc.get_functions_from_object(obj)

    @classmethod
    def get_classes_from_object(cls, obj: object= None):
        classes = []
        if obj:
            for a in dir(obj):
                attr = getattr(obj, a)
                if inspect.isclass(attr) and obj.__name__ in str(attr):
                    classes.append(cls(attr))
        return classes

    def __repr__(self):
        return str(self.markdown)

    def __str__(self):
        return str(self.markdown)


class BaseModuleRDoc(object):
    name: str
    link: str
    toc_str: str
    classes: List[BaseClassRDoc]
    functions: List[BaseFunctionRDoc]
    markdown: str

    def __init__(self, obj: object = None):
        if not inspect.ismodule(obj):
            raise TypeError(f'{obj!r} is not a module')
        self.name = obj.__name__
        self.link = f'{self.name}_{str(self.name.__hash__()).replace("-", "")}'
        self.toc_str = f'- [ {self.name} ](#{self.link})\n'
        self.markdown = f'<a name="{self.link}"></a>\n## {self.name}\n\n'
        self.classes = BaseClassRDoc.get_classes_from_object(obj)
        self.functions = BaseFunctionRDoc.get_functions_from_object(obj)

    @classmethod
    def get_modules_from_object(cls, obj: object= None):
        modules = []
        if obj:
            for a in dir(obj):
                attr = getattr(obj, a)
                if inspect.ismodule(attr) and obj.__name__ in str(attr):
                    modules.append(cls(attr))
        return modules

    def get_rdoc_list(self):
        rdocs = [self.markdown]
        if self.functions:
            rdocs.extend(self.functions)
        if self.classes:
            for c in self.classes:
                rdocs.append(c)
                if c.functions:
                    rdocs.extend(c.functions)
        return rdocs

    def __repr__(self):
        return str(self.markdown)

    def __str__(self):
        return str(self.markdown)

class RDocObject(NamedTuple):
    name: str
    modules: List[BaseModuleRDoc]

class Ridoculous(object):
    objects: List[object]
    rdoc_objects: List[RDocObject]
    docs: list

    def __init__(self, objects: List[object] = None):
        self.objects = [objects] if not isinstance(objects, list) else objects
        if self.objects:
            self.rdoc_objects = [
                RDocObject(obj.__name__, BaseModuleRDoc.get_modules_from_object(obj))
                for obj in self.objects]
        self.docs = [str(rd) for rd in self.make_doc_list()]

    def make_doc_list(self):
        docs = []

        #build Table of Contents
        for o in self.rdoc_objects:
            for m in o.modules:
                if m.functions or m.classes:
                    docs.append(m.toc_str)
                    for f in m.functions:
                        docs.append('\t' + f.toc_str)
                    for c in m.classes:
                        docs.append('\t'+c.toc_str)
                        for f in c.functions:
                            docs.append('\t\t'+f.toc_str)
        docs.append('\n\n')
        #build object docs
        for o in self.rdoc_objects:
            for m in o.modules:
                if m.functions or m.classes:
                    docs.append(m)
                    for f in m.functions:
                        docs.append(f)
                    for c in m.classes:
                        docs.append(c)
                        for f in c.functions:
                            docs.append(f)
        return docs

    def write(self, filename: str= 'GENERATED_README.md'):
        with open(filename, 'w') as fout:
            fout.write(''.join(self.docs))

    @classmethod
    def makedocs(cls, objs: List[object]= None, filename: str= 'GENERATED_README.md'):
        return cls(objs).write(filename)