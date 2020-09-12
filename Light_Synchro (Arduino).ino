// Connect the output light to the pins 3,5,7,9, which will be the output for the 'a','b','c','d' light codes, feel free to
// add more lights as you see fit, and don't forget to adjust both codes to accomodate the new setting

int pins [4] = {3,5,7,9};
char names[4] = {'a','b','c','d'};


void setup() {
  Serial.begin(9600);
  for (int i; i<4; i++){
    pinMode(pins[i],OUTPUT);
  }
  for (int i; i<4; i++){
    digitalWrite(pins[i],LOW);
  }

}

void loop() {
  if (Serial.available() > 0) {
    
    String msg = Serial.readStringUntil('\n');
    String code = "";
    int stp = 0;
    
    for (int i = 0; i<msg.length(); i++){

      if (msg[i] == ' '){
        stp = i+1;
        break;
      }
      else{
        code += msg[i];
      }
    }
    Serial.print(code);
    Serial.print(' ');
    
    String dur = "";

    if (not stp==0){
    
    for (int i = stp; i<msg.length(); i++){
      dur+=msg[i];
    }
    }
    else{
      dur="1000";
    }
    
    int zoom = dur.toInt();
    Serial.print(zoom);
    Serial.print('\n');

    if (zoom>=50 and zoom<=5000)
    {
    for (int i; i<4; i++){
    if (code[0] == names[i] and code.length()==1)
    {
      digitalWrite(pins[i],HIGH);
      delay(zoom);
      digitalWrite(pins[i],LOW);
    }
    }
    }
}
}
