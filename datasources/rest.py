from typing import List

import dlt
from dlt.sources.rest_api import rest_api_source


class RESTfulAPI:
    def __init__(
        self,
        pipeline_name: str,
        destination: str = "duckdb",
        dataset_name: str = "rest_api_data",
    ):
        self.pipeline = dlt.pipeline(
            pipeline_name=pipeline_name,
            destination=destination,
            dataset_name=dataset_name,
        )

    def set_source(self, endpoint: str, resources: List[str], auth_token: str = None):
        config = {
            "client": {"base_url": endpoint},
            "resources": resources,
        }

        if auth_token:
            config["auth"] = {"token": auth_token}

        self.source = rest_api_source(config)
        return self

    def run_pipeline(self) -> None:
        self.pipeline.run(self.source)
