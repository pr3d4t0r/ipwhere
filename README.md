# ipwhere

IP geo location command line tool (relies on 3rd-party to provide actual
location).


## API key required

The program uses IPInfoDB for resolving locations.  They provide a free service,
just ask you to register so that they can give you a unique API key.

The API key is defined as an environment variable:

```bash
IPWHERE_API_KEY=your-API-key-here
```

ipwhere won't start if the environment variable isn't defined.


### Getting an IPInfoDB API Key

Head to http://www.ipinfodb.com/ip_location_api_json.php and follow the
instructions.  API keys are free!  They take up to 10 minutes to be activated.


### Query Frequency

IPInfoDB is a free service, but require that API requests are spaced about 2
seconds apart to lighten their server load.  If possible, use local caching as
well.

ipwhere makes a single query per call, so no attempt at pacing is done in this
implementation.


## Version history

1.1 - Change provider from geobytes.com to IPInfoDB; Unicode/UTF-8 strings

