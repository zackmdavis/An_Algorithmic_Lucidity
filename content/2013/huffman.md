Title: Huffman
Date: 2013-06-08 18:47
Status: published
Category: computing
Tags: algorithms, Python

Dear reader, you know what's _way_ more fun than [feeling](http://zackmdavis.net/blog/2013/04/the-horror-of-naturalism/) [sad](http://zackmdavis.net/blog/2013/05/relativity/) [about](http://zackmdavis.net/blog/2013/05/relevance/) [the](http://zackmdavis.net/blog/2013/05/retirement/) [nature](http://zackmdavis.net/blog/2013/06/remembering/) of the cosmos? _Data compression_, that's what! Suppose you want to send a message to your friends in a nearby alternate universe, but interuniversal communication bandwidth is _very expensive_ (different universes can't _physically_ interact, so we and our alternate-universe analogues can only communicate by mutually _inferring_ what the other party must be saying, which takes monstrous amounts of computing power and is not cheap), so you need to make your message as brief as possible. Note that 'brief' doesn't just have to do with how long your message is in natural language, it also has to do with how that message is _represented_ over the transuniveral communication channel: indeed, the more efficient the encoding, the more you can afford to say on a fixed budget.

The classic [ASCII](http://en.wikipedia.org/wiki/ASCII) encoding scheme uses seven bits to represent each character. (_Seven?_—you ask perplexedly, _surely you mean eight?_ Apparently it was seven in the original version.) Can we do better? Well ... ASCII has a lot of stuff that arguably you don't need _that_ badly. Really, upper _and_ lower case letters? Ampersands, asterisks, backslashes? And don't get me started about those unprintable control characters! If we restrict our message to just the uncased alphabet _A_ through _Z_ plus space and a few punctuation marks, then we can encode our message using only a 32 (= $2^5$) character set, at five bits per character.

Can we do better? Seemingly not—$2^4 = 16$ isn't a big enough character set to cover the alphabet. Unless ...

_Unless we abandon the assumption that each character needs to be represented by the same number of bits!_

Adopting such a variable-length character encoding scheme couldn't help us if all possible messages were equally likely, but this is manifestly _not_ true of the sort of messages anyone would actually want to send: the letter _e_ is more common than the letter _q_; the word _the_ more common than the string _zkb_. We can take advantage of the regularities in the sort of messages people would actually want to send by adopting a variable-length encoding scheme that assigns shorter codes to characters that occur more frequently. But then since we can no longer rely on each _n_ bits (for some fixed _n_) representing one character, we'll also want our encoding scheme to be _prefix-free_: no character code should be a prefix of any other. That way, our message is unambiguous: if the message starts with (say) 010, which represents (say) _e_, then we know that the first character is _e_, because there won't be any other characters with codes that start with 010 (like say 01011).

Consider the process of decoding a prefix-free code: we read bits from the start of the message until we recognize a valid character code. We can visualize this graphically in the form of a binary tree with the characters in our character set at the leaves: start at the root, and then go the the left child if the first bit is 0, and the right child if it's 1, and so on until you reach a leaf, the path taken representing the code for the character at that leaf. The task of constructing such an optimal such tree (and thereby, an optimal prefix-free code) given the relative frequencies of the characters (either in a particular message, or a general class of messages that people would actually want to send) is solved by a algorithm due to David A. Huffman, which we'll implement here in Python.

First, we'll need a data structure to represent the nodes of the tree. Actually, we'll use a structure that represents a node _and_ all of its children, which we'll call `Subtree`. Each instance of `Subtree` will have fields for a _character_ and _frequency_ associated with a node, and the node's left and right children if any (which are also instances of `Subtree`).

```python
class Subtree:
    def __init__(self, char, freq, left, right):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
```

The leaf nodes of our tree will have the character field set to a character in our set, the frequency field set to the frequency of that character, and the left and right children fields set to `None`. The internal nodes of the tree will have the character field set to `None` and the frequency field set to the sum of the frequencies of its children.

We'll also want nodes to be comparable by their frequencies:

```python
    def __gt__(self, othernode):
        return self.freq > othernode.freq
```

When all is said and done, Huffman's algorithm will give us an instance of `Subtree` representing our tree, but it would really be more convenient to have the decoding information embodied by the tree in the form of Python dictionary mapping bitstrings to the characters they encode. We can get this by doing a standard recursive tree walk:

```python
    def codebook(self):
        codes = {}
        def traversal(item, code):
            if item != None:
                traversal(item.left, code+'0')
                if item.char != None:
                    codes[item.char] = code
                traversal(item.right, code+'1')
        traversal(self, '')
        return codes
```

We're also going to need a _min-priority queue_, a dynamic set from which we can insert items and retrieve the "smallest":

```python
class MinPriorityQueue:
    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.append(item)
        self.queue.sort(reverse=True)

    def get(self):
        return self.queue.pop()
```

Now that we have the appropriate data structures, we're ready for Huffman's algorithm. Suppose our character/frequency data are given to us in a Python dictionary `C`. For each character, we create an instance of `Subtree` to be the corresponding leaf node in our tree, and put them all in a min-priority queue. Then we build our tree from the bottom up by selecting the two lowest-frequency nodes in the queue, making them the children of a new node whose frequency is the sum of their frequencies, putting the new node back in the priority queue, and again until we've built the entire tree:

```python
def Huffman(C):
    Q = MinPriorityQueue()
    leaves = {Subtree(k, C[k], None, None) for k in C}
    for leaf in leaves:
        Q.put(leaf)
    for i in range(len(C)-1):
        left = Q.get()
        right = Q.get()
        new_node = Subtree(None, left.freq + right.freq, left, right)
        Q.put(new_node)
    return Q.get().codebook()
```

And that's Huffman's algorithm. Of course, we'll also want functions for encoding and decoding a message:

```python
def code(plaintext, codebook):
    return ''.join(codebook[c] for c in plaintext)

def decode(ciphertext, codebook):
    decodebook = {v:k for k, v in codebook.items()}
    codeword = ''
    plaintext = ''
    for i in range(len(ciphertext)):
        codeword += ciphertext[i]
        if codeword in decodebook:
            plaintext += decodebook[codeword]
            codeword = ''
    return plaintext
```

So, suppose you want to send your friends in a nearby alternate universe the eighty-two character message, "I USED TO WONDER WHAT FRIENDSHIP COULD BE, UNTIL YOU ALL SHARED ITS MAGIC WITH ME." If you used seven-bit ASCII, you'd have to pay the cost of transmitting 82\*7 = 574 bits. But if you use a Huffman code informed by knowledge of [English letter frequencies](http://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_the_English_language) ...

```python
eng_freqs = {'A' : 8167, 'B' : 1492, 'C' : 2782, 'D' : 4253, 'E' : 12702,
'F' : 2228, 'G' : 2015, 'H' : 6094, 'I' : 6966, 'J' : 153, 'K' : 772,
'L' : 4025, 'M' : 2406, 'N' : 6749, 'O' : 7507, 'P' : 1929, 'Q' : 95,
 'R' : 5987, 'S' : 6327, 'T' : 9056, 'U' : 2758, 'V' : 978, 'W': 2360,
'X' : 150, 'Y' : 1974, 'Z' : 74, ' ' : 13000, '.': 4250, ',': 4250}
eng_codebook = Huffman(eng_freqs)
plain = "I USED TO WONDER WHAT FRIENDSHIP COULD BE, UNTIL YOU ALL SHARED ITS MAGIC WITH ME."
cipher = code(plain, eng_codebook)
```

You can send _this_ instead:

```text
0111010111100000100111001010110110010101110101001011011001001111110101110100
0001010110101011100111111011100101101100100010000011110000101011110110011111
0010110110010101000000011100001011110001101101011110110010100010100111110001
0101010110101100100001000010101111100111001010011111010001010111011101010001
1011111110101011101001111101000001011101100110111
```

—which is only 353 bits, for a savings of 38.5%.

___Bibliography___
Cormen _et al._, _Introduction to Algorithms_, third ed'n, §16.3
