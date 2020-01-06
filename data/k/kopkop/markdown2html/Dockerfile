FROM ubuntu:bionic

LABEL maintainer="kopwei <kopkop@gmail.com>"

RUN apt-get update && apt-get -y install pandoc

ADD https://gist.githubusercontent.com/dashed/6714393/raw/ae966d9d0806eb1e24462d88082a0264438adc50/github-pandoc.css /github-pandoc.css


CMD ["pandoc", "-f", "markdown", "-c", "/github-pandoc.css"]
