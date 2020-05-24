import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer

from channels.db import database_sync_to_async

class ArticleConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		print('ws connected', event)

	async def websocket_receive(self, event):
		print('ws receive', event)

	async def websocket_disconnect(self, event):
		print('ws disconnected', event)