FROM docker.elastic.co/elasticsearch/elasticsearch:6.5.4
MAINTAINER Tobias L. Maier <tobias.maier@baucloud.com>

RUN elasticsearch-plugin install --batch analysis-phonetic
RUN true \
  && mkdir -p config/german/dictionaries \
  && curl -sSL --output "german-decompounder.zip" "https://github.com/uschindler/german-decompounder/archive/master.zip" \
  && unzip "german-decompounder.zip" -x "german-decompounder-master/NOTICE.txt" "german-decompounder-master/README.md" \
  && mv german-decompounder-master/* config/german/dictionaries/ \
  && rmdir "german-decompounder-master" \
  && rm -f "german-decompounder.zip"
