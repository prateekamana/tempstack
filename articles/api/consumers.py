import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer

from channels.db import database_sync_to_async

class ArticleConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		print('ws connected', event)
		await self.send({
            "type": "websocket.accept",
        })


	async def websocket_receive(self, event):
		print('ws receive', event)
		await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })

	async def websocket_disconnect(self, event):
		print('ws disconnected', event)
		await self.send({
            "type": "websocket.close",
        })