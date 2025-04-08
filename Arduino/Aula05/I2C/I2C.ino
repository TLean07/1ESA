#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.begin(16,2);
  lcd.setCursor(6,0);
  lcd.print("Leandro");

}

void loop() {
  // put your main code here, to run repeatedly:

}
