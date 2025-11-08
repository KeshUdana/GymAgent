# Developer Guide - Gym Agent

A comprehensive guide to understanding how the Gym Agent application works, from user input to response.

## Table of Contents

1. [Overview](#overview)
2. [Application Flow](#application-flow)
3. [Architecture Overview](#architecture-overview)
4. [Component Details](#component-details)
5. [Data Flow](#data-flow)
6. [Request Processing Flow](#request-processing-flow)
7. [Adding New Features](#adding-new-features)

---

## Overview

The Gym Agent is a Streamlit-based chatbot that helps users with gym-related questions. It uses Mistral AI to generate intelligent responses and has specialized handlers for different types of queries.

### What the App Does

1. User types a question in the Streamlit interface
2. App determines what type of question it is (workout, pricing, contact, or general)
3. App routes the question to the appropriate handler
4. Handler processes the question and generates a response
5. Response is displayed back to the user

---

## Application Flow

### High-Level Flow Diagram

```
┌─────────────┐
│   User      │
│  (Browser)  │
└──────┬──────┘
       │ Types question
       ▼
┌─────────────────────┐
│  Streamlit UI       │
│  (app.py)           │
└──────┬──────────────┘
       │ Captures input
       ▼
┌─────────────────────┐
│  Intent Router      │
│  (intent_router.py) │
└──────┬──────────────┘
       │ Routes to handler
       ▼
┌─────────────────────┐
│  Handler             │
│  (workout/pricing/   │
│   contact/general)   │
└──────┬──────────────┘
       │ Processes request
       ▼
┌─────────────────────┐
│  Service Layer      │
│  (workout_service/  │
│   gym_info_service/ │
│   chat_service)     │
└──────┬──────────────┘
       │ Gets data/API
       ▼
┌─────────────────────┐
│  Repository/Client   │
│  (data files or     │
│   Mistral API)      │
└──────┬──────────────┘
       │ Returns data
       ▼
┌─────────────────────┐
│  Response to User   │
└─────────────────────┘
```

---

## Architecture Overview

### Layer Structure

The app follows a **layered architecture** where each layer has a specific responsibility:

```
┌─────────────────────────────────────────┐
│         PRESENTATION LAYER              │
│  ┌───────────────────────────────────┐  │
│  │  UI (Streamlit)                   │  │
│  │  - app.py                         │  │
│  │  - ui/streamlit_app.py            │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│         ROUTING LAYER                   │
│  ┌───────────────────────────────────┐  │
│  │  Handlers                         │  │
│  │  - handlers/intent_router.py      │  │
│  │  - handlers/workout_handler.py    │  │
│  │  - handlers/pricing_handler.py    │  │
│  │  - handlers/contact_handler.py    │  │
│  │  - handlers/general_handler.py    │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│         BUSINESS LOGIC LAYER            │
│  ┌───────────────────────────────────┐  │
│  │  Services                         │  │
│  │  - services/workout_service.py    │  │
│  │  - services/gym_info_service.py   │  │
│  │  - services/chat_service.py       │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
┌──────────────────┐  ┌──────────────────┐
│  DATA LAYER      │  │  EXTERNAL API    │
│  ┌────────────┐  │  │  ┌────────────┐  │
│  │Repository  │  │  │  │Mistral API │  │
│  │- gym_info  │  │  │  │Client      │  │
│  │- workout   │  │  │  │            │  │
│  └────────────┘  │  │  └────────────┘  │
│  ┌────────────┐  │  │                  │
│  │Data Files  │  │  │                  │
│  │- JSON      │  │  │                  │
│  └────────────┘  │  │                  │
└──────────────────┘  └──────────────────┘
```

### Key Principles

1. **Separation of Concerns**: Each layer handles one specific responsibility
2. **Dependency Injection**: Components receive dependencies rather than creating them
3. **Strategy Pattern**: Different handlers for different types of queries
4. **Repository Pattern**: Clean data access abstraction

---

## Component Details

### 1. Presentation Layer (UI)

**Location**: `app.py`, `ui/streamlit_app.py`

**What it does**:
- Displays the chat interface to users
- Captures user input
- Shows responses

**How it works**:
```python
# User types message
user_input = st.chat_input("Ask me...")

# App routes to handler
response = router.route(user_input)

# Display response
st.markdown(response)
```

### 2. Routing Layer (Handlers)

**Location**: `handlers/`

**What it does**:
- Determines what type of question the user asked
- Routes to the appropriate handler

**Handler Types**:

```
┌─────────────────────────────────────────┐
│         Intent Router                   │
│                                         │
│  Checks each handler in order:          │
│                                         │
│  1. WorkoutHandler                      │
│     └─ Keywords: workout, program, etc. │
│                                         │
│  2. PricingHandler                      │
│     └─ Keywords: price, membership, etc.│
│                                         │
│  3. ContactHandler                      │
│     └─ Keywords: contact, location, etc.│
│                                         │
│  4. GeneralHandler (fallback)           │
│     └─ Handles everything else          │
└─────────────────────────────────────────┘
```

**How it works**:
```python
# Intent Router checks each handler
for handler in handlers:
    if handler.can_handle(user_input):
        return handler.handle(user_input)
```

### 3. Business Logic Layer (Services)

**Location**: `services/`

**What it does**:
- Contains the business logic for processing requests
- Formats responses
- Coordinates between repositories and clients

**Service Types**:

- **WorkoutService**: Generates personalized workout plans
- **GymInfoService**: Provides gym information (pricing, contact)
- **ChatService**: Handles general chat queries

### 4. Data Layer

**Location**: `repositories/`, `data/`

**What it does**:
- Accesses data from JSON files
- Provides clean interface for data access
- Caches data for performance

**Repository Types**:

- **GymInfoRepository**: Reads gym information from `data/gym.info.json`
- **WorkoutRepository**: Reads workout programs from `data/program.json`

### 5. External API Layer

**Location**: `clients/`

**What it does**:
- Communicates with Mistral AI API
- Handles API errors gracefully
- Formats API requests and responses

---

## Data Flow

### Complete Request Flow

Let's trace a request from start to finish:

#### Example: User asks "What's the pricing?"

```
Step 1: User Input
┌─────────────┐
│ User types: │
│ "What's the│
│  pricing?"  │
└──────┬──────┘
       │
       ▼
Step 2: UI Captures Input
┌─────────────────────┐
│ streamlit_app.py    │
│ - Receives input    │
│ - Creates Message   │
└──────┬──────────────┘
       │
       ▼
Step 3: Route to Handler
┌─────────────────────┐
│ intent_router.py    │
│ - Checks handlers   │
│ - Finds match:      │
│   PricingHandler    │
└──────┬──────────────┘
       │
       ▼
Step 4: Handler Processes
┌─────────────────────┐
│ pricing_handler.py  │
│ - Calls service     │
└──────┬──────────────┘
       │
       ▼
Step 5: Service Gets Data
┌─────────────────────┐
│ gym_info_service.py │
│ - Calls repository  │
└──────┬──────────────┘
       │
       ▼
Step 6: Repository Reads File
┌─────────────────────┐
│ gym_info_repository │
│ - Reads JSON file   │
│ - Returns data      │
└──────┬──────────────┘
       │
       ▼
Step 7: Service Formats Response
┌─────────────────────┐
│ gym_info_service.py │
│ - Formats pricing   │
│ - Returns string    │
└──────┬──────────────┘
       │
       ▼
Step 8: Display to User
┌─────────────────────┐
│ streamlit_app.py    │
│ - Shows response    │
└─────────────────────┘
```

#### Example: User asks "Create a workout plan"

```
Step 1: User Input
┌─────────────┐
│ "Create a   │
│  workout    │
│  plan"      │
└──────┬──────┘
       │
       ▼
Step 2: Route to WorkoutHandler
┌─────────────────────┐
│ workout_handler.py  │
└──────┬──────────────┘
       │
       ▼
Step 3: WorkoutService Processes
┌─────────────────────┐
│ workout_service.py  │
│ 1. Detects goal     │
│ 2. Gets base program│
└──────┬──────────────┘
       │
       ▼
Step 4: Get Base Program
┌─────────────────────┐
│ workout_repository  │
│ - Reads program.json│
│ - Returns program   │
└──────┬──────────────┘
       │
       ▼
Step 5: Call Mistral API
┌─────────────────────┐
│ mistral_client.py   │
│ - Sends request     │
│ - Gets AI response  │
└──────┬──────────────┘
       │
       ▼
Step 6: Return to User
┌─────────────────────┐
│ Personalized plan   │
│ displayed to user   │
└─────────────────────┘
```

---

## Request Processing Flow

### Detailed Flow Diagram

```
                    ┌──────────────┐
                    │   User       │
                    │  Input       │
                    └──────┬───────┘
                           │
                           ▼
            ┌───────────────────────────┐
            │   Streamlit UI            │
            │   (ui/streamlit_app.py)   │
            │                           │
            │  - Captures input         │
            │  - Creates ChatMessage    │
            │  - Calls IntentRouter     │
            └──────┬────────────────────┘
                   │
                   ▼
        ┌──────────────────────────┐
        │   Intent Router           │
        │   (handlers/intent_router)│
        │                           │
        │  Checks handlers in order:│
        │  1. WorkoutHandler        │
        │  2. PricingHandler        │
        │  3. ContactHandler        │
        │  4. GeneralHandler        │
        └──────┬───────────────────┘
               │
               ▼
    ┌──────────────────────────────┐
    │   Handler (e.g., Workout)    │
    │   (handlers/workout_handler)  │
    │                               │
    │  - can_handle() checks input │
    │  - handle() processes request │
    └──────┬───────────────────────┘
           │
           ▼
    ┌──────────────────────────────┐
    │   Service                    │
    │   (services/workout_service) │
    │                              │
    │  - Business logic            │
    │  - Coordinates data/API      │
    └──────┬───────────────────────┘
           │
    ┌──────┴───────┐
    │              │
    ▼              ▼
┌─────────┐   ┌──────────┐
│Repository│   │  Client   │
│(data)    │   │(Mistral)  │
└────┬─────┘   └─────┬────┘
     │               │
     └───────┬───────┘
             │
             ▼
    ┌─────────────────┐
    │   Response      │
    │   (formatted)   │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │   Display to    │
    │     User        │
    └─────────────────┘
```

---

## Component Interactions

### How Components Talk to Each Other

```
┌─────────────┐
│   Handler   │
│             │
│  Uses:      │
│  └─> Service│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Service   │
│             │
│  Uses:      │
│  ├─> Repository│
│  └─> Client    │
└──────┬──────┘
       │
   ┌───┴───┐
   │       │
   ▼       ▼
┌─────┐ ┌──────┐
│ Rep │ │Client│
└─────┘ └──────┘
```

### Dependency Flow

```
UI Layer
  └─> IntentRouter
       └─> Handlers
            └─> Services
                 ├─> Repositories (for data)
                 └─> Clients (for API)
```

**Key Point**: Each layer only knows about the layer directly below it. This makes the code:
- Easy to test
- Easy to modify
- Easy to understand

---

## Adding New Features

### How to Add a New Handler

**Step 1**: Create the handler file
```python
# handlers/my_handler.py
from handlers.base import IntentHandler
from services.my_service import MyService

class MyHandler(IntentHandler):
    def __init__(self, my_service: MyService | None = None):
        self.my_service = my_service or MyService()
        self.keywords = ["keyword1", "keyword2"]
    
    def can_handle(self, user_input: str) -> bool:
        lower = user_input.lower()
        return any(keyword in lower for keyword in self.keywords)
    
    def handle(self, user_input: str) -> str:
        return self.my_service.process(user_input)
```

**Step 2**: Register in IntentRouter
```python
# handlers/intent_router.py
from handlers.my_handler import MyHandler

self.handlers = [
    WorkoutHandler(),
    MyHandler(),  # Add here
    PricingHandler(),
    # ...
]
```

**Step 3**: Create service (if needed)
```python
# services/my_service.py
class MyService:
    def process(self, input: str) -> str:
        # Your business logic here
        return "Response"
```

### Flow for New Feature

```
1. User asks question
   │
   ▼
2. IntentRouter checks handlers
   │
   ▼
3. Your new handler matches
   │
   ▼
4. Handler calls your service
   │
   ▼
5. Service processes and returns
   │
   ▼
6. Response shown to user
```

---

## Key Concepts Explained Simply

### 1. Strategy Pattern (Handlers)

**What it is**: Different ways to handle different types of questions

**Why we use it**: Makes it easy to add new question types without changing existing code

**Example**:
- Workout questions → WorkoutHandler
- Pricing questions → PricingHandler
- Contact questions → ContactHandler

### 2. Repository Pattern

**What it is**: A clean way to access data

**Why we use it**: 
- Separates data access from business logic
- Easy to change data source (file → database)
- Easy to test

**Example**:
```python
# Instead of this (bad):
data = json.load(open("data/gym.info.json"))

# We do this (good):
repository = GymInfoRepository()
data = repository.get_gym_info()
```

### 3. Service Layer

**What it is**: Business logic that processes requests

**Why we use it**:
- Keeps business logic separate from UI and data
- Reusable across different handlers
- Easy to test

### 4. Dependency Injection

**What it is**: Components receive dependencies instead of creating them

**Why we use it**:
- Easy to test (can pass mock objects)
- Flexible (can swap implementations)
- Clear dependencies

**Example**:
```python
# Good: Dependency injection
def __init__(self, service: MyService | None = None):
    self.service = service or MyService()

# Bad: Creates dependency
def __init__(self):
    self.service = MyService()  # Hard to test
```

---

## Common Questions

### Q: Where does the app start?
**A**: `app.py` → calls `ui/streamlit_app.py` → creates the Streamlit interface

### Q: How does it know which handler to use?
**A**: `IntentRouter` checks each handler's `can_handle()` method in order until one matches

### Q: Where is the data stored?
**A**: JSON files in the `data/` folder:
- `data/gym.info.json` - Gym information
- `data/program.json` - Workout programs

### Q: How does it call Mistral AI?
**A**: `clients/mistral_client.py` sends HTTP requests to Mistral API using the `requests` library

### Q: What happens if Mistral API fails?
**A**: The client catches the error and returns a user-friendly error message instead of crashing

### Q: How do I add a new question type?
**A**: 
1. Create a new handler in `handlers/`
2. Create a service in `services/` (if needed)
3. Register the handler in `IntentRouter`

---

## File Structure Quick Reference

```
GymAgent/
├── app.py                    # Entry point
├── ui/
│   └── streamlit_app.py     # Streamlit UI
├── handlers/
│   ├── intent_router.py     # Routes to handlers
│   ├── workout_handler.py   # Handles workout questions
│   ├── pricing_handler.py   # Handles pricing questions
│   ├── contact_handler.py   # Handles contact questions
│   └── general_handler.py    # Handles everything else
├── services/
│   ├── workout_service.py   # Workout business logic
│   ├── gym_info_service.py  # Gym info business logic
│   └── chat_service.py      # General chat logic
├── repositories/
│   ├── gym_info_repository.py  # Access gym data
│   └── workout_repository.py  # Access workout data
├── clients/
│   └── mistral_client.py    # Mistral API client
├── models/
│   ├── gym_info.py          # Gym data models
│   ├── workout.py           # Workout data models
│   └── chat.py              # Chat data models
├── config/
│   └── settings.py          # Configuration
└── data/
    ├── gym.info.json        # Gym information
    └── program.json         # Workout programs
```

---

## Summary

The Gym Agent follows a clean, layered architecture:

1. **UI Layer** - Shows interface to users
2. **Routing Layer** - Determines question type
3. **Handler Layer** - Processes specific question types
4. **Service Layer** - Contains business logic
5. **Data/API Layer** - Accesses data and external APIs

Each layer has a clear responsibility, making the code:
- ✅ Easy to understand
- ✅ Easy to test
- ✅ Easy to modify
- ✅ Easy to extend

When a user asks a question, it flows through these layers, gets processed, and returns a response. Simple!

