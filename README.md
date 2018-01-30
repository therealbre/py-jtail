# py-jtail
Tail script for streaming json files with filterable keys

## Usage
`jtail.py [-h] [--keys KEYS [KEYS ...]] --file FILE [--follow]`

Tail script for json w/ filterable keys

optional arguments:
* -h, --help            show this help message and exit
* --keys KEYS [KEYS ...], -k KEYS [KEYS ...] Keys to pull from the log while tailing (default:None)
* --file FILE, -f FILE  File to tail (default: None)
* --follow              Follow from end (skips directly to end of file) (default: False)
