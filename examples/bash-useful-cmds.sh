for i in `<executable shell cmd on remote mc>`; do echo $i; ssh -n $i sudo grep -i "error" /var/log/my-cool*.log*; done

# for some reason the ls command needs ot be enclosed in double or single quotes, not so the grep command above!
for i in `<executable shell cmd on remote mc>`; do echo $i; ssh -n $i 'sudo ls -l /var/www/cosmos/release_*'; done

# multiple cmds on remote
for i in `<executable shell cmd on remote mc>`; do echo $i; ssh -n $i cd /var/www/media && find . -name img312489.jpg -print; done

# multi-line for loop with if - continue
for i in `ls cosmos/products`; \
	do echo $i; \
	if [$i == '__init__.py']; then \
	  continue; \
	fi \
	tar -aczf ~/dist-packages/cosmos.templates.tar.gz -C cosmos/products/$i/templates .; \
done \


#!/bin/bash
for i in `ls cosmos/products`;
	do echo $i;
	if [$i == '__init__.py']; then
	  continue
	fi
	tar -aczf ~/dist-packages/cosmos.templates.tar.gz -C cosmos/products/$i/templates .;
done

# find exec
find . -name \*.pyc -exec rm {} \;
