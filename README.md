# run
```bash
# should use a venv
python -m venv .venv
source .venv/bin/activate

# install deps
pip install -r requirements.txt
# run it
python main.py
```

# hardware
- raspberry pi 5, i think
- ES08MD servos
    - connection is 5V, ground, and some kind of gpio (try 18)
# notes
- uses the [GPIO library](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo)
- servos draw ~700mA at stall, which is why we detach at the end of the loop
