FROM mgagcode/tmibase:latest

ADD . /app
WORKDIR /app

RUN ["python", "build_compile.py", "--main", "TMIStation", "--flask", "--lang", "3", "--compile", "--rm-source", "--name", "TMIStation"]
RUN rm -rf /app/.git && rm -rf /app/scratch && rm -rf /app/build

FROM python:3.6-alpine
COPY --from=0 /usr/local/lib/python3.6/site-packages/ /usr/local/lib/python3.6/site-packages/
COPY --from=0 /app /app

RUN apk add libstdc++ libjpeg-turbo libpq
RUN apk add nodejs

VOLUME ["/app"]
WORKDIR /app

ENTRYPOINT ["./TMIStation"]

# Build:
#   docker build -t tmistation .
#
# Run Demo Mode:
#   docker run -ti -p 6800:6800 mgagcode/tmistation
#
# Run Production Mode:
#   git clone https://github.com/mgagcode/tmi_scripts.git
#   cd ./public
#   docker run -ti -p 6800:6800 -v $(pwd):/app/public mgagcode/tmistation
