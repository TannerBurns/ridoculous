## ridoculous.core

### ridoculous.core.BaseClassRDoc(self, obj: object = None)

None

#### `BaseClassRDoc.__init__(self, obj: object = None)`

None

#### `BaseClassRDoc.__repr__(self)`

None

#### `BaseClassRDoc.__str__(self)`

None

### ridoculous.core.BaseFunctionRDoc(self, obj: object = None)

None

#### `BaseFunctionRDoc.__init__(self, obj: object = None)`

None

#### `BaseFunctionRDoc.__repr__(self)`

None

#### `BaseFunctionRDoc.__str__(self)`

None

### ridoculous.core.BaseModuleRDoc(self, obj: object = None)

None

#### `BaseModuleRDoc.__init__(self, obj: object = None)`

None

#### `BaseModuleRDoc.__repr__(self)`

None

#### `BaseModuleRDoc.__str__(self)`

None

#### `BaseModuleRDoc.get_rdoc_list(self)`

None

### ridoculous.core.RDocObject(self, /, *args, **kwargs)

RDocObject(name, modules)

#### `RDocObject.__getnewargs__(self)`

Return self as a plain tuple.  Used by copy and pickle.

#### `RDocObject.__new__(_cls, name: str, modules: List[ridoculous.core.BaseModuleRDoc])`

Create new instance of RDocObject(name, modules)

#### `RDocObject.__repr__(self)`

Return a nicely formatted representation string

#### `RDocObject._asdict(self)`

Return a new OrderedDict which maps field names to their values.

#### `RDocObject._replace(_self, **kwds)`

Return a new RDocObject object replacing specified fields with new values

### ridoculous.core.Ridoculous(self, objects: List[object] = None)

None

#### `Ridoculous.__init__(self, objects: List[object] = None)`

None

#### `Ridoculous.make_docs(self)`

None

#### `Ridoculous.write(self, filename: str = 'RIDOCULOUS_README.md')`

None

