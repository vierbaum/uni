;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "daiber_01"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "amsmath"
    "amssymb"
    "circledsteps"))
 :latex)

