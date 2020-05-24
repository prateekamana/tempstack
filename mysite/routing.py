from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from articles.api import consumers

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
    	URLRouter([
    		path('api/', consumers.ArticleConsumer)

    		])
    )
})