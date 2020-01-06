FROM ubuntu:18.04

WORKDIR /usr/src/app
COPY . .

RUN apt update \
    && apt install -y \
    firefox \
    wget \
    && wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz \
    && tar -xvzf geckodriver* \
    && chmod +x geckodriver \
    && mv geckodriver /usr/local/bin/ \
    && apt install -y python3-pip \
    && pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "./fake_phones.py"]

# iceweasel = firefox in debian ?
#
#