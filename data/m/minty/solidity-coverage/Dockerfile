# minty/solidity-coverage
#

FROM minty/truffle:py2


ENV SC_VERSION="^0.5"


RUN npm install -g \
	solidity-coverage@$SC_VERSION \
	--unsafe

ENTRYPOINT ["/.npm/bin/solidity-coverage"]
