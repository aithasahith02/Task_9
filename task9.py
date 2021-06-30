#!/usr/bin/python3
import cgi
import subprocess
print("Content-Type: text/html\n\n")
field = cgi.FieldStorage()
cmd = field.getvalue('q')
msg=cmd.split()
def run(inp) :
	print("Yeah Sure Im Always for you....\n")
	out = subprocess.getoutput("sudo "+inp+" --kubeconfig admin.conf")
	print(out)
	
if msg[4] == "pod" :
	inp="kubectl run "+msg[10]+" --image="+msg[6]
	run(inp)
elif msg[2] == "delete" :
	inp = "kubectl delete all --all --all-namespaces"
	run(inp)
elif msg[4] == "deployment" :
	inp = "kubectl create deployment --name="+msg[11]+" --image="+msg[6]
	run(inp)
else
	print("Im unable to understand you")
