# Nearest Neighbor Search
A very simple service that implement nearest neighbor search.

## To start service
```bash
docker build -t nn_search .
docker run -p 5000:5000 -v /path/to/persistent/location:/db nn_search
```
The -v flag is only required if persistence is desired

## API
See https://github.com/monochromegane/gannoy for API specification
