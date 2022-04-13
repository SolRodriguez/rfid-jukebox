
#include <SparkFun_UHF_RFID_Reader.h>
#include <Arduino.h>

#include "wiring_private.h"

Uart mySerial (&sercom1, 2, 3, SERCOM_RX_PAD_1, UART_TX_PAD_0);

RFID nano; //Create instance

const int analogInPin2 = A2; 
int sensorValue = 0; 

void setup() {
  // Reassign pins 5 and 6 to SERCOM alt
//  pinPeripheral(2, PIO_SERCOM);
//  pinPeripheral(3, PIO_SERCOM);
//
//  // Start my new hardware serial
//  mySerial.begin(9600);
//  mySerial.println("hello");

Serial.begin(9600);
Serial.println("setup");
}

void loop() {
  // put your main code here, to run repeatedly:
  // read the analog in value
  sensorValue = analogRead(analogInPin2); 
  // print the results to the Serial Monitor 
  Serial.print("sensor = ");
  Serial.println(sensorValue);
  // wait 2 milliseconds before the next loop for the analog-to-digital 
  // converter to settle after the last reading:
  delay(2);
}
