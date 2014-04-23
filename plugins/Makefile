SHELL := /bin/sh
PGBUILD := ./pgbuild.py

BUILDDIR := _build
PLUGINS_PATH := $(BUILDDIR)/plugins
TESTING_PATH := $(BUILDDIR)/testing
STABLE_PATH := $(BUILDDIR)/stable

REMOTE_HOST := provd.xivo.fr
REMOTE_USER := root
REMOTE_TESTING_ADDONS_PATH := /var/www/provd.xivo.fr/plugins/1/addons/testing
REMOTE_STABLE_ADDONS_PATH := /var/www/provd.xivo.fr/plugins/1/addons/stable


.PHONY : build
build :
	rm -rf $(PLUGINS_PATH) $(TESTING_PATH)
	mkdir -p $(PLUGINS_PATH) $(TESTING_PATH)
	$(PGBUILD) -B -s . -d $(PLUGINS_PATH)
	$(PGBUILD) -P -s $(PLUGINS_PATH) -d $(TESTING_PATH)
	$(PGBUILD) -D -s $(TESTING_PATH) -d $(TESTING_PATH)
	chmod +r $(TESTING_PATH)/*


.PHONY : upload
upload : build
	rsync -v -rt --delete $(TESTING_PATH)/ $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_TESTING_ADDONS_PATH)


.PHONY : download-stable
download-stable :
	rsync -v -rt --delete $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_STABLE_ADDONS_PATH)/ $(STABLE_PATH)


.PHONY : build-stable
build-stable :
	$(PGBUILD) -D -s $(STABLE_PATH) -d $(STABLE_PATH)
	chmod +r $(STABLE_PATH)/*


.PHONY : upload-stable
upload-stable : build-stable
	rsync -v -rt --delete --exclude testing $(STABLE_PATH)/ $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_STABLE_ADDONS_PATH)


.PHONY : clean
clean :
	rm -rf $(BUILDDIR)/*
