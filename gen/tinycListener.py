# Generated from C:/Users/PLAS/PycharmProjects/pythonProject\tinyc.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tinycParser import tinycParser
else:
    from tinycParser import tinycParser

# This class defines a complete listener for a parse tree produced by tinycParser.
class tinycListener(ParseTreeListener):
    newText = {}
    indent_size = 4
    indent = indent_size * ' '
    #     # Enter a parse tree produced by tinycParr#program.
    def enterProgram(self, ctx:tinycParser.ProgramContext):
        pass

    # Exit a parse tree produced by tinycParser#program.
    def exitProgram(self, ctx:tinycParser.ProgramContext):
        for child in ctx.getChildren():
            lines = self.newText[child].split('\n')
            cnt = 0
            for line in lines:
                if len(line) == 0:
                    continue
                else:
                    if line == '{':
                        print(cnt * self.indent + line)
                        cnt += 1
                    elif line[0:1] == '}':
                        cnt -= 1
                        print(cnt * self.indent + line)
                    else:
                        print(cnt * self.indent + line)

        pass


    # Enter a parse tree produced by tinycParser#statement.
    def enterStatement(self, ctx:tinycParser.StatementContext):
        pass

    # Exit a parse tree produced by tinycParser#statement.
    def exitStatement(self, ctx:tinycParser.StatementContext):
        text = ''
        first_text = ctx.getChild(0).getText()

        if first_text == 'if':
            text = 'if' + self.newText[ctx.getChild(1)] +'\n'+ self.newText[ctx.getChild(2)]
            if ctx.getChildCount() == 5:
                text = text + '\nelse' + self.newText[ctx.getChild(4)]
        elif first_text == 'while':
            text = 'while' + self.newText[ctx.getChild(1)] + '\n' + self.newText[ctx.getChild(2)]
        elif first_text == 'do':
            text = 'do\n' + self.newText[ctx.getChild(1)] + '\nwhile' + self.newText[ctx.getChild(3)] + ';'
        elif first_text == '{':
            for i in range(1, ctx.getChildCount() - 1):
                text = text + self.newText[ctx.getChild(i)]
            text = '{\n' + text + '}'
        elif first_text == ';':
            text = ';\n'
        else:
            text = self.newText[ctx.getChild(0)] + ';\n'
        self.newText[ctx] = text
        pass


    # Enter a parse tree produced by tinycParser#paren_expr.
    def enterParen_expr(self, ctx:tinycParser.Paren_exprContext):
        pass

    # Exit a parse tree produced by tinycParser#paren_expr.
    def exitParen_expr(self, ctx:tinycParser.Paren_exprContext):
        text = '( ' + self.newText[ctx.getChild(1)] + ' )'
        self.newText[ctx] = text
        pass


    # Enter a parse tree produced by tinycParser#expr.
    def enterExpr(self, ctx:tinycParser.ExprContext):
        pass

    # Exit a parse tree produced by tinycParser#expr.
    def exitExpr(self, ctx:tinycParser.ExprContext):
        text = ''

        for child in ctx.getChildren():
            if child in self.newText:
                text = text + self.newText[child]
            else:
                text = text + ' ' + child.getText() + ' '

        self.newText[ctx] = text
        pass


    # Enter a parse tree produced by tinycParser#test.
    def enterTest(self, ctx:tinycParser.TestContext):
        pass

    # Exit a parse tree produced by tinycParser#test.
    def exitTest(self, ctx:tinycParser.TestContext):
        text = ''

        for child in ctx.getChildren():
            if child in self.newText:
                text = text + self.newText[child]
            else:
                text = text + ' ' + child.getText() + ' '

        self.newText[ctx] = text
        pass


    # Enter a parse tree produced by tinycParser#sum.
    def enterSum(self, ctx:tinycParser.SumContext):
        pass

    # Exit a parse tree produced by tinycParser#sum.
    def exitSum(self, ctx:tinycParser.SumContext):
        text = ''

        for child in ctx.getChildren():
            if child in self.newText:
                text = text + self.newText[child]
            else:
                text = text + ' ' + child.getText() + ' '

        self.newText[ctx] = text
        pass


    # Enter a parse tree produced by tinycParser#term.
    def enterTerm(self, ctx:tinycParser.TermContext):
        pass

    # Exit a parse tree produced by tinycParser#term.
    def exitTerm(self, ctx:tinycParser.TermContext):
        self.newText[ctx] = self.newText[ctx.getChild(0)]
        pass


    # Enter a parse tree produced by tinycParser#id.
    def enterId(self, ctx:tinycParser.IdContext):
        pass

    # Exit a parse tree produced by tinycParser#id.
    def exitId(self, ctx:tinycParser.IdContext):
        self.newText[ctx] = ctx.getText()
        pass


    # Enter a parse tree produced by tinycParser#integer.
    def enterInteger(self, ctx:tinycParser.IntegerContext):
        pass

    # Exit a parse tree produced by tinycParser#integer.
    def exitInteger(self, ctx:tinycParser.IntegerContext):
        self.newText[ctx] = ctx.getText()
        pass



del tinycParser