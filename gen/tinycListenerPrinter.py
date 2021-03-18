import sys
from antlr4 import *
import tinycParser
import tinycLexer
import tinycListener

def main(file_name):
    input = FileStream(file_name)
    lexer = tinycLexer.tinycLexer(input)

    stream = CommonTokenStream(lexer)

    parser = tinycParser.tinycParser(stream)

    tree = parser.program()

    printer = tinycListener.tinycListener()

    walker = ParseTreeWalker()

    walker.walk(printer, tree)

if __name__ == '__main__':
    main("input.c")

