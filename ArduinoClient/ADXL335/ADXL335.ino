//Analog read pins
const int xPin = A0;
const int yPin = A1;
const int zPin = A2;
const int finger1 = A3;
const int finger2 = A4;
const int finger3 = A5;
const int finger4 = A6;


int minVal = 274; //3;   // 265;
int maxVal = 344; //685; // 402

char label='?';
double x;
double y;
double z;
boolean pause=true;

void setup(){
  Serial.begin(9600);
}

void loop(){

  //read the analog values from the accelerometer
  int xRead = analogRead(xPin);
  int yRead = analogRead(yPin);
  int zRead = analogRead(zPin);
  int fingerVal1 = analogRead(finger1);
  int fingerVal2 = analogRead(finger2);
  int fingerVal3 = analogRead(finger3);
  int fingerVal4 = analogRead(finger4);
  
  //convert read values to degrees -90 to 90 – Needed for atan2
  int xAng = map(xRead, minVal, maxVal, //atan2 outputs the value of -π to π (radians)
  //We are then converting the radians to degrees
  -90, 90);
  int yAng = map(yRead, minVal, maxVal, -90, 90);
  int zAng = map(zRead, minVal, maxVal, -90, 90);
  
  //Caculate 360deg values like so: atan2(-yAng, -zAng)
  x = RAD_TO_DEG * (atan2(-yAng, -zAng) + PI);
  y = RAD_TO_DEG * (atan2(-xAng, -zAng) + PI);
  z = RAD_TO_DEG * (atan2(-yAng, -xAng) + PI);

  if (Serial.available()>0) {
    char input = Serial.read();
    if (input == '5') {
      pause = !pause;
    }
    else if (input >= 'A' && input <= 'Z') {
      label = input;
//      Serial.print("label changed to : ");
//      Serial.println(label);
    }
  }


  if (!pause) {
    //Output the caculations
    Serial.print("label: ");
    Serial.print(label);
    Serial.print(", x: ");
    Serial.print(x);
    Serial.print(", y: ");
    Serial.print(y);
    Serial.print(", z: ");
    Serial.print(z);
    Serial.print(", f: ");
    Serial.println(fingerVal1);
//    Serial.print(", g: ");
//    Serial.print(fingerVal2);
//    Serial.print(", h: ");
//    Serial.print(fingerVal3);
//    Serial.print(", i: ");
//    Serial.println(fingerVal4);
  }
  
  
  
  delay(50);//just here to slow down the serial output – Easier to read
}
