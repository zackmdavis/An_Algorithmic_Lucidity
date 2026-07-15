Title: XXX III
Date: 2015-04-12 09:19
Status: published
Category: computing
Tags: Rust

```rust
const PSEUDO_DIGITS: [char; 7] = ['M', 'D', 'C', 'L', 'X', 'V', 'I'];
const PSEUDO_PLACE_VALUES: [usize; 7] = [1000, 500, 100, 50, 10, 5, 1];

#[allow(unused_parens)]
fn integer_to_roman(integer: usize) -> String {
    let mut remaining = integer;
    let mut bildungsroman = String::new();
    // get it?? It sounds like _building Roman_ (numerals), but it's
    // also part of the story about me coming into my own as a
    // programmer by learning a grown-up language
    //
    // XXX http://tvtropes.org/pmwiki/pmwiki.php/Main/DontExplainTheJoke
    for ((index, value), &figure) in PSEUDO_PLACE_VALUES.iter()
        .enumerate().zip(PSEUDO_DIGITS.iter())
    {
        let factor = remaining / value;
        remaining = remaining % value;

        if figure == 'M' || factor < 4 {
            for _ in 0..factor {
                bildungsroman.push(figure);
            }
        }

        // IV, IX, XL, &c.
        let smaller_unit_index = index + 2 - (index % 2);
        if smaller_unit_index < PSEUDO_PLACE_VALUES.len() {
            let smaller_unit_value = PSEUDO_PLACE_VALUES[smaller_unit_index];
            let smaller_unit_figure = PSEUDO_DIGITS[smaller_unit_index];

            if value - remaining <= smaller_unit_value {
                bildungsroman.push(smaller_unit_figure);
                bildungsroman.push(figure);
                remaining -= (value - smaller_unit_value);
            }
        }
    }
    bildungsroman
}
```
