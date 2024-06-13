import subprocess
import time

def run_client_script(script_name, python_path):
    process = subprocess.Popen([python_path, script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process


if __name__ == '__main__':
    # Full path to the Python interpreter with the necessary packages
    python_path = r'C:\Users\utkar\PycharmProjects\Infilect\infilect\Scripts\python.exe'

    client_scripts = ["client1.py", "client2.py", "client3.py", "client4.py", "client5.py"]

    processes = []
    start_time = time.time()
    for script in client_scripts:
        process = run_client_script(script, python_path)
        processes.append(process)


    # Wait for all processes to complete
    for process in processes:
        stdout, stderr = process.communicate()
        print(f"Output of {process.args[1]}:\n{stdout.decode()}")
        if stderr:
            print(f"Error in {process.args[1]}:\n{stderr.decode()}")
    print("End time of all--- %s seconds ---" % (time.time() - start_time))
