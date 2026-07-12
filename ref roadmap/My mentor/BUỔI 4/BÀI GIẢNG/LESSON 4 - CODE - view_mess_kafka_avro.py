import json
from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer

# Cấu hình Schema Registry
schema_registry_conf = {'url': 'http://localhost:8081'}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# Lấy schema
key_schema = schema_registry_client.get_latest_version('pgserver.public.hoa_don-key').schema.schema_str
value_schema = schema_registry_client.get_latest_version('pgserver.public.hoa_don-value').schema.schema_str
key_deserializer = AvroDeserializer(schema_registry_client, key_schema)
value_deserializer = AvroDeserializer(schema_registry_client, value_schema)

# Cấu hình consumer
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-consumer-group',
    'auto.offset.reset': 'earliest',
    'key.deserializer': key_deserializer,
    'value.deserializer': value_deserializer
}
consumer = DeserializingConsumer(consumer_conf)
consumer.subscribe(['pgserver.public.hoa_don'])

# Đọc và in JSON đẹp
while True:
    try:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error()}")
            continue
        # Làm sạch dữ liệu
        key = msg.key()
        value = msg.value()
        # In JSON đẹp
        print(json.dumps({'key': key, 'value': value}, indent=2))
        print('---')
    except KeyboardInterrupt:
        break

consumer.close()
