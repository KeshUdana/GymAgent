# Exceptions Folder

## Purpose

This folder contains **custom exception classes** - error types specific to this application.

## Why It Exists

- **Custom Error Handling**: Application-specific error types
- **Better Error Messages**: User-friendly error messages
- **Error Categorization**: Different exception types for different errors
- **Error Details**: Stores additional context about errors

## Use Cases

- **API Errors**: When external API calls fail (MistralAPIError)
- **Data Errors**: When data files can't be loaded (DataLoadError, DataNotFoundError)
- **Business Logic Errors**: Custom errors for business rules
- **Validation Errors**: When input validation fails

## What Goes Here

- Custom exception classes
- Exception hierarchies
- Error message formatting
- Error context storage

## What Doesn't Go Here

- Error handling logic (that goes in services/clients)
- Logging (that goes in `utils/`)
- Business logic (that goes in `services/`)

## Exception Hierarchy

```
GymAgentException (base)
├── APIError
│   └── MistralAPIError
└── DataLoadError
    └── DataNotFoundError
```

