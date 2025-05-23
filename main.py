import win32serviceutil
import win32service
import win32event
import subprocess
import sys
import os

class UvicornService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MyUvicornService"
    _svc_display_name_ = "Uvicorn FastAPI Service"
    _svc_description_ = "Runs a Uvicorn server as a Windows service"

    def __init__(self, args):
        super().__init__(args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.process = None

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        if self.process:
            self.process.terminate()

    def SvcDoRun(self):
        base_dir = r"C:\path\to\your\project"
        uvicorn_cmd = [
            sys.executable, "-m", "uvicorn",
            "app:app",
            "--host", "0.0.0.0",
            "--port", "8000"
        ]
        self.process = subprocess.Popen(uvicorn_cmd, cwd=base_dir)
        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(UvicornService)
