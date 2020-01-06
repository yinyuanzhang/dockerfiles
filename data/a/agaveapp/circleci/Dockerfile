FROM circleci/ruby:2.6.5-node-browsers
RUN sudo apt-get update
RUN sudo apt-get install fonts-migmix
RUN sudo wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
RUN sudo tar xvf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
RUN sudo mv wkhtmltox/bin/wkhtmlto* /usr/bin/
RUN sudo ln -nfs /usr/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf

