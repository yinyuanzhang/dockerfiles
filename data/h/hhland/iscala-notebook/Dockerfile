FROM java:7

RUN mkdir /d

WORKDIR /d

ENV P_HOME /d/program

RUN apt-get update && apt-get install -y curl git wget vim unzip 

RUN  mkdir /d/download && mkdir /d/git && mkdir $P_HOME

#scala
RUN cd download && wget http://downloads.typesafe.com/scala/2.11.4/scala-2.11.4.tgz && tar -xvf scala-2.11.4.tgz && mv  scala-2.11.4 $P_HOME 
ENV SCALA_HOME $P_HOME/scala-2.11.4

#python
RUN apt-get install -y libbz2-dev libgdbm-dev liblzma-dev libreadline-dev libsqlite3-dev libssl-dev tcl-dev tk-dev dpkg-dev libzmq3-dev 
RUN wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz && tar -xvf Python-2.7.8.tgz && mv Python-2.7.8 $P_HOME && cd $P_HOME/Python-2.7.8 && ./configure && make && make install && cd -
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python  && easy_install pip
RUN pip install ipython[notebook] 
#RUN wget https://dl.bintray.com/sbt/native-packages/sbt/0.13.7/sbt-0.13.7.tgz && tar -xvf sbt-0.13.7.tgz && mv sbt $P_HOME/sbt-0.13.7
#ENV SBT_HOME $P_HOME/sbt-0.13.7

ENV PATH $PATH:$SCALA_HOME/bin


#RUN cd git &&  git clone https://github.com/mattpap/IScala.git && cd IScala && sbt compile package

RUN cd download && wget https://github.com/mattpap/IScala/releases/download/v0.1/IScala-0.1.tgz  && tar -xvf IScala-0.1.tgz 

RUN ipython profile create scala && mkdir notebook &&  cd /root/.ipython/profile_scala && mv ipython_config.py ipython_config.py.bak && mv static/custom/custom.js static/custom/custom.js.bak && mv static/custom/custom.css static/custom/custom.css.bak
#&& cp -r git/IScala/examples/*  notebook 

ADD https://raw.githubusercontent.com/hhland/IScala/master/examples/Display.ipynb  /d/notebook/Display.ipynb

ADD add/start-notebook.sh /d/download/IScala-0.1/bin/
RUN chmod +x /d/download/IScala-0.1/bin/start-notebook.sh

ADD add/custom.js //root/.ipython/profile_scala/static/custom/
ADD add/custom.css //root/.ipython/profile_scala/static/custom/
ADD add/Display.ipynb  /d/notebook/

#ADD ipython_config.py //.ipython/profile_scala/ipython_config.py

EXPOSE 8888

CMD /d/download/IScala-0.1/bin/start-notebook.sh

#CMD ipython notebook --ip=0.0.0.0 --profile scala --notebook-dir=/d/notebook


