FROM frolvlad/alpine-miniconda2
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.cloud.tencent.com/' /etc/apk/repositories && sed -i 's/http:/https:/' /etc/apk/repositories && apk --no-cache add ca-certificates openssl wget && wget -q -O - https://gist.githubusercontent.com/hetykai/5e517df165afeb9ccbcfefcbf2498c00/raw | sh
