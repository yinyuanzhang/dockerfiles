FROM python:3.6.6

# Install Flower
ARG FLOWER_VERSION='0.9.3'
ENV FLOWER_PORT '5555'
ENV FLOWER_ADDRESS '0.0.0.0'

RUN pip install --upgrade pip
RUN pip install flower==$FLOWER_VERSION
RUN pip install redis

EXPOSE 5555
ENTRYPOINT ["sh", "-c", "flower --port=$FLOWER_PORT --address=$FLOWER_ADDRESS --broker=redis://$REDIS_SERVICE_HOST:$REDIS_SERVICE_PORT/$REDIS_DB_NUMBER --auto_refresh=True --persistent=True --db=/flowerdb"]
