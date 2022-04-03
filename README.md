# LED-Rollsign

## Introduction

This is a LED Rollsign controller made in Python. It uses a REST API to control it

```python
requests.get(BASE + "SetRollsign", json={"Train": "TX3000", "Mode": "Normal", "Type": "Local", "Dest": "Tsukuba"})
```

```json
{
    "Message": "Rollsign set",
    "Args": {
        "Mode": "Normal",
        "Train": "TX3000",
        "Type": "Local",
        "Dest": "Tsukuba",
        "Line": None,
        "TypeChange": None,
        "Next": None,
        "StopsAt": None
    }
}
```


- [X] Base system
- [X] Add Seibu Laview support
- [X] Add E233 support
- [X] Add scrolling text support
- [ ] Implement OTMS-Client
