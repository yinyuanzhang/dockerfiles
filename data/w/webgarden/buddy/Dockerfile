FROM webgarden/php

ADD processUrl.sh /usr/bin/processUrl
RUN chmod +x /usr/bin/processUrl

## Test it

RUN echo $(bash /usr/bin/processUrl "aym" "ft/branche" "neco.cz") \
	&& echo $(bash /usr/bin/processUrl "aym" "ft/branche-with-name" "neco.cz") \
	&& echo $(bash /usr/bin/processUrl "aym" "1.2.3" "neco.cz") \
	&& echo $(bash /usr/bin/processUrl "aym" "v1.2.3" "neco.cz") \
	&& echo $(bash /usr/bin/processUrl "aym" "develop" "neco.cz") \
	&& echo $(bash /usr/bin/processUrl "aym" "master" "neco.cz")
