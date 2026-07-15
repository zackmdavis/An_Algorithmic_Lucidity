Title: Convert Markdown to HTML Within Emacs Using Pandoc
Date: 2014-11-24 05:00
Status: published
Category: computing
Tags: Emacs

Okay, so there actually is a [pandoc-mode](http://joostkremers.github.io/pandoc-mode/), but I couldn't figure out how to configure and use it, so it was easier to just write the one command that I wanted—

```elisp
(defun markdown-to-html ()
  (interactive)
  (let* ((basename (file-name-sans-extension (buffer-file-name)))
         (html-filename (format "%s.html" basename)))
    (shell-command (format "pandoc -o %s %s"
                           html-filename (buffer-file-name)))
    (find-file-other-window html-filename)))
```
