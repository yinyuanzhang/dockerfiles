FROM circleci/python:3.6.1
ADD Pipfile .
ADD Pipfile.lock .
RUN sudo pip install -U pipenv
RUN sudo pipenv install --python 3.6.1 --system --dev --ignore-pipfile 
