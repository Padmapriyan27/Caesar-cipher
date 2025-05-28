from argparse import ArgumentParser, ArgumentTypeError
from typing import Literal
import sys

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich import box
except ImportError:
    import subprocess
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'rich'])
        from rich.console import Console
        from rich.table import Table
        from rich.panel import Panel
        from rich import box
    except Exception as e:
        print(f"Error installing rich: {e}")
        sys.exit(1)

console = Console()

def pos_shift(value: str) -> int:
    """Ensure the shift value is a positive integer."""
    try:
        ivalue = int(value)
        if ivalue < 0:
            raise ArgumentTypeError("Shift value must be a non-negative integer.")
        return ivalue
    except ValueError:
        raise ArgumentTypeError("Shift value must be an integer.")

class CaesarCipher:
    def __init__(self, text: str, shift: int, mode: Literal['encrypt', 'decrypt']) -> None:
        self.text = text
        self.shift = shift
        self.mode = mode
        self.result = ""

    def sanitize_text(self) -> None:
        """Remove non-printable characters (optional)"""
        self.text = ''.join(c for c in self.text if c.isprintable())

    def process(self) -> str:
        self.sanitize_text()
        shift = self.shift if self.mode == 'encrypt' else -self.shift
        result = ""

        for char in self.text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                shifted = (ord(char) - offset + shift) % 26 + offset
                result += chr(shifted)
            else:
                result += char

        self.result = result
        return result

    def display_result(self) -> None:
        """Display the result in a rich table."""
        mode_color = "bold bright_green" if self.mode == "encrypt" else "bold bright_red"

        console.rule(f"[bold {mode_color}]{self.mode.upper()} MODE[/bold {mode_color}]", style=mode_color)
        table = Table(
            title="🔐 Caesar Cipher Result",
            box=box.DOUBLE_EDGE,
            show_header=True,
            header_style="bold bright_yellow",
            title_style="bold bright_cyan"
        )
        table.add_column("Field", style="bold bright_cyan", justify="right")
        table.add_column("Value", style="bold orange_red1")

        table.add_row("Mode", self.mode)
        table.add_row("Shift", str(self.shift))
        table.add_row("Input", f"[dim]{self.text}[/]")
        table.add_row("Output", f"[bold bright_green]{self.result}[/]")

        console.print(table)
        console.rule("[bold bright_cyan]Completed Successfully[/]")

class CipherApp:
    def __init__(self) -> None:
        self.args = self.parse_arguments()

    def show_help(self):
        help_text = """
[bold bright_cyan]Caesar Cipher Tool[/]

[bold orange_red1]Beta Version 0.1[/]

[bold bright_yellow]Usage:[/] python caesar_cipher.py [cyan]"text" shift mode[/]

[bold green]Positional Arguments:[/]
  [bright_cyan]text[/]        Text to encrypt or decrypt (use quotes for spaces)
  [bright_cyan]shift[/]       Non-negative integer shift value
  [bright_cyan]mode[/]        Either [green]'encrypt'[/] or [red]'decrypt'[/]

[bold green]Optional Arguments:[/]
  [bright_cyan]-h, --help[/]   Show this help message

[bold]Example:[/]
  [bright_green]python caesar_cipher.py "Attack at dawn!" 3 encrypt[/]
"""
        console.print(Panel(help_text, title="Help", title_align="left", border_style="bold orange_red1", expand=False))

    def parse_arguments(self):
        """Parse command line arguments."""
        if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
            self.show_help()
            sys.exit(0)

        parser = ArgumentParser(add_help=False)
        parser.add_argument("text", type=str, help="Text to encrypt or decrypt")
        parser.add_argument("shift", type=pos_shift, help="Shift value (non-negative integer)")
        parser.add_argument("mode", type=str, choices=['encrypt', 'decrypt'], help="Mode: 'encrypt' or 'decrypt'")
        return parser.parse_args()

    def run(self) -> None:
        """Run the Caesar Cipher application."""
        try:
            cipher = CaesarCipher(self.args.text, self.args.shift, self.args.mode)
            cipher.process()
            cipher.display_result()
        except Exception as e:
            console.print(f"[bold bright_red]Error:[/] {str(e)}", style="bold bright_red")
            console.print("[bold yellow]Please check your input and try again.[/]")

if __name__ == "__main__":
    app = CipherApp()
    app.run()
