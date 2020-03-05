- [ ridoculous ](#ridoculous_7865052736533038166)
	- [ ridoculous.core.Ridoculous ](#ridoculous.core.Ridoculous_4980956698812898237)
		- [ Ridoculous.__init__ ](#Ridoculous.__init___5329516786272341419)
		- [ Ridoculous.make_doc_list ](#Ridoculous.make_doc_list_6180417009006101326)
		- [ Ridoculous.write ](#Ridoculous.write_371011066631934688)
- [ ridoculous.core ](#ridoculous.core_2627093724066764050)
	- [ ridoculous.core.ClassRDoc ](#ridoculous.core.ClassRDoc_1007863446355550982)
		- [ ClassRDoc.__init__ ](#ClassRDoc.__init___2849687536006719513)
		- [ ClassRDoc.__repr__ ](#ClassRDoc.__repr___8448518769835862056)
		- [ ClassRDoc.__str__ ](#ClassRDoc.__str___3751587697851652572)
	- [ ridoculous.core.FunctionRDoc ](#ridoculous.core.FunctionRDoc_3313046137265364404)
		- [ FunctionRDoc.__init__ ](#FunctionRDoc.__init___3439615006007036159)
		- [ FunctionRDoc.__repr__ ](#FunctionRDoc.__repr___5172363454404446523)
		- [ FunctionRDoc.__str__ ](#FunctionRDoc.__str___7853124042233211835)
	- [ ridoculous.core.ModuleRDoc ](#ridoculous.core.ModuleRDoc_1869669420531181160)
		- [ ModuleRDoc.__init__ ](#ModuleRDoc.__init___4627504572361824363)
		- [ ModuleRDoc.__repr__ ](#ModuleRDoc.__repr___5349142152078159126)
		- [ ModuleRDoc.__str__ ](#ModuleRDoc.__str___1089423834691915156)
		- [ ModuleRDoc.get_rdoc_list ](#ModuleRDoc.get_rdoc_list_7552241777703920840)
	- [ ridoculous.core.RDocObject ](#ridoculous.core.RDocObject_8437025642643904252)
		- [ RDocObject.__getnewargs__ ](#RDocObject.__getnewargs___6308439009366307422)
		- [ RDocObject.__new__ ](#RDocObject.__new___4974135651110935806)
		- [ RDocObject.__repr__ ](#RDocObject.__repr___2032358439946994422)
		- [ RDocObject._asdict ](#RDocObject._asdict_8174946457664163165)
		- [ RDocObject._replace ](#RDocObject._replace_1661665314837781897)
	- [ ridoculous.core.Ridoculous ](#ridoculous.core.Ridoculous_4980956698812898237)
		- [ Ridoculous.__init__ ](#Ridoculous.__init___5329516786272341419)
		- [ Ridoculous.make_doc_list ](#Ridoculous.make_doc_list_6180417009006101326)
		- [ Ridoculous.write ](#Ridoculous.write_371011066631934688)


<a name="ridoculous_7865052736533038166"></a>
## ridoculous

<a name="ridoculous.core.Ridoculous_4980956698812898237"></a>
### ridoculous.core.Ridoculous(self, objects: List[object] = None)

None

<a name="Ridoculous.__init___5329516786272341419"></a>
#### `Ridoculous.__init__(self, objects: List[object] = None)`

None

<a name="Ridoculous.make_doc_list_6180417009006101326"></a>
#### `Ridoculous.make_doc_list(self)`

None

<a name="Ridoculous.write_371011066631934688"></a>
#### `Ridoculous.write(self, filename: str = 'GENERATED_README.md')`

None

<a name="ridoculous.core_2627093724066764050"></a>
## ridoculous.core

<a name="ridoculous.core.ClassRDoc_1007863446355550982"></a>
### ridoculous.core.ClassRDoc(self, obj: object = None)

None

<a name="ClassRDoc.__init___2849687536006719513"></a>
#### `ClassRDoc.__init__(self, obj: object = None)`

None

<a name="ClassRDoc.__repr___8448518769835862056"></a>
#### `ClassRDoc.__repr__(self)`

None

<a name="ClassRDoc.__str___3751587697851652572"></a>
#### `ClassRDoc.__str__(self)`

None

<a name="ridoculous.core.FunctionRDoc_3313046137265364404"></a>
### ridoculous.core.FunctionRDoc(self, obj: object = None)

None

<a name="FunctionRDoc.__init___3439615006007036159"></a>
#### `FunctionRDoc.__init__(self, obj: object = None)`

None

<a name="FunctionRDoc.__repr___5172363454404446523"></a>
#### `FunctionRDoc.__repr__(self)`

None

<a name="FunctionRDoc.__str___7853124042233211835"></a>
#### `FunctionRDoc.__str__(self)`

None

<a name="ridoculous.core.ModuleRDoc_1869669420531181160"></a>
### ridoculous.core.ModuleRDoc(self, obj: object = None)

None

<a name="ModuleRDoc.__init___4627504572361824363"></a>
#### `ModuleRDoc.__init__(self, obj: object = None)`

None

<a name="ModuleRDoc.__repr___5349142152078159126"></a>
#### `ModuleRDoc.__repr__(self)`

None

<a name="ModuleRDoc.__str___1089423834691915156"></a>
#### `ModuleRDoc.__str__(self)`

None

<a name="ModuleRDoc.get_rdoc_list_7552241777703920840"></a>
#### `ModuleRDoc.get_rdoc_list(self)`

None

<a name="ridoculous.core.RDocObject_8437025642643904252"></a>
### ridoculous.core.RDocObject(self, /, *args, **kwargs)

RDocObject(name, modules)

<a name="RDocObject.__getnewargs___6308439009366307422"></a>
#### `RDocObject.__getnewargs__(self)`

Return self as a plain tuple.  Used by copy and pickle.

<a name="RDocObject.__new___4974135651110935806"></a>
#### `RDocObject.__new__(_cls, name: str, modules: List[ridoculous.core.ModuleRDoc])`

Create new instance of RDocObject(name, modules)

<a name="RDocObject.__repr___2032358439946994422"></a>
#### `RDocObject.__repr__(self)`

Return a nicely formatted representation string

<a name="RDocObject._asdict_8174946457664163165"></a>
#### `RDocObject._asdict(self)`

Return a new OrderedDict which maps field names to their values.

<a name="RDocObject._replace_1661665314837781897"></a>
#### `RDocObject._replace(_self, **kwds)`

Return a new RDocObject object replacing specified fields with new values

<a name="ridoculous.core.Ridoculous_4980956698812898237"></a>
### ridoculous.core.Ridoculous(self, objects: List[object] = None)

None

<a name="Ridoculous.__init___5329516786272341419"></a>
#### `Ridoculous.__init__(self, objects: List[object] = None)`

None

<a name="Ridoculous.make_doc_list_6180417009006101326"></a>
#### `Ridoculous.make_doc_list(self)`

None

<a name="Ridoculous.write_371011066631934688"></a>
#### `Ridoculous.write(self, filename: str = 'GENERATED_README.md')`

None

