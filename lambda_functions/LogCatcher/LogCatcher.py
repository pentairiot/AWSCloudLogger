from SQSLogger import SQSLogger
from CloudwatchLogger import CloudwatchLogger
from logging import makeLogRecord
import json


def lambda_handler(event, context):
    body = json.loads(event['body'])
    if event['pathParameters'] is not None and 'destination' in event['pathParameters'] and \
            event['pathParameters']['destination'].lower() == 'cloudwatch':
        stream_name = body['name'] if 'name' in body else 'default'
        logger = CloudwatchLogger(stream_name)
    else:
        logger = SQSLogger()
    if isinstance(body, str):
        body = json.loads(body)
    record = makeLogRecord(body)
    logger.logger.handle(record)
    return {'statusCode': 200}
