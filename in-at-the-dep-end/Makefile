all: main.r

main.r: main.exe
	./$< > $@ 2>&1
	cat $@

SOURCES := $(sort $(wildcard module*.f90))
OBJECTS := $(SOURCES:.f90=.o)

main.exe: main.o $(OBJECTS)
	nagfor $^ -o $@

%.o %.mod: %.f90
	nagfor -c $<

DEPS := $(SOURCES:.f90=.P) main.P

%.P: %.f90
	nagfor =depend -otype=make $< -o $@

include Depends

Depends: $(DEPS)
	cat $^ > $@

clean:
	rm -f *.r *.exe *.o *.mod Depends *.P
