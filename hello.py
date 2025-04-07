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
    print("msgpack is available in the plugin as expected")
    """))
    interp.close()

    try:
        import msgpack  # noqa
    except ImportError:
        print("msgpack is not available in the main program as expected")


if __name__ == "__main__":
    main()
