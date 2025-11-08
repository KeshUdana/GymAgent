# Clients Folder

## Purpose

This folder contains **external API clients** - code that communicates with third-party services and APIs.

## Why It Exists

- **Separation of Concerns**: Keeps all external API communication in one place
- **Reusability**: API clients can be used by multiple services
- **Error Handling**: Centralized error handling for API calls
- **Testability**: Easy to mock API clients for testing

## Use Cases

- **Mistral AI Client**: Sends requests to Mistral AI API for generating AI responses
- **Future API Clients**: Add new clients here for other external services (e.g., payment APIs, email services)

## What Goes Here

- API client classes that handle HTTP requests
- API authentication logic
- API error handling
- Request/response formatting

## What Doesn't Go Here

- Business logic (that goes in `services/`)
- Data access (that goes in `repositories/`)
- Configuration (that goes in `config/`)

