
## Install

On Linux, you need `python-dev` and `libpcap-dev` installed. 
On MacOS, these packages are installed by default.

Tested on MacOS 10.12.5, Ubuntu 14 and 16.

```
git clone https://github.com/GedRap/mcintercept.git
cd mcintercept
pip install -r requirements.txt
```

That's it!

## Running

```
$ python -m mcintercept -i lo0 -p 11211 -c config.json
[2017-06-27 22:49:42,055] INFO -- Listening to lo0 port 11211
[2017-06-27 22:49:42,063] INFO -- Loaded config from config.json
[2017-06-27 22:49:56,100] command=get, key=hello, patterns=[u'hello']
```

* `-i` interface name, such as `eth0`, `lo` or `lo0`;
* `-p` memcached port, usually 11211;
* `-c` path to config file.

Linux might require running the script as root in order to sniff network interfaces.

## Configuration

`config.sample.json` contains an example, which is a good starting point.

`paterns` is a list of regular expression that will be tried to match against all
memcached keys in captured traffic. `regexp` is a simple regular expression 
(python `re` module is used to evaluate them), and `name` is a name which 
will be used in output (e.g. StatsD key). Multiple patterns can have the same name.

`output` configures output handlers, only stdout and Statsd are supported at the moment.
If Statsd is used, the key will contain prefix given in the configuration file,
memcached command, and matching pattern name.

For example, given `config.sample.json` configuration, caputring memcached command `get hello11`
will increase Statsd counter `stats.counters.mcintercept.get.hello` by 1.

Memcached commands that did not match any patterns are not outputted. 