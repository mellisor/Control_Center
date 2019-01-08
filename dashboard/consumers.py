from django.conf import settings
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from dashboard.models import Project
import channels

class Consumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        self.rooms = set()


    async def join_room(self,content):
        id = content.get('id')
        key = content.get('key')
        if id is not None and key is not None:
            p = Project.objects.get(project_id=id,secret_key=key)
            if p is not None:
                self.rooms.append(p)
        print(self.rooms)
        resp = {'joined' : id}
        await self.send_json(resp)
            

    async def receive_json(self, content):
        print(content)
        command = content.get('command')
        if command == 'join':
            await self.join_room(content)
        else:
            resp = {'Error':'Command not recognized'}
            await self.send_json(resp)

    async def disconnect(self, code):
        self.rooms = None
        await self.close()
