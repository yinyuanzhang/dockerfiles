FROM python:3.7
MAINTAINER MrSpinne <spinningplays.gaming@gmail.com>

COPY . .
RUN pip install -r requirements.txt

ENV POSTGRES_HOST localhost
ENV POSTGRES_PORT 5432
ENV POSTGRES_DATABASE shiro
ENV POSTGRES_USER shiro
ENV POSTGRES_PASSWORD shiro
ENV LAVALINK_HOST localhost
ENV LAVALINK_PORT 2333
ENV LAVALINK_PASSWORD shiro
ENV LAVALINK_REGION eu

CMD ["python3", "shiro.py"]