# 🐾 Virtual Pet Game

A simple, interactive virtual pet simulator written in Python! Take care of your digital pet by feeding it, playing with it, and keeping it healthy.

## Features

- **Adopt a pet** with a custom name (or use the default name "Buddy")
- **Feed your pet** to increase food and health
- **Play with your pet** to boost happiness
- **Visit the vet** to fully restore health
- **Check status** to monitor food, happiness, and health levels
- Automatic **attribute decay** over time:
  - Food and happiness decrease after each action
  - Low food or happiness reduces health
- **Health warnings** and critical status alerts
- Graceful handling of `Ctrl+C` or `Ctrl+D` (defaults to name "Buddy" and exits cleanly)
