FROM debian:stretch

WORKDIR /tmp

COPY . .

RUN apt-get update && apt-get install -y toilet && bash +x script.sh

#ENTRYPOINT ["bash", "+x", "script.sh"]
CMD echo "le code est quelque part par la...."

