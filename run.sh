#!/bin/bash


# Also docker build -t nn_search .
docker run -it -p 5000:5000 -v /db/index3:/db nn_search
