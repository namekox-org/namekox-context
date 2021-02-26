# Install
```shell script
pip install -U namekox-context
```

# Example
> ping.py
```python
# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


from namekox_webserver.core.entrypoints.app import app
from namekox_context.core.dependencies import ContextHelper


class Ping(object):
    name = 'ping'

    ctx = ContextHelper()

    @app.api('/api/context/', methods=['GET'])
    def context(self, request):
        return self.ctx.data
```

# Running
> config.yaml
```yaml
WEBSERVER:
  host: 0.0.0.0
  port: 80
```
> namekox run ping
```shell script
2020-12-01 14:25:00,878 DEBUG load container class from namekox_core.core.service.container:ServiceContainer
2020-12-01 14:25:00,878 DEBUG starting services ['ping']
2020-12-01 14:25:00,879 DEBUG starting service ping entrypoints [ping:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:context, ping:namekox_webserver.core.entrypoints.app.server.WebServer:server]
2020-12-01 14:25:00,880 DEBUG spawn manage thread handle ping:namekox_webserver.core.entrypoints.app.server:handle_connect(args=(), kwargs={}, tid=handle_connect)
2020-12-01 14:25:00,881 DEBUG service ping entrypoints [ping:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:context, ping:namekox_webserver.core.entrypoints.app.server.WebServer:server] started
2020-12-01 14:25:00,881 DEBUG starting service ping dependencies [ping:namekox_context.core.dependencies.ContextHelper:ctx]
2020-12-01 14:25:00,881 DEBUG service ping dependencies [ping:namekox_context.core.dependencies.ContextHelper:ctx] started
2020-12-01 14:25:00,882 DEBUG services ['ping'] started
2020-12-01 14:25:28,750 DEBUG spawn manage thread handle ping:namekox_webserver.core.entrypoints.app.server:handle_request(args=(<eventlet.greenio.base.GreenSocket object at 0x110800c50>, ('127.0.0.1', 50695)), kwargs={}, tid=handle_request)
2020-12-01 14:25:31,816 DEBUG spawn worker thread handle ping:context(args=(<Request 'http://127.0.0.1/api/context/' [GET]>,), kwargs={}, context={})
127.0.0.1 - - [01/Dec/2020 14:25:31] "GET /api/context/ HTTP/1.1" 200 292 0.002656
^C2020-12-01 14:25:36,177 DEBUG stopping services ['ping']
2020-12-01 14:25:36,178 DEBUG stopping service ping entrypoints [ping:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:context, ping:namekox_webserver.core.entrypoints.app.server.WebServer:server]
2020-12-01 14:25:36,179 DEBUG wait service ping entrypoints [ping:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:context, ping:namekox_webserver.core.entrypoints.app.server.WebServer:server] stop
2020-12-01 14:25:36,179 DEBUG service ping entrypoints [ping:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:context, ping:namekox_webserver.core.entrypoints.app.server.WebServer:server] stopped
2020-12-01 14:25:36,179 DEBUG stopping service ping dependencies [ping:namekox_context.core.dependencies.ContextHelper:ctx]
2020-12-01 14:25:36,180 DEBUG service ping dependencies [ping:namekox_context.core.dependencies.ContextHelper:ctx] stopped
2020-12-01 14:25:36,180 DEBUG services ['ping'] stopped
2020-12-01 14:25:36,180 DEBUG killing services ['ping']
2020-12-01 14:25:36,181 DEBUG service ping already stopped
2020-12-01 14:25:36,181 DEBUG services ['ping'] killed
```
> curl http://127.0.0.1/api/context/
```json
{
    "errs": "",
    "code": "Request:Success",
    "data": {
        "parent_call_id": null,
        "call_id": "c76e5230-4a7b-4712-b03b-18f5070a115e"
    },
    "call_id": "c76e5230-4a7b-4712-b03b-18f5070a115e"
}
```
