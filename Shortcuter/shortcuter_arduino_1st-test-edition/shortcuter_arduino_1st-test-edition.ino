#include <Keyboard.h>

String inData = ""; // Buffer for incoming serial data

void setup() {
  Serial.begin(9600);   // For debugging (USB)
  Serial1.begin(9600);  // Nextion connection (TX1/RX1)
  Keyboard.begin();
  
  Serial.println("Shortcuter ready!");
}

void loop() {
  while (Serial1.available()) {
    char c = Serial1.read();

    // Collect characters until newline or semicolon (optional)
    if (c == '\n' || c == '\r') {
      if (inData.length() > 0) {
        handleCommand(inData);
        inData = "";
      }
    } else {
      inData += c;
    }
  }
}

// This runs when a full message like "b0" is received. Examples below.
void handleCommand(String cmd) {
  cmd.trim();

  if (cmd == "b0") {
    sendShortcut(KEY_LEFT_CTRL, 'c');  // Ctrl + C
  } 
  else if (cmd == "b1") {
    sendShortcut(KEY_LEFT_CTRL, 'v');  // Ctrl + V
  } 
  else if (cmd == "b2") {
    sendShortcut(KEY_LEFT_CTRL, 'z');  // Ctrl + Z
  } 
  else if (cmd == "b3") {
    sendShortcut(KEY_LEFT_GUI, 'r');   // Windows + R
  } 
  // and so on. the last button might be the one to switch templates/screens. might use physical button for that.
}

// Needed to press 2 keys(as I understood). Example: Ctrl + C.
void sendShortcut(uint8_t modKey, char key) {
  Keyboard.press(modKey);
  Keyboard.press(key);
  delay(100);
  Keyboard.releaseAll();
}