## Regex
### Atoms
- r""   raw string
- \     escape
- .     any char
- \d    decimal digit
- \D    not \d
- \s    whitespace char
- \S    not \s
- \w    word char + number + _
- \W    not a word char

### Quantifiers
- *     0 or more repetitions
- +     1 or more repetitions
- ?     0 or 1 repetition
- a|b   a or b
### Structure
- ^     start of string
- $     end of string
- (a)   group
- (?:a) non-captruing group (not included by .group() method)
- [a]   set of char
- [^a]  complement of the set
- {n}   n repetitions
- {n,}  at least n repetitions
- {n,m} n~m repetitions
