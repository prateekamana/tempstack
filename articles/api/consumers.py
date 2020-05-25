import asyncio
import json
from django.contrib.auth import get_user_model
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from channels.db import database_sync_to_async

class ArticleConsumer(AsyncJsonWebsocketConsumer):
	async def connect(self):
		print("WebSocket Connected")
		await self.accept()

	async def receive(self, text_data=None, bytes_data=None):
		print("Sending WebSocket Text Data : ", text_data)
		print("Sending WebSocket Bytes Data : ", bytes_data)
		await self.send(text_data="Hi this is text")
		await self.send(bytes_data="Hi this is frame")

	async def disconnect(self):
		print("WebSocket Disconnected")