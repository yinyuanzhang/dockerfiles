FROM piotrmaks/cpp

RUN set -ex; \
	apt-get update; \
	apt-get install --yes --no-install-recommends \
		clang-8 \
		clang-format-8 \
		clang-tidy-8 \
	; \
	apt-get clean; \
	update-alternatives --install /usr/bin/clang-format clang-format /usr/bin/clang-format-8 800; \
	update-alternatives --install /usr/bin/clang-tidy clang-tidy /usr/bin/clang-tidy-8 800;

ENV CC=clang-8
ENV CXX=clang++-8
