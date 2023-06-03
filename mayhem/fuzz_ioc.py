#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers


with atheris.instrument_imports():
    import Evtx.Evtx as evtx
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    with fdp.ConsumeTemporaryFile(suffix='.evtx', as_bytes=False, all_data=True) as f:
        evtx.FileHeader(f, 0x0)



def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
