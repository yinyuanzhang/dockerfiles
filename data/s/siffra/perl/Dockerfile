FROM perl:threaded

LABEL maintainer="Luiz Benevenuto <luiz@siffra.com.br>"

RUN apt-get update \
    && apt-get install -y curl procps libgmp-dev psmisc \
    && rm -fr /var/lib/apt/lists/*

RUN curl -L https://cpanmin.us | perl - --sudo App::cpanminus

RUN cpanm YAML;
RUN cpanm Log::Log4perl;
RUN cpanm Log::Dispatch::Email::MailSend;
RUN cpanm JSON::Parse;
RUN cpanm File::Slurp;
RUN cpanm Benchmark;
RUN cpanm Modern::Perl;
RUN cpanm common::sense;
RUN cpanm DDP;
RUN cpanm MIME::Lite DBI;
RUN cpanm JSON;
RUN cpanm Net::SFTP;
RUN cpanm Net::FTP;
RUN cpanm Spreadsheet::XLSX;
RUN cpanm Spreadsheet::ParseXLSX;
RUN cpanm List::Util;
RUN cpanm Digest::MD5;
RUN cpanm DateTime;
RUN cpanm Date::Parse;
RUN cpanm Text::Soundex;
RUN cpanm Net::Curl;
RUN cpanm YADA;
RUN cpanm WWW::UserAgent::Random;
RUN cpanm File::Listing;
RUN cpanm JSON::Any;
RUN cpanm Locale::Currency::Format;
RUN cpanm Date::Calc;
RUN cpanm Date::Calc::XS;
RUN cpanm Cpanel::JSON::XS;
RUN cpanm JSON::XS;
RUN cpanm File::Path;
RUN cpanm String::Similarity;
RUN cpanm File::Basename;
RUN cpanm Scalar::Util;
RUN cpanm POSIX;
RUN cpanm Data::Peek;
RUN cpanm DBD::Pg;
RUN cpanm Log::Log4perl::Appender::SMTP;
RUN cpanm Ref::Util;
RUN cpanm utf8;
RUN cpanm File::Touch;
RUN cpanm String::Util;
RUN cpanm DateTime::Format::Excel;
RUN cpanm Excel::Writer::XLSX;
RUN cpanm DBIx::Class;
RUN cpanm LWP::UserAgent LWP::Protocol::https;
RUN cpanm Encode;
RUN cpanm Try::Tiny;
RUN cpanm Text::CSV_XS;
RUN cpanm Sys::Info;
RUN cpanm Sys::Info::Constants;
RUN cpanm Params::Util;
RUN cpanm List::MoreUtils;
RUN cpanm CPAN;