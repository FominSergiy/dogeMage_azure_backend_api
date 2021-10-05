import logging
import os
from datetime import datetime as dt
import azure.functions as func
import azure.common
from azure.cosmosdb.table.tableservice import TableService

STORAGE_ACC_NAME = os.environ['STORAGE_ACC_NAME']
STORAGE_ACC_KEY = os.environ['STORAGE_ACC_KEY']
TABLE_NAME = os.environ['TABLE_NAME']


def main(req: func.HttpRequest) -> func.HttpResponse:
    ''' create a new entry in table store based on params passed to the func '''
    logging.info(f'params: {req.params}')

    are_params_provided = check_for_params(req.params)
    if not are_params_provided:
        return func.HttpResponse(
            "Please specify partitionKey, userName, score in your request params",
            status_code=400
        )

    table_service = TableService(
        account_name=STORAGE_ACC_NAME,
        account_key=STORAGE_ACC_KEY
    )

    # these params will be passed in the request
    partition_key = req.params.get('partitionKey')
    user_name = req.params.get('userName')
    score = req.params.get('score')

    timestamp = dt.now().strftime('%Y-%m-%d, %H:%M:%S:%f')

    new_row = {
        'PartitionKey': partition_key,
        'RowKey': timestamp,
        'UserName' : user_name,
        'Score': score
    }
    logging.info(f'{new_row}')


    # insert a record and return 200 if success, otherwise return err and
    try:
        table_service.insert_entity(TABLE_NAME, new_row)
        return func.HttpResponse(
            "Entry Created",
            status_code=200
        )
    except azure.common.AzureConflictHttpError as err:
        # https://docs.microsoft.com/en-us/rest/api/storageservices/blob-service-error-codes
        logging.info(err)
        return func.HttpResponse(
            "The specified entity already exists.",
            status_code=409
        )
    except:
        return func.HttpResponse(
            f"Something went wrong :(",
            status_code=400
        )


def check_for_params(params: dict) -> bool:
    ''' checks if params were provided to the request '''

    partition_key = params.get('partitionKey')
    user_name = params.get('userName')
    score = params.get('score')

    if partition_key is None or user_name is None or score is None:
        return False
    else:
        return True
