#!/bin/bash


# Also docker build -t nn_search .
docker run -it -p 1323:1323 -v /db/index256:/db -e "ANN_INDEX_LENGTH=256" nn_search
