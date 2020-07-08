from SQSLogger import SQSLogger
from CloudwatchLogger import CloudwatchLogger
from logging import makeLogRecord
import json
import os

group_name = 'CloudLogger'
if 'GROUP_NAME' in os.environ:
    group_name = os.environ['GROUP_NAME']


def lambda_handler(event, context):
    body = json.loads(event['body'])
    if isinstance(body, str):
        body = json.loads(body)
    if event['pathParameters'] is not None and 'destination' in event['pathParameters'] and \
            event['pathParameters']['destination'].lower() == 'sqs':
        logger = SQSLogger()
    else:
        stream_name = body['name'] if 'name' in body else 'default'
        logger = CloudwatchLogger(stream_name, group_name)
    record = makeLogRecord(body)
    logger.logger.handle(record)
    return {'statusCode': 200}
