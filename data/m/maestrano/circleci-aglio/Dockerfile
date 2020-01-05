FROM circleci/ruby:2.3-stretch-node

RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    graphviz

RUN sudo yarn global add aglio@2.3.0

CMD ["aglio", "-v"]
