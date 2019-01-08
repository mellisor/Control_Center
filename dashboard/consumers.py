from django.conf import settings
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from dashboard.models import Room
import channels

class Consumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        self.rooms = set()

    async def receive_json(self, content):
        print(content)
        print(channels.layers.get_channel_layer())
        await self.channel_layer.group_send(
            "HI",
            {"what" : "is up"},
        )

    async def disconnect(self, code):
        self.rooms = None
        await self.close
