import argparse
import subprocess
import os


def red(text):
    return (u"\u001b[31m"
            + text
            + u"\u001b[0m")


def green(text):
    return (u"\u001b[32m"
            + text
            + u"\u001b[0m")


def bold(text):
    return (u"\033[1m"
            + text
            + u"\u001b[0m")


def blue(text):
    return (u"\033[0;34m"
            + text
            + u"\u001b[0m")


def parser():

    # create parser
    parser = argparse.ArgumentParser(prog='dogsay')

    # add basic arguments, such as tongue and execute
    parser.add_argument('-e', '--eye', default='o',
                        help="change Bruno's eye")
    parser.add_argument('-n', '--nose', default='O',
                        help="change Bruno's nose")
    parser.add_argument('-t', '--tongue', default='U',
                        help="change Bruno's tongue")
    parser.add_argument('-x', '--execute', action='store_true',
                        help="give Bruno an order")

    # add mutually exclusive arguments, such as big and wings
    variety = parser.add_mutually_exclusive_group()
    variety.add_argument('-b', '--big', action='store_true',
                         help="zoom out")
    variety.add_argument('-w', '--wings', action='store_true',
                         help="give Bruno wings")
    variety.add_argument('-f', '--fancy', action='store_true',
                         help="clarify")

    # message for dogsay to display
    parser.add_argument('message', nargs='?', default="",
                        help='give Bruno something to say')

    args = parser.parse_args()
    return args


def big(args):
    print("""                   _____
  /|              / \\/ %s\___
 / |             /         %s
 \\  \___________/      ____/ %s
  \\_                  ]  %s
   |                  /
    \\___/_/----\\  /  /
     | | |      | | |
     | | /      | | /
     (_}_}      (_}_}\n""" % (args.eye[0], args.nose[0], args.message,
                              args.tongue[0]))


def fancy(args):
    print("""\n                      ;`\\
                      |' \\
   _                  ; : ;
  / `-.              /: : |
 |  ,-.`-.          ,': : |
 \\  :  `. `.       ,'-. : |
  \\ ;    ;  `-.__,'    `-.|
   \\ ;   ;  :::  ,::'`:.  `.
    \\ `-. :  `    :.    `.  \\
     \\   \\    ,   ;   ,:    (\\
      \\   :., :.    ,'%s)): ` `-.
     ,/,' ;' ,::"'`.`---'   `.  `-._
   ,/  :  ; '"      `;'          ,--`.
  ;/   :; ;             ,:'     (   ,:)
    ,.,:.    ; ,:.,  ,-._ `.     \\""'/
    '::'     `:'`  ,'(  \\`._____.-'"'
       ;,   ;  `.  `. `._`-.  \\        %s
       ;:.  ;:       `-._`-.\\  \\`.
        '`:. :        |' `. `\\  ) \\
           ` ;:       |    `--\\__,'
             '`      ,'
                  ,-'\n""" % (args.eye, args.message))


def wings(args):
    print("""         ___       _____
  /|    //\\\\\\     / \\/ %s\___
 / |    |||\\\\\\   /         %s
 \\  \____\\\\\\\\\\\\_/      ____/ %s
  \\_      ||||/        ]  %s
   |                  /
    \\___/_/----\\  /  /
     | | |      | | |
     | | /      | | /
     (_}_}      (_}_}\n""" % (args.eye[0], args.nose[0], args.message,
                              args.tongue[0]))


def default(args):
    print("""     _____
    / \\/ %s\___
   /         %s
  /      ____/ %s
 /______/   %s\n""" % (args.eye[0], args.nose[0], args.message,
                       args.tongue[0]))


def dogsay(args):
    if args.big:
        big(args)
    elif args.fancy:
        fancy(args)
    elif args.wings:
        wings(args)
    else:
        default(args)
    if args.execute:
        os.system(args.message)


def main():
    dogsay(parser())


if __name__ == "__main__":
    main()
