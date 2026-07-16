Title: Ford-Fulkerson
Date: 2013-08-19 17:26
Status: published
Category: computing
Tags: algorithms, Ruby

Dear reader, have you ever dreamed of solving instances of the maximum flow problem? Sure you have! Suppose we have a weighted directed graph, which we might imagine as a network of pipes (represented by the edges) between locations (represented by the nodes), pipes through which some sort of fluid might thereby be transported across the network. One node is designated the _source_, another is called the _sink_, and the weight of the edge (_i_, _j_) represents the maximum capacity of the pipe which transports fluid from the location _i_ to location _j_. The maximum-flow problem is precisely the question of how to transport the maximum possible amount of fluid _from_ the source _to_ the sink (without any fluid leaking or magically appearing at any of the intermediate nodes). That is, we want to assign an amount of fluid _flow_ to each edge, not to exceed that edge's capacity, such that inflow equals outflow for all the intermediate (_i.e._, non-source, non-sink) nodes, and such that the total flow reaching the sink is maximized.

It turns out that there's a conceptually straightforward algorithm for solving the maximum flow problem, known as the Ford-Fulkerson method, which we'll implement in Ruby. But first, we'll want to pin down exactly how the flow network will be represented. Let's define an `Edge` class, each instance of which will be initialized with the names of the nodes at its head and tail, and the edge's maximum capacity:

```ruby
class Edge
  attr_accessor :tail
  attr_accessor :head
  attr_accessor :capacity

  def initialize(t, h, c)
    @tail = t
    @head = h
    @capacity = c
  end
end
```

And let's also make a `FlowNetwork` class, defined by the names of its source and sink nodes, and a hash which maps `Edge`s to the amount of flow currently assigned to that `Edge`:

```ruby
class FlowNetwork
  attr_accessor :source
  attr_accessor :sink
  attr_accessor :network
  
  def initialize(source, sink, edges)
    @source = source
    @sink = sink
    @network = {}
    edges.each do |e|
      @network[e] = 0
    end
  end
```

(Note that I haven't yet closed the `FlowNetwork` class definition yet, because we still want to define more methods implementing the Ford-Fulkerson algorithm!)

So how _do_ we solve the maximum-flow problem? It's pretty simple! We start with the "zero flow." (In our code above, this is already done when we initialize an instance of `FlowNetwork`.) We then find an _augmenting path_ from the source to the sink (possibly including edges traversed backwards) such that all the forward-traversed edges along the path have not been assigned their maximum capacity, and all the backward-traversed edges have a nonzero amount of flow. This is path along which we can _push_ more flow from the source to the sink, by increasing the amount of flow along the forward-traversed edges, and decreasing the amount of flow along the backward-traversed edges. (Convince yourself that pushing flow through an edge _backwards_ amounts to decreasing the amount of flow along that edge.) Once we've found such an augmenting path, we push as much flow as we can along it. Then we look for another augmenting path and do the same, until no more augmenting paths can be found. It turns out that the resulting flow assignment solves our problem. So that's the Ford-Fulkerson method:

```ruby
  def ford_fulkerson
    path = augmenting_path
    while path
      flow_augmentation(path)
      path = augmenting_path
    end
  end
```

Of course, we need to specify exactly how to _find_ these augmenting paths. This is a little bit more involved. It amounts to doing walking through the graph starting at the source, "labeling" nodes that could be part of an augmenting path, and scanning neighbors of labeled nodes looking for more labelable nodes, until we reach the sink (in which case we have found a path) or until we run out of nodes to scan (in which case there are no augmenting paths left). Sort of like this:

```ruby
  def augmenting_path
    labeled = {@source=>nil} # keys are labeled nodes; values, parents thereof
    scanned = {}
    now_scanning = @source
    while not labeled.empty?
      if labeled.include?(@sink) # i.e., we've found an augmenting path
        backtrace = [@sink]
        parent = labeled[@sink]
        while parent != nil # reconstruct the path found
          backtrace.push(parent)
          parent = scanned[parent]
        end
        return backtrace.reverse!
      end
      edges = @network.select do |e, v|
        e.tail == now_scanning or e.head == now_scanning
      end
      edges.each do |e, v|
        if e.tail == now_scanning
          if @network[e] < e.capacity
            if not labeled.merge(scanned).include?(e.head)
              labeled[e.head] = now_scanning
            end
          end
        elsif e.head == now_scanning
          if @network[e] > 0
            if not labeled.merge(scanned).include?(e.tail)
              labeled[e.tail] = now_scanning
            end
          end
        end
      end
      scanned[now_scanning] = labeled[now_scanning]
      labeled.delete(now_scanning)
      now_scanning = labeled.keys[0]
    end
    return nil # no path found
  end
```

And of course, we also need code to actually augment the flow along the path found—

```ruby
  def flow_augmentation(path)
    flow = +1.0/0 # positive infinity
    edges = []
    def query_edge(tail, head) # select edge given node names
      @network.select{|e, v| e.tail == tail and e.head == head}
    end
    path[0..path.length-2].each_index do |i|
      forward = query_edge(path[i], path[i+1])
      backward = query_edge(path[i+1], path[i])
      if backward.empty?
        edge_flow = forward
        edges.push(edge_flow.keys[0])
        available = edge_flow.keys[0].capacity - edge_flow.values[0]
        if flow > available
          flow = available
        end
      elsif forward.empty?
        edge_flow = backward
        edges.push(edge_flow.keys[0])
        available = edge_flow.values[0]
        if flow > available
          flow = available
        end
      end
    end
    edges.each do |e|
      network[e] += flow
    end
  end
```

Then throw in a reporting method so we have some way of actually inspecting our network and its completed flow assignment, close the `FlowNetwork` class definition (at long last) ...

```ruby
  def report
    print "Source: ", @source, "\n"
    print "Sink: ", @sink, "\n"
    @network.each_pair do |e, v|
      print e.tail, ' -> ', e.head, '; capacity: ', e.capacity, ', flow: ', v, "\n"
    end
    puts
  end

end
```

—and dear reader, the maximum-flow problem is _solved_! For suppose we are faced with the network depicted in the following diagram:

[![our flow network]({static}/images/flownetwork-300x174.jpg)]({static}/images/flownetwork.jpg)

We can then (admittedly with some typing) call for a solution like so:

```ruby
my_edges = [Edge.new('A', 'B', 12), Edge.new('A', 'E', 15),
  Edge.new('A', 'G', 13), Edge.new('B', 'C', 9), Edge.new('E', 'C', 11),
  Edge.new('G', 'E', 7), Edge.new('C', 'D', 18), Edge.new('C', 'F', 10),
  Edge.new('H', 'E', 8), Edge.new('G', 'H', 12), Edge.new('F', 'D', 6),
  Edge.new('H', 'F', 6), Edge.new('D', 'I', 12), Edge.new('F', 'I', 20),
  Edge.new('H', 'I', 10)]
my_network = FlowNetwork.new('A', 'I', my_edges)
my_network.ford_fulkerson
my_network.report
```

And receive it like so:

```text
Source: A
Sink: I
A -> B; capacity: 12, flow: 9
A -> E; capacity: 15, flow: 11
A -> G; capacity: 13, flow: 12
B -> C; capacity: 9, flow: 9
E -> C; capacity: 11, flow: 11
G -> E; capacity: 7, flow: 0
C -> D; capacity: 18, flow: 12
C -> F; capacity: 10, flow: 8
H -> E; capacity: 8, flow: 0
G -> H; capacity: 12, flow: 12
F -> D; capacity: 6, flow: 0
H -> F; capacity: 6, flow: 2
D -> I; capacity: 12, flow: 12
F -> I; capacity: 20, flow: 10
H -> I; capacity: 10, flow: 10
```

___Bibliography___

Dimitris Bertsimas and John N. Tsitsiklis, _Introduction to Linear Optimization_, §7.5

Anany Levitin, _Introduction to the Design and Analysis of Algorithms_, §10.2
