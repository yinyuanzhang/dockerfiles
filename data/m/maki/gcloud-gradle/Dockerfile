FROM google/cloud-sdk:274.0.1-alpine

MAINTAINER Vadim Homchik <homchik@gmail.com>

RUN apk --update --no-cache add gradle

RUN gcloud components install app-engine-java --quiet

CMD ["gradle"]
