# Arduino + Sparkfun AD8232 ECG sensor

![ECG GIF](/ArduinoECG/ecg.gif?raw=true "ECG signal")

Basic ECG measurement using arduino uno and SparkFun AD8232 ECG sensor.

There is no signal processing here, only plotting raw data in more or less real time.

Arduino reads analog data from the sensor and writes it to the serial port.

Python script reads this data and displays the waveform in real time using matplotlib.

## Arduino compilation

```
arduino-cli compile -b arduino:avr:uno --upload --port /dev/tty.usbmodem14201 ./
```
