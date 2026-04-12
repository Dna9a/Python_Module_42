from abc import ABC, abstractmethod
from typing import Any, Protocol


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
                    isinstance(k, str) and isinstance(v, str) for k, v in item.items()
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class Json:
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        return all(
            isinstance(item, tuple)
            and len(item) == 2
            and isinstance(item[0], int)
            and isinstance(item[1], str)
            for item in data
        )

    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid format for Json plugin")
        import json

        json_dict = {f"item_{rank}": content for rank, content in data}
        print("JSON Output:")
        print(json.dumps(json_dict, indent=None))


class Csv:
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        return all(
            isinstance(item, tuple)
            and len(item) == 2
            and isinstance(item[0], int)
            and isinstance(item[1], str)
            for item in data
        )

    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid format for Csv plugin")
        print("CSV Output:")
        # The briefing implies a comma-separated list of values on one line
        print(",".join(content for _, content in data))


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, pros: DataProcessor) -> None:
        self.processors.append(pros)

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
        print("\n== DataStream statistics ==")
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """
        Extract nb elements from each processor and send them to the plugin.
        """
        for processor in self.processors:
            processor_output: list[tuple[int, str]] = []
            count = 0
            while count < nb and processor.internal:
                processor_output.append(processor.output())
                count += 1
            if processor_output:
                plugin.process_output(processor_output)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Processors\n")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    ds.register_processor(num_proc)
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    test_batch_1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access" "! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    batch_1_msg = (
        "Send first batch of data on stream: ['Hello world', "
        "[3.14, -1, 2.71], [{'log_level': 'WARNING', "
        "'log_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message': "
        "'User wil is connected'}], 42, ['Hi', 'five']]"
    )
    print(f"{batch_1_msg}\n")
    ds.process_stream(test_batch_1)
    ds.print_processors_stats()

    msg_csv = "Send 3 processed data from each processor to a CSV plugin:"
    print(f"\n{msg_csv}")
    csv_plugin = Csv()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    test_batch_2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    batch_2_msg = (
        "Send another batch of data: [21, ['I love AI', "
        "'LLMs are wonderful', 'Stay healthy'], "
        "[{'log_level': 'ERROR', 'log_message': '500 server crash'}, "
        "{'log_level': 'NOTICE', 'log_message': "
        "'Certificate expires in 10 days'}], "
        "[32, 42, 64, 84, 128, 168], "
        "'World hello']"
    )
    print(f"\n{batch_2_msg}")
    ds.process_stream(test_batch_2)
    ds.print_processors_stats()

    msg_json = "Send 5 processed data from each processor to a JSON plugin:"
    print(f"\n{msg_json}")
    json_plugin = Json()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()
