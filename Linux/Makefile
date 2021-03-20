CFLAGS_ALA_MISC_DRIVER.o = -DDEBUG

obj-m += ALA_MISC_DRIVER.o

KDIR ?= /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)

default:
	$(MAKE) -C $(KDIR) M=$(PWD) modules
clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean
 
