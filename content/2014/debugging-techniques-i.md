Title: Debugging Techniques I
Date: 2014-08-27 22:03
Status: published
Category: computing
Tags: Python
Slug: debugging-techniques-i

```python
#def my_problematic_function(x):
def my_problematic_function(x, call_count=[]):
    call_count.append(1)
    print("ZMD DEBUG call #{}".format(len(call_count)))
    import traceback; traceback.print_stack()
    result = do_stuff(x)
    etc()
```
