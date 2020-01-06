arg code_version="latest"
FROM ubuntu:$code_version
run echo $code_version
arg license_key="123-456"
env ora_port=1521
LABEL MAINTAINER DJ@devops.com
run mkdir /code
COPY Sample.sh /code/Sample.sh
RUN chmod +x /code/Sample.sh
run echo $license_key
WORKDIR /code
cmd sh /code/Sample.sh
