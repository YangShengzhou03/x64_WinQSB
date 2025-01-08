import subprocess

from PyQt6.QtCore import QThread, pyqtSignal


class CheckVCRuntimesThread(QThread):
    finished = pyqtSignal(bool)

    def run(self):
        result = self.check_vcruntimes_installed()
        self.finished.emit(result)

    def check_vcruntimes_installed(self):
        try:
            output = subprocess.check_output(['wmic', 'product', 'get', 'name'], stderr=subprocess.STDOUT, shell=True)
            output_str = output.decode('utf-8', errors='ignore').split('\n')

            runtimes_to_check = [
                "Microsoft Visual C++ 2022 X86 Minimum Runtime",
                "Microsoft Visual C++ 2022 X86 Additional Runtime"
            ]
            for line in output_str:
                line = line.strip()
                if any(runtime in line for runtime in runtimes_to_check):
                    return True
            return False

        except Exception as e:
            print(f"Error: {e}")
            return False
