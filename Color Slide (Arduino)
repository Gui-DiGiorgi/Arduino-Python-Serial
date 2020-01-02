// This is the arduino part of the project, the led needs to be the RGB Led to make the colors mix, but it also works for three separate 
// leds, all this does is synchron the lhe value of the slide on python with the intensity of three leds of the arduino
// The debug part was there so I could see what was going on with the value of the variables while making it

const int n_pins = 3;

int pins [n_pins] = {3,5,6};

int intense [n_pins] = {0,0,0};

int debug = 0;

void setup() {
  Serial.begin(9600);
  for (int i; i<n_pins; i++){
    pinMode(pins[i],OUTPUT);
  }
  for (int i; i<n_pins; i++){
    analogWrite(pins[i],0);
  }

}

void loop() {
  
  if (Serial.available() > 0) {
    
    String bytes = Serial.readStringUntil('\n');
    int cycle = 0;
    int stage = 0;
    String msg [n_pins] = {"","",""};
    
    while (cycle<bytes.length() and stage<3){
      
      if (bytes[cycle] == ' '){
        stage++;
      }
      else{
        msg[stage] += bytes[cycle];
      }
      cycle++;
    }
    
    for (int j = 0; j<stage+1; j++){
      int power = msg[j].toInt();
      if (power>=0 and power<256){
        intense[j] = power; 
    }
    }

    if (debug == 1){
    Serial.print("Message: ");
    for (int i = 0; i<n_pins; i++){
    Serial.print(msg[i]);
    Serial.print(' ');
    }
    Serial.print("Values: ");
    for (int i = 0; i<n_pins; i++){
    Serial.print(intense[i]);
    Serial.print(' ');
    }
    Serial.print('\n');
    }

  }

  if (debug == 0){
  for (int i = 0; i<n_pins; i++){
      analogWrite(pins[i],intense[i]);
}
}
}
