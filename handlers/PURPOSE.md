# Handlers Folder

## Purpose

This folder contains **intent handlers** - code that routes and processes different types of user queries.

## Why It Exists

- **Strategy Pattern**: Different handlers for different question types
- **Extensibility**: Easy to add new question types
- **Separation**: Each handler handles one specific type of query
- **Routing Logic**: Determines which handler to use for each query

## Use Cases

- **Workout Queries**: Handles questions about workouts, programs, exercises
- **Pricing Queries**: Handles questions about membership prices
- **Contact Queries**: Handles questions about location, hours, contact info
- **General Queries**: Fallback handler for everything else

## What Goes Here

- Intent handler classes (implement IntentHandler interface)
- Intent router (routes queries to appropriate handler)
- Handler base class (defines handler interface)

## What Doesn't Go Here

- Business logic (that goes in `services/`)
- API clients (that goes in `clients/`)
- Data access (that goes in `repositories/`)

## How It Works

1. User asks a question
2. IntentRouter checks each handler
3. First handler that can handle the query processes it
4. Handler calls appropriate service
5. Response is returned to user

## Adding New Handlers

1. Create a new handler class extending `IntentHandler`
2. Implement `can_handle()` and `handle()` methods
3. Register in `IntentRouter`

