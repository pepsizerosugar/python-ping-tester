from dataclasses import dataclass


@dataclass
class EventElements:
    logger: None

    select_type: str = None
    select_type_of_first: str = "All"
    select_type_of_second: str = None
