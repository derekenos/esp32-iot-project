# ESP32 IOT Project Template
An ESP32 / Micropython project template that uses [micropython-docker](https://github.com/derekenos/micropython-docker/tree/esp32) (`esp32` branch) for device administration and [femtoweb](https://github.com/derekenos/femtoweb/tree/micropython) (`micropython` branch) as HTTP and web application server.

## Dependencies
- make (`v4.1`)
- docker (`v19.03.13`)
- docker-compose (`v1.25.3`)
- linux? (`Ubuntu 18.04`)

## Program the ESP32
The top-level [Makefile](https://github.com/derekenos/esp32-iot-project/blob/main/Makefile) defines a single target that will:
1. Initialize all git submodules
2. Create an initial `config.json` by copying [config.json.template](https://github.com/derekenos/esp32-iot-project/blob/main/filesystem/data/config.json.template)
3. Create a symlink to `filesystem` in the `micropython-docker` subdir called `devicefs`
4. Use `micropython-docker` to erase, flash, and copy application files to the device
  - Not that Docker will need to build the `micropython-esp32` image when you first run this.

### Do it
Connect the ESP32 to your computer via USB and run the following command in the repo root:
```
make
```

## Connect to REPL
See https://github.com/derekenos/micropython-docker/tree/esp32#connect-to-the-micropython-repl

## Helper Scripts
Once `femtoweb` is running, you can use the `./put` and `./reset` helper scripts to write files to and reset the device.

### put
`put` expects a single `filesystem` directory sub-path argument.

Example:
```
./put filesystem/main.py
```

### reset
`reset` will trigger a device reset and takes no arguments.
