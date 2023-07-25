# A script to publish Nostr notes, from a local file

## install

`pip install nostr`

run using `python main.py`

requires you to have a `random_quotes.txt` file with a quote on each line

uses the python nostr library by [jeffthibault](https://github.com/jeffthibault/python-nostr)

- reads lines from a local file `random_quotes.txt` downloaded from [erossignon](https://github.com/erossignon/qod4outlook/blob/master/quotes.txt)
- publishes the quotes as _notes_ to a Nostr profile.

Of course, this is dumb and amateur hour on display here. The idea was to learn about Nostr and I have many questions, most of them very very basic.

It should get better from here - if you have some suggestions/advice, I'm all ears.


### Questions

- I don't understand how I could access the same 'user' again. I understand that I can save the private key(`private_key.bech32()`) but how do I save the instance of `PrivateKey()` (stored as `private_key` in this script), in other words, how do I perform, for eg., `private_key.sign_event()` at a later stage. Does storing the `nsec...` enable me with that? Yeah, that's what happens when one hasn't put in the time - would need to read up more to understand better.
- dumber questions to follow...
