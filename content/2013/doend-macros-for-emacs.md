Title: do/end Macros for Emacs
Date: 2013-08-30 14:43
Status: published
Category: computing
Tags: Emacs, Ruby

Dear reader, Ruby is a pretty okay programming language, but I have to say I feel ambivalent about the use of `do` and `end` as block delimiters. (Contrast to braces in C/Java/_&c._ or indentation in Python.) _Three_ keystrokes just to close a block?! Scandalous!

Or _maybe_ ... _not_-so-scandalous. For two or three _characters_ need not imply two or three _keystrokes_; one need only configure one's editor with convenient bindings for the insertion of `do` and `end`. For example, pasting the following code into one's Emacs init file assigns `M-[` (respectively `M-]`) to insert the text `do` (respectively `end`), much as one would type `Shift-[` (respectively `Shift-]`) for an open- (respectively close-) brace, except with Alt ("Meta" in Emacs parlance) instead of Shift—

```elisp
(fset 'block-do
   "do")
(global-set-key (kbd "M-[") 'block-do)

(fset 'block-end
   "end")
(global-set-key (kbd "M-]") 'block-end)
```

I guess this would also be useful for like, Lua.
