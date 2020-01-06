FROM mongo

RUN mkdir -p /data/archive
COPY archive/amelie_oss.gz /data/archive/amelie_oss.gz
COPY archive/docclassifier.gz /data/archive/docclassifier.gz
COPY archive/docclustering.gz /data/archive/docclustering.gz
COPY archive/syncpipes.gz /data/archive/syncpipes.gz

CMD mongorestore --host mongo --port 27017 --drop --gzip --archive=/data/archive/amelie_oss.gz --db amelie_oss; mongorestore --host mongo --port 27017 --drop --gzip --archive=/data/archive/docclassifier.gz --db docclassifier; mongorestore --host mongo --port 27017 --drop --gzip --archive=/data/archive/docclustering.gz --db docclustering; mongorestore --host mongo --port 27017 --drop --gzip --archive=/data/archive/syncpipes.gz --db syncpipes;