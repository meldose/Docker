#!/usr/bin/env python3

import rospy
import subprocess
import os
from std_msgs.msg import String


class VoiceProgramExecutor():
    def __init__(self):
        self._sub_command = rospy.Subscriber("/command", String, self._command_cb)
        self._program_dir = ""

    def _command_cb(self, msg: String):
        command = msg.data
        command_list = command.split(" ")
        if command_list[0] != "sort":
            return
        script_path = os.path.expanduser("~/neura/GUI/backend/py_script/runnerGroupSystems.sh")
        # feel free to change something here :)
        program_path = os.path.join(self._program_dir, f"sort_{command_list[1]}.py")
        subprocess.run([script_path, program_path], check=True)

if __name__ == "__main__":
    rospy.init_node("voice_program_executor")
    VPE = VoiceProgramExecutor
    rospy.spin()