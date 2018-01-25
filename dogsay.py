import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--eye', '-e', metavar='eye', default='o',
                        help="change Bruno's eye")
    parser.add_argument('--nose', '-n', metavar='nose', default='O',
                        help="change Bruno's nose")
    parser.add_argument('--tongue', '-t', metavar='tongue', default='U',
                        help="change Bruno's tongue")
    parser.add_argument('--execute', '-x', action='store_true',
                        help="give Bruno an order")
    variety = parser.add_mutually_exclusive_group()
    variety.add_argument('--big', '-b', action='store_true',
                         help="zoom out")
    variety.add_argument('--wings', '-w', action='store_true',
                         help="give Bruno wings")
    parser.add_argument('message', nargs='?', default="",
                        help='give Bruno something to say')
    args = parser.parse_args()
    if args.big:
        print """                   _____
  /|              / \\/ %s\___
 / |             /         %s
 \\  \___________/      ____/ %s
  \\_                  ]  %s
   |                  /
    \\___/_/----\\  /  /
     | | |      | | |
     | | /      | | /
     (_}_}      (_}_}\n""" % (args.eye[0], args.nose[0], args.message,
                              args.tongue[0])
    elif args.wings:
        print """         ___       _____
  /|    //\\\\\\     / \\/ %s\___
 / |    |||\\\\\\   /         %s
 \\  \____\\\\\\\\\\\\_/      ____/ %s
  \\_      ||||/        ]  %s
   |                  /
    \\___/_/----\\  /  /
     | | |      | | |
     | | /      | | /
     (_}_}      (_}_}\n""" % (args.eye[0], args.nose[0], args.message,
                              args.tongue[0])
    else:
        print """     _____
    / \\/ %s\___
   /         %s
  /      ____/ %s
 /______/   %s\n""" % (args.eye[0], args.nose[0], args.message,
                       args.tongue[0])
    if args.execute:
        os.system(args.message)


if __name__ == "__main__":
    main()
