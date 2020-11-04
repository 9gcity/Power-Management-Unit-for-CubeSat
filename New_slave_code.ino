#include <Wire.h>
#define SLAVE_ADDR 0x06

void setup() {
    Serial.begin(9600);
    Wire.begin(SLAVE_ADDR);

    // Uses callbacks to process the data
    Wire.onReceive(receivedData);
    Serial.println("Ready");
}

void loop() {
    delay(100);
}

void receivedData(int byteCount){
    int data;

    while(Wire.available()) {
        data = Wire.read();
        Serial.print("Received: ");
        Serial.println(data);
    }
}
