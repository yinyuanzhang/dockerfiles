FROM python:2.7

LABEL maintainer="iglov" \
      description="Simple test docker cloud" \
      units="test app"

COPY . /usr/bin/myapp
WORKDIR /usr/bin/myapp

ENTRYPOINT ["./launcher"]
CMD ["test"]
