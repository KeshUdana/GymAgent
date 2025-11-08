# Utils Folder

## Purpose

This folder contains **utility functions** - helper functions and utilities used across the application.

## Why It Exists

- **Reusability**: Common functions used in multiple places
- **Organization**: Keeps utility code separate from business logic
- **Maintainability**: Easy to find and update utility functions
- **Testing**: Utilities can be tested independently

## Use Cases

- **Logging Setup**: Configures application logging
- **Helper Functions**: Common utility functions
- **Formatting**: Data formatting utilities
- **Validation**: Input validation helpers
- **Future Utilities**: Add new utilities as needed

## What Goes Here

- Utility functions
- Helper classes
- Common formatting functions
- Setup functions (like logging)
- Validation helpers

## What Doesn't Go Here

- Business logic (that goes in `services/`)
- Data models (that goes in `models/`)
- Configuration (that goes in `config/`)

## Current Utilities

- **Logging Setup**: Configures application-wide logging with file and console handlers

## Utility Characteristics

- **Stateless**: Utilities don't maintain state
- **Pure Functions**: Same input = same output
- **Reusable**: Used across multiple components
- **Simple**: Do one thing well

