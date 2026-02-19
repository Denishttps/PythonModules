from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def format_output(self, result: str) -> str:
        return "[OUTPUT] " + result


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        print(self.format_output("Processing data: \"Hello Nexus World\""))
        if self.validate(data):
            return self.format_output(
                f"Processed text: {len(data)} characters, "
                f"{len(data.split(" "))} words"
            )
        raise TypeError(f"Musst be str not {data.__class__.__name__}")

    def validate(self, data) -> bool:
        print(self.format_output("Validation: Text data verified"))
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class NumericProcessor(DataProcessor):
    def process(self, data: list[int]) -> str:
        print(self.format_output(f"Processing data: {data}"))
        if self.validate(data):
            return self.format_output(
                f"Processed {len(data)} numeric values, "
                f"sum={sum(data)}, avg={sum(data) / len(data)}"
            )
        raise TypeError("Musst be list of int")

    def validate(self, data: list[int]) -> bool:
        print(self.format_output("Validation: Numeric data verified"))
        if not isinstance(data, list):
            return False
        if not all(isinstance(i, int) for i in data):
            return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def format_output(self, result: str) -> str:
        return f"[LOG] {result}"

    def process(self, data: str) -> str:
        print(self.format_output(f"Processing data: {data}"))
        if self.validate(data):
            return self.format_output(data)
        raise ValueError("Str is empty!")

    def validate(self, data: str) -> bool:
        print(self.format_output("Validation: Log entry verified"))
        return bool(data)


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("Initializing Numeric Processor...")
    num = NumericProcessor()
    print(num.process([1, 2, 3, 4, 5]))

    print()

    print("Initializing Text Processor...")
    string = TextProcessor()
    print(string.process("Hello Nexus World"))

    print()

    print("Initializing Log Processor...")
    log = LogProcessor()
    print(log.process("ERROR: Connection timeout"))

    print("\n== Polymorphic Processing Demo ===")


if __name__ == "__main__":
    main()
