import cv2
import numpy as np
import threading

class CoconutIDE:
    def __init__(self):
        self.editor_text = ""  # Text input for code editor
        self.output_text = "Welcome to Coconut IDE!"  # Output display
        self.running = True
        self.interpreter = None

    def draw_editor(self, frame):
        """Draw the code editor on the frame."""
        font = cv2.FONT_HERSHEY_SIMPLEX
        y_offset = 30
        for line in self.editor_text.split("\n")[-20:]:  # Show the last 20 lines
            cv2.putText(frame, line, (10, y_offset), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            y_offset += 20

    def draw_output(self, frame):
        """Draw the output display on the frame."""
        font = cv2.FONT_HERSHEY_SIMPLEX
        y_offset = 30
        for line in self.output_text.split("\n")[-10:]:  # Show the last 10 lines
            cv2.putText(frame, line, (10, y_offset), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            y_offset += 20

    def execute_code(self, code):
        """Run the Coconut code and capture the output."""
        self.output_text += "\nRunning...\n"
        try:
            # Mock interpreter logic here
            result = f"Executed: {code}"  # Replace with actual interpreter
            self.output_text += f"{result}\nExecution Complete.\n"
        except Exception as e:
            self.output_text += f"Error: {e}\n"
        self.output_text += "-" * 30 + "\n"

    def run(self):
        """Main loop for the IDE."""
        editor_frame = np.zeros((400, 600, 3), dtype=np.uint8)
        output_frame = np.zeros((200, 600, 3), dtype=np.uint8)

        while self.running:
            # Create frames
            editor_frame.fill(0)
            output_frame.fill(0)

            # Draw text
            self.draw_editor(editor_frame)
            self.draw_output(output_frame)

            # Display frames
            cv2.imshow("Coconut IDE - Editor", editor_frame)
            cv2.imshow("Coconut IDE - Output", output_frame)

            key = cv2.waitKey(100) & 0xFF
            if key == ord('q'):  # Quit
                self.running = False
            elif key == ord('r'):  # Run the code
                threading.Thread(target=self.execute_code, args=(self.editor_text,)).start()
            elif key == 13:  # Enter key for new line
                self.editor_text += "\n"
            elif key == 8:  # Backspace
                self.editor_text = self.editor_text[:-1]
            elif key != 255:  # Append other keys to the editor text
                self.editor_text += chr(key)

        cv2.destroyAllWindows()

if __name__ == "__main__":
    ide = CoconutIDE()
    ide.run()
