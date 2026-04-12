from abc import ABC, abstractmethod
from typing import Any
import typing


class DataProcessor(ABC):
	def __init__(self) -> None:
		self.internal = []
		self.processing_rank = 0

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

    def ingest(self, data: int | list[int] | float | list[float]) -> None:
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
			self.internal += [data]

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in item.items()) for item in data)
        return isinstance(data, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in data.items())

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for entry in data:
                formatted_log = ": ".join(entry.values())
                self.internal.append(formatted_log)
        else:
            formatted_log = ": ".join(data.values())
            self.internal.append(formatted_log)

class DataStreanm:
	def __init__(self) -> None:
		self.processors = []

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
				print(f"DataStream error - Can't process element in stream: {element}")

	def print_processors_stats(self) -> None:
		if not self.processors:
			print("No processor found, no data")
			return
		for processor in self.processors:
			print(f"{processor.__class__.__name__}: total {len(processor.internal)} items processed, remaining {len(processor.internal)} on processor")






'''
• Create a DataStream class that will receive a stream of data containing different
types and then will route each element to the appropriate data processor using
polymorphic behavior.

• This class will implement the
def register_processor(self, proc: DataProcessor) -> None:
method that allows you to register a new data processor to process the data stream.

• This class will implement the
def process_stream(self, stream: list[typing.Any]) -> None:
method that will analyze each element of the list received as a parameter and send
it to the appropriate registered data processor. Error messages will be printed if no
data processor can handle an element.

• Finally, the class will implement the def print_processors_stats(self) -> None:
method in order to print stream statistics.

• Create a test scenario that demonstrates the correct processing of a data stream.
Display statistics on registered data processors, consume elements using the output
method of each data processor and show updated statistics.

Example:
$> python3 data_stream.py
=== Code Nexus - Data Stream ===
Initialize Data Stream...
== DataStream statistics ==
No processor found, no data
Registering Numeric Processor
Send first batch of data on stream: ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', '
log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is
connected'}], 42, ['Hi', 'five']]
DataStream error - Can't process element in stream: Hello world
DataStream error - Can't process element in stream: [{'log_level': 'WARNING', 'log_message': 'Telnet
access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is connected'}]
DataStream error - Can't process element in stream: ['Hi', 'five']
== DataStream statistics ==
Numeric Processor: total 4 items processed, remaining 4 on processor
Registering other data processors
Send the same batch again
== DataStream statistics ==
Numeric Processor: total 8 items processed, remaining 8 on processor
Text Processor: total 3 items processed, remaining 3 on processor
Log Processor: total 2 items processed, remaining 2 on processor
Consume some elements from the data processors: Numeric 3, Text 2, Log 1
== DataStream statistics ==
Numeric Processor: total 8 items processed, remaining 5 on processor
Text Processor: total 3 items processed, remaining 1 on processor
Log Processor: total 2 items processed, remaining 1 on processor
How does polymorphism allow the DataStream to handle different data
types in the stream without knowing their specific implementations?
What are the benefits of this design approach?


'''