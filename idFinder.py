import subprocess

def get_connected_emulators():
    """
    Returns a list of emulator IDs currently connected via ADB.
    """
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")[1:]  # Skip the first line: "List of devices attached"
    devices = [line.split()[0] for line in lines if "device" in line]
    return devices

def type_text_on_emulator(emulator_id, text):
    """
    Makes the emulator type the given text using ADB input.
    Special characters like '-' and ':' are encoded for ADB.
    """
    # Encode special characters
    text = text.replace("-", "%2D").replace(":", "%3A")
    
    # Send text to emulator
    subprocess.run(["adb", "-s", emulator_id, "shell", "input", "text", text])

def main():
    emulators = get_connected_emulators()
    if not emulators:
        print("No emulators found.")
        return
    
    print(f"Found emulators: {emulators}")
    
    for emu in emulators:
        print(f"Typing ID on {emu}...")
        type_text_on_emulator(emu, emu)

if __name__ == "__main__":
    main()
