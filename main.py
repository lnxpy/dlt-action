from typing import List

from pyaction import PyAction

from datasources.rest import RESTfulAPI

workflow = PyAction()


def serialize_resources(resources: List[str] | str) -> List[str]:
    if isinstance(resources, str):
        return resources.split()

    return resources


@workflow.action()
def my_action(
    pipeline_name: str,
    destination: str,
    dataset_name: str,
    endpoint_url: str,
    resources: List[str] | str,
):
    data_instance = RESTfulAPI(
        pipeline_name=pipeline_name, destination=destination, dataset_name=dataset_name
    ).set_source(endpoint=endpoint_url, resources=serialize_resources(resources))

    data_instance.run_pipeline()
