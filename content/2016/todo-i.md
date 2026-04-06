Title: TODO I
Date: 2016-01-09 05:00
Status: published
Category: Uncategorized
Tags: Rust
Slug: todo-i

```
    let path = Path::new("/proc/meminfo");
    let proc_meminfo = match File::open(path) {
        Ok(f) => f,
        Err(e) => {
            println!("Error: {:?}", e);
            // TODO: be kinder to our friends still under Cupertino's rule
            moral_panic!("couldn't read /proc/meminfo?! It is possible \
                          that you are struggling with an inferior nonfree \
                          operating system forced on you by your masters in \
                          Cupertino or Redmond");
        }
    };
```
