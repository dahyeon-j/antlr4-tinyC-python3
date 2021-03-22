import sys
from antlr4 import *
import tinycParser
import tinycLexer
import tinycVisitor

def main(file_name):
    input = FileStream(file_name)
    lexer = tinycLexer.tinycLexer(input)

    stream = CommonTokenStream(lexer)

    parser = tinycParser.tinycParser(stream)

    tree = parser.program()

    printer = tinycVisitor.tinycVisitor()

    printer.visitProgram(tree)



if __name__ == '__main__':
    main("input.c")

