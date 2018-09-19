#!/bin/sh
# this script is used to boot a Docker container

gannoy create -d $ANN_INDEX_LENGTH -K $(( $ANN_INDEX_LENGTH * 2 )) -p /db db
gannoy-db
