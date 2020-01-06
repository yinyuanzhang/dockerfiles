FROM golang:1.10-alpine

RUN apk add --no-cache curl git make zip python jq
RUN apk add --update gcc g++
RUN apk add --update bash && rm -rf /var/cache/apk/*
RUN go get -u github.com/golang/lint/golint 
RUN go get bitbucket.org/liamstask/goose/cmd/goose
RUN go get github.com/gorilla/mux 
RUN go get github.com/go-sql-driver/mysql
RUN go get github.com/asaskevich/govalidator
RUN go get github.com/go-redis/redis
RUN go get -u go.uber.org/zap 
RUN go get github.com/awslabs/aws-lambda-go-api-proxy/gorillamux
RUN go get gopkg.in/DATA-DOG/go-sqlmock.v1
RUN go get github.com/icrowley/fake
RUN go get github.com/alicebob/miniredis
RUN go get github.com/newrelic/go-agent
RUN wget https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_amd64.zip; unzip terraform_0.11.7_linux_amd64.zip; echo "export PATH=\"\$PATH:$(pwd)\"" >> /etc/profile; rm -Rf terraform_0.11.7_linux_amd64.zip
RUN curl -O https://bootstrap.pypa.io/get-pip.py; python get-pip.py --user; echo "export PATH=\"\$PATH:/root/.local/bin\"" >> /etc/profile; source /etc/profile; pip install awscli --upgrade --user
RUN echo "export PATH=\"\$PATH:/go/bin\"" >> /etc/profile