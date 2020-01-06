FROM python:3.6-alpine3.7

RUN pip install grip
RUN cd /home && touch test.md \
      && grip test.md --export test.html && rm test.*

EXPOSE 6419
WORKDIR /home
ENTRYPOINT ["grip"]
