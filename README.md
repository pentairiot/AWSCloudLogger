# AWS CloudLogger
This project allows for sending log messages from remote devices to AWS, either to a SQS FIFO queue or Cloudwatch. Additionally a library is included for managing and ingesting those logs via the python REPL.

## Deployment
Download and install [Serverless](https://serverless.com), then deploy the LogCatcher lambda

```
cd lambda_functions/LogCatcher
sls deploy
```

This sets up a Cloudwatch Log Group, an SQS FIFO queue, and an https endpoint in API Gateway. Requests sent to the https endpoint will be forwarded to either Cloudwatch or SQS (default) depending on the optional destination path parameter. 

## Usage
### Producing
Producing log messages is done by sending https requests. These should be a post with the body being the json format of a standard Python [LogRecord](https://docs.python.org/3/library/logging.html#logging.LogRecord) (i.e. you should be able to call `logging.makeRecord(**record)` on it).

```
POST /logs/{destination}
  {
    "name": "foo",
    "level": "INFO",
    "pathname": "/home/user/Foo.py",
    "lineno": 1337,
    "message": "foo",
    "args": null,
    "exc_info": null,
    "func": "Foo.foo",
    "sinfo": ""
  }
```

### Consuming
Consuming log messages can be done via the Cloudwatch interface, or if using SQS, via the Python REPL. Consuming a message deletes it from the SQS queue.

```
from SQSLogger import SQSLogger
sl = SQSLogger()
sl.consume([name])
```
