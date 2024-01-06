import cmd, sys
from simplepytagger_lib import *


class TaggerShell(cmd.Cmd):
    intro = 'Welcome to the tagger shell.   Type help or ? to list commands.\n'
    prompt = '(>_<) '
    file = None
    open_file = None

    def do_open(self, arg):
        self.open_file = parse(arg)[0]
        print(self.open_file)

    def do_title(self, arg):
        if self.open_file is not None:
            apply_track_title(self.open_file, parse(arg)[0])

    def do_num(self, arg):
        if self.open_file is not None:
            apply_track_idx(self.open_file, parse(arg)[0])

    def do_year(self, arg):
        if self.open_file is not None:
            apply_release_year(self.open_file, parse(arg)[0])

    def do_art(self, arg):
        if self.open_file is not None:
            apply_album_art(self.open_file, parse(arg)[0])

    def do_album(self, arg):
        if self.open_file is not None:
            apply_album_title(self.open_file, parse(arg)[0])

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def do_bye(self, arg):
        print('Thank you for using tagger')
        self.close()
        return True



    def close(self):
        if self.file:
            self.file.close()
            self.file = None


def parse(arg):
    return tuple(map(str, arg.split()))


if __name__ == "__main__":
    TaggerShell().cmdloop()
