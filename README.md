## dltHub Loading Action <img alt="action-badge" src="https://img.shields.io/badge/dlt Action-white?logo=github-actions&label=GitHub%20Action&labelColor=white&color=0064D7"> <a href="https://github.com/lnxpy/pyaction"><img alt="pyaction" src="https://img.shields.io/badge/PyAction-white?label=Made%20with&labelColor=white&color=0064D7"></a>

This action fetches RESTful resources into your repositories. A good solution for packages and libraries that utilize data resources into their pipelines.

### Usage
```yml
jobs:
  Test:
    runs-on: ubuntu-latest
    name: Testing the action
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Fetching the data
        uses: lnxpy/dlt-action@main
        with:
          pipeline_name: rest_api_pokemon
          destination: duckdb
          dataset_name: rest_api_data
          endpoint_url: https://pokeapi.co/api/v2/
          resources: pokemon berry location

      - uses: EndBug/add-and-commit@v9
        with:
          default_author: github_actions
          message: 'data updated'
```

### License
MIT