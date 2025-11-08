# Repositories Folder

## Purpose

This folder contains **data repositories** - code that accesses and retrieves data from storage.

## Why It Exists

- **Repository Pattern**: Clean abstraction for data access
- **Separation of Concerns**: Keeps data access separate from business logic
- **Flexibility**: Easy to change data source (file → database)
- **Caching**: Can cache data for performance
- **Testability**: Easy to mock repositories for testing

## Use Cases

- **Gym Info Repository**: Reads gym information from JSON files
- **Workout Repository**: Reads workout programs from JSON files
- **Future Repositories**: Can add database repositories, API repositories, etc.

## What Goes Here

- Repository classes that extend BaseRepository
- Data access methods (get, find, load)
- Data caching logic
- Data transformation (JSON → Models)

## What Doesn't Go Here

- Business logic (that goes in `services/`)
- Data models (that goes in `models/`)
- Actual data files (that goes in `data/`)

## Repository Pattern Benefits

1. **Abstraction**: Services don't know where data comes from
2. **Flexibility**: Can swap file storage for database without changing services
3. **Testability**: Easy to create mock repositories
4. **Caching**: Centralized caching logic

## How It Works

1. Service needs data
2. Service calls repository method
3. Repository reads from data source (file/database)
4. Repository converts to model
5. Repository returns model to service

