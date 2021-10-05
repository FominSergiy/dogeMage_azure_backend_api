import logging
import os
import json
from azure.cosmosdb.table.models import TablePermissions
import azure.functions as func
import azure.common
from azure.cosmosdb.table.tableservice import TableService

STORAGE_ACC_NAME = os.environ['STORAGE_ACC_NAME']
STORAGE_ACC_KEY = os.environ['STORAGE_ACC_KEY']
TABLE_NAME = os.environ['TABLE_NAME']


def main(req: func.HttpRequest) -> func.HttpResponse:
    ''' returns all entries for a given partition key as JSON'''

    partition_key = req.params.get('partitionKey')
 
    if partition_key is None:
        return func.HttpResponse(
            "Please specify partitionKey.",
            status_code=400
        )

    table_service = TableService(
        account_name=STORAGE_ACC_NAME,
        account_key=STORAGE_ACC_KEY
    )

    rows = table_service.query_entities(
        TABLE_NAME,
        filter=f"PartitionKey eq '{partition_key}'",
        select='UserName,Score,RowKey'
    )

    dict_rows = get_dict_rows(rows)
    logging.info(f"\nReturning following table rows:\n{json.dumps(dict_rows, indent=2)}")

    return func.HttpResponse(
        json.dumps(dict_rows),
        status_code=200
    )

def get_dict_rows(rows: azure.cosmosdb.table.common.models.ListGenerator) -> dict:
    ''' covert returned azure table obj into dict '''
    return_dict = {}
    for row in rows:
        return_dict.update({
            row.UserName : {
                "Score" : row.Score,
                "TimeStamp" : row.RowKey
            }
        })

    return return_dict
