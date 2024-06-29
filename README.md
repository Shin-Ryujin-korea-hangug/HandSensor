# Hand-Sensor

FIRST
----------------------------------------------------------------------
  git clone https://github.com/Shin-Ryujin-korea-hangug/HandSensor &&
  pip install opencv-python &&
  pip install numpy &&
  pip install python-time &&
  pip install PyAutoGUI &&
  cd HandSensor &&
  python3 main.py
----------------------------------------------------------------------

  How to Use the Hand Tracking and Control Program
This program allows you to control your computer's mouse using hand gestures detected through your webcam. Here’s a step-by-step guide on how to use it and what each hand gesture does:

Setup and Start the Program:

Ensure your webcam is connected and working.
Run the eltanima.py script.
Hand Detection:

The program will start by detecting your hand and its landmarks using the webcam.
Ensure your hand is visible within the webcam frame for proper detection.
Mouse Movement:

Single Index Finger Up (Moving Mode):
Raise only your index finger while keeping the other fingers folded.
Move your index finger around, and the mouse cursor on your screen will follow the movement of your finger.
This mode allows you to move the cursor to different positions on the screen.
Mouse Clicking:

Index and Middle Fingers Up (Clicking Mode):
Raise both your index and middle fingers while keeping the other fingers folded.
When you bring your index and middle fingers close together (less than 40 pixels apart), the program will perform a mouse click.
This mode allows you to click on items on your screen without physically pressing the mouse button.
Visual Feedback:

A rectangle is drawn on the webcam feed to indicate the active area for hand detection.
A circle will appear on your finger tip in Moving Mode, showing the detected finger position.
When a click is detected in Clicking Mode, another circle will be drawn to indicate the click action.
Summary of Hand Gestures and Actions:
Single Index Finger Up:

Action: Move the mouse cursor.
How: Keep only the index finger up, others folded.
Index and Middle Fingers Up:

Action: Click the mouse.
How: Keep both the index and middle fingers up and bring them close together.
This program provides an intuitive way to control your computer using simple hand gestures, making it especially useful for touch-free interactions.

If you encounter any issues or need further customization, feel free to adjust the parameters or add additional functionality to the code as per your requirements.
