import subprocess
batch_file_path = r'E:\note.bat'

try:
    subprocess.run([batch_file_path], shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error executing batch file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
