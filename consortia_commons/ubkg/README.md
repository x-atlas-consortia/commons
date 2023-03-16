# Consortia Commons > UBKG

## Configuration

### Heading
`[UBKG]`. This may be changed by specifying a `config_key` when calling `initialize_ubkg('YOUR_KEY')`

### Sub Keys
#### `server` *str*: This is the host name.
#### `endpoint_$key` *str*: Define a reusable endpoint specifying a name for key. Example:
```
endpoint_valueset = valueset?parent_sab=SENNET&parent_code={code}&child_sabs=SENNET
endpoint_foo = "foo?application_context=SENNET"
```
#### `codes` *json*: A JSON string, in the form of key/value pair. Examples:
```
codes = {"specimen_categories":"C020076", "organ_types": {"code": "C000008", "key": "foo"}, "organ_metadata": {"code": "C000009", "key": "foo"}, "assay_types":{"code": "C004000", "key": "datasets", "endpoint": "datasets?application_context=SENNET"}}
```
Notice that the value can either be another `str`, or JSON with the following properties:
- `code` *str*: Required. This is used as suffix of the cache dict key.
- `key` *str*: Required. Specify this to point to a specific `endpoint_$key` configuration and as prefix of cache dict key.
- `endpoint` *str*: Specify a specific endpoint to query. 

In the example `codes` above, programmatically could have:
```
from consortia_commons.ubkg import initialize_ubkg
from consortia_commons.rest import rest_ok, rest_server_err

ubkg = initialize_ubkg()
@app.route('/')
def valuesets():
    response = ubkg.get_ubkg_valueset(ubkg.specimen_categories)
    return _respond(response)
    
@app.route('/foo')
def datasets():
    response = ubkg.get_ubkg_by_key(ubkg.organ_types)
    # response = ubkg.get_ubkg_by_key(ubkg.organ_metadata)
    return _respond(response)
 
@app.route('/datasets')
def datasets():
    response = ubkg.get_ubkg_by_endpoint(ubkg.assay_types)
    return _respond(response)

def _respond(response):
    return rest_ok(response) if ubkg.error is None else rest_server_err(response) 
```