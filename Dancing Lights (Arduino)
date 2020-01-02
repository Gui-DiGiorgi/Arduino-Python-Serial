// The Arduino part of the project

const int n_pins = 7;

int pins [n_pins] = {2,3,5,7,8,12,13};

int intense [n_pins] = {0,0,0,0,0,0,0};

char code [n_pins] = {'A','B','C','D','E','F','G'};

int chosen_light = 0;

char old_bytes = '0';

int old_light = 0;

int debug = 0;

long unsigned now = 0;

int detection_delay = 500;

void setup() {
  Serial.begin(9600);
  for (int i; i<n_pins; i++){
    pinMode(pins[i],OUTPUT);
  }
  
  for (int i; i<n_pins; i++){
    digitalWrite(pins[i],LOW);
  }

  delay(500);
  
  now = millis();

}

void loop() {
  
  if (Serial.available()) {

    String bytes = Serial.readStringUntil('\n');

    int no_sound = 0;
    
    for (int i; i<n_pins; i++){
      if (bytes[0] == code[i]){
        chosen_light = i;
        no_sound++;
        break;
        }
    }
    
    if (no_sound == 0 and millis()-now >= detection_delay){
      digitalWrite(pins[chosen_light],LOW);
      intense[chosen_light] = 0;
      now = millis();
      old_bytes = bytes[0];
    }
    
    if (bytes[0] != old_bytes and no_sound == 1){
      digitalWrite(pins[chosen_light],HIGH);
      intense[chosen_light] = 1;
      if (chosen_light != old_light){
        digitalWrite(pins[old_light],LOW);
        intense[old_light] = 0;
      }
      old_bytes = bytes[0];
      old_light = chosen_light;
    }

    if (no_sound == 1){
        now = millis();
    }
    
    if (debug == 1){
      
    Serial.print("bytes[0]: ");
    Serial.print(bytes[0]);
    Serial.print(" - chosen_light: ");
    Serial.print(chosen_light);
    Serial.print(" - no_sound: ");
    Serial.print(no_sound);
    
    if (no_sound == 0 and millis()-now >= detection_delay){
      Serial.print(" - old_bytes(delay): ");
      Serial.print(old_bytes);
    }
    
    if (bytes[0] != old_bytes and no_sound == 1){
      Serial.print(" - old_bytes(change): ");
      Serial.print(old_bytes);
    }

    Serial.print('\n');
    
    Serial.print("Values: ");
    for (int i = 0; i<n_pins; i++){
    Serial.print(intense[i]);
    Serial.print(' ');
    }
    Serial.print('\n');
    }
  }
}
