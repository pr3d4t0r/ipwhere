# ipwhere

IP geo location command line tool (relies on 3rd-party to provide actual
location).

The current supported provider for ipwhere is IP2Location.io - a future version
will use a free service or list.


## API key required

The program uses ipstack.io for resolving locations.  They provide a free
service that requires an API key and grants up to 1,000 HTTP requests per
calendar month.

The API key is defined as an environment variable:

```bash
IPWHERE_API_KEY=your-API-key-here
```

ipwhere won't start if the environment variable isn't defined.


### Getting an ipstack.io API key

Head to https://ipstack.io, sign up to the service and follow the
instructions.  Activation and usage are immediate.


### Query Frequency

If possible, use local caching as well.  This will help you extend the number of
monthly requests beyond the 1,000 limit imposed by ipstack.io.

ipwhere makes a single query per call.  Future versions may implement local
caching to `/tmp` or similar.

