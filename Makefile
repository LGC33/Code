BIN_DIR=bin
C_DIR=c
CPP_DIR=cpp
JAVA_DIR=java
PY_DIR=python
CFLAGS=-Wall -std=c11
CXXFLAGS=-Wall -std=c++17

C_SOURCES := $(shell find $(C_DIR) -name '*.c')
CPP_SOURCES := $(shell find $(CPP_DIR) -name '*.cpp')
JAVA_SOURCES := $(shell find $(JAVA_DIR) -name '*.java')

all: $(BIN_DIR) build-c build-cpp build-java

$(BIN_DIR):
	mkdir -p $(BIN_DIR)

build-c:
	@for f in $(C_SOURCES); do \
	out=$(BIN_DIR)/$$(basename "$$f" .c); \
		$(CC) $(CFLAGS) "$$f" -o "$$out" || true; \
	done

build-cpp:
	@for f in $(CPP_SOURCES); do \
	out=$(BIN_DIR)/$$(basename "$$f" .cpp); \
		$(CXX) $(CXXFLAGS) "$$f" -o "$$out" || true; \
	done

build-java:
	@for f in $(JAVA_SOURCES); do \
		javac -d $(BIN_DIR) "$$f" || true; \
	done

run-python:
	@python3 $(FILE)

clean:
	rm -rf $(BIN_DIR)
