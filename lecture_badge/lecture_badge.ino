/*
  SerialNumberRead
 Read the serial number of the IC card.
 

 */

#include <SPI.h>
#include <RFID.h>
#define SS_PIN 10
#define RST_PIN 9
RFID rfid (SS_PIN, RST_PIN);   
unsigned char status;
unsigned char str[MAX_LEN];  

void setup()
{
  Serial.begin(9600);
  SPI.begin();
  rfid.init(); 
}

void loop()
{
  //Search card, return card types
  if (rfid.findCard(PICC_REQIDL, str) == MI_OK) {
    Serial.println("Find the card!");
    // Show card type
    ShowCardType(str);
   
    if (rfid.anticoll(str) == MI_OK) {
      Serial.print("The card's number is  : ");
    
      for(int i = 0; i < 4; i++){
        Serial.print(0x0F & (str[i] >> 4),HEX);
        Serial.print(0x0F & str[i],HEX);
      }
      Serial.println("");
    }
  
    rfid.selectTag(str);
  }
  rfid.halt();  
}

void ShowCardType(unsigned char * type)
{
  Serial.print("Card type: ");
  if(type[0]==0x04&&type[1]==0x00) 
    Serial.println("MFOne-S50");
  else if(type[0]==0x02&&type[1]==0x00)
    Serial.println("MFOne-S70");
  else if(type[0]==0x44&&type[1]==0x00)
    Serial.println("MF-UltraLight");
  else if(type[0]==0x08&&type[1]==0x00)
    Serial.println("MF-Pro");
  else if(type[0]==0x44&&type[1]==0x03)
    Serial.println("MF Desire");
  else
    Serial.println("Unknown");
}

