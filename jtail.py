import os
import sys
import time
import json
import argparse


def filter_dict(d, keys):
    return { k: d.get(k) for k in keys if k in d }    
    

def watch(fname, keys=None, from_what=os.SEEK_SET):
    with open(fname, 'r') as fp:
        # Seek our file pointer
        fp.seek(0, from_what)
        
        while True:
            # Returns '' if no new line is present
            line = fp.readline()
            try:
                if line:
                    data = json.loads(line)
                    
                    if keys:
                        data = filter_dict(data, keys)
                        
                    yield data
                else:
                    time.sleep(0.5)
            except:
                pass
            
             

def main(args):
    sys.stdout.write("[+] :: Tailing file: {0}\n".format(args.file))
    if args.keys:
        sys.stdout.write("[+] :: Filtering keys: {0}\n".format(', '.join(args.keys)))
    
    from_what = os.SEEK_END if args.follow else os.SEEK_SET
    
    for data in watch(args.file, args.keys, from_what):
        sys.stdout.write(json.dumps(data) + '\n')

        
def get_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Tail script for json w/ filterable keys'
    )
    
    # Keys to pull from the log while tailing
    parser.add_argument('--keys', '-k', nargs='+', help='Keys to pull from the log while tailing')
    
    # File to watch
    parser.add_argument('--file', '-f', help='File to tail', required=True)
    
    # Follow file from the end
    parser.add_argument('--follow', action='store_true', help='Follow from end (skips directly to end of file)')
    
    return parser
    
    
def validate(args):        
    ## Host and Port must be configured for both client and server
    if not (args.file):
        raise ValueError("A file name must be passed to tail")
        
    return True
    

if __name__ == "__main__":
    try:
        parser = get_parser()
        
        args = parser.parse_args()
        
        if validate(args):
            main(args)
        
    except (KeyboardInterrupt):
        print("%%Exit invoked - bye!")
    except ValueError as ex:
        print("%% Error: {0}\n".format(ex))
        parser.print_help()
