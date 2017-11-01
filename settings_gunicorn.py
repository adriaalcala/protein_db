import os

accesslog = '-'
access_log_format = '%a %l %u %t "%r" %s %b "%{Referrer}i" "%{User-Agent}i" %Tf'    # noqa

protein_api_log = '-'
protein_api_log_format = '%a %l %u %t "%r" %s %b "%{Referrer}i" "%{User-Agent}i" %Tf'    # noqa

bind = ['0.0.0.0:8080']
workers = 4
worker_class = 'aiohttp.worker.GunicornWebWorker'
reload = True
