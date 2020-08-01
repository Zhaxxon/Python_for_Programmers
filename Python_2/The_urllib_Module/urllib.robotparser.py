import urllib.robotparser
robot = urllib.robotparser.RobotFileParser()
print (robot.set_url('http://arstechnica.com/robots.txt'))
#None

print (robot.read())
#None

print (robot.can_fetch('*', 'http://arstechnica.com/'))
#True

print (robot.can_fetch('*', 'http://arstechnica.com/cgi-bin/'))
#False