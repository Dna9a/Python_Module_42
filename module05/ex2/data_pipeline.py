from abc import ABC, abstractmethod
from typing import Any
import typing


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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
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
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
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
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()
    ds.print_processors_stats()



'''

Authorized: builtins, standard types, import typing, import abc
Engineering Briefing: Your final challenge is to integrate everything into a complete
data processing pipeline that demonstrates mastery of polymorphic architecture at an
enterprise scale.
Use your code from Exercise 1 and improve it in order to obtain a complete data pipeline.
Your DataStream class already handles input streams correctly. You need now to handle
the output part of the pipeline. This will be achieved by using a plugin system for export
classes, made export-compatible through duck typing.
Implement the following:
• A new ExportPlugin class that inherits from the special Protocol class.
• This class will define the following method, which will act as a constraint for each
export plugin:
def process_output(self, data: list[tuple[int, str]]) -> None:
The type of the data parameter is a list of tuples that matches the return value of
the output method from the DataProcessor class.
• The DataStream class will now implement the
def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
method, to be used after calling process_stream, that will consume nb elements
from all registered data processors and export them using the provided compatible
plugin.
• Create at least a CSV export plugin and a JSON export plugin. No need to use a
specific import for these plugins, manually create valid CSV and JSON strings.


Example:
$> python3 data_pipeline.py
=== Code Nexus - Data Pipeline ===
Initialize Data Stream...
== DataStream statistics ==
No processor found, no data
Registering Processors
Send first batch of data on stream: ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', '
log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is
connected'}], 42, ['Hi', 'five']]
== DataStream statistics ==
Numeric Processor: total 4 items processed, remaining 4 on processor
Text Processor: total 3 items processed, remaining 3 on processor
Log Processor: total 2 items processed, remaining 2 on processor
Send 3 processed data from each processor to a CSV plugin:
CSV Output:
3.14,-1,2.71
CSV Output:
Hello world,Hi,five
CSV Output:
WARNING: Telnet access! Use ssh instead,INFO: User wil is connected
== DataStream statistics ==
Numeric Processor: total 4 items processed, remaining 1 on processor
Text Processor: total 3 items processed, remaining 0 on processor
Log Processor: total 2 items processed, remaining 0 on processor
Send another batch of data: [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'], [{'log_level': '
ERROR', 'log_message': '500 server crash'}, {'log_level': 'NOTICE', 'log_message': 'Certificate
expires in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']
== DataStream statistics ==
Numeric Processor: total 11 items processed, remaining 8 on processor
Text Processor: total 7 items processed, remaining 4 on processor
Log Processor: total 4 items processed, remaining 2 on processor
Send 5 processed data from each processor to a JSON plugin:
JSON Output:
{"item_3": "42", "item_4": "21", "item_5": "32", "item_6": "42", "item_7": "64"}
JSON Output:
{"item_3": "I love AI", "item_4": "LLMs are wonderful", "item_5": "Stay healthy", "item_6": "World hello
"}
JSON Output:
{"item_2": "ERROR: 500 server crash", "item_3": "NOTICE: Certificate expires in 10 days"}
== DataStream statistics ==
Numeric Processor: total 11 items processed, remaining 3 on processor
Text Processor: total 7 items processed, remaining 0 on processor
Log Processor: total 4 items processed, remaining 0 on processor
'''