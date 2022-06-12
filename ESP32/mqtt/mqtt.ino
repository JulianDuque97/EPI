#include <WiFi.h>
#include <PubSubClient.h>
// Replace the next variables with your SSID/Password combination
const char* ssid = "EPI";
const char* password = "ventilador";
// Add your MQTT Broker IP address, example:
//const char* mqtt_server = "192.168.1.144";
const char* mqtt_server = "10.42.0.1";
WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;
String messageTemp;
///////////////////////////////
TaskHandle_t Tarea1;
//////////////////////////////
const int  sensor1=25; // Llave optica 1  //rojo
const int sensor2=26;  // Llave optica 2  //verde
int cont=0;
int EstadoActual=0;
int EstadoAnterior=0;
//////////////////////////////
#define RPWM 33  // Entrada RPWM del driver
#define LPWM 27  // Entrada LPWM del driver
#define PWM 32   // Entrada PWM_Enable del driver  
//////////////////////////////
float TI = 0; //tiempo inspiratorio
float TE = 0; //tiempo espiratorio
float TI_aux = 0; //tiempo inspiratorio auxiliar
float TE_aux = 0; //tiempo espiratorio auxiliar
float TP=0; // tiempo de pausa
/////////////////////////////
float contVolumen = 0;
float contVolumen_aux=0;
float aux_cont = 3;
int volumen=0;
////////////////////////////
#define ADCFLUJO   36 //ESP32 pin GIOP3 (ADC0) connected to Venturi
#define ADCPRESION 39 // ESP32 pin GIOP36 (ADC3)
const float ADC_mV = 0.8056640625;       // convesion multiplier from ESP32 ADC value to voltage in mV
const float SensorOffset = 200.0;     // in mV taken from datasheet; 244mv medido con multimetro
const float sensitivity = 4.413;      // in mV/mmH2O taken from datasheet
const float mmh2O_cmH2O = 10;         // divide by this figure to convert mmH2O to cmH2O
const float mmh2O_kpa = 0.00981;      // convesion multiplier from mmH2O to kPa
///////////////////////////////

void setup() {

  Serial.begin(115200); //iniciar puerto serie a 115200 baudios}
  ledcAttachPin(PWM, 0);
  ledcSetup(0, 10000, 8);
  pinMode(sensor1 , INPUT);
  pinMode(sensor2 , INPUT);
  pinMode (RPWM, OUTPUT);
  pinMode (LPWM, OUTPUT);
  xTaskCreatePinnedToCore(
      loop_tarea1, /* Funcion de la tarea1 */
      "Tarea1", /* Nombre de la tarea */
      10000,  /* Tamaño de la pila */
      NULL,  /* Parametros de entrada */
      0,  /* Prioridad de la tarea */
      &Tarea1,  /* objeto TaskHandle_t. */
      0); /* Nucleo donde se correra */

  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  
}

void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}


void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();
  
  if (String(topic) == "esp32/volumen") {
    Serial.print("VOLUMEN:");
    volumen = messageTemp.toInt();
    Serial.println(volumen);
  }
  
  if (String(topic) == "esp32/frecuencia") {
    Serial.print("FRECUENCIA:");
    Serial.println(messageTemp);
  }
  messageTemp="0";
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      client.subscribe("esp32/volumen");
      client.subscribe("esp32/frecuencia");      
            }
     else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}


void motor_cw() {
  digitalWrite (LPWM, LOW);
  digitalWrite (RPWM, HIGH);
  ledcWrite(0, 223.14) ;//0-255  //DRIVER - ENABLE  // CODIGO - PWM
  //Serial.println ("MOTOR RUN CW");
}

void motor_ccw() {
  digitalWrite (LPWM, HIGH);
  digitalWrite (RPWM, LOW);
  ledcWrite(0, 223.14);//Chanel  0-255
  //Serial.println ("MOTOR RUN CCW");
}

void motor_stop() {
  digitalWrite (LPWM, LOW);
  digitalWrite (RPWM, LOW);
  ledcWrite(0, 0);// Chanel  0-255
  //Serial.println ("STOP");
}

void lecturaEncoder(){ 
   EstadoActual=digitalRead(sensor1);
  if (EstadoActual==1 & EstadoAnterior == 0){
      EstadoAnterior = EstadoActual;
      cont ++;
      //Serial.println(cont);
  }
   if (EstadoActual == 0 & EstadoAnterior == 1){
      EstadoAnterior = EstadoActual;
  }
}


void loop_tarea1(void * pvParameters){
  while(1)
  {

    float FLUJO = (analogRead(ADCFLUJO) * ADC_mV - SensorOffset) / sensitivity / mmh2O_cmH2O; // resultado en cmH2O
    Serial.println(FLUJO);
    delay(1000);
  }
}


void loop(){
  
  if (!client.connected()){
      reconnect();
      }
     client.loop();
     long now =millis();
     if(now - lastMsg > 1000){
      lastMsg=now;
      client.publish("esp32/dato","12");
     }
  
}
   
