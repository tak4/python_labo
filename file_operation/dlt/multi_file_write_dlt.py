from pathlib import Path
import shutil

from pydlt import (
    ArgumentString,
    DltFileWriter,
    DltMessage,
    MessageLogInfo,
    MessageType,
    StorageHeader,
)

base_dir = Path(__file__).resolve().parent
output_dir = base_dir / "output"

if output_dir.exists():
    shutil.rmtree(output_dir)

output_dir.mkdir(exist_ok=True)

for i in range(1, 11):

    # Create DLT message
    msg1 = DltMessage.create_verbose_message(
        [ArgumentString(f"hello, pydlt! message No.{i}")],
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
    output_dlt = output_dir / Path(f"sample_{i}.dlt")
    with DltFileWriter(output_dlt) as writer:
        writer.write_messages([msg1, msg2])
