# CopyPasteKiller Plugin

Sublime text 3 plugin to help to refactor duplicated code.

This command sets snippets for "Find and Replace" with regular expression.  
You can find any code blocks without caring about indentation
and some differences like variable names.  
You can replace those matches with refactored code
by changing the given 'replace_string' and hitting "Replace".

<img width="640" alt="0x_git_diff" src="https://user-images.githubusercontent.com/275284/60776513-d93f0480-a167-11e9-95d4-270d53906b7b.png">

## Usage:

You can declare shortcut like:

```
{ "keys": ["ctrl+shift+i"], "command": "copy_paste_killer" }
```

### Guide

#### Select lines

<img width="640" alt="01_select_lines" src="https://user-images.githubusercontent.com/275284/60691557-7fda9980-9f0b-11e9-90de-3ca8af98af5b.png">

#### Run "copy_paste_killer" command

The snippets for "Find" and "Replace" are set

<img width="640" alt="02_run_copy_paste_killer" src="https://user-images.githubusercontent.com/275284/60691564-9123a600-9f0b-11e9-8457-b3fe2c804208.png">

#### Change the snippet for "Find"

Find parts which have variations(e.g. variable name) in the snippet for "Find" and select them

<img width="640" alt="03_edit_find_string" src="https://user-images.githubusercontent.com/275284/60691572-a6003980-9f0b-11e9-833d-04e872559deb.png">

#### Replace variables with Regex

Replace variable name parts with Regex in the snippet for "Find"  
You can name regex groups as you want  

The typical format to name regex group is `(?<name>.*)`

Copy the snippet into "Find:"  
“Select All ⌘A” -> “Use Selection for Find ⌘E”

<img width="640" alt="04_change_variable_to_regex" src="https://user-images.githubusercontent.com/275284/60691585-c5976200-9f0b-11e9-8088-2f6226902a33.png">

#### Hit "Find" and confirm matches

You can find duplicated codes even if they have different indents and **different variable names**

<img width="640" alt="05_confirm_find" src="https://user-images.githubusercontent.com/275284/60691596-dd6ee600-9f0b-11e9-8de0-da1fef677605.png">

#### Change the snippet for "Replace"

Change the snippet for "Replace" using regex groups named in "Find"  
The format is `$+{name}`

Copy the snippet into "Replace:"  
"Select All ⌘A" -> "Use Selection for Replace ⇧⌘E"

<img width="640" alt="06_edit_replace_string" src="https://user-images.githubusercontent.com/275284/60691609-fbd4e180-9f0b-11e9-8678-3f9c04156dbd.png">

#### Hit "Replace" and confirm changes

Hit "Replace" and confirm if changes are expected

<img width="640" alt="07_replace_matches" src="https://user-images.githubusercontent.com/275284/60691627-127b3880-9f0c-11e9-8699-62381789fbc5.png">

#### Check changes

Check changes with `git diff`

Reset(Undo) changes with `git checkout` etc if replacements were wrong

<img width="640" alt="08_git_diff" src="https://user-images.githubusercontent.com/275284/60691635-245cdb80-9f0c-11e9-8eda-9441ae477767.png">

## Test

### UnitTesting plugin

Use [UnitTesting plugin](https://github.com/SublimeText/UnitTesting)

- Open _tests/test_copy_paste_killer_selection_converter.py_
- Open "Command Palette..." (⇧⌘P)
- Run "UnitTesting: Test Current File"

#### Test scenarios

- "tests/data/*_source.txt" -> Expected snippet for selection
- "tests/data/*_find.txt" -> Expected snippet for find_string
- "tests/data/*_replace.txt" -> Expected snippet for replace_string

### Manual testing

Any selection shouldn't change with "copy_paste_killer" command and "Find" and "Replace" when replace_string isn't changed.
