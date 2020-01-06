FROM node:10.4.1

EXPOSE 8000

RUN npm install --global gatsby --no-optional gatsby@1.9

RUN mkdir -p /site
WORKDIR /site
VOLUME /site

COPY ./entry.sh /
RUN chmod +x /entry.sh
ENTRYPOINT ["/entry.sh"]





