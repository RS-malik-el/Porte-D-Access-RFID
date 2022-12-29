/**
 *  e-mail : rachelsysteme@gmail.com
 *  gitHub : https://github.com/RS-malik-el
 *  Donation : paypal.me/RachelSysteme
 *
 *  DATE : 20/01/2022
 *  MODIFIER : 28/12/2022
 *  @AUTEUR : RACHEL SYSTEME
 *  
 *  @Board : Arduino Mega
 * 
 *  Ce programme consiste à interagir avec un logiciel conçu pour l'occasion afin d'échangé
 *  les données plus précisement envoyé le numéro de la carte RFID au logiciel, après vérification
 *  le logiciel revoie "TRUE" ou "FALSE" selon que la carte RFID a été enregistrée ou pas
 * 
 *  Le message envoyé par le logicile à l'arduino permet d'ouvrir ou pas la porte 
 *  (servomoteur positionné à 0° ou 90°) la led concerné s'allume puis s'éteint après. 
 * 
 *  Si la porte s'ouvre, tant que le capteur reste actionné, le porte reste ouverte sinon elle
 *  se ferme juste après que le capteur n'est plus actionné
 * 
 *  ID des cartes utilisé pour les explications
 *  0x49, 0xD3, 0x46, 0xC1  /49D346C1
 *  0x53, 0x7B, 0x91, 0x3   /537B9103
 *
 *
 *  -----------------------------------------------------------------------------------------
 *              MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino
 *              Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
 *  Signal      Pin          Pin           Pin       Pin        Pin              Pin
 *  -----------------------------------------------------------------------------------------
 *  RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST
 *  SPI SS      SDA(SS)      10            53        D10        10               10
 *  SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16
 *  SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14
 *  SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15
*/

#include <Servo.h>
#include <SPI.h> // SPI
#include <MFRC522.h> // RFID

// Arduino mega pin 
#define SS_PIN  53
#define RST_PIN 5

MFRC522 rfid(SS_PIN, RST_PIN); // Déclaration object MFRC522

// Déclaration object Servo
const byte pin_servo = 2;
Servo monServo;

// pins leds
#define Led_rouge 4
#define Led_verte 3

#define capteur_ir 6 // pin capteur ir

#define ATTENTE 1500 // Attente extinction led 
#define TIMEOUT 4000 // Délais de fermeture automatique de la porte 

unsigned long init_time; // Temps de depart de comptage

String reception;    // stock les données reçu via le port série

void setup(){ 
  Serial.begin(9600);// Initialisation de la communication série
  SPI.begin();       // Initialisation du bus SPI
  rfid.PCD_Init();   // Init Initialisation

  // Servo moteur relier au pin
  monServo.attach(pin_servo);
  monServo.write(0);
  
  //initialisation des pins des leds comme sortie
  pinMode(Led_rouge, OUTPUT);
  pinMode(Led_verte, OUTPUT);

  //initialisation du pin du capteur ir comme entrée
  pinMode(capteur_ir, INPUT);
}
 
void loop() {
  // Initialise la boucle si aucun badge n'est présent 
  if ( !rfid.PICC_IsNewCardPresent()){return;}
  // Vérifie la présence d'un nouveau badge 
  if ( !rfid.PICC_ReadCardSerial()){return;}
    
  // Transmission de l'ID du badge (4 octets) 
  for(byte i = 0; i < 4; i++){
    Serial.write(rfid.uid.uidByte[i]);
  } 

  // Attente de reception des données
  while(true){
    if(Serial.available()){
      // Reception des données via le port série
      reception = Serial.readStringUntil('\n');
      break;// sortie de la boucle 
    }   
  }

  // Si badge reconnu : Ouverture & Fermeture de la porte
  if(reception == "TRUE"){
    // Etats des leds
    digitalWrite(Led_rouge, LOW);
    digitalWrite(Led_verte, HIGH);
  
    // Positionnement du servomoteur
    for(int i = 0; i < 90; ++i){
      monServo.write(i);
      delay(11); 
    }
      
    init_time = millis(); // Initialisation du temps de départ pour la fermeture automatique
    
    // Attente déclanchement capteur
    while(digitalRead(capteur_ir) == true){
      // Si capteur déclanché : on sort de la boucle 
      if(digitalRead(capteur_ir) == false && millis() - init_time < TIMEOUT){break;}
      // Si le temps est écoulé : on sort de la boucle 
      if(millis() - init_time > TIMEOUT){break;}
    }
      
    // Attente fermeture de la porte : Si le capteur n'est plus déclanché, on sort de la boucle
    while(digitalRead(capteur_ir) == false){delay(10);}
         
    // Positionnement du servomoteur
    for(int i = 90; i >= 0; --i){
      monServo.write(i);
      delay(11); 
    }   
  }// fin if

  // Si badge non reconnu
  if(reception == "FALSE"){
    //etats des leds
    digitalWrite(Led_rouge, HIGH);
    digitalWrite(Led_verte, LOW);
    delay(ATTENTE); // Attente 
  }

  // Extinction des leds
  digitalWrite(Led_rouge, LOW);
  digitalWrite(Led_verte, LOW);
  
  reception=""; // Re-initialisation de la variable
  
  // Re-initialisation RFID
  rfid.PICC_HaltA(); // Halt PICC
  rfid.PCD_StopCrypto1(); // Stop encryption on PCD
}