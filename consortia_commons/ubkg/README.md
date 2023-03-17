# Consortia Commons > UBKG

## Configuration

### CONFIG KEY
`UBKG`. This may be changed by specifying a `config_key` when calling `initialize_ubkg(config, 'YOUR_KEY')`

### Sub Keys
#### `UBKG_SERVER` *str*: This is the host name.
#### `UBKG_ENDPOINT_$key` *str*: Define a reusable endpoint specifying a name for key. Example:
```
UBKG_ENDPOINT_VALUESET = 'valueset?parent_sab=SENNET&parent_code={code}&child_sabs=SENNET'
UBKG_ENDPOINT_FOO = 'foo?application_context=SENNET'
```
#### `UBKG_CODES` *json*: A JSON string, in the form of key/value pair. Examples:
```
UBKG_CODES = '{"specimen_categories":"C020076", "organ_types": {"code": "C000008", "key": "FOO"}, "organ_metadata": {"code": "C000009", "key": "FOO"}, "assay_types":{"code": "C004000", "key": "DATASETS", "endpoint": "datasets?application_context=SENNET"}}'
```
Notice that the value can either be another `str`, or JSON with the following properties:
- `code` *str*: Required. This is used as suffix of the cache dict key.
- `key` *str*: Required. Specify this to point to a specific `UBKG_ENDPOINT_$key` configuration and as prefix of cache dict key.
- `endpoint` *str*: Specify a specific endpoint to query. 

In the example `UBKG_CODES` above, programmatically could have:
```
from consortia_commons.ubkg import initialize_ubkg
from consortia_commons.rest import rest_ok, rest_server_err

ubkg = initialize_ubkg(config)
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