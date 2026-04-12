from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.internal: list[str] = []
        self.processing_rank = 0
        self.total_processed = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.internal:
            raise IndexError("No data to output")
        data = self.internal.pop(0)
        rank = self.processing_rank
        self.processing_rank += 1
        return rank, data


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return isinstance(data, (int, float))

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            self.internal += [str(item) for item in data]
            self.total_processed += len(data)
        else:
            self.internal.append(str(data))
            self.total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            self.internal += data
            self.total_processed += len(data)
        else:
            self.internal.append(data)
            self.total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items()
                )
                for item in data
            )
        return isinstance(data, dict) and all(
            isinstance(k, str) and isinstance(v, str) for k, v in data.items()
        )

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for entry in data:
                formatted_log = ": ".join(entry.values())
                self.internal.append(formatted_log)
                self.total_processed += 1
        else:
            formatted_log = ": ".join(data.values())
            self.internal.append(formatted_log)
            self.total_processed += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"  Trying to validate input '42': {num_proc.validate(42)}")
    print(f"  Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print("  Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except ValueError as e:
        print(f"  Got exception: {e}")

    test_nums = [1, 2, 3, 4, 5]
    print(f"  Processing data: {test_nums}")
    num_proc.ingest(test_nums)

    print("  Extracting 3 values...")
    for i in range(3):
        rank, val = num_proc.output()
        print(f"  Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"  Trying to validate input '42': {text_proc.validate(42)}")
    test_text = ["Hello", "Nexus", "World"]
    print(f"  Processing data: {test_text}")
    text_proc.ingest(test_text)
    print("  Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"  Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"  Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    test_logs = [
        {"  log_level": "NOTICE", "log_message": "Connection to server"},
        {"  log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"  Processing data: {test_logs}")
    log_proc.ingest(test_logs)
    print("  Extracting 2 values...")
    for i in range(2):
        rank, val = log_proc.output()
        print(f"  Log entry {rank}: {val}")
