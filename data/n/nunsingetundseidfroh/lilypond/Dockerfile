FROM ubuntu
RUN apt -qq update && apt -qq -y install wget unzip
RUN wget http://lilypond.org/download/binaries/linux-64/lilypond-2.19.82-1.linux-64.sh; \
sh lilypond-2.19.82-1.linux-64.sh --batch; \
rm lilypond-2.19.82-1.linux-64.sh
RUN wget https://bitbucket.org/georgd/eb-garamond/downloads/EBGaramond-0.016.zip; \
unzip EBGaramond-0.016.zip; \
mkdir -p $HOME/.fonts; \
cp EBGaramond-0.016/otf/*.otf $HOME/.fonts/; \
rm -r EBGaramond-0.016.zip EBGaramond-0.016
RUN apt -qq purge -y wget unzip && apt -qq autoremove -y --purge && apt -qq clean
