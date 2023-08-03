FROM python:3.11

ENV HOME=/home/python/apps

COPY . $HOME/extratoclube

WORKDIR $HOME/extratoclube

RUN pip install -r requirements.txt 
RUN playwright install chromium 
RUN playwright install-deps

CMD ["echo", "hello"]