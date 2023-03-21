# Atlas Consortia Commons > REST

## Configuration

 - To facilitate the decorator `@app.errorhandler` you can initialize this block of code:
```
from atlas_consortia_commons.rest import *

    for exception in get_http_exceptions_classes():
        app.register_error_handler(exception, abort_err_handler)
```
 - Calling, for example,  `abort_bad_req(<error>)` will gracefully return a 400 with a JSON body containing `error`

