# avro チュートリアルサイト
# https://avro.apache.org/docs/1.11.1/getting-started-python/
# ライブラリ
# https://pypi.org/project/avro/

from avro.datafile import DataFileReader
from avro.io import DatumReader

reader = DataFileReader(open("users.avro", "rb"), DatumReader())
for user in reader:
    print(user)
reader.close()
