///////////////////////////////
TaskHandle_t Tarea1;
///////////////////////////////
#define ADCFLUJO   36 //ESP32 pin GIOP3 (ADC0) connected to Venturi
#define ADCPRESION 39 // ESP32 pin GIOP36 (ADC3)
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
void setup() {

  
  Serial.begin(115200); //iniciar puerto serie a 115200 baudios}
  ledcAttachPin(PWM, 0);
  ledcSetup(0, 5000, 8);
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
  
  while(digitalRead(sensor2)==LOW){
    digitalWrite (LPWM, HIGH);
    digitalWrite (RPWM, LOW);
    ledcWrite(0, 175); 
    }
  motor_stop();
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


void loop_tarea1(void * pvParameters)
{
  while(1)
  {
    if (Serial.available() > 0)
   {
      String str = Serial.readStringUntil('\n');
      volumen = str.toInt();
      Serial.println(volumen);
   }
   delay(10);
  }
}


void loop(){
  
   TI=millis();
   while(cont != volumen)
   {
    lecturaEncoder();
    motor_cw();
   }
   motor_stop();
   //Serial.println(TI);
   while((digitalRead(sensor2))!=HIGH){
   motor_ccw();
   }
   TE=millis();
   TE=(TE-TI)/1000;
   Serial.println(TE);
   
   
   delay(100);
   cont=0;
}
