# UbkgSDK
The UBKG SDK class will allow for requesting various nodes within the UBKG ecosystem.
app.cfg must be set up. See [the docs for details.](https://github.com/x-atlas-consortia/commons/tree/main/atlas_consortia_commons/ubkg)

## Transforming UBKG results using the SDK.
Node result set can be transformed with various options.
### Options
```
as_arr = False  # Return as an array/list
cb = str  # The callback function to run on value of the transform result 
as_data_dict = False  # Return as a dict
prop_callback = to_snake_case_upper  # The callback to apply on the dict key of the transform result 
data_as_val = False  # Whether to return the full UBKG data as value of key
url_params = None  # Url parameters to apply to the request
key = 'term'  # Which property value from the item to return as the key of the transform result 
val_key = None  # Which property value from the item to return as the value of the transform result 
```

### Examples:
```
UbkgSDK.ops().entities()
```
Will yield a class with name `Entities`:
```
<class 'atlas_consortia_commons.object.Entities'>
Entities.DATASET
```

`UbkgSDK.ops(as_arr=True, cb=enum_val_lower).entities()`
Will return a list of strings from the `term` key property
```
['dataset', 'sample', 'source', 'publication entity']
```

`UbkgSDK.ops(as_arr=True, key='code', cb=enum_val_lower).entities()`
Will return a list of strings from the `code` key property
```
['c050002', 'c050003', 'c050004', 'c050021']
```

`UbkgSDK.ops(as_data_dict=True, data_as_val=True).entities()`
Will return the following transform result:
```
{'DATASET': {'code': 'C050002', 'sab': 'SENNET', 'term': 'Dataset'}, 'SAMPLE': {'code': 'C050003', 'sab': 'SENNET', 'term': 'Sample'}, 'SOURCE': {'code': 'C050004', 'sab': 'SENNET', 'term': 'Source'}, 'PUBLICATION_ENTITY': {'code': 'C050021', 'sab': 'SENNET', 'term': 'Publication Entity'}}
```

When dealing with nested objects, can grab values by providing `prop_callback` and `val_callback` functions. With `key='value'` in `UbkgSDK.assay_classes()` and given the following data example (full list truncated):
```
Data:
[
  {
    "rule_description": {
      "application_context": "SENNET",
      "code": "C200001",
      "name": "non-DCWG primary AF"
    },
    "value": {
      "active_status": "active",
      "assaytype": "AF",
      "contains_full_genetic_sequences": false,
      "dataset_type": "Auto-fluorescence",
      "description": "Auto-fluorescence Microscopy",
      "dir_schema": "af-v0",
      "is_multiassay": false,
      "must_contain": [],
      "pipeline_shorthand": null,
      "process_state": "primary",
      "tbl_schema": "af-v",
      "vitessce_hints": []
    }
  },
  {
    "rule_description": {
      "application_context": "SENNET",
      "code": "C200010",
      "name": "derived AF_pyramid"
    },
    "value": {
      "active_status": "active",
      "assaytype": "AF_pyramid",
      "contains_full_genetic_sequences": false,
      "dataset_type": "Auto-fluorescence",
      "description": "Auto-fluorescence Microscopy [Image Pyramid]",
      "dir_schema": null,
      "is_multiassay": false,
      "must_contain": [],
      "pipeline_shorthand": "Image Pyramid",
      "process_state": "derived",
      "tbl_schema": null,
      "vitessce_hints": [
        "is_support",
        "pyramid"
      ]
    }
  },
   {
    "rule_description": {
      "application_context": "SENNET",
      "code": "C200020",
      "name": "non-DCWG primary ATACseq-bulk"
    },
    "value": {
      "active_status": "active",
      "assaytype": "ATACseq-bulk",
      "contains_full_genetic_sequences": true,
      "dataset_type": "ATACseq",
      "description": "Bulk ATACseq",
      "dir_schema": "bulkatacseq-v0",
      "is_multiassay": false,
      "must_contain": [],
      "pipeline_shorthand": null,
      "process_state": "primary",
      "tbl_schema": "bulkatacseq-v",
      "vitessce_hints": []
    }
  },
  :
  :
 ]
def prop_callback(d):
    return d["assaytype"]

def val_callback(d):
    return d["dataset_type"]
    
UbkgSDK.ops(prop_callback=prop_callback, val_callback=val_callback, as_arr=True, cb=enum_val).assay_classes()
```
Will return the following transform result:
```
['Auto-fluorescence', 'ATACseq', 'Cell DIVE', 'CODEX', 'DART-FISH', 'DESI', 'UNKNOWN', '2D Imaging Mass Cytometry', '3D Imaging Mass Cytometry', 'LC-MS', 'Light Sheet', 'MALDI', 'MIBI', 'Histology', 'RNAseq', 'seqFISH', 'SIMS', 'Slideseq', 'WGS', 'Visium (no probes)', 'Visium (with probes)', 'GeoMx (NGS)', '10X Multiome', 'RNAseq (with probes)', 'PhenoCycler', 'CyCIF', 'MERFISH', 'nanoSPLITS', 'Confocal', 'Thick section Multiphoton MxIF', 'Second Harmonic Generation (SHG)', 'Enhanced Stimulated Raman Spectroscopy (SRS)', 'Molecular Cartography', None, 'MS Lipidomics', 'Segmentation Mask', 'Xenium', 'CyTOF']
```


If call say `UbkgSDK.ops().specimen_categories()` directly after a previous call with `ops(...)` settings, the settings will be reused from the last call.
To make a fresh call on each request with default options, use `UbkgSDK.ops().*`.


## Retrieving raw UBKG results
May also retrieve the raw UBKG results
### By Valueset
To retrieve a node whose app.cfg is setup to use `UBKG_ENDPOINT_VALUESET`
```
current_app.ubkg.get_ubkg_valueset(current_app.ubkg.specimen_categories)
```

### By Endpoint
If a particular node name has a specific endpoint set in `app.cfg.UBKG_CODES`
```
current_app.ubkg.get_ubkg_by_endpoint(current_app.ubkg.organ_types)
```

### Additional
May pass another endpoint.
```
current_app.ubkg.get_ubkg(current_app.ubkg.assay_types, prefix_key, f"{endpoint}{url_params}")
```