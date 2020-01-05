FROM node:11

WORKDIR /home/galleryjs

ENV PUID=1000
ENV PGID=1000

RUN apt-get update && \
    apt-get -y install sudo

COPY . .

RUN chmod +x dockerstart.sh

RUN npm install
RUN npm run build

RUN mv dist/data dist/data-origin
RUN ln -s /data dist/data

EXPOSE 3000

CMD [ "./dockerstart.sh" ]