import json
from logging import critical, debug, error, info, warning
from pprint import pprint as pp

from pygnition.configure import ARGUMENTS, PROGRAM_PATH
from pygnition.stdinput import get_piped_input

from .alerts import QuestionDialog
#
if __name__ == "__main__":
    print("Running hw")
    s = get_piped_input()
    if s:
        s = s.rstrip()
    else:
        critical("No piped input")
        exit(1)

    pp(f"Piped input: {s}")

    request = json.loads(s)
    if request["dialog"] == "question":
        params = {}
        modal = QuestionDialog(request["text"], title=request["title"])
        response = modal.run()
        print(response)
