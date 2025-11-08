# Services Folder

## Purpose

This folder contains **business logic services** - code that processes requests and coordinates between different components.

## Why It Exists

- **Business Logic Layer**: Contains all business rules and logic
- **Coordination**: Coordinates between repositories and clients
- **Reusability**: Services can be used by multiple handlers
- **Testability**: Easy to test business logic in isolation

## Use Cases

- **Workout Service**: Generates personalized workout plans
- **Gym Info Service**: Formats and provides gym information
- **Chat Service**: Handles general chat interactions with AI
- **Future Services**: Add new services as features grow

## What Goes Here

- Business logic classes
- Request processing logic
- Response formatting
- Coordination between repositories and clients

## What Doesn't Go Here

- Data access (that goes in `repositories/`)
- API clients (that goes in `clients/`)
- UI code (that goes in `ui/`)
- Data models (that goes in `models/`)

## Service Layer Benefits

1. **Separation**: Business logic separate from UI and data
2. **Reusability**: Same service can be used by different handlers
3. **Testability**: Easy to test business logic
4. **Maintainability**: Changes to business rules in one place

## How It Works

1. Handler receives user query
2. Handler calls appropriate service
3. Service processes request using business logic
4. Service may call repositories (for data) or clients (for APIs)
5. Service formats and returns response
6. Handler returns response to user

