export IMAGE_TAG=$(cat VERSION)
export AARCH=`uname -m`

docker build -t cachengo/nn_search-$AARCH:$IMAGE_TAG .
docker push cachengo/nn_search-$AARCH:$IMAGE_TAG