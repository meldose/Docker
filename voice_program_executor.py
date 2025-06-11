#!/usr/bin/env python3

import rospy # imported rospy
import subprocess  # imported subprocess
import os # imported os module 
from std_msgs.msg import String # imported String   


# class for Voice Program Executor
class VoiceProgramExecutor():
    def __init__(self):
        self._sub_command = rospy.Subscriber("/command", String, self.command)
        self._program_dir = ""

# function for command 
    def command(self, msg: String):
        command = msg.data
        command_list = command.split(" ")
        if command_list[0] != "sort":
            return
        script_path = os.path.expanduser("~/neura/GUI/backend/py_script/runnerGroupSystems.sh")
        # feel free to change something here :)
        program_path = os.path.join(self._program_dir, f"sort_{command_list[1]}.py")
        subprocess.run([script_path, program_path], check=True)

# calling main function 
if __name__ == "__main__":
    rospy.init_node("voice_program_executor")
    VPE = VoiceProgramExecutor
    rospy.spin()