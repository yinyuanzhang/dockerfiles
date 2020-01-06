FROM siwatinc/nodejsubuntu_base_image
RUN apt-get update
RUN apt-get -y install ffmpeg
RUN npm install -g h265ize
CMD script --return -c "h265ize --watch -v $extraarg -m '$preset' -d '$output' -q $qp -f '$format' '$input'" /dev/null
