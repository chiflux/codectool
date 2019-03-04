FROM python

RUN pip install bottle

WORKDIR /app

COPY app/ /app/

EXPOSE 8080

CMD ["python", "app.py"]
