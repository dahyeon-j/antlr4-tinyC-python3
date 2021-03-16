import sys
from antlr4 import *
from generated import tinycLexer
from generated import tinycParser
from generated import tinycListener

def main(argv):
    input = FileStream(argv[1])
    lexer = tinycLexer(input)
    stream = CommonTokenStream(lexer)
    parser = tinycParser(stream)
    tree = parser.init()

    walker = ParseTreeWalker()
    walker.walk(tinycListener(), tree)

if __name__ == '__main__':
    main(sys.argv)

