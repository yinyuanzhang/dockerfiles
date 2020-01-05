FROM bxwill/nirvana-base-img:svc
MAINTAINER Will v.stone@163.com
WORKDIR /workspace

COPY . .
RUN mkdir /book_house && \
    pip install -r requirements.txt
CMD ./launch.sh
EXPOSE 9090
