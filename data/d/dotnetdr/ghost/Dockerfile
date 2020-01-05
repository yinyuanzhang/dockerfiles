FROM ghost

RUN sed -i 's/https:\/\/code.jquery.com\/jquery-1.11.3.min.js/{{asset \"js\/jquery-1.11.3.min.js\"}}/' /usr/src/ghost/content/themes/casper/default.hbs
COPY jquery-1.11.3.min.js /usr/src/ghost/content/themes/casper/assets/js/jquery-1.11.3.min.js