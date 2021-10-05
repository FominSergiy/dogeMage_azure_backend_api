# Scoreboard built on Azure

## Azure Functions

> This repo contains code used to deploy 2 Azure Functions. Functions are used to perform HTTP GET and POST.

## Repo Structure

> A lot of it came pre-built by Azure extension. Both functions use Python 3.8 as their runtime environment.

```
    .
    |__PostNewScore
    |    |____init__.py     <<-- function used to post a new score to the Table Storage on Azure
    |    |__function.json   <<-- function definition (provided by Azure)
    |
    |__ReturnTableResults
    |    |____init__.py      <<-- function used to return all records for a given partition key
    |
    |__requirements.txt      <<-- packages needed for functions to run.

```

## Resources

- [How To Work With Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/)
- [More on Azure Functions](https://docs.microsoft.com/en-us/learn/modules/azure-compute-fundamentals/azure-functions)
- [More on Azure Table Storage](https://docs.microsoft.com/en-us/learn/modules/explore-non-relational-data-offerings-azure/2-explore-azure-table-storage)
- [Environment Variables Config](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal)
- [More on Azure](https://docs.microsoft.com/en-gb/learn/paths/az-900-describe-cloud-concepts/)

## Requirements

- vsCode
- Azure Extension for VsCode
- make sure you have defined env variables for your given azure function
