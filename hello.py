from test.support import interpreters
import textwrap


def main():
    interp = interpreters.create()
    # interp.prepare_main()
    interp.exec(textwrap.dedent("""
    from pathlib import Path
    from splitbrain import bootstrap

    bootstrap._bootstrap(Path("samples/example-plugin/example-plugin.pex"))

    import msgpack
    print("OK")
    """))
    interp.close()


if __name__ == "__main__":
    main()
