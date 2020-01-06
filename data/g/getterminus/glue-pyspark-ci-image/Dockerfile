FROM getterminus/java-ci-image:20190122

COPY requirements.txt ./

RUN apt-get -y update && \
    apt-get install -y python-pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

WORKDIR /app
COPY . /app


