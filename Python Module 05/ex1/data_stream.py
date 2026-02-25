from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
    ) -> List[Any]:
        if not criteria:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.__class__.__name__,
            "processed_count": len(getattr(self, "_processed", []))
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        self._processed = data_batch
        avg_temp = (
            sum([item["temp"] for item in data_batch]) / len(data_batch)
        ) if data_batch else 0
        return (
            f"Sensor analysis: {len(data_batch)} readings processed, "
            f"avg temp: {avg_temp:.2f}°C"
        )


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        self._processed = data_batch
        error_count = sum(1 for e in data_batch if e == "error")
        return (
            f"Event analysis: {len(data_batch)} events, "
            f"{error_count} error(s) detected"
        )


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        self._processed = data_batch
        net_flow = sum([
            item.get("buy", 0) - item.get("sell", 0) for item in data_batch
        ])
        return (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: {net_flow} units"
        )


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream):
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]):
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")

        for i in range(len(self.streams)):
            stream = self.streams[i]
            batch = batches[i]

            if isinstance(stream, SensorStream):
                criteria = "temp"
            elif isinstance(stream, TransactionStream):
                criteria = "buy"
            elif isinstance(stream, EventStream):
                criteria = "error"
            else:
                criteria = None

            filtered_batch = stream.filter_data(batch, criteria)
            result = stream.process_batch(filtered_batch)

            if isinstance(stream, SensorStream):
                data_name = "Sensor data"
            elif isinstance(stream, TransactionStream):
                data_name = "Transaction data"
            elif isinstance(stream, EventStream):
                data_name = "Event data"
            else:
                data_name = "Data"

            print(f"Batch {i + 1} Results:")
            print(f"- {data_name}: {len(filtered_batch)} items processed")
            print(f"Detail: {result}\n")

        print(
            "All streams processed successfully. Nexus throughput optimal.\n"
        )


def get_header(data_batch: List[Any]) -> str:
    data = [
        f"{k}:{v}" for item in data_batch for k, v in item.items()
    ]
    data = (
        "["
        + ", ".join(data)
        + "]"
    )
    return data


def main():
    print("=== CODE NEXUS - DATA STREAM PROCESSOR ===")
    sensor_data = [{"temp": 22.5}, {"temp": 24}, {"temp": 21}]
    event_data = ["start", "error", "stop", "error", "restart"]
    transaction_data = [{"buy": 100}, {"sell": 50}, {"buy": 200}]

    print("\nInitializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    sensor_stats = sensor_stream.get_stats()
    print(
        f"Stream ID: {sensor_stats['stream_id']}, "
        f"Type: {sensor_stats['stream_type']}, "
        f"Processed Count: {sensor_stats['processed_count']}"
    )
    header = get_header(sensor_data)
    print(f"Processing sensor batch: {header}")
    print(sensor_stream.process_batch(sensor_data))

    print()

    print("Initializing Event Stream...")
    event_stream = EventStream("EVENT_002")
    event_stats = event_stream.get_stats()
    print(
        f"Stream ID: {event_stats['stream_id']}, "
        f"Type: {event_stats['stream_type']}, "
        f"Processed Count: {event_stats['processed_count']}"
    )
    header = str(event_data)
    print(f"Processing event batch: {header}")
    print(event_stream.process_batch(event_data))

    print()

    print("Initializing Transaction Stream...")
    transaction_stream = TransactionStream("TRANSACTION_003")
    transaction_stats = transaction_stream.get_stats()
    print(
        f"Stream ID: {transaction_stats['stream_id']}, "
        f"Type: {transaction_stats['stream_type']}, "
        f"Processed Count: {transaction_stats['processed_count']}"
    )
    header = get_header(transaction_data)
    print(f"Processing transaction batch: {header}")
    print(transaction_stream.process_batch(transaction_data))

    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(event_stream)
    processor.add_stream(transaction_stream)

    processor.process_all(
        batches=[sensor_data, event_data, transaction_data]
    )


if __name__ == "__main__":
    main()
