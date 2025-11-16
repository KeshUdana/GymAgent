# Data Module

Static JSON data files containing gym information, schedules, and FAQs.

## Files

### `membership.json`
Membership plans, pricing, and policies.

**Structure:**
```json
{
  "plans": [
    {
      "name": "Plan Name",
      "price": 8500,
      "features": ["feature1", "feature2"]
    }
  ],
  "cancellation_policy": "Policy text"
}
```

**Plans:**
- Monthly: Rs 8,500
- Quarterly: Rs 24,000
- Yearly: Rs 80,000
- Student (6 months): Rs 30,000

**Used by:** `routers/intent_router.py` → `build_membership_reply()`

### `schedule.json`
Class schedules and timetables.

**Structure:**
```json
{
  "today": [
    {"class": "Class Name", "time": "6:00 AM"}
  ],
  "weekly": {
    "monday": ["Class1", "Class2"],
    ...
  },
  "booking_info": "Booking instructions"
}
```

**Used by:** `routers/intent_router.py` → `build_schedule_reply()`

### `trainers.json`
Trainer information and availability.

**Structure:**
```json
{
  "trainers": [
    {
      "name": "Trainer Name",
      "specialty": "Specialty",
      "hours": "3:00 PM - 8:00 PM",
      "rate_per_session": 4000,
      "notes": "Additional info"
    }
  ],
  "booking_policy": "Policy text"
}
```

**Used by:** `routers/intent_router.py` → `build_trainer_reply()`

### `faqs.json`
Frequently asked questions and answers.

**Structure:**
```json
{
  "faqs": [
    {
      "question": "Question text",
      "answer": "Answer text"
    }
  ]
}
```

**FAQ Topics:**
- Opening hours
- Ladies-only classes
- Parking availability
- Personal training
- Membership cancellation

**Used by:** `routers/intent_router.py` → `build_faq_reply()`

### `gym_info.json`
Gym location, contact, hours, and general information.

**Structure:**
```json
{
  "name": "Gym Name",
  "location": "Address",
  "contact": "Phone number",
  "opening_hours": "Hours text",
  "parking": "Parking info",
  "payment_methods": ["Method1", "Method2"],
  "notes": "Additional notes"
}
```

**Used by:** `routers/intent_router.py` for location, hours, parking intents

## Data Flow

1. Data files are loaded once at module import in `intent_router.py`
2. Functions access pre-loaded data (no file I/O during request handling)
3. Updates to JSON files require server restart to take effect

## Updating Data

To update gym information:
1. Edit the relevant JSON file
2. Ensure valid JSON syntax
3. Restart the bot application
4. Changes take effect immediately

## Notes

- All prices are in Sri Lankan Rupees (Rs)
- Time formats: 12-hour format (e.g., "6:00 AM")
- File encoding: UTF-8
- All files must be valid JSON

