FROM gradle:6.0-jdk13
COPY . /home/gradle/src
WORKDIR /home/gradle/src

RUN gradle dependencies

CMD ["gradle", "run"]