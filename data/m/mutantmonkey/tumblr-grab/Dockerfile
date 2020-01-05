FROM python:2

RUN apt-get update && apt-get install -y \
        build-essential lua5.1 liblua5.1-0-dev python python-setuptools \
        python-dev openssl libssl-dev python-pip make zlib1g-dev flex \
        libgnutls28-dev rsync
RUN pip install --no-cache-dir seesaw

# create a directory owned by the user
RUN useradd -m -g users -u 1000 grabber

USER grabber
WORKDIR /home/grabber/

COPY get-wget-lua.sh /home/grabber/
RUN ./get-wget-lua.sh

COPY . /home/grabber/

CMD ["bash"]
