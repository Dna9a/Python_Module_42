from pydantic import (  # type: ignore[import-not-found]
    BaseModel,
    Field,
    ValidationError,
)
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2026, 4, 20, 15, 30, 0),
        notes="Galek all systems are nominal.",
    )

    print("Valid station created:")
    print(f"ID: {valid_station.station_id}")
    print(f"Name: {valid_station.name}")

    print(f"Crew: {valid_station.crew_size} people")
    print(f"Power: {valid_station.power_level}%")
    print(f"Oxygen: {valid_station.oxygen_level}%")
    status = (
        "Operational" if valid_station.is_operational else "Non-operational"
    )
    print(f"Status: {status}")
    print("")
    print("=" * 40)
    print("Expected validation error:")

    try:
        SpaceStation(
            station_id="ISS002",
            name="Research Outpost",
            crew_size=25,
            power_level=76.0,
            oxygen_level=88.5,
            last_maintenance=datetime(2026, 4, 19, 9, 10, 0),
        )
    except ValidationError as exc:
        print(exc.errors()[0]["msg"])


if __name__ == "__main__":
    main()
