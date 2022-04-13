
#include <SparkFun_UHF_RFID_Reader.h>
#include <Arduino.h>

#include "wiring_private.h"

Uart mySerial (&sercom1, 2, 3, SERCOM_RX_PAD_1, UART_TX_PAD_0);

RFID nano; //Create instance


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
  Serial.println("loop");
}
