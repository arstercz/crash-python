# Stubs for gdb.command.pretty_printers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import gdb
from typing import Any

def parse_printer_regexps(arg: Any): ...
def printer_enabled_p(printer: Any): ...

class InfoPrettyPrinter(gdb.Command):
    def __init__(self) -> None: ...
    @staticmethod
    def enabled_string(printer: Any): ...
    @staticmethod
    def printer_name(printer: Any): ...
    def list_pretty_printers(self, pretty_printers: Any, name_re: Any, subname_re: Any) -> None: ...
    def invoke1(self, title: Any, printer_list: Any, obj_name_to_match: Any, object_re: Any, name_re: Any, subname_re: Any) -> None: ...
    def invoke(self, arg: Any, from_tty: Any) -> None: ...

def count_enabled_printers(pretty_printers: Any): ...
def count_all_enabled_printers(): ...
def pluralize(text: Any, n: Any, suffix: str = ...): ...
def show_pretty_printer_enabled_summary() -> None: ...
def do_enable_pretty_printer_1(pretty_printers: Any, name_re: Any, subname_re: Any, flag: Any): ...
def do_enable_pretty_printer(arg: Any, flag: Any) -> None: ...

class EnablePrettyPrinter(gdb.Command):
    def __init__(self) -> None: ...
    def invoke(self, arg: Any, from_tty: Any) -> None: ...

class DisablePrettyPrinter(gdb.Command):
    def __init__(self) -> None: ...
    def invoke(self, arg: Any, from_tty: Any) -> None: ...

def register_pretty_printer_commands() -> None: ...
