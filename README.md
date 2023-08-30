# ipwhere

IP geo location command line tool (relies on 3rd-party to provide actual
location).

Unlike with previous versions **`ipwhere` does not require an API key starting
on version 2.0.2.**


## No API key required

`ipwhere` uses https://ip-api.com for resolving locations.  They provide a free
service that does not require an API key and grants up to 45 requests per minute
from a given IP address.


### Query Frequency

If possible, use local caching as well.  This will help you extend the number of
requests per minute from `ipwhere`.

ipwhere makes a single query per call.  Future versions may implement local
caching to `/tmp` or similar.

