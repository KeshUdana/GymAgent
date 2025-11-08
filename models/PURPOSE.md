# Models Folder

## Purpose

This folder contains **data models** - classes that represent data structures used throughout the application.

## Why It Exists

- **Type Safety**: Strongly typed data structures
- **Data Validation**: Ensures data integrity
- **Reusability**: Models can be used across different layers
- **Documentation**: Models serve as documentation of data structures

## Use Cases

- **Gym Information Models**: GymInfo, ContactInfo, PricingInfo
- **Workout Models**: WorkoutProgram, WorkoutPlan, WorkoutGoal
- **Chat Models**: ChatMessage, ChatHistory, MessageRole
- **Future Models**: Add new models as the app grows

## What Goes Here

- Data classes (using @dataclass)
- Enums for constants
- Model conversion methods (from_dict, to_dict)
- Data validation logic

## What Doesn't Go Here

- Business logic (that goes in `services/`)
- Data access (that goes in `repositories/`)
- API clients (that goes in `clients/`)

## Model Characteristics

- **Immutable**: Models represent data, not behavior
- **Serializable**: Can convert to/from JSON
- **Validated**: Ensures data integrity
- **Documented**: Clear docstrings explain purpose

