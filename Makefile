# Makefile for multi-language project
# Supports C, C++, Java, and Python

# Directory definitions
BIN_DIR=bin
C_DIR=c
CPP_DIR=cpp
JAVA_DIR=java
PY_DIR=python

# Compiler flags
CC=gcc
CXX=g++
CFLAGS=-Wall -std=c11
CXXFLAGS=-Wall -std=c++17

# Source file discovery
C_SOURCES := $(shell find $(C_DIR) -name '*.c' 2>/dev/null)
CPP_SOURCES := $(shell find $(CPP_DIR) -name '*.cpp' 2>/dev/null)
JAVA_SOURCES := $(shell find $(JAVA_DIR) -name '*.java' 2>/dev/null)

# Generated targets
C_TARGETS := $(patsubst $(C_DIR)/%.c,$(BIN_DIR)/%,$(C_SOURCES))
CPP_TARGETS := $(patsubst $(CPP_DIR)/%.cpp,$(BIN_DIR)/%,$(CPP_SOURCES))
JAVA_CLASSES := $(patsubst $(JAVA_DIR)/%.java,$(BIN_DIR)/%.class,$(JAVA_SOURCES))

# Phony targets
.PHONY: all build-c build-cpp build-java run-python clean help

# Default target
all: $(BIN_DIR) build-c build-cpp build-java

# Create bin directory
$(BIN_DIR):
	mkdir -p $(BIN_DIR)

# Build C programs
build-c: $(BIN_DIR) $(C_TARGETS)

$(BIN_DIR)/%: $(C_DIR)/%.c
	@echo "Compiling C: $<"
	$(CC) $(CFLAGS) "$<" -o "$@"

# Build C++ programs
build-cpp: $(BIN_DIR) $(CPP_TARGETS)

$(BIN_DIR)/%: $(CPP_DIR)/%.cpp
	@echo "Compiling C++: $<"
	$(CXX) $(CXXFLAGS) "$<" -o "$@"

# Build Java programs
build-java: $(BIN_DIR) $(JAVA_CLASSES)

$(BIN_DIR)/%.class: $(JAVA_DIR)/%.java
	@echo "Compiling Java: $<"
	javac -d $(BIN_DIR) "$<"

# Run Python script
run-python:
	@if [ -z "$(FILE)" ]; then \
		echo "Usage: make run-python FILE=path/to/script.py"; \
		exit 1; \
	fi
	@if [ ! -f "$(FILE)" ]; then \
		echo "Error: File $(FILE) not found"; \
		exit 1; \
	fi
	python3 "$(FILE)"

# Clean build artifacts
clean:
	rm -rf $(BIN_DIR)

# Help target
help:
	@echo "Available targets:"
	@echo "  all        - Build all C, C++, and Java programs"
	@echo "  build-c    - Build only C programs"
	@echo "  build-cpp  - Build only C++ programs"
	@echo "  build-java - Build only Java programs"
	@echo "  run-python - Run a Python script (usage: make run-python FILE=script.py)"
	@echo "  clean      - Remove all build artifacts"
	@echo "  help       - Show this help message"
