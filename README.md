- [ ridoculous.core ](#ridoculous.core_1225138404)
	- [ ridoculous.core.BaseClassRDoc ](#ridoculous.core.BaseClassRDoc_507489281)
		- [ BaseClassRDoc.__init__ ](#BaseClassRDoc.__init___2095759286)
		- [ BaseClassRDoc.__repr__ ](#BaseClassRDoc.__repr___1467402247)
		- [ BaseClassRDoc.__str__ ](#BaseClassRDoc.__str___617675410)
	- [ ridoculous.core.BaseFunctionRDoc ](#ridoculous.core.BaseFunctionRDoc_192133315)
		- [ BaseFunctionRDoc.__init__ ](#BaseFunctionRDoc.__init___905781060)
		- [ BaseFunctionRDoc.__repr__ ](#BaseFunctionRDoc.__repr___208544670)
		- [ BaseFunctionRDoc.__str__ ](#BaseFunctionRDoc.__str___1249175190)
	- [ ridoculous.core.BaseModuleRDoc ](#ridoculous.core.BaseModuleRDoc_1662577655)
		- [ BaseModuleRDoc.__init__ ](#BaseModuleRDoc.__init___1514878822)
		- [ BaseModuleRDoc.__repr__ ](#BaseModuleRDoc.__repr___120071931)
		- [ BaseModuleRDoc.__str__ ](#BaseModuleRDoc.__str___992059393)
		- [ BaseModuleRDoc.get_rdoc_list ](#BaseModuleRDoc.get_rdoc_list_588066363)
	- [ ridoculous.core.RDocObject ](#ridoculous.core.RDocObject_1355439107)
		- [ RDocObject.__getnewargs__ ](#RDocObject.__getnewargs___114722693)
		- [ RDocObject.__new__ ](#RDocObject.__new___1096507896)
		- [ RDocObject.__repr__ ](#RDocObject.__repr___871828497)
		- [ RDocObject._asdict ](#RDocObject._asdict_1285752106)
		- [ RDocObject._replace ](#RDocObject._replace_1262668292)
	- [ ridoculous.core.Ridoculous ](#ridoculous.core.Ridoculous_412949436)
		- [ Ridoculous.__init__ ](#Ridoculous.__init___811718801)
		- [ Ridoculous.make_doc_list ](#Ridoculous.make_doc_list_1829338688)
		- [ Ridoculous.write ](#Ridoculous.write_1529523973)


<a name="ridoculous.core_1225138404"></a>
## ridoculous.core

<a name="ridoculous.core.BaseClassRDoc_507489281"></a>
### ridoculous.core.BaseClassRDoc(self, obj: object = None)

None

<a name="BaseClassRDoc.__init___2095759286"></a>
#### `BaseClassRDoc.__init__(self, obj: object = None)`

None

<a name="BaseClassRDoc.__repr___1467402247"></a>
#### `BaseClassRDoc.__repr__(self)`

None

<a name="BaseClassRDoc.__str___617675410"></a>
#### `BaseClassRDoc.__str__(self)`

None

<a name="ridoculous.core.BaseFunctionRDoc_192133315"></a>
### ridoculous.core.BaseFunctionRDoc(self, obj: object = None)

None

<a name="BaseFunctionRDoc.__init___905781060"></a>
#### `BaseFunctionRDoc.__init__(self, obj: object = None)`

None

<a name="BaseFunctionRDoc.__repr___208544670"></a>
#### `BaseFunctionRDoc.__repr__(self)`

None

<a name="BaseFunctionRDoc.__str___1249175190"></a>
#### `BaseFunctionRDoc.__str__(self)`

None

<a name="ridoculous.core.BaseModuleRDoc_1662577655"></a>
### ridoculous.core.BaseModuleRDoc(self, obj: object = None)

None

<a name="BaseModuleRDoc.__init___1514878822"></a>
#### `BaseModuleRDoc.__init__(self, obj: object = None)`

None

<a name="BaseModuleRDoc.__repr___120071931"></a>
#### `BaseModuleRDoc.__repr__(self)`

None

<a name="BaseModuleRDoc.__str___992059393"></a>
#### `BaseModuleRDoc.__str__(self)`

None

<a name="BaseModuleRDoc.get_rdoc_list_588066363"></a>
#### `BaseModuleRDoc.get_rdoc_list(self)`

None

<a name="ridoculous.core.RDocObject_1355439107"></a>
### ridoculous.core.RDocObject(self, /, *args, **kwargs)

RDocObject(name, modules)

<a name="RDocObject.__getnewargs___114722693"></a>
#### `RDocObject.__getnewargs__(self)`

Return self as a plain tuple.  Used by copy and pickle.

<a name="RDocObject.__new___1096507896"></a>
#### `RDocObject.__new__(_cls, name: str, modules: List[ridoculous.core.BaseModuleRDoc])`

Create new instance of RDocObject(name, modules)

<a name="RDocObject.__repr___871828497"></a>
#### `RDocObject.__repr__(self)`

Return a nicely formatted representation string

<a name="RDocObject._asdict_1285752106"></a>
#### `RDocObject._asdict(self)`

Return a new OrderedDict which maps field names to their values.

<a name="RDocObject._replace_1262668292"></a>
#### `RDocObject._replace(_self, **kwds)`

Return a new RDocObject object replacing specified fields with new values

<a name="ridoculous.core.Ridoculous_412949436"></a>
### ridoculous.core.Ridoculous(self, objects: List[object] = None)

None

<a name="Ridoculous.__init___811718801"></a>
#### `Ridoculous.__init__(self, objects: List[object] = None)`

None

<a name="Ridoculous.make_doc_list_1829338688"></a>
#### `Ridoculous.make_doc_list(self)`

None

<a name="Ridoculous.write_1529523973"></a>
#### `Ridoculous.write(self, filename: str = 'README.md')`

None

