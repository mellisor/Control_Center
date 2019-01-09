from django.conf import settings
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from dashboard.models import Project
import channels

class Consumer(AsyncJsonWebsocketConsumer):

    # Websocket functions

    async def connect(self):
        await self.accept()
        self.rooms = list()

    async def receive_json(self, content):
        print(content)
        command = content.get('command')
        if command == 'join':
            await self.join_room(content)
        elif command == 'message':
            await self.send_room(content)
        else:
            resp = {'Error':'Command not recognized'}
            await self.send_json(resp)

    async def disconnect(self, code):
        self.rooms = None
        await self.close()

    # Helper functions

    async def join_room(self,content):
        id = content.get('id')
        key = content.get('key')
        if id is not None and key is not None:
            p = Project.objects.filter(project_id=id,secret_key=key)
            if len(p) != 0:
                p = p[0]
                self.rooms.append(p.project_id)
                await self.channel_layer.group_add(id,self.channel_name)
                await self.send_json({'join' : 'success'})
        else:
            await self.send_json({'Error' : 'Project id/key combination not found'})

    async def leave_room(self,content):
        id = content.get('id')
        if id is not None and id in self.rooms:
            await self.channel_layer.group_discard(id,self.channel_name)
            await self.send_json({'leave' : 'success'})
        else:
            await self.send_json({'Error' : 'Not in project'})

    async def send_room(self,content):
        room = content.get('project')
        if room in self.rooms:
            await self.channel_layer.group_send(
                room,
                {
                    "type" : "project.message",
                    "project_id" : room,
                    "name" : content.get('name'),
                    "value" : content.get('value'),
                }
            )
        else:
            resp = {'Error' : 'Not in project'}
            await self.send_json(resp)

    # Event handlers

    async def project_message(self,event):
        # Send message
        await self.send_json(
            {
                "msg_type" : settings.MSG_TYPE_MESSAGE,
                "project" : event["project_id"],
                event["name"] : event["value"],
            }
        )
            

