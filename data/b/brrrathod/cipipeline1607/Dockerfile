from ubuntu

LABEL MAINTAINER bridgeeta@oracle.com
arg image_variable=local
env ora_port=1521
env ora_host="localhost"
run mkdir /code
copy sample.sh /code/sample.sh
run chmod +x /code/sample.sh
run echo "Building an image!"
run echo $image_variable
workdir /code
cmd sh /code/sample.sh
