FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y unzip curl libcurl4 libssl1.0.0 && \
    url=$(curl -L -s https://minecraft.net/en-us/download/server/bedrock/ | grep bin-linux | sed "s/.*href=['\"]\([^'\"]*\)['\"].*/\1/g"); curl $url --output bedrock-server.zip && \
    unzip bedrock-server.zip -d bedrock-server && \
    rm bedrock-server.zip

WORKDIR /bedrock-server
ENV LD_LIBRARY_PATH=.
CMD ./bedrock_server