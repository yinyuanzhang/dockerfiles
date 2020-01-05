FROM sistemicorp/dkrpybase:latest

ADD . /app
WORKDIR /app

RUN ["python", "build_compile.py", "--main", "lente", "--flask", "--lang", "3", "--compile", "--rm-source", "--name", "lente"]
RUN rm -rf /app/.git && rm -rf /app/scratch && rm -rf /app/build

FROM python:3.6-slim
COPY --from=0 /app /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc g++
RUN pip3 install -r app/requirements.txt --no-cache-dir
RUN apt-get remove -y gcc g++
RUN apt autoremove -y
RUN apt install -y nodejs

VOLUME ["/app"]
WORKDIR /app

ENTRYPOINT ["./lente"]

# Build:
#   docker build -t lente .
#   docker images ls
#   docker tag <hash> sistemi/lente
#   docker push sistemicorp/lente
#
# Pull:
#   docker pull sistemicorp/lente
#
# Setup DB:
#         docker network create lentenet
#         docker run --net lentenet --name lentedb -v $(pwd)/datadir:/var/lib/postgresql/data -e POSTGRES_PASSWORD=qwerty -d postgres:11
#         docker exec -it lentedb createdb -U postgres resultbasekeysv1
#
# Run Demo Mode:
#   docker run --net lentenet -ti -p 6595:6595 lente
#
# Run Production Mode:
#   git clone https://github.com/sistemi-mg/scripts.git
#   cd ./public
#   docker run --net lentenet -ti -p 6595:6595 -v $(pwd):/app/public sistemicorp/lente
#
# How to get shell in container:
#   docker run -ti -p 6595:6595 -v $(pwd):/app/public --entrypoint "/bin/sh" lente
