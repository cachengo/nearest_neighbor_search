# Nearest Neighbor Search
A very simple service that implement nearest neighbor search.

## To start service
```bash
docker build -t nn_search .
docker run -p 5000:5000 -v /path/to/persistent/location:/db nn_search
```
The -v flag is only required if persistence is desired

## API
There are two endpoints `/add` and `/find` both of which take a json payload.
Currently, the only supported parameter is "vector" which is the vector to be
indexed/compared. The "/add" endpoint will index the given vector and return the
id with which it was stored. The "/find" vector will return the id of and distance
to the nearest vector currently indexed.

## Drawbacks
The index is not currently able to update itself without restarting the service.
Hence, you will need to restart the docker container in order for the "/find" endpoint
to start considering new vectors. The current version of this service is for demonstration
purposes only and we hope that in the future we can provide a version that can handle
live-updating.