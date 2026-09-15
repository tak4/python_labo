from pydlt import (
    ArgumentString,
    DltFileWriter,
    DltMessage,
    MessageLogInfo,
    MessageType,
    StorageHeader,
)

# Create DLT message
msg1 = DltMessage.create_verbose_message(
    [ArgumentString("hello, pydlt!")],
    MessageType.DLT_TYPE_LOG,
    MessageLogInfo.DLT_LOG_INFO,
    "App",
    "Ctx",
    message_counter=0,
    str_header=StorageHeader(0, 0, "Ecu"),
)
print(msg1)
# > 1970/01/01 00:00:00.000000 0 Ecu App Ctx log info verbose 1 hello, pydlt!
msg2 = DltMessage.create_non_verbose_message(
    0,
    b"\x01\x02\x03",
    message_counter=1,
    str_header=StorageHeader(0, 0, "Ecu"),
)
print(msg2)
# > 1970/01/01 00:00:00.000000 1 Ecu non-verbose [0] 010203

# Write DLT messages to file
with DltFileWriter("sample.dlt") as writer:
    writer.write_messages([msg1, msg2])
