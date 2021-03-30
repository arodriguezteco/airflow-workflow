airflow:
	docker run \
		-it --rm \
		--entrypoint bash \
		-v ${PWD}/dags:/opt/airflow/dags \
		-p 8080:8080 \
		-e AIRFLOW__SCHEDULER__DAG_DIR_LIST_INTERVAL=10 \
		-e AIRFLOW__WEBSERVER__EXPOSE_CONFIG=True \
		docker.pkg.github.com/arodriguezteco/airflow-docker/airflow:latest
	