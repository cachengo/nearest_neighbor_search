export IMAGE_TAG=$(cat VERSION)

docker manifest create --amend cachengo/nn_search:$IMAGE_TAG cachengo/nn_search-x86_64:$IMAGE_TAG cachengo/nn_search-aarch64:$IMAGE_TAG
docker manifest push cachengo/nn_search:$IMAGE_TAG