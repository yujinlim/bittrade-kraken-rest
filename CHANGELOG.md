# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.13.14] - 2024-03-25

### Added

- Edit order endpoint

### Changed

- The sign function provided as example, handles json payloads such as cancel batch

## [0.13.13] - 2024-03-10

### Changed

- Example signature method updated to reflect fix for json body
- `prepare_private` accepts a `json` dict; if provided, content type header is set to application/json
- batch cancel orders uses that new json argument to work
- batch cancel orders reverts to regular cancel if only one id is passed (Kraken fails otherwise)

## [0.13.11] - 2024-03-10

### Changed

- Cancel order batch is now exported on root module
- Results of requests mapped throught `send_and_map_result` aren't printed anymore; they are logged at the debug level

## [0.13.10] - 2024-03-10

### Added

- Cancel order batch

## [0.13.9] - 2024-03-09

### Changed

- Nonce uses nanoseconds

## [0.13.8] - 2024-03-06

### Changed

- `oflags` not sent when not sent (fixes order creation error)

## [0.13.7] - 2024-02-29

### Added

- Status of recent withdrawals

## [0.13.6] - 2024-02-27

### Added

- Extended balance

## [0.13.4] - 2024-02-19

- Add cancel order endpoint
- Add add order endpoint
- Add withdraw funds endpoint
- Add check recent deposits status endpoint
- More top level exports

## [0.13.0] - 2023-01-17

- Add cancel all orders endpoint

## [0.12.0] - 2023-01-07

- Complete overhaul to use Observables
- Add Black, iSort, mypy and pyright
- Nothing that worked on 0.10 will work anymore

## [0.10.0] - 2022-12-27

### Changed

- All CLI has been moved to [bittrade-kraken-cli](https://github.com/TechSpaceAsia/bittrade-kraken-cli)
- Removed `with_api_key` decorator
- Renamed files under endpoints to remove `get_` prefix

### Added

- Endpoint methods are now exported at the `private` and `public` levels as well as at the root level