# A script to publish Nostr notes, from a local file

## install
1. `git clone git@github.com:pleb21/Quotstr.git`
2. `cd Quotstr`
3. create a virtual environment, as it keeps things a little cleaner. I like to keep it that way. Depending upon your os and python version, it may vary, try `python3 -m venv venv` or best would be to do a google search `"how to install virtual environment on <your OS>"`
4. activate virtual environment; again varies between python versions and OS; on Linux/mac, do `source venv/bin/activate`
5. `pip install nostr` or `pip install -r requirements.txt`
6. run using `python main.py`

(apologies for the detailed yet broken instructions - I assume the world is as clumsy as me)

requires you to have a `random_quotes.txt` file with a quote on each line

uses the python nostr library by [jeffthibault](https://github.com/jeffthibault/python-nostr)

- reads lines from a local file `random_quotes.txt` downloaded from [erossignon](https://github.com/erossignon/qod4outlook/blob/master/quotes.txt)
- publishes the quotes as _notes_ to a Nostr profile.

Of course, this is dumb and amateur hour on display here. The idea was to learn about Nostr and I have many questions, most of them very very basic.

It should get better from here - if you have some suggestions/advice, I'm all ears.


### Questions

- I don't understand how I could access the same 'user' again. I understand that I can save the private key(`private_key.bech32()`) but how do I save the instance of `PrivateKey()` (stored as `private_key` in this script), in other words, how do I perform, for eg., `private_key.sign_event()` at a later stage. Does storing the `nsec...` enable me with that? Yeah, that's what happens when one hasn't put in the time - would need to read up more to understand better. __got the answer to this - like I said, need to put in time - while my question may not have been clear, the answer to it is that one can retrieve it using `from_nsec` method, like so: `private_key = PrivateKey.from_nsec('nseck3yg035h3r3')`__
- dumber questions to follow...
