# inondation

sudo raspi-config to access the configuration menu. select “Advanced Settings” and select “I2C Enable/Disable automatic loading” to enable I2C

INSTALL I2C-TOOLS AND SMBUS
sudo apt-get install i2c-tools python-smbus

i2cdetect -y 1
change address in the I2C lib file
