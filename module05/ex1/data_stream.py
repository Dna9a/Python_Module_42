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
        self.total_processed += 1
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
        else:
            self.internal.append(str(data))


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
        else:
            self.internal.append(data)


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
        else:
            formatted_log = ": ".join(data.values())
            self.internal.append(formatted_log)

class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break
            if not processed:
                msg = "DataStream error - Can't process element in stream: "
                print(f"{msg}{element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data\n")
            return
        for processor in self.processors:
            name = processor.__class__.__name__
            display_name = name.replace("Processor", " Processor")
            print(
                f"{display_name}: total {processor.total_processed} items "
                f"processed, remaining {len(processor.internal)} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Numeric Processor\n")
    num_proc = NumericProcessor()
    ds.register_processor(num_proc)

    test_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_messa"
             "ge": "Telnet ""access! Use ssh instead"},
            {"log_level": "INFO", "log_messag"
             "e": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("Send first batch of data on stream: " + str(test_batch))
    ds.process_stream(test_batch)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    print("Send the same batch again")
    ds.process_stream(test_batch)
    ds.print_processors_stats()

    print(
        "\nConsume some elements from the data proce"
        "ssors: " "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()
    ds.print_processors_stats()