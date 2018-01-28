FROM tedimaging/jmeter
RUN apt-get update \
    && apt-get install -y \
        python-dev \
        libpq-dev \
        git \
        curl \
        expect \
    && curl https://bootstrap.pypa.io/get-pip.py | python
RUN pip install requests
RUN mkdir /app
COPY . /app/
RUN chmod +x /app/run-local.sh
RUN chmod +x /app/stability.sh
WORKDIR /app
CMD ["/app/run-local.sh"]
