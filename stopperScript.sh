kill "$(ps -fu | grep "python3 CONTROL_" | grep -v -e grep -e "stop" | awk '{print $2}')"

