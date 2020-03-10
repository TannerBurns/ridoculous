import inspect
import re

from typing import List, NamedTuple

class FunctionRDoc(object):
    """This class documents functions. The format will look like the following for a function. Link is used for a
    table of contents and the hash of the name is used to keep the links unique.

        Table of Contents String:
            - [ name ](#link)

        Markdown string:
            <a name="[link]"></a>
            #### [name]

                [docstring]

    """
    name: str
    sig: str
    doc: str
    link: str
    toc_str: str
    markdown: str

    def __init__(self, obj: object= None):
        """When a new `FunctionRDoc` is created, all attributes are set during init. First the `obj` that was passed
        will be verified as a function using the inspect library. The name will be found using a regex pattern,
        the signature is obtained using the inspect library, the docstring is copied and then the document attributes
        are created. The link is created to connect the table of contents to the header, the table of contents string
        is then created, and lastly the markdown for the function.

        Args:
            obj {object} -- object to document (should be a function)

        """
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
    def get_functions_from_object(cls, obj: object= None) -> list:
        """The given object will be searched for any functions and then return a list of the function as `FunctionRDoc`
        objects that have document attributes set.

        Args:
            obj {object} -- object to document

        return:
            list -- a list of FunctionRDoc objects created from the given object
        """
        functions = []
        if obj:
            for a in dir(obj):
                attr = getattr(obj, a)
                if inspect.isclass(obj):
                    if inspect.isfunction(attr) and obj.__name__ in str(attr):
                        functions.append(cls(attr))
                else:
                    if inspect.isfunction(attr):
                        functions.append(cls(attr))
        return functions

    def __repr__(self) -> str:
        """overloaded for ease of use, when class is printed, it will be the str of the markdown generated for the
        instance of `FunctionRDoc`
        """
        return str(self.markdown)

    def __str__(self) -> str:
        """overloaded for ease of use
        """
        return str(self.markdown)

class ClassRDoc(object):
    """This class documents class objects. The format will look like the following for a documented class. Link is
    used for a table of contents and the hash of the name is used to keep the links unique.

        Table of Contents String:
            - [ name ](#link)

        Markdown string:
            <a name="[link]"></a>
            #### [name]

                [docstring]

    """
    name: str
    sig: str
    doc: str
    toc_str: str
    link: str
    functions: List[FunctionRDoc]
    markdown: str

    def __init__(self, obj: object = None):
        """When a new `ClassRDoc` is created, all attributes are set during init. First the `obj` that was passed
        will be verified as a class object using the inspect library. The name will be found using a regex pattern,
        the signature is obtained using the inspect library, the docstring is copied and then the document attributes
        are created. The link is created to connect the table of contents to the header, the table of contents string
        is then created, and lastly the markdown for the class object.

        Args:
            obj {object} -- object to document (should be a function)

        """
        if not inspect.isclass(obj):
            raise TypeError(f'{obj!r} is not a class')

        name = re.findall("\'(.*)\'", str(obj))
        self.name = name[0] if len(name) > 0 else None
        self.sig = str(inspect.signature(getattr(obj, '__init__')))
        self.doc = obj.__doc__
        self.link = f'{self.name}_{str(self.name.__hash__()).replace("-", "")}'
        self.toc_str = f'- [ {self.name} ](#{self.link})\n'
        self.markdown = f'<a name="{self.link}"></a>\n### {self.name}{self.sig}\n\n{self.doc}\n\n'
        self.functions = FunctionRDoc.get_functions_from_object(obj)

    @classmethod
    def get_classes_from_object(cls, obj: object= None):
        """The given object will be searched for any classes and then return a list of classes as a list of `ClassRDoc`
        objects that have document attributes set.

        Args:
            obj {object} -- object to document

        return:
            list -- a list of ClassRDoc objects created from the given object
        """
        classes = []
        if obj:
            for a in dir(obj):
                attr = getattr(obj, a)
                if inspect.isclass(attr) and obj.__name__ in str(attr):
                    classes.append(cls(attr))
        return classes

    def __repr__(self):
        """overloaded for ease of use, when class is printed, it will be the str of the markdown generated for the
        instance of `ClassRDoc`
        """
        return str(self.markdown)

    def __str__(self):
        """overloaded for ease of use
        """
        return str(self.markdown)

class ModuleRDoc(object):
    """This class documents module objects. The format will look like the following for a module. Link is
    used for a table of contents and the hash of the name is used to keep the links unique.

        Table of Contents String:
            - [ name ](#link)

        Markdown string:
            <a name="[link]"></a>
            #### [name]

    """
    name: str
    link: str
    toc_str: str
    classes: List[ClassRDoc]
    functions: List[FunctionRDoc]
    markdown: str

    def __init__(self, obj: object = None):
        """When a new `ModuleRDoc` is created, all attributes are set during init. First the `obj` that was passed
        will be verified as a module using the inspect library. The name will be the `__name__` of the object.
        The link is created to connect the table of contents to the header, the table of contents string
        is then created, and lastly the markdown for the module.

        Args:
            obj {object} -- object to document

        """
        if not inspect.ismodule(obj):
            raise TypeError(f'{obj!r} is not a module')

        self.name = obj.__name__
        self.link = f'{self.name}_{str(self.name.__hash__()).replace("-", "")}'
        self.toc_str = f'- [ {self.name} ](#{self.link})\n'
        self.markdown = f'<a name="{self.link}"></a>\n## {self.name}\n\n'
        self.classes = ClassRDoc.get_classes_from_object(obj)
        self.functions = FunctionRDoc.get_functions_from_object(obj)

    @classmethod
    def get_modules_from_object(cls, obj: object= None):
        """The given object will be searched for any modules and then return a list of modules as a list of `ModuleRDoc`
        objects that have document attributes set.

        Args:
            obj {object} -- object to document

        return:
            list -- a list of ClassRDoc objects created from the given object
        """
        modules = []
        if obj:
            if inspect.ismodule(obj):
                modules.append(cls(obj))
            for a in dir(obj):
                attr = getattr(obj, a)
                if inspect.ismodule(attr) and obj.__name__ in str(attr):
                    modules.append(cls(attr))
        return modules


    def __repr__(self):
        """overloaded for ease of use, when class is printed, it will be the str of the markdown generated for the
        instance of `ModuleRDoc`
        """
        return str(self.markdown)

    def __str__(self):
        """overloaded for ease of use
        """
        return str(self.markdown)

class RDocObject(NamedTuple):
    """An `RDocObject` is a container object that is the starting object to document. The name will be taken
    from the initial object provided. It will then be walked to find any sub modules, classes, and functions inside the
    given module(s)

    Args:
        name {str} -- name of RDocObject
        modules {List[ModuleRDoc]} -- list holding the documented modules
    """
    name: str
    modules: List[ModuleRDoc]

class Ridoculous(object):
    """Ridoculous - making documentation for any python object
        The `Ridoculous` class is meant to take any object and document all modules, classes, and functions found
        inside that object. Ridoculous relies heavily on the code being documented using docstrings that are easy
        to read and understand. A table of contents that links to all the found objects will be creating along with
        the documents that were built.

        The goal of this utility is to help document code cleanly and quickly, that will then be used inside a readme
        or document to display the information found from the objects.

    """
    objects: List[object]
    rdoc_objects: List[RDocObject]
    docs: list

    def __init__(self, objects: List[object] = None):
        """The given list of objects will be parsed and ready to be documented. The list of strings that are written to
        the file are held in `.docs`. This is a raw version of what is dumped into the final output.

        Args:
            objects {List[object]} -- a list of object to document
        """
        self.objects = [objects] if not isinstance(objects, list) else objects
        if self.objects:
            self.rdoc_objects = [
                RDocObject(obj.__name__, ModuleRDoc.get_modules_from_object(obj))
                for obj in self.objects]
        self.docs = [str(rd) for rd in self.make_doc_list()]

    def make_doc_list(self):
        """creates the list of markdown strings to be help in `.docs`. firstly iterates over the RDocObjects and creates
        a table of contents, lastly reiterating over the RDocObjects and ordering the markdown

        return:
            list -- a list of markdown strings to be written in a file
        """
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
        """write `.docs` to a file

        Args:
            filename {str} -- the path of the filename to save the markdown as [default: GENERATED_README.md]

        """
        with open(filename, 'w') as fout:
            fout.write(''.join(self.docs))

    @classmethod
    def makedocs(cls, objs: List[object]= None, filename: str= 'GENERATED_README.md'):
        """makedocs is a quick class function to easily allow documenting objects in one line of python

        Args:
            objs {List[object]} -- a list of objects to quickly document
            filename {str} -- the path of the filename to save the markdown as [default: GENERATED_README.md]

        return:
            returns the parsed `Ridoculous` instance
        """
        new_cls = cls(objs)
        new_cls.write(filename)
        return new_cls