# LED-Rollsign

## Introduction

This is a LED Rollsign controller made in Python. It uses a REST API to control it

```python
requests.get(BASE + "rollsign", json={"train": "TX3000", "mode": "Normal", "type": "Local", "dest": "Tsukuba"})
```

```json
{
    "message": "Rollsign set",
    "args": {
        "mode": "Normal",
        "train": "TX3000",
        "type": "Local",
        "dest": "Tsukuba",
        "line": None,
        "type_change": None,
        "next": None,
        "stops_at": None
    }
}
```


- [X] Base system
- [X] Add Seibu Laview support
- [X] Add E233 support
- [X] Add scrolling text support
- [ ] Implement OTMS