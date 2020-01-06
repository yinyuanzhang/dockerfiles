FROM tensorflow/tensorflow:1.13.1-py3
RUN pip install bert-serving-server
RUN apt-get install -y wget
RUN apt-get install unzip



COPY ./ /app
COPY ./entrypoint.sh /app
EXPOSE 5555
EXPOSE 5556
WORKDIR /app
RUN wget https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip
RUN unzip uncased_L-12_H-768_A-12.zip
RUN rm -rf model/ && mv uncased_L-12_H-768_A-12 model/

RUN ls
ENTRYPOINT ["/app/entrypoint.sh"]
RUN ["chmod", "+x", "/app/entrypoint.sh"]
CMD []
