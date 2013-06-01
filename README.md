Rosetta Fight
=============
*Quick Lookup and Comparison on Rosetta Code Languages*

[Rosetta Code](http://rosettacode.org/) provides a corpus of programming tasks and solutions across numerous programming languages.
The idea is to present solutions to the same task in as many different languages as possible, to demonstrate how languages are similar and different, and to aid a person with a grounding in one approach to a problem in learning another.
The Wikipedia format that it currently exists in is not, in my belief, the format best used for such a comparison.

*Rosetta Fight* aims to allow direct side by side comparisons between two languages for a given task.
This is a work in progress and only provides a way to query for a solution to a task in a particular language currently.

Using the [MediaWiki API](http://www.mediawiki.org/wiki/API:Main_page), the Rosetta Code site is queryable for both the list of tasks and the MediaWiki markup of those tasks.
If you're curious as to an example, you can view the pretty printed JSON MediaWiki markup for [99 Bottles of Beer](http://rosettacode.org/mw/api.php?format=jsonfm&action=query&titles=99_Bottles_of_Beer&prop=revisions&rvprop=content).

```bash
smerity@pegasus:~/Coding/rosettafight$ python get_solution.py
Task: String interpolation (included)
Language Choices: ada, aikido, algol68, autohotkey, bash, bracmat, c, coffeescript, cpp, csh, csharp, d, delphi, dos, e, euphoria, factor, fantom, fortran, fsharp, go, groovy, haskell, hicest, icon, j, java, javascript, lisp, lua, mathematica, maxima, nemerle, netrexx, ocaml, oz, parigp, perl, perl6, php, picolisp, prolog, purebasic, python, racket, rebol, rexx, ruby, runbasic, scala, seed7, sh, snobol, tcl, tuscript, ursala
Lang: go
=-=-=-=-=-=-=-=-=-=-
  package main

	import (
	    "fmt"
	)

	func main() {
	    str := "Mary had a %s lamb"
	    txt := "little"
	    out := fmt.Sprintf(str, txt)
	    fmt.Println(out)
	}
=-=-=-=-=-=-=-=-=-=-
```

Development Environment
-----------------------

To retrieve all the components required for the development environment, install the Python dependencies using [pip](http://www.pip-installer.org/en/latest/) and the web dependencies using [bower](http://bower.io/).
It may also be useful to install the Python dependencies in a virtualenv.

```bash
pip install -r requirements.txt
bower install
```

Testing
-------

The Flask backend is responsible for generating the static JSON solution files from the raw data.
Testing in there is backed with unittest, mock and Flask-Testing.
To run these tests, `python tests.py`.

The AngularJS frontend serves the content up to users.
Testing is done using AngularJS Mock and the Jasmine test runner.
To run these, run the local web server via `python main.py` and then visit `/test` in a browser.

Note
----

Do not run the crawler yourself unless you have a *particularly* good reason.
If you want access to this data for yourself contact me and I'll happily supply it.
The data comes to approximately 8 megabytes compressed (35 megabytes raw) and includes:

+ `tasks.json` which has the MediaWiki markup for all existing tasks
+ `solutions.json` which contains, for every task, the list of languages and their solutions
