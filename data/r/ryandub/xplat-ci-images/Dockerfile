FROM circleci/python:3.6-stretch
ADD requirements.txt .
RUN sudo apt-get update
RUN sudo apt-get install shellcheck
RUN sudo pip install -U pip
RUN sudo pip install -r requirements.txt 

# Circle comes with a pip installed version of poetry that doesn't play nice with preview versions we need
# We will remove it and reinstall it with the "proper" install script that vendors its dependencies
# The default home for poetry doesn't get added to the circle users path. Overridding POETRY_HOME
ENV POETRY_HOME="/home/circleci/.local"
ADD get-poetry.py .
RUN sudo pip uninstall poetry cleo -y
RUN python get-poetry.py -y
