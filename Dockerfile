FROM Python:3:14 alpine
WORKDIR /app
COPY app.py
RUN pip install flask
CMD["Python","app.py"]
