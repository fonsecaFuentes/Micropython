/*
Blog: www.descargatuscosas.blogspot.com
facebook: www.fb.com/LosMejoresContenidosParaTi
Instagram: www.instagram.com/marioalot
YouTube:www.youtube.com/user/descargatuscosas
*/
#include <Filters.h>
float testFrequency = 60;                     // Frecuencia (Hz)
float windowLength = 40.0/testFrequency;     // promedio de la señal
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4);
int Sensor = 0; //A0

float intercept = -0.04; // to be adjusted based on calibration testing
float slope = 0.0405; // to be adjusted based on calibration testing
float volts; // Voltage

unsigned long periodo = 1000;
unsigned long tiempoAnterior = 0;


void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  delay(5000);
}

void loop() {
  RunningStatistics inputStats;
  inputStats.setWindowSecs(windowLength);

  while(true) {
    Sensor = analogRead(A1);  //Leer pin Analógico
    inputStats.input(Sensor);
    if((unsigned long)(millis() - tiempoAnterior) >= periodo) {
      volts = intercept + slope * inputStats.sigma(); //offset y amplitud
      volts = volts*(40.3231);                        //calibración
      Serial.print("\tVoltage: ");
      Serial.println(volts);
      lcd.setCursor(0,0);
      lcd.print("Voltaje RMS:");
      lcd.setCursor(0,1);
      lcd.print(volts);
      tiempoAnterior = millis();
    }
  }

}
