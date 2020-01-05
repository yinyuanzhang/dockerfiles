FROM python:3.6.3
ENV PYTHONUNBUFFERED 1

# Change Timezone to GMT+7
ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
    && apt-get install -y gettext\
    && pip install pipenv

WORKDIR /ton/dev

# COPY Pipfile Pipfile.lock ./

COPY ./djang/  .

RUN pipenv install --system --dev

EXPOSE 8000

# CMD echo $(ls)
# RUN python manage.py runserver 0.0.0.0:8000
CMD python manage.py runserver 0.0.0.0:8000

# docker image build -t pyjango01:1.0.1 .
# docker container run -p 8000:8000  pyjango01:1.0.1 python manage.py runserver 0.0.0.0:8000

# docker tag <source>:<tag> <destinationhub>:<tag> 
# docker tag <destinationhub>:<tag> 
