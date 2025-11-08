# Config Folder

## Purpose

This folder contains **application configuration** - settings, environment variables, and configuration management.

## Why It Exists

- **Centralized Configuration**: All app settings in one place
- **Environment Management**: Handles environment variables and .env files
- **Singleton Pattern**: Ensures configuration is loaded once and reused
- **Easy Updates**: Change settings without touching business logic

## Use Cases

- **Settings Management**: Loads and manages application settings
- **Environment Variables**: Reads from .env file
- **Path Configuration**: Defines paths to data files, logs, etc.
- **API Configuration**: Stores API keys and endpoints

## What Goes Here

- Settings classes
- Configuration loaders
- Environment variable readers
- Path definitions

## What Doesn't Go Here

- Business logic (that goes in `services/`)
- Data models (that goes in `models/`)
- Actual data files (that goes in `data/`)

