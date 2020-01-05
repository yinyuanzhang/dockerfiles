FROM ubuntu:bionic
WORKDIR /
RUN apt-get update -y
RUN apt-get install ssh -y
RUN apt-get install mysql-client -y
# CMD mysql -u admin -p'qwer1234' -h jameswitts-db.clsfcha2sblu.us-east-1.rds.amazonaws.com -P 3306 -D teamcity
EXPOSE 22 3306
