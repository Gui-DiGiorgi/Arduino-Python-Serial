// It reads and sends the values of the joystick, it needs the 50 delay because if not, it's too fast for the python code to process it

#define pinVRx A2 // Pino Analog
#define pinVRy A1

void setup() {
  Serial.begin(9600);
  pinMode(pinVRx, INPUT);
  pinMode(pinVRy, INPUT);
}

void loop() {

  int valorVRx = analogRead(pinVRx);
  int valorVRy = analogRead(pinVRy);
  
  Serial.print(map(valorVRx,0,1023,0,180)); // Valor VRx
  Serial.print(" "); // Espaço de separação das variáveis
  Serial.print(map(valorVRy,0,1023,0,180)); // Valor VRy
  Serial.print('\n'); // Nova linha para a próxima dupla de variáveis
  
  delay(50);
  
 }  
