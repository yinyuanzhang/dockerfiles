
FROM mono:5.12.0.226

RUN apt update \
    && apt install -y \
        python3-pip \
        git \
        wget \
        unzip


RUN pip3 install --upgrade setuptools pip && pip3 install jupyter

WORKDIR /
#RUN git clone https://github.com/fsprojects/IfSharp.git
RUN mkdir IfSharp
RUN mkdir notebooks
VOLUME notebooks

RUN useradd -ms /bin/bash ifsharp-user
RUN chown -R ifsharp-user /notebooks && chown -R ifsharp-user /IfSharp
USER ifsharp-user

WORKDIR /IfSharp
RUN wget https://github.com/fsprojects/IfSharp/releases/download/v3.0.0-beta3/IfSharp.v3.0.0-beta3.zip
RUN unzip IfSharp.v3.0.0-beta3.zip
RUN mono ifsharp.exe --install

EXPOSE 8888

ENTRYPOINT ["jupyter", \
            "notebook", \
            "--no-browser", \
            "--ip='*'", \
            "--port=8888", \
            "--notebook-dir=/notebooks" \
            ]
