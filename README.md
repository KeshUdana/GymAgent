# Gym Agent

A highly modular, OOP-based gym assistant application powered by Mistral AI.

## Architecture

This project follows a clean, modular architecture designed for maintainability and collaboration:

```
GymAgent/
├── models/          # Data models (dataclasses)
├── repositories/    # Data access layer
├── services/        # Business logic layer
├── clients/         # External API clients
├── handlers/        # Intent handlers (Strategy pattern)
├── ui/             # User interface components
├── config/         # Configuration management
├── exceptions/     # Custom exceptions
├── utils/         # Utility functions
├── data/          # Data files (JSON)
└── logs/          # Log files
```

## Features

- **Modular Design**: Clear separation of concerns with distinct layers
- **OOP Principles**: Object-oriented design with proper abstractions
- **Strategy Pattern**: Intent handlers for extensible routing
- **Repository Pattern**: Clean data access abstraction
- **Service Layer**: Business logic separated from UI and data access
- **Error Handling**: Comprehensive exception handling with custom exceptions
- **Logging**: Structured logging for debugging and monitoring

## Documentation

- **[Developer Guide](DEVELOPER_GUIDE.md)**: Comprehensive guide explaining the application flow, architecture, and how to add new features
- **README**: This file - setup and quick reference

## Setup

1. Create virtual environment with `uv`:
   ```bash
   uv venv --python 3.12
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Set up environment variables:
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Edit .env and add your Mistral API key
   # Get your API key from: https://console.mistral.ai/
   ```

4. Configure your `.env` file:
   ```env
   # Required
   MISTRAL_API_KEY=your_actual_api_key_here
   
   # Optional
   LOG_LEVEL=INFO
   ```

5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Environment Variables

The application uses the following environment variables (configured in `.env` file):

### Required Variables

- **`MISTRAL_API_KEY`**: Your Mistral AI API key
  - Get it from: https://console.mistral.ai/
  - Required for the app to function

### Optional Variables

- **`LOG_LEVEL`**: Logging level (default: `INFO`)
  - Options: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
  - Controls the verbosity of application logs

See `env.example` for a complete template.

## Project Structure

### Models (`models/`)
- `gym_info.py`: Gym information models (GymInfo, ContactInfo, PricingInfo)
- `workout.py`: Workout-related models (WorkoutProgram, WorkoutPlan)
- `chat.py`: Chat message models (ChatMessage, ChatHistory)

### Repositories (`repositories/`)
- `base.py`: Base repository with caching
- `gym_info_repository.py`: Gym information data access
- `workout_repository.py`: Workout program data access

### Services (`services/`)
- `gym_info_service.py`: Gym information business logic
- `workout_service.py`: Workout plan generation logic
- `chat_service.py`: General chat interactions

### Clients (`clients/`)
- `mistral_client.py`: Mistral API client with error handling

### Handlers (`handlers/`)
- `base.py`: Base intent handler interface
- `workout_handler.py`: Handles workout-related queries
- `pricing_handler.py`: Handles pricing queries
- `contact_handler.py`: Handles contact information queries
- `general_handler.py`: Fallback handler for general queries
- `intent_router.py`: Routes queries to appropriate handlers

### UI (`ui/`)
- `streamlit_app.py`: Streamlit application interface

### Configuration (`config/`)
- `settings.py`: Application settings and configuration

### Exceptions (`exceptions/`)
- `base.py`: Base exception classes
- `api.py`: API-related exceptions
- `data.py`: Data-related exceptions

## Adding New Features

### Adding a New Intent Handler

1. Create a new handler in `handlers/`:
   ```python
   from handlers.base import IntentHandler
   
   class MyHandler(IntentHandler):
       def can_handle(self, user_input: str) -> bool:
           # Check if this handler can handle the input
           return "keyword" in user_input.lower()
       
       def handle(self, user_input: str) -> str:
           # Process and return response
           return "Response"
   ```

2. Register it in `IntentRouter`:
   ```python
   self.handlers = [
       WorkoutHandler(),
       PricingHandler(),
       MyHandler(),  # Add your handler
       GeneralHandler(),
   ]
   ```

### Adding a New Service

1. Create a service class in `services/`:
   ```python
   class MyService:
       def __init__(self, dependency=None):
           self.dependency = dependency
       
       def do_something(self):
           # Business logic
           pass
   ```

2. Use dependency injection for testability

## Development Guidelines

- Follow OOP principles: encapsulation, inheritance, polymorphism
- Use type hints for better code clarity
- Write docstrings for all classes and methods
- Keep functions small and focused (single responsibility)
- Use dependency injection for testability
- Handle errors gracefully with custom exceptions
- Log important events and errors

## Testing

(Add testing instructions when tests are added)

## Contributing

1. Create a feature branch
2. Make your changes following the architecture
3. Ensure code follows OOP principles
4. Submit a pull request
