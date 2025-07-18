import typer
from rich import print
from deep_translator import GoogleTranslator

app = typer.Typer()


@app.command()
def translate(
    text: str = typer.Argument(..., help="翻訳するテキスト"),
    target: str = typer.Option("en", "--target", "-t", help="翻訳先の言語コード")
):
     """
     翻訳ツール
     """
     try:                  
        translated = GoogleTranslator(source="auto", target=target).translate(text)
        print("[翻訳結果]:", translated)
     except Exception as e:
        print('[エラー]:', e)

if __name__ == "__main__":
    app()

