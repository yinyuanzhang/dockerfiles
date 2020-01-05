FROM sistemicorp/dkrpybase:latest

ADD . /app
WORKDIR /app

RUN ["python", "build_compile.py", "--main", "prism", "--flask", "--lang", "3", "--compile", "--rm-source", "--name", "prism"]
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

ENTRYPOINT ["./prism"]

# Build:
#   docker build -t prism .
#
# Run Demo Mode:
#   docker run -ti -p 6590:6590 sistemicorp/prism
#
# Run Production Mode:
#   git clone https://github.com/sistemicorp/scripts.git
#   cd ./public
#   docker run -ti -p 6590:6590 -v $(pwd):/app/public sistemicorp/prism
#
# How to get shell in container:
#   docker run -ti -p 6590:6590 -v $(pwd):/app/public --entrypoint "/bin/sh" prism
