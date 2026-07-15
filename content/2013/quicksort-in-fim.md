Title: Quicksort in FIM++
Date: 2013-07-09 18:49
Status: published
Category: computing
Tags: algorithms, Friendship Is Magic, Ruby

Dear reader, I have got to tell you, fandom is _intense_. One day last October _Equestria Daily_ (internet clearinghouse for fans of the animated series _My Little Pony: Friendship Is Magic_) [posts a joke proposal](http://www.equestriadaily.com/2012/10/editorial-fim-pony-programming-language.html) for a programming language (FIM++) based on the show, and [within the week](https://github.com/KarolS/fimpp/commits/master) there's a working interpreter for it. What does it mean to model a _programming language_ after a _cartoon_, you ask? Well, in the show, episodes typically end with our heroine Twilight Sparkle (or after Season Two, Episode Three "Lesson Zero", one of her friends) writing a letter about what she's learned about the magic of friendship to her mentor (and God-Empress of the sun) Princess Celestia. So, then, why not have an esoteric programming langauge where the source code reads like a letter to Princess Celestia? Adorable, right?

So, this gift having been provided to us courtesy of [Karol S.](https://github.com/KarolS) and the brony community, let's _do_ something with it! More specifically, how about we implement quicksort?—that is a _classic_. What's quicksort? Well, we want to sort a list, right? So—bear with me—we define this partitioning procedure that, given indices into an array, partitions the subarray between those indices into a subsubarray of elements less-than-or-equal-to a given element dubbed the _pivot_, then the pivot itself, then a subsubarray of elements greater than the pivot. How do we do that? Well, let's designate the last element in our subarray as the pivot. Then we're going to scan through all the other elements, and if any of them are less-than-or-equal-to the pivot, we swap it into our first subsubarray and increment a variable keeping track of where the first subsubarray ends. Then, we swap the pivot into place and return its index. In Ruby—

```ruby
def partition(array, p, r)
  i = p-1
  for j in p..(r-1) do
      if array[j] <= array[r]
        i += 1
        array[i], array[j] = array[j], array[i]
      end
  end
  array[i+1], array[r] = array[r], array[i+1]
  i+1
end
```

Then we can sort an entire array with a bunch of recursive calls to our partitioning procedure:

```ruby
def quicksort(array, p, r)
  if p < r
    q = partition(array, p, r)
    quicksort(array, p, q-1)
    quicksort(array, q+1, r)
  end
end

# Let's try it!
my_array = [9, 5, 4, 11, 2, 10, 6, 3, 8, 12, 1, 7]
quicksort(my_array, 0, my_array.length-1)
print my_array # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

So that's quicksort. With a little more effort, we can do the same thing in FIM++:

```text
Dear Princess Celestia: Letter about Quicksort:

I learned about exchange with Applejack, Rainbow Dash, and Rarity.

  On the page numbered by Rarity of Applejack I read about Sweetie
  Belle.

  On the page numbered by Rainbow Dash of Applejack I read about
  Scootaloo.

  On the page numbered by Rarity of Applejack I wrote what I knew
  about Scootaloo.

  On the page numbered by Rainbow Dash of Applejack I wrote what I
  knew about Sweetie Belle.

That's about exchange.


I learned about partitioning with Applejack, Rainbow Dash, and Rarity.

  On the page numbered by Rarity of Applejack I read about Apple
  Bloom.

  Sweetie Belle made the difference of Rainbow Dash and the number one.

  Did you know Scootaloo likes Rainbow Dash?

  I did this while Scootaloo had less than Rarity:

    On the page numbered by Scootaloo of Applejack I read about
    Diamond Tiara.

      When Diamond Tiara had not more than Apple Bloom:

        Sweetie Belle got one more.

        I did exchange of Applejack, Sweetie Belle, and Scootaloo.

      That's what I did.

    Scootaloo got one more.

  That's what I did.

  Sweetie Belle got one more.

  I also caused exchange of Applejack, Sweetie Belle, and Rarity.

That's about partitioning with Sweetie Belle.


I learned about quicksort with Applejack, Rainbow Dash, and Rarity:

  When Rainbow Dash had less than Rarity:

    Fluttershy did partitioning of Applejack, Rainbow Dash, and Rarity.

    Fluttershy got one less.

    I caused quicksort of Applejack, Rainbow Dash, and Fluttershy.

    Fluttershy got two more.

    I caused quicksort of Applejack, Fluttershy, and Rarity.

  That's what I did.

That's about quicksort.


Today I learned:

  Did you know Applejack likes 9, 5, 4, 11, 2, 10, 6, 3, 8, 12, 1, and 7?

  Applejack did dictionary of Applejack.

  I said: Applejack!

  I did quicksort of Applejack, one, and twelve.

  I said: Applejack! 

Your Faithful Student,
Twilight Sparkle
```

___Bibliography___
Cormen _et al._, _Introduction to Algorithms_, third ed'n, §7.1
