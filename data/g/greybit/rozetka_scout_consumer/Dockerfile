FROM dilks/windscribe-httpproxy
WORKDIR /app
COPY requirements.txt ./
COPY . /app
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
