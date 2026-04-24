from __future__ import annotations
from datetime import datetime
from enum import Enum
from pydantic import (  # type: ignore[import-not-found]
    BaseModel,
    Field,
    ValidationError,
    model_validator,
)


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Validated mission with a nested crew list and safety rules."""

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def _validate_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        has_senior_officer = any(
            member.rank in {Rank.COMMANDER, Rank.CAPTAIN}
            for member in self.crew
        )
        if not has_senior_officer:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            experienced_ratio = experienced_count / len(self.crew)
            if experienced_ratio < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)"
                )

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def _first_error_message(error: ValidationError) -> str:
    """Extract a single, human-friendly message from a ValidationError."""

    errors = error.errors()
    if not errors:
        return str(error)

    first = errors[0]
    ctx = first.get("ctx")
    if isinstance(ctx, dict):
        raw_error = ctx.get("error")
        if isinstance(raw_error, Exception):
            return str(raw_error)

    msg = first.get("msg")
    if isinstance(msg, str):
        return msg.removeprefix("Value error, ")
    return str(error)


def main() -> None:
    title = "Space Mission Crew Validation"
    separator = "=" * 41

    print(title)
    print(separator)

    try:
        mission_payload: dict[str, object] = {
            "mission_id": "M2024_MARS",
            "mission_name": "Mars Colony Establishment",
            "destination": "Mars",
            "launch_date": "2026-11-01T09:30:00Z",
            "duration_days": 900,
            "budget_millions": 2500.0,
            "crew": [
                {
                    "member_id": "CM001",
                    "name": "Sarah Connor",
                    "rank": "commander",
                    "age": 45,
                    "specialization": "Mission Command",
                    "years_experience": 12,
                    "is_active": True,
                },
                {
                    "member_id": "CM002",
                    "name": "John Smith",
                    "rank": "lieutenant",
                    "age": 38,
                    "specialization": "Navigation",
                    "years_experience": 6,
                    "is_active": True,
                },
                {
                    "member_id": "CM003",
                    "name": "Alice Johnson",
                    "rank": "officer",
                    "age": 29,
                    "specialization": "Engineering",
                    "years_experience": 2,
                    "is_active": True,
                },
            ],
        }
        mission = SpaceMission.model_validate(mission_payload)
    except ValidationError as exc:
        print("Unexpected validation failure for valid example:")
        print(_first_error_message(exc))
        return

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions:.1f}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) "
            f"- {member.specialization}"
        )
    print(separator)

    print("Expected validation error:")
    try:
        invalid_payload: dict[str, object] = {
            "mission_id": "M2024_TEST",
            "mission_name": "Supply Run",
            "destination": "Moon",
            "launch_date": "2026-07-10T14:00:00Z",
            "duration_days": 100,
            "budget_millions": 150.0,
            "crew": [
                {
                    "member_id": "CM010",
                    "name": "Jamie Lee",
                    "rank": "lieutenant",
                    "age": 34,
                    "specialization": "Logistics",
                    "years_experience": 7,
                    "is_active": True,
                },
                {
                    "member_id": "CM011",
                    "name": "Taylor Ray",
                    "rank": "officer",
                    "age": 28,
                    "specialization": "Engineering",
                    "years_experience": 4,
                    "is_active": True,
                },
            ],
        }
        SpaceMission.model_validate(invalid_payload)
    except ValidationError as exc:
        print(_first_error_message(exc))


if __name__ == "__main__":
    main()
