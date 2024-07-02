RESDIR = results

.PHONY: all clean

all: dir

dir:
	@mkdir -p $(RESDIR)

clean:
	@rm -rf $(RESDIR)