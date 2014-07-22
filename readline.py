import sys
import re
 
for i,line in enumerate(sys.stdin): 
		pattern = re.compile(r'^[0-9]{8,16} T (mu_\w+$)')
		match = pattern.match(line);
		if match:
			sys.stdout.write(match.group(1) + '\n')
