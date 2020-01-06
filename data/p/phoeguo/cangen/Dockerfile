FROM frolvlad/alpine-python-machinelearning

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/cancerPortal

# install sqlite
#RUN apk update \
#    && apk --no-cache --update-cache add sqlite

# install dependencies
#COPY ./Pipfile /usr/src/cancerPortal/Pipfile
#RUN pip install --upgrade pip \
#    && pip install pipenv \
#    && pipenv install --skip-lock --system --dev
COPY ./requirements.txt /usr/src/cancerPortal/requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

# copy project
COPY . /usr/src/cancerPortal/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/cancerPortal/entrypoint.sh"]