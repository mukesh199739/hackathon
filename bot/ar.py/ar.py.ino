#include <ESP8266WiFi.h>
#include <WebSocketsServer.h>

const char* ssid     = "hnr";
const char* password = "qwerty1211";


WebSocketsServer webSocket = WebSocketsServer(81);

void webSocketEvent(uint8_t num, WStype_t type, uint8_t * payload, size_t lenght) {
    Serial.printf("[%u] get Message: %s\r\n", num, payload);
    switch(type) {
        case WStype_DISCONNECTED:      
            break;
        case WStype_CONNECTED: 
            {
              IPAddress ip = webSocket.remoteIP(num);
              Serial.printf("[%u] Connected from %d.%d.%d.%d url: %s\r\n", num, ip[0], ip[1], ip[2], ip[3], payload);    
            }
            break;
        
        case WStype_TEXT:
            {
              //Serial.printf("[%u] get Text: %s\r\n", num, payload);
              String _payload = String((char *) &payload[0]);
              //Serial.println(_payload);
              
              String idLed = (_payload.substring(0,4));
              String intensity = (_payload.substring(_payload.indexOf(":")+1,_payload.length()));
              int intLed = intensity.toInt();
              if(intLed==1)
              {
                Serial.println("youtube");
                digitalWrite(D2,HIGH);
                digitalWrite(D3,LOW);
                digitalWrite(D5,HIGH);
                digitalWrite(D6,LOW);
              }
              else if(intLed==2)
              {
                Serial.println("google");
                digitalWrite(D2,LOW);
                digitalWrite(D3,HIGH);
                digitalWrite(D5,LOW);
                digitalWrite(D6,HIGH);
              }
              else if(intLed==3)
              {
                Serial.println("gmail");
                digitalWrite(D2,HIGH);
                digitalWrite(D3,LOW);
                digitalWrite(D5,LOW);
                digitalWrite(D6,HIGH);
              }
              else if(intLed==4)
              {
                Serial.println("yahoo");
                digitalWrite(D2,LOW);
                digitalWrite(D3,HIGH);
                digitalWrite(D5,HIGH);
                digitalWrite(D6,LOW);
              }
              else
              {
                Serial.println("twitter");
                digitalWrite(D2,LOW);
                digitalWrite(D3,LOW);
                digitalWrite(D5,LOW);
                digitalWrite(D6,LOW);
              }
             
              
            }   
            break;     
             
        case WStype_BIN:
            {
              hexdump(payload, lenght);
            }
            // echo data back to browser
            webSocket.sendBIN(num, payload, lenght);
            break;
  
    }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
  pinMode(D2,OUTPUT);
  pinMode(D3,OUTPUT);
  pinMode(D5,OUTPUT);
  pinMode(D6,OUTPUT);

  while(WiFi.status() != WL_CONNECTED) {
     Serial.print(".");
     delay(200);
  }
    
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  delay(500);  
   
  Serial.println("Start Websocket Server");
  webSocket.begin();
  webSocket.onEvent(webSocketEvent);
}

void loop() {
  webSocket.loop();
}



