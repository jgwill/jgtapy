FROM jgwill/ubuntu:18.04-py3.7.2-ml-lzma

RUN apt remove python2.7 python3.6  libpython2.7 libpython2.7-dev libpython2.7-minimal libpython2.7-stdlib python2.7-minimal -y && \
 apt autoremove -y

RUN apt remove libpython3.6 libpython3.6-minimal python3-minimal python3.6-minimal -y && \
   apt autoremove -y

RUN ln -sf /usr/local/bin/python3.7 /usr/local/bin/python3
RUN ln -sf /usr/local/bin/python3.7 /usr/local/bin/python
RUN git config --global --add safe.directory /work
