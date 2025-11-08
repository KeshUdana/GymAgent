# Data Folder

## Purpose

This folder contains **static data files** - JSON files and other data sources used by the application.

## Why It Exists

- **Data Storage**: Centralized location for all data files
- **Easy Updates**: Update data without changing code
- **Version Control**: Track data changes in git
- **Separation**: Keeps data separate from code

## Use Cases

- **Gym Information**: Stores gym details (address, hours, contact, pricing)
- **Workout Programs**: Stores base workout programs and templates
- **Future Data**: Can store other JSON/CSV data files

## What Goes Here

- JSON data files
- CSV files (if needed)
- Static configuration data
- Template data

## What Doesn't Go Here

- Code files (that goes in other folders)
- Log files (that goes in `logs/`)
- Environment files (that goes in root as `.env`)

## Current Files

- `gym.info.json`: Gym information (address, hours, contact, pricing)
- `program.json`: Workout program templates

