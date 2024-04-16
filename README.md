# utv_robot
for building, navigate to catkin_ws and do catkin_make
source devel/setup.bash from catkin_ws
for running:
roslaunch utv_simulation utv_sim.launch

for simple_robot sim:
- step 1: open a new terminal window
- step 2: navigate to catkin_ws folder
- step 3: run 'catkin_make'
- step 4: run 'source devel/setup.bash'
- step 5: run 'roslaunch utv_simulation simple_world.launch'
- step 6: open a new termnal window
- step 7: run 'source devel/setup.bash'
- step 8: run 'rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/my_robot/cmd_vel'
- step 9: use q/z to adjust speed to ~0.15. use e/c to adjust turn to ~0.25
