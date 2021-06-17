FROM golang:alpine
LABEL maintainer="Ali Belachkar"

COPY . /go/src/app
WORKDIR /go/src/app

RUN go build -o helloworld
EXPOSE 6111

CMD [ "./helloworld" ]
