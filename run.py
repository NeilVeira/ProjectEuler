import os
import argparse 
import time

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("-x", action="store_true", default=False, help="don't compile")
args = parser.parse_args()
f = args.file
 
if os.path.exists(f):
    name = f[:f.rfind(".")]
        
    if args.x:
        compile = 0
    else:
        compile = os.system("g++ -o %s.exe -std=c++11 %s.cpp " %(name,name))
        
    if compile == 0:
        start = time.time()
        os.system("%s.exe"  %(name))
        end = time.time()
        print "Execution time: %.2fs" %(end-start)
else:
    print "Error: no such file",f