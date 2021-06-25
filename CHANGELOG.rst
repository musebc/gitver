Bugfixes since v0.3.0
=====================

    2014-01-19  Manuel Bua  <manuel.bua@gmail.com>

        * Update README.md

        * Fix commit_count in templates not being an empty string when 0

    2014-01-18  Manuel Bua  <manuel.bua@gmail.com>

        * Fix README.md

Updates and fixes since v0.3.0-RC1
==================================

Release highlights:

    * fixes lot of bugs
    * much internal refactoring
    * stdout and stderr streams now handled correctly
    * renamed command "cleanall" to "clean-all"
    * gitver's version string switched to the Semantic Versioning scheme
    * adds custom version string formatting (see config file)
    * adds new command "gitver preview" for previewing templates
    * adds new "--quiet" and "--quiet-errors" flags
    * adds new "current" command
    * adds new "--colors" flag to switch coloring on/off, regardless of
      the configuration file
    * adds new "check" command to perform basic .gitignore checking
    * adds support for optional revision numbers (x.y.z.W)
    * adds support for optional pre-release metadata in tags
    * adds support for tags without a "v" prefix
    * adds new "safe_mode", enabled by default
    * adds new template variable placeholders
    * updated configuration file, you should mvoe or remove the
      previous configuration file (at .gitver/config) and regenerate the
      new one with the "gitver init" command
    * console colors disabled by default, better support for old
      terminal emulators


Release details:

    2014-01-18  Manuel Bua  <manuel.bua@gmail.com>

        * Update README.md

        * Add support for REV and REV_PREFIX to templates, update test template

        * Fix wrong link in README.md

        * Add initial INSTALL.md documentation, update README.md

        * Remove old comment from post-commit bash script

    2014-01-17  Manuel Bua  <manuel.bua@gmail.com>

        * Add Flattr button to README.md

        Thank you much you fellow developers, that was totally unexpected!

    2014-01-17  Manuel Bua  <manuel.bua@gmail.com>

        * Fix wrong explanation

        * Update README.md with latest "--help" output

        * Update gitver's configuration file comments

        * Update gitver to latest configuration

        * Update comments for default configuration

        * More PEP8 compliance

        * Merge branch 'revision-support'

        * Minor README.md enhancement

        * Update README.md

        * Add whole lot of missing comments

        * Reorganize condition

        * Minor refactoring

        * Fix grammar in command line help strings

        * Reword help, normalize casing, help made more clear

        * Update error message to include the optional revision

        * Minor update to README.md

        * More PEP8 compliance

        * Add revision support to custom NEXT string

        * Add support for an optional fourth number (x.y.z.W)

    2014-01-16  Manuel Bua  <manuel.bua@gmail.com>

        * More updates to the README.md file

        * Update README.md

    2014-01-15  Manuel Bua  <manuel.bua@gmail.com>

        * Add support for [v]X.Y.Z[-PRE-RELEASE-METADATA] tag format

        Note that square brackets denote *optional* data.

        - do not use git-describe for looking up hash length
        - do not cross-check hashes with git-describe output
        - a minimum 7-chars hash length has been introduced, to avoid frequent
        hash string length variations in fast-growing projects
        - refactor error message

    2014-01-15  Manuel Bua  <manuel.bua@gmail.com>

        * Add __git_raw proxy method, returns the raw stdout

        * Fix bad code layout

        * Update THANKS file

        * Cleanup import

        * Fix #22

        * Add ohloh.net badge

    2014-01-14  Manuel Bua  <manuel.bua@gmail.com>

        * Enhance #18, more comments, refactor, add "preview" command for templates

        The "gitver preview <templates>" command will output to stdout instead of
        creating the destination file, useful for testing or previewing the result.

    2014-01-14  Manuel Bua  <manuel.bua@gmail.com>

        * Fix missing exit if template file couldn't be written

    2014-01-14  Manuel Bua  <manuel.bua@gmail.com>

        * Behavior change, default config file now created at "gitver init"

        - refactoring
        - pass loaded configuration instead of importing it
        - enhance "gitver init" command help

    2014-01-14  Manuel Bua  <manuel.bua@gmail.com>

        * Fix missing spaces, output text layout

        * Add "check" command to perform a sanity check on the .gitignore file

        * Enhance comments and command output

        * Add safe_mode option, auto perform .gitignore check only for selected cmds

        * Fix #15, add message if .gitignore is fine

        * Add THANKS file

    2014-01-14  Manuel Bua  <manuel.bua@gmail.com>

        * Do not advertise the email address as-is

        ..even though it doesn't look like it's enough for spammers to stay away..

    2014-01-13  Manuel Bua  <manuel.bua@gmail.com>

        * Merge branch 'term-output'

        * Set this repository's gitver colors on

        * Better message if the current repository can't be described properly

        * Add "--quiet" and "--quiet-errors", disable stdout and stderr, respectively

        * More descriptive warning if no trace of ".gitver" is found in .gitignore

        * Update gitver repository configuration and default config, fix grammar

        * Minor refactoring

        * Be nice and compatible, set terminal output colors off by default

        * Fix wrong output stream usage

        * Add proper stdout/stderr usage, add "--color" command line option, refactor

        * Add color terminal output setting to config file and default configuration

        * Refactor git interface, more readable

        * More comments for the better!

    2014-01-13  Manuel Bua  <manuel.bua@gmail.com>

        * Fix #7

        - track .gitver/templates
        - move templates/* to .gitver/templates/* (now tracked)

    2014-01-13  Manuel Bua  <manuel.bua@gmail.com>

        * Fix #8

        * Fix #11

        * Do not permit to run "make_release" as root

        * Fix #9 and #12

        * Fix #10, remove debug output

    2014-01-12  Manuel Bua  <manuel.bua@gmail.com>

        * Default to dot-separated commit count, more config file error detection

        * Minor refactoring

        * Warn user if a deprecated configuration file is being used

    2014-01-12  Manuel Bua  <manuel.bua@gmail.com>

        * Bump to v0.3.0-RC1

        (obviously forgot this manual step)

    2014-01-12  Manuel Bua  <manuel.bua@gmail.com>

        * Fix typo, grammar

        * Update documentation with new 0.3.x functionalities

        * Add missing template check, a valid output shall be defined at line #0

        * Fix missing color output on error

        * Add "current" command, output current version only, without any formatting

        * Fix casing, unneeded string concatenation, add parenthesis on unused data

        * Always show NEXT and pre-release metadata, mark used data with "Using"
