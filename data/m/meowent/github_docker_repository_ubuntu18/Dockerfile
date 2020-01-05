FROM ubuntu:18.04

COPY Im_cute_text_document.text Im_cute_bash_script.sh /meowent/

WORKDIR /meowent

RUN chmod +x "Im_cute_bash_script.sh"

RUN apt update && apt-get update

CMD cat Im_cute_text_document.text && ./Im_cute_bash_script.sh && /bin/bash && echo lu I love you
