ARG RVERSION=RVERSION
FROM raw996/dbase:${RVERSION}
MAINTAINER "Carl Boettiger and Dirk Eddelbuettel" rocker-maintainers@eddelbuettel.com

# DRAT PACKAGES FROM EUROMOMO
RUN . /etc/environment \ 
  && install2.r --error \
  MOMO 

## DRAT PACKAGES FROM RICHARD
RUN . /etc/environment \ 
  && install2.r --error \
  RAWmisc \
  org

## DRAT PACKAGES FROM FHI
RUN . /etc/environment \ 
  && install2.r --error \
  fhidata \
  fhiplot \
  fhi \
  fd \
  sykdomspuls \
  normomo \
  sykdomspulslog \
  sykdomspulspdf \
  noispiah \
  smhb \
  spread

