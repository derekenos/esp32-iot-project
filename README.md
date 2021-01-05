# ESP32 IOT Project Template
An ESP32 / Micropython project template that uses [micropython-docker](https://github.com/derekenos/micropython-docker/tree/esp32) (`esp32` branch) for device administration and [femtoweb](https://github.com/derekenos/femtoweb/tree/micropython) (`micropython` branch) as HTTP and web application server.

## Dependencies
- make
- docker
- docker-compose

## Program the ESP32
The top-level [Makefile](https://github.com/derekenos/esp32-iot-project/blob/main/Makefile) defines a single target that will:
1. Initialize all git submodules
2. Create an initial `config.json` by copying [config.json.template](https://github.com/derekenos/esp32-iot-project/blob/main/filesystem/data/config.json.template)
3. Create a symlink to `filesystem` in the `micropython-docker` subdir called `devicefs`
4. Use `micropython-docker` to erase, flash, and copy application files to the device
  - Not that Docker will need to build the `micropython-esp32` image when you first run this.

### Do it
In the repo root, run the command:
```
make
```
