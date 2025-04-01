#include <DHT.h>
 
#define dhtPin 2
#define dhtType DHT11
 
int led = 12;
int led2 = 11;
int led3 = 10;
 
DHT dht(dhtPin, dhtType);
 
void setup() {
  Serial.begin(9600);
  dht.begin();
  
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}
 
void loop() {
  int temp = dht.readTemperature();
  int umi = dht.readHumidity();
 
  Serial.print("Temperatura: ");
  Serial.println(temp);
  Serial.print("Umidade: ");
  Serial.println(umi);
 
  delay(2000);
 
  if (temp == 15 && umi == 15) {
    digitalWrite(led, HIGH);
    delay(1000);
    digitalWrite(led, LOW);
    delay(1000);
  } else if (temp == 25 && umi == 25) {
    digitalWrite(led2, HIGH);
    delay(1000);
    digitalWrite(led2, LOW);
    delay(1000);
  } else {
    digitalWrite(led3, HIGH);
    delay(1000);
    digitalWrite(led3, LOW);
    delay(1000);
  }
}
 