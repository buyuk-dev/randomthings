# Arduino + Sparkfun AD8232 ECG sensor

![ECG SAMPLE RECORDING](/ecg/ecg.png?raw=true "ECG signal")

Basic ECG measurement using arduino uno and SparkFun AD8232 ECG sensor.

+ streaming data via serial port
+ plotting data in realtime with matplotlib

## Arduino compilation

```
arduino-cli compile -b arduino:avr:uno --upload --port /dev/tty.usbmodem14201 ./
```


## Usage

```
ArduinoECG.py [-h] [--window WINDOW] [--nsamples NSAMPLES]
                     [--refresh REFRESH] [--port {usb,bluetooth}]
```

**-h, --help** show this help message and exit

**--window WINDOW** plot width in samples

**--nsamples NSAMPLES** numbder of reads per frame

**--refresh REFRESH** frame duration in milliseconds

**--port {usb,bluetooth}** default serial port

