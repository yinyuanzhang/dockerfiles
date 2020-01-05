FROM python:3.7.4

LABEL maintainer "ritsuki1227 <ritsuki1227@gmail.com>"

RUN apt-get update \
  && apt-get install -y build-essential git less openjdk-11-jre vim

# install mecab
RUN apt-get install -y mecab \
                       libmecab-dev \
                       mecab-ipadic-utf8 \ 
  && apt-get clean \ 
  && rm -rf /var/lib/apt/lists/*

# install neologd
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git /tmp/neologd \
  && cd /tmp/neologd \
  && ./bin/install-mecab-ipadic-neologd -n -u -y \
  && rm -rf /tmp/neologd \
  && sed -i -e "/^dicdir = /c dicdir = \/usr\/lib\/x86_64-linux-gnu\/mecab\/dic\/mecab-ipadic-neologd" /etc/mecabrc

# install crf++
RUN CRFPP_ID=0B4y35FiV1wh7QVR6VXJ5dWExSTQ \ 
  && CRFPP_NAME=CRF++-0.58 \ 
  && CRFPP_EXT=.tar.gz \ 
  && curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${CRFPP_ID}" > /dev/null \
  && CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)" \
  && curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${CRFPP_ID}" -o /tmp/crf++/$CRFPP_NAME$CRFPP_EXT --create-dirs \
  && cd /tmp/crf++ \
  && tar zxf $CRFPP_NAME$CRFPP_EXT \ 
  && cd $CRFPP_NAME \
  && ./configure \ 
  && make \ 
  && make install \ 
  && cd / \ 
  && rm -rf /tmp/crf++ \
  && sed -i -e '$a include /usr/local/lib' /etc/ld.so.conf \ 
  && ldconfig

# install cabocha
RUN CABOCHA_ID=0B4y35FiV1wh7SDd1Q1dUQkZQaUU \
  && CABOCHA_NAME=cabocha-0.69 \
  && CABOCHA_EXT=.tar.bz2 \ 
  && curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${CABOCHA_ID}" > /dev/null \
  && CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)" \
  && curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${CABOCHA_ID}" -o /tmp/cabocha/$CABOCHA_NAME$CABOCHA_EXT --create-dirs \
  && cd /tmp/cabocha \
  && tar -jxvf $CABOCHA_NAME$CABOCHA_EXT \ 
  && cd $CABOCHA_NAME \ 
  && ./configure --with-mecab-config=`which mecab-config` --with-charset=UTF8 --with-posset=juman \ 
  && make \
  && make install \ 
  && ldconfig \ 
  && cd python \
  && python setup.py install \
  && cd / \
  && rm -rf /tmp/cabocha

# install Stanford CoreNLP
RUN STANFORD_CORENLP=stanford-corenlp-full-2018-10-05 \ 
  && wget http://nlp.stanford.edu/software/$STANFORD_CORENLP.zip -P /tmp/ \  
  && unzip /tmp/$STANFORD_CORENLP.zip -d /usr/local/lib/ \
  && rm /tmp/$STANFORD_CORENLP.zip
EXPOSE 9000 

# install python packages
COPY requirements.txt /tmp/.
RUN pip install -r /tmp/requirements.txt --no-cache-dir \
  && rm /tmp/requirements.txt \ 
  && jupyter notebook --generate-config \ 
  && sed -i -e "s/#c.NotebookApp.ip = 'localhost'/c.NotebookApp.ip = '0.0.0.0'/" /root/.jupyter/jupyter_notebook_config.py \ 
  && sed -i -e "s/#c.NotebookApp.allow_root = False/c.NotebookApp.allow_root = True/" /root/.jupyter/jupyter_notebook_config.py \ 
  && sed -i -e "s/#c.NotebookApp.allow_remote_access = False/c.NotebookApp.allow_remote_access = True/" /root/.jupyter/jupyter_notebook_config.py
EXPOSE 8888

# install StanfordNLP
RUN python -c "import stanfordnlp; stanfordnlp.download('en', force=True)"
ENV CORENLP_HOME=/usr/local/lib/stanford-corenlp-full-2018-10-05

# install NLTK
RUN python -c "import nltk; nltk.download('stopwords', force=True)"
