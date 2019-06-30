# CopyPasteKiller Plugin

Sublime text 3 plugin to help to refactor duplicated code.

This commands set snippets for "Find and Replace" with regular expression.
You can find any code blocks without caring about indentation.
You can replace those matches with refactored code
by changing the given 'replace_string' and hitting "Replace".

## Usage:

You can declare shortcut like:

```
{ "keys": ["ctrl+shift+i"], "command": "copy_paste_killer" }
```

### Guide

#### Select lines

<img width="640" alt="01_select_lines" src="https://user-images.githubusercontent.com/275284/60395570-6387d700-9b70-11e9-9212-629087c24fa7.png">

#### Run "copy_paste_killer" command

The snippets for "Find" and "Replace" are set

<img width="640" alt="02_run_copy_paste_killer" src="https://user-images.githubusercontent.com/275284/60395590-b06bad80-9b70-11e9-8cef-ead5880e8627.png">

#### Hit "Find" and confirm matches

You can find duplicated codes even if they have different indents

<img width="640" alt="03_find_with_snippet" src="https://user-images.githubusercontent.com/275284/60395613-02acce80-9b71-11e9-9616-dba3e76431ae.png">

#### Change the snippet for "Replace"

Change the snippet for "Replace"

You can change it in the Panel and "Select All ⌘A" -> "Use Selection for Replace ⇧⌘E"

<img width="640" alt="04_edit_replace_string" src="https://user-images.githubusercontent.com/275284/60395616-1f490680-9b71-11e9-810f-d3ce6978e3a3.png">

#### Hit "Replace" and confirm changes

<img width="640" alt="05_replace_matches" src="https://user-images.githubusercontent.com/275284/60395621-34259a00-9b71-11e9-82f6-c06af4b081bf.png">

#### Check changes

Check changes with `git diff`

Reset changes with `git checkout` etc if replacements are wrong

<img width="640" alt="06_git_diff" src="https://user-images.githubusercontent.com/275284/60395629-4b648780-9b71-11e9-8462-ad6a10eee17d.png">

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
