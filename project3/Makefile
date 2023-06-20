run:
    python xkcdpwgen.py
all:
	mv xkcdpwgen xkcdpwgen.py
	echo -e '#!/bin/bash\npython xkcdpwgen.py "$$@"' > xkcdpwgen
	chmod +x xkcdpwgen

