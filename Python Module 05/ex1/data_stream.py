from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    @abstractmethod
    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        ...

    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        ...


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id


class StreamProcessor:
    def __init__(self, stream: DataStream):
        self.stream = stream