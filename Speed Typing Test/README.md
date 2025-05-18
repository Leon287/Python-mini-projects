Typing Speed Calculator (GUI)

A simple yet interactive **Typing Speed Calculator** built using `tkinter`. This application lets you test and improve your typing speed with real-time feedback in terms of characters per second (CPS), characters per minute (CPM), words per second (WPS), and words per minute (WPM).

Features

Random text prompts loaded from a file
Real-time typing accuracy highlighting (green for correct, red for incorrect)
Live speed tracking (CPS, CPM, WPS, WPM)
Reset functionality for new attempts
Clean and responsive `tkinter` GUI

How to Run

1. Clone this repository or download the source code.

2. Make sure you have Python installed (>= 3.6).

3. Add your typing texts to the `texts.txt` file (one sentence per line).

4. Update the path to `texts.txt` in the code if needed:
   ```python
   self.texts = open("path/to/your/texts.txt", "r").read().split("\n")