# ipwhere

IP geo location command line tool (relies on 3rd-party to provide actual
location).

The current supported provider for ipwhere is IP2Location.io - a future version
will use a free service or list.


## API key required

The program uses IP2Location for resolving locations.  They provide a free
service, just ask you to register so that they can give you a unique API key.

The API key is defined as an environment variable:

```bash
IPWHERE_API_KEY=your-API-key-here
```

ipwhere won't start if the environment variable isn't defined.


### Getting an IP2Location API Key

Head to http://www.ip2location.io, sign up to the service and follow the
instructions.  API keys are free for the first 30,000 requests.  They take up to
10 minutes to be activated.


### Query Frequency

IP2Location is a free service, but require that API requests are spaced about 2
seconds apart to lighten their server load.  If possible, use local caching as
well.

ipwhere makes a single query per call, so no attempt at pacing is done in this
implementation.

