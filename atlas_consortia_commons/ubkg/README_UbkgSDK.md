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

When dealing with nested objects, one can grab values by providing `prop_callback` and `val_callback` functions (both must be provided even if `as_arr=True`). 
So with `key='value'` in `UbkgSDK.assay_classes()` and given the following data example (full list truncated):
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

If changed the result to be returned as a dict, would produce:
```
UbkgSDK.ops(prop_callback=prop_callback, val_callback=val_callback, as_data_dict=True).assay_classes()
{'10x-multiome': '10X Multiome', 'AB-PAS': 'Histology', 'AF': 'Auto-fluorescence', 'AF_pyramid': 'Auto-fluorescence', 'ATACseq-bulk': 'ATACseq', 'CODEX': 'CODEX', 'CODEX2': 'CODEX', 'DART-FISH': 'DART-FISH', 'DESI': 'DESI', 'DESI-IMS': 'DESI', 'DESI_pyramid': 'DESI', 'IMC2D': '2D Imaging Mass Cytometry', 'IMC2D_pyramid': '2D Imaging Mass Cytometry', 'IMC3D': '3D Imaging Mass Cytometry', 'IMC3D_pyramid': '3D Imaging Mass Cytometry', 'LC-MS': 'LC-MS', 'LC-MS-untargeted': 'LC-MS', 'LC-MS_bottom_up': 'LC-MS', 'LC-MS_top_down': 'LC-MS', 'Lightsheet': 'Light Sheet', 'MALDI-IMS': 'MALDI', 'MALDI-IMS_pyramid': 'MALDI', 'MIBI': 'MIBI', 'MS': 'MS Lipidomics', 'MS_bottom_up': 'LC-MS', 'MS_top_down': 'LC-MS', 'MxIF': 'UNKNOWN', 'MxIF_pyramid': 'UNKNOWN', 'NanoDESI': 'DESI', 'NanoDESI_pyramid': 'DESI', 'NanoPOTS': 'UNKNOWN', 'NanoPOTS_pyramid': 'UNKNOWN', 'PAS': 'Histology', 'PAS_pyramid': 'Histology', 'SIMS-IMS': 'SIMS', 'SNARE-ATACseq2': 'ATACseq', 'SNARE-RNAseq2': 'RNAseq', 'Slide-seq': 'Slideseq', 'TMT-LC-MS': 'LC-MS', 'Targeted-Shotgun-LC-MS': 'LC-MS', 'WGS': 'WGS', 'bulk-RNA': 'RNAseq', 'bulk_atacseq': 'ATACseq', 'cell-dive': 'Cell DIVE', 'celldive_deepcell': 'Cell DIVE', 'codex_cytokit_v1': 'CODEX', 'confocal': 'Confocal', 'cycif': 'CyCIF', 'cytof': 'CyTOF', 'enhanced-srs': 'Enhanced Stimulated Raman Spectroscopy (SRS)', 'geomx-rnaseq-with-probes': 'RNAseq (with probes)', 'geomx_ngs': 'GeoMx (NGS)', 'h-and-e': 'Histology', 'image_pyramid': 'UNKNOWN', 'lc-ms-ms_label-free': 'LC-MS', 'lc-ms-ms_labeled': 'LC-MS', 'lc-ms_label-free': 'LC-MS', 'lc-ms_labeled': 'LC-MS', 'merfish': 'MERFISH', 'mibi_deepcell': 'MIBI', 'molecular-cartography': 'Molecular Cartography', 'multiome-snare-seq2': 'RNAseq', 'music': 'RNAseq', 'nano-splits': 'nanoSPLITS', 'pas_ftu_segmentation': 'Histology', 'phenocycler': 'PhenoCycler', 'phenocycler_deepcell': None, 'publication': 'UNKNOWN', 'publication_ancillary': 'UNKNOWN', 'rnaseq-visium-no-probes': 'RNAseq', 'salmon_rnaseq_10x': 'RNAseq', 'salmon_rnaseq_bulk': 'RNAseq', 'salmon_rnaseq_sciseq': 'RNAseq', 'salmon_rnaseq_slideseq': 'Slideseq', 'salmon_rnaseq_snareseq': 'RNAseq', 'salmon_sn_rnaseq_10x': 'RNAseq', 'scRNAseq-10xGenomics-v2': 'RNAseq', 'scRNAseq-10xGenomics-v3': 'RNAseq', 'scRNAseq-visium-with-probes': 'RNAseq (with probes)', 'scRNAseq-with-probes': 'RNAseq (with probes)', 'sc_atac_seq_sci': 'ATACseq', 'sc_atac_seq_snare': 'ATACseq', 'sc_atac_seq_snare_lab': 'ATACseq', 'sc_rna_seq_snare_lab': 'RNAseq', 'sciATACseq': 'ATACseq', 'sciRNAseq': 'RNAseq', 'second-harmonic-generation': 'Second Harmonic Generation (SHG)', 'segmentation-mask': 'Segmentation Mask', 'seqFish': 'seqFISH', 'seqFish_lab_processed': 'seqFISH', 'seqFish_pyramid': 'seqFISH', 'snATACseq': 'ATACseq', 'snRNAseq-10xGenomics-v2': 'RNAseq', 'snRNAseq-10xGenomics-v3': 'RNAseq', 'sn_atac_seq': 'ATACseq', 'thick-section-multiphoton-mxif': 'Thick section Multiphoton MxIF', 'visium-no-probes': 'Visium (no probes)', 'visium-with-probes': 'Visium (with probes)', 'xenium': 'Xenium'}
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