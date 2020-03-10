# Ridoculous

    Easily document any python object to a linked table of contents and markdown

# Documentation

   The documentation below was generated using Ridoculous by running the following:
```python
import ridoculous.core
ridoculous.Ridoculous.makedocs(ridoculous.core, 'RIDOCULOUS_README.md')
```

- [ ridoculous.core ](#ridoculous.core_1529377134)
	- [ ridoculous.core.ClassRDoc ](#ridoculous.core.ClassRDoc_277831325)
		- [ ClassRDoc.__init__ ](#ClassRDoc.__init___1734499510)
		- [ ClassRDoc.__repr__ ](#ClassRDoc.__repr___684002517)
		- [ ClassRDoc.__str__ ](#ClassRDoc.__str___1102790725)
	- [ ridoculous.core.FunctionRDoc ](#ridoculous.core.FunctionRDoc_2006125902)
		- [ FunctionRDoc.__init__ ](#FunctionRDoc.__init___254940244)
		- [ FunctionRDoc.__repr__ ](#FunctionRDoc.__repr___1802332811)
		- [ FunctionRDoc.__str__ ](#FunctionRDoc.__str___374102979)
	- [ ridoculous.core.ModuleRDoc ](#ridoculous.core.ModuleRDoc_438349111)
		- [ ModuleRDoc.__init__ ](#ModuleRDoc.__init___273728676)
		- [ ModuleRDoc.__repr__ ](#ModuleRDoc.__repr___737580618)
		- [ ModuleRDoc.__str__ ](#ModuleRDoc.__str___2135828915)
	- [ ridoculous.core.RDocObject ](#ridoculous.core.RDocObject_973396301)
		- [ RDocObject.__getnewargs__ ](#RDocObject.__getnewargs___1737972049)
		- [ RDocObject.__new__ ](#RDocObject.__new___671582273)
		- [ RDocObject.__repr__ ](#RDocObject.__repr___350994193)
		- [ RDocObject._asdict ](#RDocObject._asdict_1837743226)
		- [ RDocObject._replace ](#RDocObject._replace_991483276)
	- [ ridoculous.core.Ridoculous ](#ridoculous.core.Ridoculous_983589323)
		- [ Ridoculous.__init__ ](#Ridoculous.__init___2004908398)
		- [ Ridoculous.make_doc_list ](#Ridoculous.make_doc_list_1854256711)
		- [ Ridoculous.write ](#Ridoculous.write_1109144762)


<a name="ridoculous.core_1529377134"></a>
## ridoculous.core

<a name="ridoculous.core.ClassRDoc_277831325"></a>
### ridoculous.core.ClassRDoc(self, obj: object = None)

This class documents class objects. The format will look like the following for a documented class. Link is
    used for a table of contents and the hash of the name is used to keep the links unique.

        Table of Contents String:
            - [ name ](#link)

        Markdown string:
            <a name="[link]"></a>
            #### [name]

                [docstring]

    

<a name="ClassRDoc.__init___1734499510"></a>
#### `ClassRDoc.__init__(self, obj: object = None)`

When a new `ClassRDoc` is created, all attributes are set during init. First the `obj` that was passed
        will be verified as a class object using the inspect library. The name will be found using a regex pattern,
        the signature is obtained using the inspect library, the docstring is copied and then the document attributes
        are created. The link is created to connect the table of contents to the header, the table of contents string
        is then created, and lastly the markdown for the class object.

        Args:
            obj {object} -- object to document (should be a function)

        

<a name="ClassRDoc.__repr___684002517"></a>
#### `ClassRDoc.__repr__(self)`

overloaded for ease of use, when class is printed, it will be the str of the markdown generated for the
        instance of `ClassRDoc`
        

<a name="ClassRDoc.__str___1102790725"></a>
#### `ClassRDoc.__str__(self)`

overloaded for ease of use
        

<a name="ridoculous.core.FunctionRDoc_2006125902"></a>
### ridoculous.core.FunctionRDoc(self, obj: object = None)

This class documents functions. The format will look like the following for a function. Link is used for a
    table of contents and the hash of the name is used to keep the links unique.

        Table of Contents String:
            - [ name ](#link)

        Markdown string:
            <a name="[link]"></a>
            #### [name]

                [docstring]

    

<a name="FunctionRDoc.__init___254940244"></a>
#### `FunctionRDoc.__init__(self, obj: object = None)`

When a new `FunctionRDoc` is created, all attributes are set during init. First the `obj` that was passed
        will be verified as a function using the inspect library. The name will be found using a regex pattern,
        the signature is obtained using the inspect library, the docstring is copied and then the document attributes
        are created. The link is created to connect the table of contents to the header, the table of contents string
        is then created, and lastly the markdown for the function.

        Args:
            obj {object} -- object to document (should be a function)

        

<a name="FunctionRDoc.__repr___1802332811"></a>
#### `FunctionRDoc.__repr__(self) -> str`

overloaded for ease of use, when class is printed, it will be the str of the markdown generated for the
        instance of `FunctionRDoc`
        

<a name="FunctionRDoc.__str___374102979"></a>
#### `FunctionRDoc.__str__(self) -> str`

overloaded for ease of use
        

<a name="ridoculous.core.ModuleRDoc_438349111"></a>
### ridoculous.core.ModuleRDoc(self, obj: object = None)

This class documents module objects. The format will look like the following for a module. Link is
    used for a table of contents and the hash of the name is used to keep the links unique.

        Table of Contents String:
            - [ name ](#link)

        Markdown string:
            <a name="[link]"></a>
            #### [name]

    

<a name="ModuleRDoc.__init___273728676"></a>
#### `ModuleRDoc.__init__(self, obj: object = None)`

When a new `ModuleRDoc` is created, all attributes are set during init. First the `obj` that was passed
        will be verified as a module using the inspect library. The name will be the `__name__` of the object.
        The link is created to connect the table of contents to the header, the table of contents string
        is then created, and lastly the markdown for the module.

        Args:
            obj {object} -- object to document

        

<a name="ModuleRDoc.__repr___737580618"></a>
#### `ModuleRDoc.__repr__(self)`

overloaded for ease of use, when class is printed, it will be the str of the markdown generated for the
        instance of `ModuleRDoc`
        

<a name="ModuleRDoc.__str___2135828915"></a>
#### `ModuleRDoc.__str__(self)`

overloaded for ease of use
        

<a name="ridoculous.core.RDocObject_973396301"></a>
### ridoculous.core.RDocObject(self, /, *args, **kwargs)

An `RDocObject` is a container object that is the starting object to document. The name will be taken
    from the initial object provided. It will then be walked to find any sub modules, classes, and functions inside the
    given module(s)

    Args:
        name {str} -- name of RDocObject
        modules {List[ModuleRDoc]} -- list holding the documented modules
    

<a name="RDocObject.__getnewargs___1737972049"></a>
#### `RDocObject.__getnewargs__(self)`

Return self as a plain tuple.  Used by copy and pickle.

<a name="RDocObject.__new___671582273"></a>
#### `RDocObject.__new__(_cls, name: str, modules: List[ridoculous.core.ModuleRDoc])`

Create new instance of RDocObject(name, modules)

<a name="RDocObject.__repr___350994193"></a>
#### `RDocObject.__repr__(self)`

Return a nicely formatted representation string

<a name="RDocObject._asdict_1837743226"></a>
#### `RDocObject._asdict(self)`

Return a new OrderedDict which maps field names to their values.

<a name="RDocObject._replace_991483276"></a>
#### `RDocObject._replace(_self, **kwds)`

Return a new RDocObject object replacing specified fields with new values

<a name="ridoculous.core.Ridoculous_983589323"></a>
### ridoculous.core.Ridoculous(self, objects: List[object] = None)

Ridoculous - making documentation for any python object
        The `Ridoculous` class is meant to take any object and document all modules, classes, and functions found
        inside that object. Ridoculous relies heavily on the code being documented using docstrings that are easy
        to read and understand. A table of contents that links to all the found objects will be creating along with
        the documents that were built.

        The goal of this utility is to help document code cleanly and quickly, that will then be used inside a readme
        or document to display the information found from the objects.

    

<a name="Ridoculous.__init___2004908398"></a>
#### `Ridoculous.__init__(self, objects: List[object] = None)`

The given list of objects will be parsed and ready to be documented. The list of strings that are written to
        the file are held in `.docs`. This is a raw version of what is dumped into the final output.

        Args:
            objects {List[object]} -- a list of object to document
        

<a name="Ridoculous.make_doc_list_1854256711"></a>
#### `Ridoculous.make_doc_list(self)`

creates the list of markdown strings to be help in `.docs`. firstly iterates over the RDocObjects and creates
        a table of contents, lastly reiterating over the RDocObjects and ordering the markdown

        return:
            list -- a list of markdown strings to be written in a file
        

<a name="Ridoculous.write_1109144762"></a>
#### `Ridoculous.write(self, filename: str = 'GENERATED_README.md')`

write `.docs` to a file

        Args:
            filename {str} -- the path of the filename to save the markdown as [default: GENERATED_README.md]

        
