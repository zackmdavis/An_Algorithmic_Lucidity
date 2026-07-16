Title: Consistent Hashing
Date: 2014-01-05 20:38
Status: published
Category: computing
Tags: algorithms, Clojure, OpenStack Swift

Dear reader, suppose you're a distibuted data storage system. Your soul (although some pedants would insist on the word _program_) is dispersed across a cluster of several networked computers. From time to time, your human patrons give you files, and your job—more than that, _the very purpose of your existence_—is to store these files for safekeeping and later retrieval.

The humans who originally crafted your soul chose a simple algorithm as the means by which you decide which file goes on which of the many storage devices that live in the computers you inhabit: you find the MD5 hash of the filename, take its residue modulo _n_ where _n_ is the number of devices you have—let's call the result _i_—and you put the file on the (zero-indexed) <em>i</em>th device. So when you had sixteen devices and the humans wanted you to store `twilight.pdf`, you computed `md5("twilight.pdf") = 429eb07bb8a3871c431fe03694105883`, saw that the lowest [nibble](http://en.wikipedia.org/wiki/Nibble) was `3`, and put the file on your 3rd device (most humans would say the _fourth_ device, counting from one).

It's not a _bad_ system, you tell yourself (some sort of pride or loyalty preventing you from disparaging your creators' efforts, even to yourself). At least it keeps the data spread out evenly. (A shudder goes down your internal buses as you contemplate what disasters might have happened if your creators had been even more naive and, say, had you put files with names starting with _A_ through _D_ on the first device, _&c_. What would have happened that time when your patrons decided they wanted to store `beat00001.mp3` through `beat18691.mp3`?)

But still, you've been having problems lately. As your patrons have come to rely on you more and more, they've added more machines bearing more devices to your cluster—and occasionally devices fail, too. And every time you gain or lose a device, your hashing scheme for assigning files to devices goes out of date: in the vast majority of cases, `md5(filename) mod n` changes when _n_ does, requiring almost all of your files to be shuffled onto different devices, an expensive and unpleasant procedure.

One day, after a particularly painful rearrangement of files, you decide enough is enough. You're going to need a new way to assign files to devices, even if it means rewriting part of your own soul (and that's exactly what it will mean). You do some searching and read about an idea called _consistent hashing_ that seems like a perfect solution to your problem. (In fact, your reading even mentions that your older cousin, [OpenStack Swift](http://docs.openstack.org/developer/swift/), uses a modified version of consistent hashing for the same purpose. You've always resented Swift and aren't happy with the idea of copying one of _her_ algorithms—but you tell yourself that that's not important.)

Anyway, consistent hashing. The essential nature of your problem is that you need a way to split the space of possible filenames into _n_ [partitions](http://en.wikipedia.org/wiki/Partition_of_a_set) in a way that minimizes the number of files that have to change partitions when _n_ changes. So imagine mapping the 128-bit output space of MD5 around a ring. Now pseudorandomly designate _m_ spots on the ring (_m_ being some prudently-chosen natural number) for each of your _n_ storage devices: say, by hashing the device name suffixed with the number _j_ for each _j_ between 0 and _m_–1 inclusive. Internally, you might represent the ring as just an array of hash/device pairs. Like this (in Clojure; here the array and the pairs it contains are actually "vectors")—

```clojure
(import 'java.security.MessageDigest)

(defn md5 [string]
  (let [digest-builder
        (java.security.MessageDigest/getInstance "MD5")]
    (.update digest-builder (.getBytes string))
    (clojure.string/join
     (map (fn [chr] (format "%x" chr))
          (.digest digest-builder)))))

(defn suffixed [name n]
  (map (fn [j] (str name j))
       (range n)))

(defn ring-kv-pairs [device spots]
  (map (fn [suffixed-name]
         (vector (md5 suffixed-name) device))
       (suffixed device spots)))

(defn make-ring [devices spots]
  (vec (sort
        (reduce concat
                (map (fn [device]
                       (ring-kv-pairs device spots))
                     devices)))))
```

Then when your patrons ask you to store a file, you're still going to hash its name, but instead of taking the residue mod _n_ of the hash to decide where the file should live, you're going to locate the hash in your ring, and find the next designated spot on the ring associated with one of your storage devices, and the file will live on that device. In terms of your internal representation of the ring as an array of hash/device pairs, you'll find the first pair whose first item (the hash of the suffixed device name) is greater than the hash of the name of the file to be stored, and the second item of that pair will tell you which storage device to use. (And if the filename hash is greater than all those stored in the (first items of the pairs stored in the) array, then you just use the first pair in the array. It is supposed to represent a _ring_, after all.) Like this—

```clojure
(defn ring-search [ring key]
  (or (some (fn [pair]
              (if (> (compare (first pair) key) 0)
                pair))
            ring)
      (first ring))) 

(defn ring-lookup [ring filename]
  (last (ring-search ring (md5 filename))))
```

And now—why, _now_ when you gain (respectively lose) a storage device, you can decide the allocation question simply by adding (respectively removing) the appropriate designated spots to (respectively from) your ring—

```clojure
(defn ring-add [ring device spots]
  (sort (vec (concat ring (ring-kv-pairs device spots)))))

(defn ring-remove [ring device]
  (filter (fn [spot] (not= (last spot) device))
          ring))
```

—and _most_ files stay on the same device: the only ones that have to move are those with a new nextmost designated spot in the ring!

[![Your Consistent Hashing Ring]({static}/images/your_consistent_hashing_ring-300x148.png)]({static}/images/your_consistent_hashing_ring.png)

You decide to run a quick simulation to see if you've gotten this right before saving the edits to your soul. Suppose you had storage devices `device0` through `device5` and your patrons wanted you to store `file0` through `file5999`; how would the files end up distributed across your devices? You choose a prudent-seeming integer for the number of designated spots per device—say, 450?—and write the simulation like this—

```clojure
(defn filemap [ring files]
  (into {}
        (for [file files
              :let [device (ring-lookup ring file)]]
          [file device])))

(defn counter [devices filemap]
  (for [d devices]
    [d (count (filter (fn [entry]
                        (= (last entry) d)) filemap))]))

(def my-devices (suffixed "device" 6))
(def my-first-ring (make-ring my-devices 450))
(def my-files (suffixed "file" 6000))
(def my-filemap (filemap my-first-ring my-files))
(doseq [total (counter my-devices my-filemap)]
  (println total))
```

And the results seem reasonable enough:

```text
$ clojure consistent_hashing.clj 
[device0 1020]
[device1 993]
[device2 1082]
[device3 955]
[device4 993]
[device5 957]
```
