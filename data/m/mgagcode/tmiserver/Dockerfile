FROM mgagcode/tmibase:latest

ADD . /app
WORKDIR /app

RUN ["python", "build_compile.py", "--main", "TMIServer", "--flask", "--lang", "3", "--compile", "--rm-source", "--name", "TMIServer"]
RUN rm -rf /app/.git && rm -rf /app/scratch && rm -rf /app/build

FROM python:3.6-alpine
COPY --from=0 /usr/local/lib/python3.6/site-packages/ /usr/local/lib/python3.6/site-packages/
COPY --from=0 /app /app

RUN apk add libstdc++ libjpeg-turbo libpq
RUN apk add nodejs

VOLUME ["/app"]
WORKDIR /app

ENTRYPOINT ["./TMIServer"]

# Build:
#   docker build -t tmiserver .
#   docker images ls
#   docker tag <hash> mgagcode/tmiserver
#   docker push mgagcode/tmiserver
#
# Pull:
#   docker pull mgagcode/tmiserver
#
# Setup DB:
#         docker network create tminet
#         docker run --net tminet --name tmidb -v $(pwd)/datadir:/var/lib/postgresql/data -e POSTGRES_PASSWORD=qwerty -d postgres:11
#         docker exec -it tmidb createdb -U postgres resultbasev1
#         docker exec -it tmidb createdb -U postgres resultbasekeysv1
#
# Run Demo Mode:
#   docker run --net tminet -ti -p 6600:6600 tmiserver
#
# Run Production Mode:
#   git clone https://github.com/mgagcode/tmi_scripts.git
#   cd ./public
#   docker run --net tminet -ti -p 6600:6600 -v $(pwd):/app/public tmiserver
#   Also:
#   1) create a file called 'config.json', with following,
#      {
#       "config": {
#       },
#       "postgres": {
#         "TMIDemoRecordV1": {
#           "user": "postgres",
#           "pw": "qwerty",
#           "ip": "tmidb"
#           }
#         }
#      }
#

