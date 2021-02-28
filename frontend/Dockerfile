FROM python:3.6

EXPOSE 3000

WORKDIR /

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY templates /
COPY static/stylesheets /

COPY app.py /
CMD python app.py