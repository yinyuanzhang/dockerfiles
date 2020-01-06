FROM omp4j/omp4j

EXPOSE 9000

# prepare app
WORKDIR /www
COPY . .
RUN ln -s /omp4j ./omp4j

# compile app
RUN sbt compile

# run app
CMD sbt run
