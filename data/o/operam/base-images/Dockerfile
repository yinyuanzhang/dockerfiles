FROM heroku/heroku:18-build

WORKDIR /src

ADD install_puppeteer_dependencies.sh install_puppeteer_dependencies.sh
RUN ./install_puppeteer_dependencies.sh

ADD install_node.sh install_node.sh
RUN ./install_node.sh

ADD install_yarn.sh install_yarn.sh
RUN ./install_yarn.sh
