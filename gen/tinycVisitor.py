# Generated from C:/Users/PLAS/PycharmProjects/pythonProject\tinyc.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tinycParser import tinycParser
else:
    from tinycParser import tinycParser
# This class defines a complete generic visitor for a parse tree produced by tinycParser.

class tinycVisitor(ParseTreeVisitor):
    indent_size = 4
    indent = indent_size * ' '
    # Visit a parse tree produced by tinycParser#program.
    def visitProgram(self, ctx:tinycParser.ProgramContext):
        program = ''
        for child in ctx.getChildren():
            program += str(self.visitStatement(child))
        lines = program.split('\n')
        cnt = 0
        for line in lines:
            if line == '{':
                print(cnt * self.indent + '{')
                cnt += 1
            elif line == '}':
                cnt -= 1
                print(cnt * self.indent + '}')
            else:
                print(cnt * self.indent + line)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#statement.
    def visitStatement(self, ctx:tinycParser.StatementContext):
        if ctx.getChild(0).getText() == 'if':
            if ctx.getChildCount() == 3:
                return 'if ' + self.visitParen_expr(ctx.getChild(1)) + '\n' + self.visitStatement(ctx.getChild(2))
            else:
                return 'if ' + self.visitParen_expr(ctx.getChild(1)) + '\n' + self.visitStatement(ctx.getChild(2)) + 'else\n' + self.visitStatement(4)
        elif ctx.getChild(0).getText() == 'while':
            return 'while\n' + self.visitParen_expr(ctx.getChild(1)) + '\n' + self.visitStatement(ctx.getChild(2))
        elif ctx.getChild(0).getText() == 'do':
            return 'do\n' + self.visitStatement(ctx.getChild(1)) + '\nwhile' + self.visitParen_expr(ctx.getChild(3)) + ';\n';
        elif ctx.getChild(0).getText() == '{':
            return_statement = '{\n'
            for i in range(1, ctx.getChildCount() - 1):
                return_statement += self.visitStatement(ctx.getChild(i))
            return_statement += '}'
            return return_statement
        elif ctx.getChild(0) == ';':
            return ';\n'
        else:
            return self.visitExpr(ctx.getChild(0)) + ';\n'
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#paren_expr.
    def visitParen_expr(self, ctx:tinycParser.Paren_exprContext):
        return '(' + self.visitExpr(ctx.getChild(1)) + ')'
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#expr.
    def visitExpr(self, ctx:tinycParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visitTest(ctx.getChild(0))
        else:
            return self.visitId(ctx.getChild(0)) + ' = ' + self.visitExpr(ctx.getChild(2))
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#test.
    def visitTest(self, ctx:tinycParser.TestContext):
        if ctx.getChildCount() == 1:
            return self.visitSum(ctx.getChild(0))
        else:
            return self.visitSum(ctx.getChild(0)) + ' ' + ctx.getChild(1).getText() + ' ' + self.visitSum(ctx.getChild(2))
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#sum.
    def visitSum(self, ctx:tinycParser.SumContext):
        if ctx.getChildCount() == 1:
            return self.visitTerm(ctx.getChild(0))
        else:
            return self.visitSum(ctx.getChild(0)) + ' ' + ctx.getChild(1).getText() + ' ' + self.visitTerm(ctx.getChild(2))
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#term.
    def visitTerm(self, ctx:tinycParser.TermContext):
        if 'IntegerContext' in str(ctx.getChild(0).__class__):
            return self.visitInteger(ctx.getChild(0))
        elif 'IdContext' in str(ctx.getChild(0).__class__):
            return self.visitId(ctx.getChild(0))
        elif 'Paren_exprContext' in str(ctx.getChild(0).__class__):
            return self.visitParen_expr(ctx.getChild(0))
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#id.
    def visitId(self, ctx:tinycParser.IdContext):
        return ctx.getText()
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#integer.
    def visitInteger(self, ctx:tinycParser.IntegerContext):
        return ctx.getText()
        # return self.visitChildren(ctx)

del tinycParser