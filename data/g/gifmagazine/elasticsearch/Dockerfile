FROM blacktop/elasticsearch:6.6

RUN bin/elasticsearch-plugin install analysis-kuromoji
RUN bin/elasticsearch-plugin install analysis-icu
RUN bin/elasticsearch-plugin install --batch org.codelibs:elasticsearch-analysis-kuromoji-neologd:6.5.1
