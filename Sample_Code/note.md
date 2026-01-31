## Regex
### Atoms
- `r""` raw string
- `\`   escape
- `.`   any char
- `\d`  decimal digit
- `\D`  not \d
- `\s`  whitespace char
- `\S`  not \s
- `\w`  word char + number + _
- `\W`  not a word char
- `\b`  word boundary

### Quantifiers
- `*`   0 or more repetitions
- `+`   1 or more repetitions
- `?`   0 or 1 repetition
- `a|b` a or b
### Structure
- `^`   start of string
- `$`   end of string
- `(a)` group
    - (\w)+ VS (\w+): first will create n groups (n is length of \w) while second one will have 1 group of all \w
- (?:a) non-captruing group (not included by .group() method)
- [a]   set of char can be matched (the whole [] is 1 char)
- [^a]  complement of the set
- {n}   n repetitions
- {n,}  at least n repetitions
- {n,m} n~m repetitions

## Data type
- "": string; essentially a list
- (): tuple
- []: list
- {}: dictionary
- set(): set
    - unique: no repeat items
    - unordered
    - mutable
    - hashable: no list/set/dictionary; hash is used to search items in set

## Operator
### Set Operator: only works for set()
- | or .union()
- & or .intersection()
- - or .difference()
- ^ or .symmetric_difference(): union-intersection
- |= or .update(): add elements in b set to a set
- &= or .intersection_update(): only keep elements in intersection
- -= or .difference_update()
- ^= or symmetric_difference_update()
- <= or .issubset()
- >= or .issuperset()
- .isdisjoint()

## Keywords
- global: use before a local variable
    - e.g. `global var += 1`
- constants: CAPITALIZE variable
    - e.g. `NUM = 3`
