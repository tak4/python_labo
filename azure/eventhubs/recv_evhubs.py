# Azure Event Hubsからイベントを受信する
import os
import asyncio

from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import (
    BlobCheckpointStore,
)

storage_connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
storage_container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")
event_hub_connection_string = os.getenv("AZURE_EVENT_HUB_CONNECTION_STR")
event_hub_name = os.getenv("AZURE_EVENT_HUB_NAME")

print("AZURE_STORAGE_CONNECTION_STRING=" + storage_connection_string)
print("AZURE_STORAGE_CONTAINER_NAME=" + storage_container_name)
print("AZURE_EVENT_HUB_CONNECTION_STR=" + event_hub_connection_string)
print("AZURE_EVENT_HUB_NAME=" + event_hub_name)

async def on_event(partition_context, event):
    # Print the event data.
    print(
        'Received the event: "{}" from the partition with ID: "{}"'.format(
            event.body_as_str(encoding="UTF-8"), partition_context.partition_id
        )
    )

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)

async def main():
    # Create an Azure blob checkpoint store to store the checkpoints.
    checkpoint_store = BlobCheckpointStore.from_connection_string(
        storage_connection_string, storage_container_name
    )

    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string(
        event_hub_connection_string,
        consumer_group="$Default",
        eventhub_name=event_hub_name,
        checkpoint_store=checkpoint_store,
    )
    async with client:
        # Call the receive method. Read from the beginning of the
        # partition (starting_position: "-1")
        await client.receive(on_event=on_event, starting_position="-1")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # Run the main method.
    loop.run_until_complete(main())