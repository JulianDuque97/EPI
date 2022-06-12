////////////////////////////
#define ADCFLUJO   36 //ESP32 pin GIOP3 (ADC0) connected to Venturi
#define ADCPRESION 39 // ESP32 pin GIOP36 (ADC3)
const float ADC_mV = 0.8058608058;       // convesion multiplier from ESP32 ADC value to voltage in mV
const float SensorOffset = 244.0;     // in mV taken from datasheet; 244mv medido con multimetro
const float sensitivity = 4.413;      // in mV/mmH2O taken from datasheet
const float mmh2O_cmH2O = 10;         // divide by this figure to convert mmH2O to cmH2O
const float mmh2O_kpa = 0.00981;      // convesion multiplier from mmH2O to kPa
///////////////////////////////

void setup() {
  Serial.begin(115200); //iniciar puerto serie a 115200 baudios}

}

void loop() {
  float FLUJO = (analogRead(ADCFLUJO) * ADC_mV - SensorOffset) / sensitivity / mmh2O_cmH2O; // resultado en cmH2O
  float ADC36 = (analogRead(ADCFLUJO)*ADC_mV);
  Serial.println(ADC36);
  delay(100);

}
