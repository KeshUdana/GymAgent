# UI Folder

## Purpose

This folder contains **user interface components** - code that handles the presentation layer and user interaction.

## Why It Exists

- **Presentation Layer**: Separates UI from business logic
- **UI Framework**: Contains Streamlit-specific code
- **User Interaction**: Handles user input and displays responses
- **State Management**: Manages UI state (chat history, etc.)

## Use Cases

- **Streamlit App**: Main Streamlit application interface
- **Chat Interface**: Displays chat messages and handles input
- **UI Components**: Reusable UI components (if needed)
- **Future UI**: Can add other UI frameworks or components

## What Goes Here

- Streamlit app code
- UI component functions
- User input handling
- Response display logic
- Session state management

## What Doesn't Go Here

- Business logic (that goes in `services/`)
- Routing logic (that goes in `handlers/`)
- Configuration (that goes in `config/`)

## UI Layer Responsibilities

1. **Display**: Shows interface to users
2. **Input**: Captures user input
3. **Routing**: Routes input to appropriate handler
4. **Output**: Displays responses to users
5. **State**: Manages UI state (chat history, etc.)

## How It Works

1. User sees Streamlit interface
2. User types question
3. UI captures input
4. UI calls IntentRouter
5. Router processes and returns response
6. UI displays response to user

