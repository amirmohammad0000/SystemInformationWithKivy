##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Import
from kivymd.app import MDApp
from kivy.lang import Builder
import platform
import psutil

##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Import


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Class Main App
class MainApp(MDApp):
    # Start Function Main App
    def build(self):
        return Builder.load_file("style.kv")

    def GetInformation(self):
        # Start System Information
        self.root.ids.System.text = f"System : {platform.uname().system}"
        self.root.ids.NodeName.text = f"Node Name : {platform.uname().node}"
        self.root.ids.Release.text = f"Release : {platform.uname().release}"
        self.root.ids.Version.text = f"Version : {platform.uname().version}"
        self.root.ids.Machine.text = f"Machine : {platform.uname().machine}"
        self.root.ids.Processor.text = f"Processor : {platform.uname().processor}"
        # End System Information

        # Start Boot Time
        self.root.ids.BootTime.text = f"Boot Time : {psutil.boot_time()}"
        # End Boot Time

        # Start CPU Info
        self.root.ids.PhysicalCores.text = f"Physical Cores : {psutil.cpu_count()}"
        self.root.ids.TotalCores.text = f"Total Cores : {psutil.cpu_count()}"
        self.root.ids.MaxFrequency.text = f"Max Frequency : {psutil.cpu_freq().max} Mhz"
        self.root.ids.MinFrequency.text = f"Min Frequency : {psutil.cpu_freq().min} Mhz"
        self.root.ids.CurrentFrequency.text = f"Current Frequency : {psutil.cpu_freq().current} Mhz"
        self.root.ids.CPUState.text = f"CPU State : {psutil.cpu_stats()}"
        self.root.ids.TotalCPUUsage.text = f"Total CPU Usage : {psutil.cpu_percent()}"
        # End CPU Info

        # Start Memory Information
        self.root.ids.Total.text = f"Total : {psutil.virtual_memory().total}"
        self.root.ids.Available.text = f"Available : {psutil.virtual_memory().available}"
        self.root.ids.Used.text = f"Used : {psutil.virtual_memory().used}"
        self.root.ids.PercentageMemory.text = f"Percentage : {psutil.virtual_memory().percent} %"
        # End Memory Information

    # End Function Main App


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Class Main App


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Run Game
if __name__ == "__main__":
    MainApp().run()
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Run Game