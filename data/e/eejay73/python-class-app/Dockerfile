FROM eclipse/ubuntu_python:latest

## Default pip installs

RUN sudo pip install autopep8 && sudo pip install flask

## Default port for python apps
##  Use 'http://${server.port.8081}' in Che command preview macro
EXPOSE 8081