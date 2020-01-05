FROM ubuntu:latest
RUN apt-get update && apt-get -y install git wget mc nano sudo
RUN apt-get -y install npm ffmpeg
RUN npm install -g h265ize
CMD script --return -c "h265ize -v $extraarg -m '$preset' -d $output -q $qp -f '$format' $input $delete $custom" /dev/null
