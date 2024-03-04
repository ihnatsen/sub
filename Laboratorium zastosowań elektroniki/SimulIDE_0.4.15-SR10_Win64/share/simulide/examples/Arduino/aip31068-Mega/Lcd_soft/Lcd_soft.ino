#include <SlowSoftI2CMaster.h>

SlowSoftI2CMaster si = SlowSoftI2CMaster(SDA, SCL, true);

// Defines
#define LCD_I2C_ADDR        0x3E

#define LCD_MODE_COMMAND    0x00
#define LCD_MODE_DATA       0x40

#define LCD_CLEARDISPLAY    0x01
#define LCD_RETURNHOME      0x02
#define LCD_ENTRYMODESET    0x04
#define LCD_DISPLAYCONTROL  0x08
#define LCD_CURSORSHIFT     0x10
#define LCD_FUNCTIONSET     0x20
#define LCD_SETCGRAMADDR    0x40
#define LCD_SETDDRAMADDR    0x80

#define LCD_8BITMODE        0x10
#define LCD_4BITMODE        0x00
#define LCD_2LINE           0x08
#define LCD_1LINE           0x00
#define LCD_5x10DOTS        0x04
#define LCD_5x8DOTS         0x00

#define LCD_DISPLAYON       0x04
#define LCD_DISPLAYOFF      0x00
#define LCD_CURSORON        0x02
#define LCD_CURSOROFF       0x00
#define LCD_BLINKON         0x01
#define LCD_BLINKOFF        0x00

#define LCD_ENTRYRIGHT      0x00
#define LCD_ENTRYLEFT       0x02
#define LCD_ENTRYSHIFTINC   0x01
#define LCD_ENTRYSHIFTDEC   0x00

// Variables
unsigned long startMillis = 0;

void lcdSend(unsigned char value, unsigned char mode) {
  si.i2c_start(LCD_I2C_ADDR);
  si.i2c_write(mode);
  si.i2c_write(value);
  si.i2c_stop();
  delayMicroseconds(50);
}

void lcdSetup() {
  lcdSend(LCD_FUNCTIONSET | LCD_8BITMODE | LCD_2LINE | LCD_5x8DOTS, LCD_MODE_COMMAND);
  lcdSend(LCD_DISPLAYCONTROL | LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF, LCD_MODE_COMMAND);
  lcdSend(LCD_CLEARDISPLAY, LCD_MODE_COMMAND);
  delayMicroseconds(2000);
  lcdSend(LCD_ENTRYMODESET | LCD_ENTRYLEFT | LCD_ENTRYSHIFTDEC, LCD_MODE_COMMAND);
}

void lcdClear() {
  lcdSend(LCD_CLEARDISPLAY, LCD_MODE_COMMAND);
  delayMicroseconds(2000);
}

void lcdSetCursor(int x, int y) {
  unsigned char value = 0;

  if (y > 0) {
    value = 0x40;
  }
  value += x;

  lcdSend(LCD_SETDDRAMADDR | value, LCD_MODE_COMMAND);
}

void lcdPrint(const char *str) {
  while (*str != 0) {
    lcdSend(*str, LCD_MODE_DATA);
    str++;
  }
}

void setup() {
  lcdSetup();
  startMillis = millis();
}

void loop() {
  String text;
  unsigned long elapsedMillis, elapsedSeconds;
  int hours, minutes, seconds;

  elapsedMillis = millis() - startMillis;
  elapsedSeconds = elapsedMillis / 1000;
  hours = elapsedSeconds / 3600;
  minutes = (elapsedSeconds % 3600) / 60;
  seconds = (elapsedSeconds % 3600) % 60;
  
  text = String(hours);
  text += ":";
  text += String(minutes);
  text += ":";
  text += String(seconds);
  text += ".";
  text += String(elapsedMillis % 1000);

  lcdSetCursor(0, 0);
  lcdPrint(text.c_str());
}
