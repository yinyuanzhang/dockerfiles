FROM ubuntu 

RUN sudo apt-get update && sudo apt-get -y install mailutils

CMD ["echo 'Jenkins is up' | mailx -s 'test j is up' enzotrout@gmail.com"]

EXPOSE 80 443 
