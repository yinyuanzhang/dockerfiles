FROM node:11.9.0-stretch

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-pip python3-dev && \
    npm install -g bower && \
    pip3 install setuptools wheel && \
    pip3 install coala-bears coala-html

RUN cd /usr/local/lib/python3.5/dist-packages/coalahtml/_coalahtml/ && \
    bower install --allow-root

EXPOSE 8000

WORKDIR /src

CMD [ "coala-html", "--dir", "/usr/local/lib/python3.5/dist-packages/coalahtml/_coalahtml/" ]
