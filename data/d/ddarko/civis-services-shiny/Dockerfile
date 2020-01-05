FROM civisanalytics/datascience-r:latest


RUN apt-get update && apt-get install -y \
    git

# required for R package rgdal
RUN apt-get  update && apt-get install -y \  	
    libgdal-dev

# required for R package rgdal	    
RUN apt-get  update && apt-get install -y \  
    libproj-dev 

# required for R package rgeos	        
RUN apt-get  update && apt-get install -y \  
    libgeos++-dev

# required for R package units	
RUN apt-get  update && apt-get install -y \    
    libudunits2-dev

# required for R package jqr	    
RUN apt-get  update && apt-get install -y \    
	libjq-dev

# required for R package protolite	
RUN apt-get  update && apt-get install -y \   	
	libprotobuf-dev

# required for R package protolite	
RUN apt-get  update && apt-get install -y \   		
	protobuf-compiler

# Update R	
RUN apt-get  update && apt-get install -y \  
    r-base

# update R    
RUN apt-get  update && apt-get install -y \ 
    r-base-dev

# OpenBlas library to get higher performance for linear algebra operations
RUN apt-get  update && apt-get install -y \     
    libopenblas-base  
    	
# Required for updating R packages 
RUN apt-get  update && apt-get install -y \ 
    dialog
    
# update R packages 
RUN Rscript -e  "update.packages( ask = FALSE )"

# test CRAN.  Default mirror does not include packages  ‘urca’, ‘formattable’, ‘DT’ 
# RUN Rscript -e  "install.packages( 'urca' , repos='http://cran.us.r-project.org' )"

# install R packages
COPY ./requirements.txt /requirements.txt
RUN Rscript -e "packages <- readLines('/requirements.txt'); install.packages( packages , repos='http://cran.us.r-project.org' )"


# Shiny folder and default app
COPY ./app/app.r ./app/app.r
COPY entrypoint.sh /


EXPOSE 3838

ENTRYPOINT ["/entrypoint.sh"]
