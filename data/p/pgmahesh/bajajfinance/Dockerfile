FROM java

ADD . /bajajfinanceevaluation
RUN ls -l /bajajfinanceevaluation
RUN wget https://repository.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-standalone/3.7.0/mule-standalone-3.7.0.tar.gz
RUN pwd
RUN ls -l
RUN cd /opt && tar xvzf /mule-standalone-3.7.0.tar.gz
RUN rm /mule-standalone-3.7.0.tar.gz
RUN ln -s /opt/mule-standalone-3.7.0 /opt/mule

RUN mkdir /opt/mule/apps/bajajfinanceevaluation
RUN cp /bajajfinanceevaluation/src/main/app/*.* /opt/mule/apps/bajajfinanceevaluation

RUN ls -l /opt/mule/apps/bajajfinanceevaluation
 
CMD [ "/opt/mule/bin/mule" ]
