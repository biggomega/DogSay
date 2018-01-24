import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', metavar='eye', default='o',
                        help="change Bruno's eye")
    parser.add_argument('-n', metavar='nose', default='O',
                        help="change Bruno's nose")
    parser.add_argument('-t', metavar='tongue', default='U',
                        help="change Bruno's tongue")
    parser.add_argument('message', help='give Bruno something to say')
    args = parser.parse_args()
    print """     ______
    / \\/ %s \____
   /           %s
  /       _____/ %s
 /_______/    %s\n""" % (args.e, args.n, args.message, args.t)


main()
