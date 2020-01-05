FROM birdy/sdkman:latest

SHELL ["bash", "--login", "-c"]
ADD GRAALVM_VERSION .
RUN apt-get update -y && apt-get install gcc zlib1g-dev -y
RUN sdk install java $(cat GRAALVM_VERSION) && sdk use java $(cat GRAALVM_VERSION)
RUN which native-image

ENTRYPOINT ["/bin/bash","--login", "-c"]
