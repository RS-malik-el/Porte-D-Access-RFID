/**
 * e-mail : rachelsysteme@gmail.com
 * gitHub : https://github.com/RS-malik-el
 * Donation : paypal.me/RachelSysteme
 * 
 * DATE : 24/01/2022
 * MODIFIER : 28/12/2022
 * AUTEUR : RACHEL SYSTEME
 * 
 * @Board : Arduino Mega
 *
 * <MFRC522.h> : https://github.com/miguelbalboa/rfid.git
 * 
 * Ce programme consiste à afficher l'ID des cartes RFID
 *
 * -----------------------------------------------------------------------------------------
 *             MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino
 *             Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
 * Signal      Pin          Pin           Pin       Pin        Pin              Pin
 * -----------------------------------------------------------------------------------------
 * RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST
 * SPI SS      SDA(SS)      10            53        D10        10               10
 * SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16
 * SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14
 * SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15
*/
#include <SPI.h> // SPI
#include <MFRC522.h> // RFID

// Arduino mega pin 
#define SS_PIN  53
#define RST_PIN 5

MFRC522 rfid(SS_PIN, RST_PIN); // Déclaration object MFRC522
byte identifiant[4];           // Tableau contentent l'ID

void setup() {
  Serial.begin(9600);// Initialisation de la communication série
  SPI.begin();       // Initialisation du bus SPI
  rfid.PCD_Init();   // Init Initialisation
}

void loop() {
  // Initialise la boucle si aucun badge n'est présent 
  if ( !rfid.PICC_IsNewCardPresent()){ return; }
  // Vérifie la présence d'un nouveau badge 
  if ( !rfid.PICC_ReadCardSerial()){return;}

  // Stockage de l'ID du badge (4 octets) 
  for(byte i = 0; i < 4; i++){
    identifiant[i] = rfid.uid.uidByte[i];
    Serial.print(identifiant[i],HEX);
    Serial.print(" ");
  }
  Serial.println("");// Saut de ligne

  // Re-initialisation RFID
  rfid.PICC_HaltA(); // Halt PICC
  rfid.PCD_StopCrypto1(); // Stop encryption on PCD
}