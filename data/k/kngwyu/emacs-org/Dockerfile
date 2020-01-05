# kngwyu/org-blog
FROM base/archlinux
MAINTAINER Yuji Kanagawa <yuji.kngw.80s.revive@gmail.com>
RUN pacman -Syu emacs git pygmentize --noconfirm
COPY install.el /tmp/
RUN emacs --batch --no-init-file --load /tmp/install.el --funcall install