# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ImplementationLanguageOv(str, enum.Enum):
    APPLESCRIPT = "applescript"
    BASH = "bash"
    C = "c"
    CPP = "cpp"
    CSHARP = "csharp"
    GO = "go"
    JAVA = "java"
    JAVASCRIPT = "javascript"
    LUA = "lua"
    OBJECTIVE_C = "objective_c"
    PERL = "perl"
    PHP = "php"
    POWERSHELL = "powershell"
    PYTHON = "python"
    RUBY = "ruby"
    SCALA = "scala"
    SWIFT = "swift"
    TYPESCRIPT = "typescript"
    VISUAL_BASIC = "visual_basic"
    X_86_32 = "x86_32"
    X_86_64 = "x86_64"

    def visit(
        self,
        applescript: typing.Callable[[], T_Result],
        bash: typing.Callable[[], T_Result],
        c: typing.Callable[[], T_Result],
        cpp: typing.Callable[[], T_Result],
        csharp: typing.Callable[[], T_Result],
        go: typing.Callable[[], T_Result],
        java: typing.Callable[[], T_Result],
        javascript: typing.Callable[[], T_Result],
        lua: typing.Callable[[], T_Result],
        objective_c: typing.Callable[[], T_Result],
        perl: typing.Callable[[], T_Result],
        php: typing.Callable[[], T_Result],
        powershell: typing.Callable[[], T_Result],
        python: typing.Callable[[], T_Result],
        ruby: typing.Callable[[], T_Result],
        scala: typing.Callable[[], T_Result],
        swift: typing.Callable[[], T_Result],
        typescript: typing.Callable[[], T_Result],
        visual_basic: typing.Callable[[], T_Result],
        x_86_32: typing.Callable[[], T_Result],
        x_86_64: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ImplementationLanguageOv.APPLESCRIPT:
            return applescript()
        if self is ImplementationLanguageOv.BASH:
            return bash()
        if self is ImplementationLanguageOv.C:
            return c()
        if self is ImplementationLanguageOv.CPP:
            return cpp()
        if self is ImplementationLanguageOv.CSHARP:
            return csharp()
        if self is ImplementationLanguageOv.GO:
            return go()
        if self is ImplementationLanguageOv.JAVA:
            return java()
        if self is ImplementationLanguageOv.JAVASCRIPT:
            return javascript()
        if self is ImplementationLanguageOv.LUA:
            return lua()
        if self is ImplementationLanguageOv.OBJECTIVE_C:
            return objective_c()
        if self is ImplementationLanguageOv.PERL:
            return perl()
        if self is ImplementationLanguageOv.PHP:
            return php()
        if self is ImplementationLanguageOv.POWERSHELL:
            return powershell()
        if self is ImplementationLanguageOv.PYTHON:
            return python()
        if self is ImplementationLanguageOv.RUBY:
            return ruby()
        if self is ImplementationLanguageOv.SCALA:
            return scala()
        if self is ImplementationLanguageOv.SWIFT:
            return swift()
        if self is ImplementationLanguageOv.TYPESCRIPT:
            return typescript()
        if self is ImplementationLanguageOv.VISUAL_BASIC:
            return visual_basic()
        if self is ImplementationLanguageOv.X_86_32:
            return x_86_32()
        if self is ImplementationLanguageOv.X_86_64:
            return x_86_64()
