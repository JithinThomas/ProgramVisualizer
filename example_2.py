from subprocess import Popen, PIPE, STDOUT
from threading  import Thread

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x

p = Popen(['gdb', '/home/jithinpt/custom_debugger/a.out'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
q = Queue()

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

def read_line_non_blocking():
	try: line = q.get(timeout=.1)
	except Empty:
		return '__DONE__'
	else:
		return line

def exec_cmd(proc, cmd):
	proc.stdin.write(cmd + '\n')
	while(True):
		if proc.poll() != None:
			break
		o = proc.stdout.readline()
		print(o.rstrip())

def exec_cmd_2(proc, cmd):
	proc.stdin.write(cmd + '\n')
	line = read_line_non_blocking()
	while line != '__DONE__':
		print line.rstrip()
		line = read_line_non_blocking()

def main():
	while(True):
		cmd = raw_input("[SIM] (gdb) ")
		#exec_cmd(p, cmd)
		exec_cmd_2(p, cmd)

t = Thread(target=enqueue_output, args=(p.stdout, q))
t.daemon = True # thread dies with the program
t.start()

main()
