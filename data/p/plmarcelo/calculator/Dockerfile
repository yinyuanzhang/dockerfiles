FROM gradle:jdk8

RUN git clone https://github.com/plmarcelo/calculator.git

WORKDIR calculator

RUN gradle build

CMD ["gradle", "run"]