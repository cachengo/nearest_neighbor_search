FROM golang:alpine

RUN apk --update add build-base git openssh && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/* && \
    go get github.com/cachengo/gannoy/...

COPY boot.sh /boot.sh
ENV ANN_INDEX_LENGTH=3
EXPOSE 1323
WORKDIR /db
ENTRYPOINT ["/boot.sh"]
