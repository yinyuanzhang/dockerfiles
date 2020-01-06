FROM frolvlad/alpine-python3

MAINTAINER Karel Rudisar - krudisar@gmail.com

# --- CACHE SETTINGS ---
ENV CACHE_API_REQUESTS=0
ENV CACHE_IMAGES_IN_DB=0
# ----------------------

RUN apk add --no-cache --update python3-dev gcc build-base

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# set a correct timezone
ENV TZ=Europe/Prague
RUN apk add tzdata

ENTRYPOINT ["python"]
CMD ["app.py"]

