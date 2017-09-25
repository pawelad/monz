# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog][keepachangelog] and this project
adheres to [Semantic Versioning][semver].

## Unreleased
### Added
- Added `__main__.py` file which allows running `monz` via `python -m monz`
  and is linked as `entry_point` in `setup.py`. (#7)
- Started keeping a changelog.

### Changed
- Moved from `scripts` to `entry_points` in `setup.py`. (#7)
- Removed CLI capabilities from `monz/command_line.py` so it can't be run
  directly. 
- Modified `bin/monz` script to always use local version of `monz`.
  Running `python bin/monz` is now equal to `python -m monz`.

### Fixed
- Fixed `monzo_amount_to_dec` to work with small numbers. (#3)


[keepachangelog]: http://keepachangelog.com/en/1.0.0/
[semver]: http://semver.org/spec/v2.0.0.html
