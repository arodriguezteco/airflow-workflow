FROM apache/airflow:1.10.10-python3.6

USER root
COPY scripts/entrypoint /entrypoint
COPY scripts/dagtest.py /dagtest.py

RUN chmod +x /entrypoint

ENTRYPOINT [ "/entrypoint" ]