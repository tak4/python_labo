# Azure Event Hubsへイベントを送信する
import os
import asyncio

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient

# 環境変数 EVENT_HUB_CONNECTION_STR に接続文字列を設定しておく
# 環境変数 EVENT_HUB_NAME にEventHubs の名前を設定しておく
# Linuxの場合
# export AZURE_STORAGE_CONNECTION_STRING=""
# 接続文字列は、ストレージアカウント＞アクセスキー で取得する
event_hub_connection_string = os.getenv("AZURE_EVENT_HUB_CONNECTION_STR")
event_hub_name = os.getenv("AZURE_EVENT_HUB_NAME")

print("AZURE_EVENT_HUB_CONNECTION_STR=" + event_hub_connection_string)
print("AZURE_EVENT_HUB_NAME=" + event_hub_name)

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(
        conn_str=event_hub_connection_string, eventhub_name=event_hub_name
    )
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData("First event "))
        event_data_batch.add(EventData("Second event"))
        event_data_batch.add(EventData("Third event"))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

asyncio.run(run())